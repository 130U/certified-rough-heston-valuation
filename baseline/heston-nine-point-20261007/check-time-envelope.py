"""Independent full-cover and all-513-endpoint check of fresh cell envelopes.

The storage-only instrumented generator supplies the continuous inequalities.
This checker validates its identity, exact array semantics and coverage; it
does not claim an independently implemented residual transcendental library.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib, json, sys, time
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parent / 'english-heston-release'
FROZEN = BASE / 'code/frozen'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text(encoding='utf-8'))

def validate_arrays(a, b, u, bounds, expected, expected_cells):
    import numpy as np
    assert all(x.dtype == np.dtype('float64') for x in [a,b,u,bounds]), 'exact binary64 arrays required'
    assert a.ndim == b.ndim == u.ndim == 1 and bounds.shape == (len(a), len(u)), 'array shapes'
    assert len(a) == len(b) == expected_cells, 'necessary closed time cell missing'
    assert len(u) == 513 and np.array_equal(u, np.arange(513, dtype=np.float64)/8), 'necessary frequency missing'
    assert all(np.all(np.isfinite(x)) for x in [a,b,u,bounds]), 'nonfinite endpoint'
    assert a[0] == 0 and b[-1] == .5, 'startup or terminal time omitted'
    assert np.all(a < b) and np.array_equal(b[:-1], a[1:]), 'gap or overlap in ordered exact time cover'
    assert np.all(bounds >= 0), 'negative residual upper endpoint'
    maxima = np.max(bounds, axis=0)  # selection, no floating-point sum
    exact = [str(Q.from_float(float(x))) for x in maxima]
    assert exact == expected, 'complete residual endpoints do not reproduce frozen values'
    return exact

def check():
    import numpy as np
    started = 0
    contract = load(HERE/'time-local-contract.json')
    assert contract['partition']['bins'] == 128 and contract['partition']['edge_formula'] == 'j/256 for j=0,...,128'
    fresh = load(HERE/'fresh-all-node-time-residual.json')
    assert fresh['alpha_exact'] == fresh['beta_exact'] == '13/25'
    assert fresh['T_exact'] == '1/2' and fresh['nu_exact'] == '2897/10000'
    assert fresh['approx_left_halfplane_certified'] is True
    assert fresh['frequency_scope'] == 'fixed dyadic nodes only' and len(fresh['u']) == 513
    frozen = load(FROZEN/'field-residual-certificate-point052-v3-u64.json')
    assert fresh['delta_physical_upper_exact_dyadics'] == frozen['delta_physical_upper_exact_dyadics']
    assert fresh['first_cell_physical_upper_exact_dyadics'] == frozen['first_cell_physical_upper_exact_dyadics']
    assert fresh['first_cell_Re_H_div_talpha_upper_exact_dyadics'] == frozen['first_cell_Re_H_div_talpha_upper_exact_dyadics']
    assert fresh['later_cells_Re_H_upper_exact_dyadics'] == frozen['later_cells_Re_H_upper_exact_dyadics']
    manifest = {r['path']:r['sha256'] for r in load(BASE/'code/MANIFEST.json')['artifacts']}
    for name in ['field-residual-certificate-point052-v3-u64.json', 'fixed-field-betap52-u128.npz']:
        assert sha(FROZEN/name) == manifest['code/frozen/'+name], 'frozen bytes changed'
    assert fresh['field_sha256'] == sha(FROZEN/'fixed-field-betap52-u128.npz')
    src = BASE/'code/src/certify-field-residual-v3.py'
    journal = load(HERE/'time-instrumentation.json')
    assert journal['status'] == 'STORAGE_ONLY_INSTRUMENTATION'
    assert journal['base_generator_sha256'] == sha(src)
    generated = HERE/'continuous-residual-with-time.py'
    assert fresh['source_sha256'] == journal['generated_source_sha256'] == sha(generated)
    expected_changes = [
        ("BASE=Path(__file__).parent", "BASE=Path(__file__).resolve().parents[1]/'english-heston-release'/'code'/'src'"),
        ("    aa=np.array(aa);bb=np.array(bb);cell=np.array(cell)", "    aa=np.array(aa);bb=np.array(bb);cell=np.array(cell)\n    retained=np.empty((len(aa)+1,len(u)),dtype=np.float64);retained[0]=first"),
        ("        bound=UP(point+UP(radius[:,None]*derivative_bound))", "        bound=UP(point+UP(radius[:,None]*derivative_bound))\n        retained[start+1:start+1+len(a)]=bound"),
        ("    assert hashlib.sha256(path.read_bytes()).hexdigest()==field_hash", "    time_path=Path(__file__).with_name('time-residual-alpha-13_25.npz')\n    np.savez_compressed(time_path,a=np.r_[0.,aa],b=np.r_[t[1],bb],u=u,residual_physical_upper=retained)\n    assert hashlib.sha256(path.read_bytes()).hexdigest()==field_hash"),
        ("      'alpha_exact':str(alpha)", "      'time_envelope_file':time_path.name,'time_envelope_sha256':hashlib.sha256(time_path.read_bytes()).hexdigest(),\n      'alpha_exact':str(alpha)")]
    assert journal['changes'] == [{'before':a, 'after':b} for a,b in expected_changes]
    text = src.read_text(encoding='utf-8')
    for before,after in expected_changes:
        assert text.count(before) == 1
        text = text.replace(before,after)
    assert text == generated.read_text(encoding='utf-8'), 'instrumentation changed mathematics'
    path = HERE/fresh['time_envelope_file']
    assert sha(path) == fresh['time_envelope_sha256']
    with np.load(path, allow_pickle=False) as archive:
        assert set(archive.files) == {'a','b','u','residual_physical_upper'}
        a,b,u,bounds = [archive[n] for n in ['a','b','u','residual_physical_upper']]
    exact = validate_arrays(a,b,u,bounds,frozen['delta_physical_upper_exact_dyadics'],fresh['certified_closed_subintervals'])
    assert [str(Q.from_float(float(x))) for x in bounds[0]] == fresh['first_cell_physical_upper_exact_dyadics']
    with np.load(FROZEN/'fixed-field-betap52-u128.npz',allow_pickle=False) as original:
        times=original['t'];assert a[0]==times[0] and b[0]==times[1]
        aa=[];bb=[]
        for left,right in zip(times[1:-1],times[2:]):
            edges=np.linspace(left,right,int(fresh['split'])+1);edges[0]=left;edges[-1]=right
            aa.extend(edges[:-1]);bb.extend(edges[1:])
        assert np.array_equal(a,np.r_[0.,aa]) and np.array_equal(b,np.r_[times[1],bb]), 'cell endpoints differ from generator partition'
    # Semantic negative controls bypass byte hashes and operate only in memory.
    negatives=[]
    def rejects(name, aa=a, bb=b, uu=u, rr=bounds):
        try: validate_arrays(aa,bb,uu,rr,exact,len(a))
        except AssertionError as exc: negatives.append({'name':name,'status':'PASS_REJECTED','reason':str(exc)})
        else: raise AssertionError('damaged input accepted: '+name)
    rejects('remove_startup_cell',a[1:],b[1:],u,bounds[1:])
    rejects('remove_terminal_cell',a[:-1],b[:-1],u,bounds[:-1])
    bad_b=b.copy();bad_b[len(b)//2]=np.nextafter(bad_b[len(b)//2],-np.inf)
    rejects('insert_time_gap',bb=bad_b)
    bad_u=u.copy();bad_u[1]=np.nextafter(bad_u[1],np.inf)
    rejects('change_frequency',uu=bad_u)
    bad=bounds.copy();bad[0,0]=-1.;rejects('negative_residual_bound',rr=bad)
    bad=bounds.copy();bad[0,0]=np.nextafter(np.max(bounds[:,0]),np.inf)
    rejects('inflate_frozen_complete_endpoint',rr=bad)
    result={'status':'PASS_FULL_TIME_ALL_513_FRESH_RESIDUAL_ENVELOPE_CHECK',
        'alpha':'13/25','T':'1/2','frequencies':513,'closed_time_cells':len(a),
        'all_complete_residual_endpoints_exactly_reproduced':True,
        'all_startup_residual_endpoints_exactly_reproduced':True,
        'all_halfplane_endpoint_arrays_exactly_reproduced':True,
        'full_ordered_closed_time_cover_verified':True,'storage_only_instrumentation_verified':True,
        'negative_controls':negatives,'time_envelope_sha256':sha(path),
        'frozen_field_sha256':fresh['field_sha256'],'generated_source_sha256':sha(generated),
        'implementation_sha256':sha(Path(__file__)),
        'scope':'New execution of the unchanged continuous residual mathematics at all 513 fixed nodes and every closed time cell; this checker reuses no propagation implementation.'}
    return result

if __name__=='__main__':
    result=check()
    (HERE/'time-envelope-verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
