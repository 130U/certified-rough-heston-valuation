"""Cold, pinned-thread, memory-monitored full-history omitted-node certification."""
from pathlib import Path
import argparse,ctypes,hashlib,importlib.util,json,os,platform,subprocess,sys,time
HERE=Path(__file__).resolve().parent;BASE=HERE.parent/'english-heston-release';SRC=BASE/'code/src'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def prepare():
    source=SRC/'certify-field-residual-v3.py';text=source.read_text(encoding='utf-8')
    changes=[('BASE=Path(__file__).parent',"BASE=Path(__file__).resolve().parents[1]/'english-heston-release'/'code'/'src'"),
             ('take=all_u<=U','take=(all_u>64)&(all_u<=U)'),
             ('    aa=np.array(aa);bb=np.array(bb);cell=np.array(cell)',
              "    aa=np.array(aa);bb=np.array(bb);cell=np.array(cell)\n    preflight_cells=getattr(sys.modules[__name__],'OMISSION_PREFLIGHT_CELLS',None)\n    if preflight_cells is not None:aa=aa[:preflight_cells];bb=bb[:preflight_cells];cell=cell[:preflight_cells]\n    retained=np.empty((len(aa)+1,len(u)),dtype=np.float64);retained[0]=first"),
             ('        bound=UP(point+UP(radius[:,None]*derivative_bound))',
              '        bound=UP(point+UP(radius[:,None]*derivative_bound))\n        retained[start+1:start+1+len(a)]=bound'),
             ('    assert hashlib.sha256(path.read_bytes()).hexdigest()==field_hash',
              "    time_path=Path(__file__).with_name('omission-time-'+('preflight' if preflight_cells is not None else 'high')+'.npz')\n    np.savez_compressed(time_path,a=np.r_[0.,aa],b=np.r_[t[1],bb],u=u,residual_physical_upper=retained)\n    assert hashlib.sha256(path.read_bytes()).hexdigest()==field_hash"),
             ("      'alpha_exact':str(alpha)",
              "      'time_envelope_file':time_path.name,'time_envelope_sha256':hashlib.sha256(time_path.read_bytes()).hexdigest(),\n      'alpha_exact':str(alpha)")]
    for before,after in changes:assert text.count(before)==1; text=text.replace(before,after)
    target=HERE/'omission-residual-generator.py';target.write_text(text,encoding='utf-8')
    (HERE/'omission-instrumentation.json').write_text(json.dumps({'original_source_sha256':sha(source),'instrumented_source_sha256':sha(target),
        'changes':[{'before':a,'after':b} for a,b in changes],
        'scope':'Frequency selection of existing field columns and storage of unchanged complete-cell residual mathematics. Preflight truncates cells and is not a full certificate; full mode covers all cells.'},indent=2)+'\n')
def worker(mode):
    import numpy as np
    started=time.perf_counter();p=HERE/'omission-residual-generator.py'
    sp=importlib.util.spec_from_file_location('omission_generator',p);module=importlib.util.module_from_spec(sp)
    sys.modules['omission_generator']=module;sp.loader.exec_module(module)
    if mode=='preflight':module.OMISSION_PREFLIGHT_CELLS=64
    out=module.certify(BASE/'code/frozen/fixed-field-betap52-u128.npz',__import__('fractions').Fraction(13,25),128.,4,32)
    assert len(out['u'])==512 and out['u'][0]==64.125 and out['u'][-1]==128.
    if mode=='full':assert out['certified_closed_subintervals']==8189
    else:out['status']='PREFLIGHT_PARTIAL_TIME_NONCERTIFICATE'
    out['worker_wall_seconds_after_numpy_import']=time.perf_counter()-started
    out['thread_environment']={k:os.environ.get(k) for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']}
    out['numpy_version']=np.__version__;out['python_version']=platform.python_version()
    target=HERE/('omission-residual-high.json' if mode=='full' else 'omission-residual-preflight.json')
    target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'mode':mode,'frequency_nodes':512,'closed_time_cells':out['certified_closed_subintervals'],
        'halfplane_certified':out['approx_left_halfplane_certified'],'continuous_loop_phase_seconds':out['seconds'],
        'worker_wall_seconds_after_numpy_import':out['worker_wall_seconds_after_numpy_import']},indent=2),flush=True)
def memory_counter(p):
    if os.name!='nt':return None
    from ctypes import wintypes as w
    class Counters(ctypes.Structure):
        _fields_=[('cb',w.DWORD),('PageFaultCount',w.DWORD),('PeakWorkingSetSize',ctypes.c_size_t),('WorkingSetSize',ctypes.c_size_t),
                  ('QuotaPeakPagedPoolUsage',ctypes.c_size_t),('QuotaPagedPoolUsage',ctypes.c_size_t),('QuotaPeakNonPagedPoolUsage',ctypes.c_size_t),
                  ('QuotaNonPagedPoolUsage',ctypes.c_size_t),('PagefileUsage',ctypes.c_size_t),('PeakPagefileUsage',ctypes.c_size_t)]
    counter=Counters();counter.cb=ctypes.sizeof(counter)
    fn=ctypes.WinDLL('psapi').GetProcessMemoryInfo;fn.argtypes=[w.HANDLE,ctypes.c_void_p,w.DWORD];fn.restype=w.BOOL
    if not fn(w.HANDLE(int(p._handle)),ctypes.byref(counter),ctypes.sizeof(counter)):raise OSError(ctypes.get_last_error())
    return {'peak_working_set_bytes':counter.PeakWorkingSetSize,'working_set_bytes':counter.WorkingSetSize,'peak_pagefile_bytes':counter.PeakPagefileUsage}
def launch(mode):
    env=dict(os.environ)
    for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:env[key]='1'
    command=[sys.executable,'-X','utf8','-B',str(Path(__file__).resolve()),'--worker',mode]
    start=time.perf_counter();peak=0;peak_commit=0;path=HERE/('omission-'+mode+'-output.txt')
    with path.open('w',encoding='utf-8') as log:
        p=subprocess.Popen(command,cwd=HERE,env=env,stdout=log,stderr=subprocess.STDOUT)
        while p.poll() is None:
            info=memory_counter(p)
            if info is not None:
                peak=max(peak,info['peak_working_set_bytes']);peak_commit=max(peak_commit,info['peak_pagefile_bytes'])
                if peak>1073741824:p.terminate();p.wait();raise MemoryError('One-GiB working-set contract exceeded')
            time.sleep(.25)
        info=memory_counter(p)
        if info is not None:peak=max(peak,info['peak_working_set_bytes']);peak_commit=max(peak_commit,info['peak_pagefile_bytes'])
    receipt={'mode':mode,'return_code':p.returncode,'parent_cold_wall_seconds':time.perf_counter()-start,
             'peak_working_set_bytes':peak,'peak_commit_bytes':peak_commit,'memory_monitor':'Windows OS cumulative PeakWorkingSetSize; no process-memory content read',
             'command':command,'thread_environment':{k:env[k] for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']},
             'stdout_file':path.name,'source_sha256':sha(HERE/'omission-residual-generator.py'),'numpy_import_included_in_parent_wall':True}
    (HERE/('omission-'+mode+'-execution.json')).write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True);assert p.returncode==0,path.read_text(encoding='utf-8')
    return receipt
def main():
    parser=argparse.ArgumentParser();group=parser.add_mutually_exclusive_group()
    group.add_argument('--worker',choices=['preflight','full'])
    group.add_argument('--regenerate-full',action='store_true',help='Fresh full run in the separate work copy created by run_frontier.py; retains cold-wall and peak-memory monitoring.')
    args=parser.parse_args()
    if args.worker:worker(args.worker);return
    contract=load(HERE/'omission-contract.json');assert contract['resource_preapproval']['status']=='ACCEPTED_WITHIN_AUTHORIZED_RESEARCH'
    prepare()
    if args.regenerate_full:
        launch('full');return
    receipt=launch('preflight')
    print(json.dumps({'preflight':'ACCEPTED','approximate_full_wall_extrapolation_seconds':receipt['parent_cold_wall_seconds']*8189/65,
                     'warning':'Extrapolation from the earliest cells is a resource estimate, not certificate evidence or a deadline.'}),flush=True)
    launch('full')
if __name__=='__main__':main()
