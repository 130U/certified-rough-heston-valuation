"""Bounded read-only release checks; records actual execution, never alters originals."""
from __future__ import annotations
import ctypes, importlib.util, json, platform, subprocess, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
from audit_paths import release_root
RELEASE = release_root(HERE)

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    item = importlib.util.module_from_spec(spec)
    sys.modules[name] = item
    spec.loader.exec_module(item)
    return item

def main():
    import numpy as np
    ledger = {'date':'2026-10-07','status':'RUNNING','python':platform.python_version(),
              'numpy':np.__version__,'python_executable':sys.executable,
              'release_directory':str(RELEASE),'records':[]}
    class Memory(ctypes.Structure):
        _fields_=[('length',ctypes.c_ulong),('load',ctypes.c_ulong),
                  ('total',ctypes.c_ulonglong),('available',ctypes.c_ulonglong),
                  ('total_page',ctypes.c_ulonglong),('available_page',ctypes.c_ulonglong),
                  ('total_virtual',ctypes.c_ulonglong),('available_virtual',ctypes.c_ulonglong),
                  ('available_extended',ctypes.c_ulonglong)]
    memory=Memory();memory.length=ctypes.sizeof(memory)
    if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)):
        ledger['memory_preflight']={'total_physical_bytes':memory.total,'available_physical_bytes':memory.available}
    def save():
        (HERE/'verification.json').write_text(json.dumps(ledger,indent=2)+'\n',encoding='utf-8')
    def operation(label,command,fn):
        start=time.perf_counter()
        record={'label':label,'command':command,'status':'RUNNING'}
        ledger['records'].append(record);save()
        try:
            record['result']=fn();record['return_code']=0;record['status']='PASS'
        except Exception as exc:
            record['status']='FAIL';record['return_code']=1;record['error']=repr(exc)
        record['wall_seconds']=time.perf_counter()-start;save()
        print(json.dumps(record,indent=2),flush=True)
    run=module('public_run',RELEASE/'code'/'run.py')
    operation('release_manifest','code/run.py::check_manifest()',run.check_manifest)
    operation('structure_16_signs','code/run.py::check_cover(sample_signs=16)',lambda:run.check_cover(16))
    operation('fields_residual_receipts','code/run.py::check_fields_and_residuals()',run.check_fields_and_residuals)
    operation('objectives_financial_decisions','code/run.py::check_objectives()',run.check_objectives)
    for filename in ['verify_package.py','verify_input_bounds.py','verify_terminal.py','verify_field_receipt.py']:
        path=RELEASE/'code'/'classical'/filename
        def subprocess_check(path=path):
            completed=subprocess.run([sys.executable,'-B',str(path)],cwd=RELEASE,capture_output=True,text=True,encoding='utf-8')
            logfile=HERE/(path.stem+'-stdout.txt');logfile.write_text(completed.stdout+completed.stderr,encoding='utf-8')
            assert completed.returncode==0, completed.stderr or completed.stdout
            return {'subprocess_return_code':completed.returncode,'log':str(logfile),
                    'stdout':completed.stdout,'stderr':completed.stderr}
        operation(filename,[sys.executable,'-B',str(path)],subprocess_check)
    ledger['status']='PASS_BOUNDED_SAVED_CERTIFICATE_AUDIT' if all(r['status']=='PASS' for r in ledger['records']) else 'FAIL'
    ledger['scope']='Saved records and exact arithmetic; 16 regenerated structural leaves. No full continuous residual replay or coefficient-bank regeneration.'
    save()
    return 0 if ledger['status'].startswith('PASS') else 1

if __name__=='__main__':
    raise SystemExit(main())
