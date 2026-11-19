"""Transparent instrumentation of the frozen continuous residual generator.

The generated source is saved before execution and has its own identity.
Only storage of already certified local bounds is added to the mathematics.
"""
from pathlib import Path
import hashlib, json, subprocess, sys
HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'reference'
source=BASE/'code/src/certify-field-residual.py'
text=source.read_text(encoding='utf-8')
changes=[
    ("BASE=Path(__file__).parent", "BASE=Path(__file__).resolve().parents[1]/'reference'/'code'/'src'"),
    ("    aa=np.array(aa);bb=np.array(bb);cell=np.array(cell)",
     "    aa=np.array(aa);bb=np.array(bb);cell=np.array(cell)\n    retained=np.empty((len(aa)+1,len(u)),dtype=np.float64);retained[0]=first"),
    ("        bound=UP(point+UP(radius[:,None]*derivative_bound))", 
     "        bound=UP(point+UP(radius[:,None]*derivative_bound))\n        retained[start+1:start+1+len(a)]=bound"),
    ("    assert hashlib.sha256(path.read_bytes()).hexdigest()==field_hash", 
     "    time_path=Path(__file__).with_name('time-residual-alpha-13_25.npz')\n    np.savez_compressed(time_path,a=np.r_[0.,aa],b=np.r_[t[1],bb],u=u,residual_physical_upper=retained)\n    assert hashlib.sha256(path.read_bytes()).hexdigest()==field_hash"),
    ("      'alpha_exact':str(alpha)",
     "      'time_envelope_file':time_path.name,'time_envelope_sha256':hashlib.sha256(time_path.read_bytes()).hexdigest(),\n      'alpha_exact':str(alpha)")
]
for before,after in changes:
    assert text.count(before)==1,('instrumentation anchor',before)
    text=text.replace(before,after)
generated=HERE/'continuous-residual-with-time.py'
generated.write_text(text,encoding='utf-8')
(HERE/'time-instrumentation.json').write_text(json.dumps({
    'status':'STORAGE_ONLY_INSTRUMENTATION','base_generator_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'generated_source_sha256':hashlib.sha256(generated.read_bytes()).hexdigest(),
    'changes':[{'before':a,'after':b} for a,b in changes],
    'scope':'Fresh all-513-used-frequency continuous closed-time residual regeneration for alpha=0.52; no numerical solver or field refit.'},indent=2)+'\n',encoding='utf-8')
sp=__import__('importlib.util',fromlist=['util']).spec_from_file_location('time_residual',generated)
mod=__import__('importlib.util',fromlist=['util']).module_from_spec(sp)
sys.modules['time_residual']=mod;sp.loader.exec_module(mod)
out=mod.certify(BASE/'code/frozen/fixed-field-betap52-u128.npz',__import__('fractions').Fraction(13,25),64.,4,32)
(HERE/'fresh-all-node-time-residual.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'closed_time_intervals':out['certified_closed_subintervals'],
                  'frequency_nodes':len(out['u']),'time_envelope_file':out['time_envelope_file']},indent=2),flush=True)
