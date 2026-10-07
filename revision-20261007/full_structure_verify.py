"""Recompute every shipped structural leaf from exact raw polynomials.

No original output is modified. Saved strict signs are compared field-for-field.
"""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
import ctypes,gzip,hashlib,importlib.util,json,sys,time
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
from audit_paths import release_root
RELEASE=release_root(HERE)

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    start=time.perf_counter();source=RELEASE/'code'/'frozen'/'compact-rough-layer-certificate.json.gz'
    generator=RELEASE/'code'/'src'/'compact-halfplane-certificate-v2-partial.py'
    before={str(source):sha(source),str(generator):sha(generator)}
    spec=importlib.util.spec_from_file_location('all_signs',generator);gen=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen)
    with gzip.open(source,'rt',encoding='utf-8') as stream:data=json.load(stream)
    result={'status':'RUNNING_ALL_STRUCTURAL_SIGNS','required_leaves':211241,'signs_recomputed':0,
            'source_sha256':before,'generator':'executed public raw-polynomial 100-bit outward dyadic interval generator',
            'scope':'Each complete leaf alpha/eta rectangle, all 3 B margins, 6 negative-D margins, raw determinant margin, and R real margin. Not a different implementation of transcendental primitives.'}
    assert len(data['cover'])==result['required_leaves']
    target=HERE/'full-structure-verification.json'
    def save():
        result['wall_seconds']=time.perf_counter()-start
        target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    save()
    try:
        for index,row in enumerate(data['cover']):
            fresh,reason=gen.check(*map(Q,row['alpha']),*map(Q,row['eta']))
            assert fresh is not None,(index,reason)
            assert fresh==row,('exact regenerated leaf record differs',index)
            result['signs_recomputed']=index+1
            if (index+1)%4096==0:
                save();print(json.dumps({'signs_recomputed':index+1,'required':len(data['cover']),
                                         'seconds':round(result['wall_seconds'],3)}),flush=True)
        assert result['signs_recomputed']==211241
        assert all(sha(Path(p))==value for p,value in before.items()),'input changed during run'
        result['status']='PASS_ALL_211241_EXACT_STRUCTURAL_LEAF_RECOMPUTATIONS'
        result['all_regenerated_records_identical']=True
        result['return_code']=0
    except Exception as exc:
        result['status']='FAIL';result['error']=repr(exc);result['return_code']=1;save();raise
    save();print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
