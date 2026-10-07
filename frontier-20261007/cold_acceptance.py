"""Cold parent-process acceptance with a Windows job memory measurement.

This checks the already fixed finite-history ZIP in a fresh extraction; it never
modifies the prior freeze. PeakJobMemoryUsed measures committed memory in the
assigned process tree, not peak RSS. Download/extraction precede the timer.
"""
from pathlib import Path
import ctypes as c, hashlib, json, os, platform, subprocess, sys, time, zipfile
from ctypes import wintypes as w
HERE=Path(__file__).resolve().parent
ARCHIVE=HERE.parent/'heston-nine-point-20261007'/'Theodore-Ouyang-Heston-Finite-History-Evidence-20261007.zip'
DEST=HERE/'cold-acceptance-extracted'

def main():
    start_extract=time.perf_counter()
    assert not DEST.exists(), 'Fresh extraction required; retain earlier logs.'
    DEST.mkdir()
    with zipfile.ZipFile(ARCHIVE) as z:
        assert z.testzip() is None
        for n in z.namelist():
            assert (DEST/n).resolve().is_relative_to(DEST.resolve())
        z.extractall(DEST)
    extract_seconds=time.perf_counter()-start_extract
    class Basic(c.Structure):
        _fields_=[('PerProcessUserTimeLimit',c.c_int64),('PerJobUserTimeLimit',c.c_int64),('LimitFlags',w.DWORD),('MinimumWorkingSetSize',c.c_size_t),('MaximumWorkingSetSize',c.c_size_t),('ActiveProcessLimit',w.DWORD),('Affinity',c.c_size_t),('PriorityClass',w.DWORD),('SchedulingClass',w.DWORD)]
    class IO(c.Structure):
        _fields_=[(k,c.c_uint64) for k in ['ReadOperationCount','WriteOperationCount','OtherOperationCount','ReadTransferCount','WriteTransferCount','OtherTransferCount']]
    class Extended(c.Structure):
        _fields_=[('BasicLimitInformation',Basic),('IoInfo',IO),('ProcessMemoryLimit',c.c_size_t),('JobMemoryLimit',c.c_size_t),('PeakProcessMemoryUsed',c.c_size_t),('PeakJobMemoryUsed',c.c_size_t)]
    kernel=c.WinDLL('kernel32',use_last_error=True)
    kernel.CreateJobObjectW.argtypes=[c.c_void_p,w.LPCWSTR];kernel.CreateJobObjectW.restype=w.HANDLE
    kernel.AssignProcessToJobObject.argtypes=[w.HANDLE,w.HANDLE];kernel.AssignProcessToJobObject.restype=w.BOOL
    kernel.QueryInformationJobObject.argtypes=[w.HANDLE,c.c_int,c.c_void_p,w.DWORD,c.c_void_p];kernel.QueryInformationJobObject.restype=w.BOOL
    kernel.CloseHandle.argtypes=[w.HANDLE]
    job=kernel.CreateJobObjectW(None,None);assert job
    env=os.environ.copy()
    thread_settings={k:'1' for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']}
    env.update(thread_settings)
    cmd=[sys.executable,'-X','utf8','-B',str(DEST/'heston-nine-point-20261007/run_evidence.py'),'--full']
    t=time.perf_counter()
    with (HERE/'cold-acceptance.log').open('w',encoding='utf-8') as log:
        p=subprocess.Popen(cmd,cwd=DEST,env=env,stdout=log,stderr=subprocess.STDOUT)
        assigned=bool(kernel.AssignProcessToJobObject(job,int(p._handle)))
        assign_error=None if assigned else c.get_last_error()
        return_code=p.wait()
    elapsed=time.perf_counter()-t
    ext=Extended();queried=bool(kernel.QueryInformationJobObject(job,9,c.byref(ext),c.sizeof(ext),None))
    kernel.CloseHandle(job)
    receipt=json.loads((DEST/'verification-work/execution-receipt.json').read_text(encoding='utf-8'))
    result={'status':'PASS_COLD_FULL_ACCEPTANCE' if return_code==0 else 'FAILED',
        'archive_sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),'archive_bytes':ARCHIVE.stat().st_size,
        'tested_manifest_sha256':receipt['tested_manifest_sha256'],'return_code':return_code,
        'commands_passed':len(receipt['records']),'end_to_end_parent_wall_seconds':elapsed,
        'zip_crc_hash_and_extraction_seconds_separate':extract_seconds,
        'peak_job_committed_memory_bytes':int(ext.PeakJobMemoryUsed) if assigned and queried else None,
        'peak_single_process_committed_memory_bytes':int(ext.PeakProcessMemoryUsed) if assigned and queried else None,
        'job_memory_measurement_assignment_error':assign_error,
        'memory_scope':'Windows job committed-memory peak of assigned acceptance process and descendants; not peak RSS; job assigned immediately after launching interpreter.',
        'cold_scope':'New interpreter; integrity checks, work copy, every --full subprocess, output verification included. ZIP validation/extraction measured separately; download excluded. Optional full residual regeneration excluded because retained generation evidence is checked.',
        'python':sys.version,'platform':platform.platform(),'cpu':'Intel Core Ultra 7 155U','physical_cores':12,'logical_processors':14,
        'physical_memory_visible_kib':16184696,'thread_environment_for_this_run':thread_settings,
        'historical_threads':'Not recorded; do not retroactively assign current single-thread settings to old timing observations.',
        'concurrency':'Other research and PDF-authoring processes may run on this machine. This is an observed reproducibility cost, not an isolated speed benchmark.',
        'log':'cold-acceptance.log','step_receipt':receipt}
    (HERE/'cold-acceptance.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='step_receipt'},indent=2))
    assert return_code==0
    assert all(r['return_code']==0 for r in receipt['records'])

if __name__=='__main__':main()
