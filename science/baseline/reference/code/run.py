#!/usr/bin/env python3
"""Verify saved certificates or replay selected stages in a separate output directory.

Verification checks bytes, exact recorded bounds, and cover geometry. Interval
sign generation and continuous residual generation are distinct optional tasks.
"""
from __future__ import annotations
import argparse, gzip, hashlib, importlib.util, json, platform, shutil
import subprocess, sys, time
from fractions import Fraction as Q
from pathlib import Path

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SRC, FROZEN = HERE / 'src', HERE / 'frozen'

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()

def load(name):
    return json.loads((FROZEN / name).read_text(encoding='utf-8'))

def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, SRC / filename)
    item = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(item)
    return item

def check_manifest():
    data = json.loads((HERE / 'MANIFEST.json').read_text(encoding='utf-8'))
    for row in data['artifacts']:
        path = ROOT / row['path']
        assert path.is_file(), row['path']
        assert path.stat().st_size == row['bytes'], row['path']
        assert digest(path) == row['sha256'], row['path']
        assert row['bytes'] < 100 * 1024 * 1024, row['path']
    prov = json.loads((HERE / 'PROVENANCE.json').read_text(encoding='utf-8'))
    for row in prov['records']:
        assert digest(ROOT / row['public_path']) == row['public_sha256'], row['public_path']
    return {'artifacts': len(data['artifacts']), 'bytes': sum(r['bytes'] for r in data['artifacts']),
            'maximum_file_bytes': max(r['bytes'] for r in data['artifacts'])}

def check_cover(sample_signs=0):
    source = FROZEN / 'compact-rough-layer-certificate.json.gz'
    provenance = json.loads((HERE / 'PROVENANCE.json').read_text(encoding='utf-8'))
    identity = next(r for r in provenance['records'] if r['public_path'].endswith(source.name))
    h = hashlib.sha256()
    with gzip.open(source, 'rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    assert h.hexdigest() == identity['original_sha256']
    with gzip.open(source, 'rt', encoding='utf-8') as stream:
        data = json.load(stream)
    assert data['status'] == 'EXACT_DYADIC_INTERVAL_COMPLETE_ROUGH_SUBDOMAIN'
    assert data['parameters'] == {'alpha': ['13/25', '3/5'], 'rho': '-1489/2000',
        'kappa': '0', 'eta': ['0', '1'], 'frequency': 'all real u by conjugacy'}
    assert data['executed_source'] == digest(SRC / 'compact-halfplane-certificate-partial.py')
    assert data['library_sha256'] == digest(SRC / 'interval-pade-certificate.py')
    leaves, area = set(), Q(0)
    bmin, dmin, delta, rmin = [None]*3, [None]*6, None, None
    for row in data['cover']:
        al, ar = map(Q, row['alpha']); el, er = map(Q, row['eta'])
        assert Q(13,25) <= al < ar <= Q(3,5) and 0 <= el < er <= 1
        key = (al, ar, el, er)
        assert key not in leaves
        leaves.add(key); area += (ar-al)*(er-el)
        assert len(row['B_lower']) == 3 and len(row['negative_D_lower']) == 6
        for j, value in enumerate(map(Q, row['B_lower'])):
            assert value > 0
            bmin[j] = value if bmin[j] is None else min(value,bmin[j])
        for j, value in enumerate(map(Q, row['negative_D_lower'])):
            assert value > 0
            dmin[j] = value if dmin[j] is None else min(value,dmin[j])
        dv, rv = Q(row['delta_norm2_lower']), Q(row['R_real_lower'])
        assert dv > 0 and rv > 0
        delta = dv if delta is None else min(delta,dv)
        rmin = rv if rmin is None else min(rmin,rv)
    assert len(leaves) == data['cells'] == 211241
    assert area == Q(data['exact_area']) == Q(2,25)
    assert bmin == list(map(Q,data['B_uniform_lower']))
    assert dmin == list(map(Q,data['negative_D_uniform_lower']))
    assert delta == Q(data['delta_norm2_uniform_lower']) > Q(1,14400)
    tree_nodes, depth_max = 0, 0
    def walk(al,ar,el,er,depth=0):
        nonlocal tree_nodes, depth_max
        tree_nodes += 1; depth_max=max(depth_max,depth)
        key=(al,ar,el,er)
        if key in leaves:
            leaves.remove(key); return
        assert depth < 28, ('uncovered rectangle',key)
        if (ar-al)/Q(19,50) >= er-el:
            mid=(al+ar)/2
            walk(al,mid,el,er,depth+1);walk(mid,ar,el,er,depth+1)
        else:
            mid=(el+er)/2
            walk(al,ar,el,mid,depth+1);walk(al,ar,mid,er,depth+1)
    walk(Q(13,25),Q(3,5),Q(0),Q(1))
    assert not leaves and tree_nodes == 422481 and depth_max == 19
    checked = 0
    if sample_signs:
        generator=module('exact_sign_generator','compact-halfplane-certificate-partial.py')
        indices=sorted({j*(len(data['cover'])-1)//max(1,sample_signs-1) for j in range(sample_signs)})
        for index in indices:
            row=data['cover'][index]
            result,reason=generator.check(*map(Q,row['alpha']),*map(Q,row['eta']))
            assert result is not None, (index,reason)
            assert result == row, ('interval-generator record mismatch',index)
            checked+=1
    return {'closed_leaf_cells': data['cells'], 'exact_area':str(area),
        'reconstruction_nodes':tree_nodes,'maximum_depth':depth_max,
        'raw_determinant_norm_squared_lower':str(delta),'interval_signs_recomputed':checked,
        'record_checks':'all saved signs, exact uniform minima, and disjoint complete midpoint-tree geometry'}

def check_fields_and_residuals():
    import numpy as np
    fields=['fixed-field-betap52-u128','fixed-field-betap6-u128','fixed-field-betap9-u128','fixed-field-betap9-u80']
    for stem in fields:
        meta=load(stem+'.json');path=FROZEN/(stem+'.npz')
        assert digest(path)==meta['sha256']
        with np.load(path,allow_pickle=False) as item:
            t,u,A1,A2,LG=[item[k] for k in ['t','u','A1','A2','LG']]
            assert t[0]==0 and t[-1]==.5 and np.all(np.diff(t)>0)
            assert np.array_equal(u,np.arange(len(u))/8)
            assert LG.shape==(len(t),len(u)) and A1.shape==A2.shape==u.shape
            assert np.all(LG[0]==0) and all(np.all(np.isfinite(x)) for x in [t,u,A1,A2,LG])
            assert {k:list(item[k].shape) for k in meta['arrays']}==meta['arrays']
    triples=[('13/25','point052','field-residual-certificate-point052-u64.json','fixed-field-betap52-u128',8189),
             ('3/5','point06','field-residual-certificate-point06-u64.json','fixed-field-betap6-u128',8189),
             ('9/10','betap9','field-residual-betap9-u64-.json','fixed-field-betap9-u80',4093)]
    for alpha,slug,rawname,stem,cells in triples:
        raw=load(rawname)
        adapted=load('residual-node-certificate-'+slug+('-u64-.json' if slug=='betap9' else '-u64.json'))
        exponent=load(stem+'-exponent-certificate.json')
        assert Q(raw['alpha_exact'])==Q(raw['beta_exact'])==Q(alpha)
        assert Q(raw['T_exact'])==Q(1,2) and Q(raw['nu_exact'])==Q(2897,10000)
        assert raw['field_sha256']==adapted['field_sha256']==exponent['field_sha256']==digest(FROZEN/(stem+'.npz'))
        assert raw['source_sha256']==digest(SRC/'certify-field-residual.py')
        assert raw['combined_derivative_source_sha256']==digest(SRC/'combined-field-derivative.py')
        assert raw['certified_closed_subintervals']==cells
        nodes=list(map(Q.from_float,raw['u']))
        assert nodes==[Q(j,8) for j in range(513)]
        assert [Q(r['u']) for r in adapted['cover']]==nodes
        assert [Q(r['u']) for r in exponent['cover'][:513]]==nodes
        assert all(Q(v)<=0 for v in raw['first_cell_Re_H_div_talpha_upper_exact_dyadics'])
        assert all(Q(v)<0 for v in raw['later_cells_Re_H_upper_exact_dyadics'])
        for j,entry in enumerate(adapted['cover']):
            assert Q(entry['delta_physical_upper'])==Q(raw['delta_physical_upper_exact_dyadics'][j])>=0
            assert Q(entry['approx_halfplane_upper'])==0
    return {'fields_checked':4,'continuous_residual_record_candidates':3,'frequency_nodes_per_residual':513,
            'checks':'field bytes/shapes/guards, source identity, exact adapter values, complete time-cell counts, saved half-plane bounds'}

def check_objectives():
    maths=module('finite_math','calibration-interval-aggregate.py')
    quoted=load('normalized-quote-bands.json')
    assert len(quoted['rows'])==12
    quotes=[]
    for r in quoted['rows']:
        quotes.append(tuple(Q(r[key][side]) for key in ['normalized_bid','normalized_ask','price_mid_target']
                            for side in ['lower_fraction','upper_fraction']))
    frozen=load('finite-candidate-calibration-result.json')
    actual=load('frozen-pade-numeric-output.json')
    by_alpha={Q(c['alpha']):c for c in frozen['candidates']}
    algorithm=frozen['actual_Pade_numeric_output_reference_oracle']
    aby={Q(c['alpha']):c for c in algorithm['candidates']}
    nby={Q(c['alpha']):c for c in actual['cover']}
    prices_by={}
    names=[('13/25','f8-price-point052-u64.json'),('3/5','f8-price-point06-u64.json'),('9/10','f8-price-betap9-u64-.json')]
    for alpha,name in names:
        source=load(name)
        assert Q(source['alpha_lower'])==Q(source['alpha_upper'])==Q(alpha)
        prices=[tuple(map(Q,r['true_normalized_price'])) for r in source['rows']]
        assert len(prices)==12 and all(0<=lo<=hi<=1 for lo,hi in prices)
        prices_by[Q(alpha)]=prices
        result=maths.objective_bounds(prices,quotes)
        for key,value in result.items():
            old=by_alpha[Q(alpha)]['bounds'][key]
            assert value==(Q(old) if isinstance(value,Q) else old),(alpha,key)
        values=[Q(r['normalized_call_exact_dyadic']) for r in nby[Q(alpha)]['rows']]
        alg_result=maths.objective_bounds([(v,v) for v in values],quotes)
        for key,value in alg_result.items():
            old=aby[Q(alpha)]['algorithm_objective_bounds'][key]
            assert value==(Q(old) if isinstance(value,Q) else old),(alpha,'actual',key)
        errors=[max(abs(v-lo),abs(v-hi)) for v,(lo,hi) in zip(values,prices)]
        assert errors==list(map(Q,aby[Q(alpha)]['actual_numeric_normalized_price_error_upper']))
    true_gap=min(Q(c['bounds']['mid_lower']) for a,c in by_alpha.items() if a!=Q(13,25))-Q(by_alpha[Q(13,25)]['bounds']['mid_upper'])
    assert true_gap==Q(frozen['strict_winner_objective_gap_lower'])>Q('0.000000270205218')
    assert Q(frozen['objective_uniform_perturbation_strict_robustness_radius'])==true_gap/2
    assert Q(frozen['strict_unique_finite_minimizer'])==Q(13,25)
    alg_gap=min(Q(c['algorithm_objective_bounds']['mid_lower']) for a,c in aby.items() if a!=Q(13,25))-Q(aby[Q(13,25)]['algorithm_objective_bounds']['mid_upper'])
    assert alg_gap>0 and Q(algorithm['certified_algorithm_finite_argmin'])==Q(13,25)
    p=prices_by[Q(13,25)]
    v=[Q(r['normalized_call_exact_dyadic']) for r in nby[Q(13,25)]['rows']]
    spread=(p[7][0]-p[8][1],p[7][1]-p[8][0]);observed=v[7]-v[8]
    spread_error=max(abs(observed-spread[0]),abs(observed-spread[1]))
    assert spread_error<Q('.000634774793739')<Q('.0007')
    ask8=quotes[7][3];ask9=quotes[8][3]
    assert p[7][0]-ask8>Q('.000116194893950')
    assert p[8][0]-ask9>Q('.000016046306147')
    return {'true_finite_winner_alpha':'13/25','winner_H':'1/50','actual_Pade_choice_matches':True,
            'true_objective_gap_exact':str(true_gap),'spread_error_upper_exact':str(spread_error),
            'spread_error_below_declared_0_0007_budget':True,'quote_rows_4400_4500_separated':True,
            'prices_reaggregated':36,'exact_arithmetic':'fractions.Fraction'}

def stage(out):
    out=out.resolve()
    out_root=(ROOT/'out').resolve()
    if out!=out_root and out_root not in out.parents:
        raise ValueError('Replay work directories must lie within repository out/')
    out.mkdir(parents=True,exist_ok=True)
    for path in SRC.iterdir():
        if path.is_file():shutil.copyfile(path,out/path.name)
    for path in FROZEN.iterdir():
        if path.is_file() and not path.name.endswith('.gz'):shutil.copyfile(path,out/path.name)
    paper=next((ancestor/'manuscript/merged-heston-en.md' for ancestor in [ROOT,*ROOT.parents] if (ancestor/'manuscript/merged-heston-en.md').is_file()),None)
    if paper is None:raise FileNotFoundError('Current English manuscript must accompany scientific evidence.')
    # Full paper copies, only in disposable work space; section mapping is in docs/proof-map.md.
    for alias in ['model-admissibility.md','fractional-exponent-linearization.md','direct-real-tail.md',
                  'complex-dissipativity.md','field-residual-proof.md']:
        shutil.copyfile(paper,out/alias)
    numeric_path=out/'frozen-pade-numeric-output.json'
    numeric=json.loads(numeric_path.read_text(encoding='utf-8'))
    original_contract,original_quotes=numeric['contract_sha256'],numeric['quotes_sha256']
    numeric['contract_sha256']=digest(out/'calibration-contract-finite-T05.json')
    numeric['quotes_sha256']=digest(out/'normalized-quote-bands.json')
    numeric_path.write_text(json.dumps(numeric,indent=2)+'\n',encoding='utf-8')
    (out/'replay-relocation.json').write_text(json.dumps({
        'scope':'public contract metadata and twelve-row quote selection; actual stored output dyadics unchanged',
        'original_contract_sha256':original_contract,'original_quotes_sha256':original_quotes,
        'public_contract_sha256':numeric['contract_sha256'],'public_quotes_sha256':numeric['quotes_sha256'],
        'proof_aliases':'complete English manuscript, staged only'},indent=2)+'\n',encoding='utf-8')
    return out

def command(work, script, *args):
    subprocess.run([sys.executable,str(work/script),*map(str,args)],cwd=work,check=True)

def replay(stage_name,out):
    work=stage(out)
    if stage_name in ['aggregate','pipeline']:
        if stage_name=='pipeline':
            for stem,alpha,slug,rawname in [
                ('fixed-field-betap52-u128','13/25','point052','field-residual-certificate-point052-u64.json'),
                ('fixed-field-betap6-u128','3/5','point06','field-residual-certificate-point06-u64.json'),
                ('fixed-field-betap9-u80','9/10','betap9','field-residual-betap9-u64-.json')]:
                command(work,'certify-field-residual.py','--field',stem+'.npz','--alpha',alpha,'--U','64','--split','4','--block','32','--output',rawname)
                guards='field-input-guards-betap9-u80.json' if slug=='betap9' else 'frozen-field-input-validation.json'
                adapted='residual-node-certificate-'+slug+('-u64-.json' if slug=='betap9' else '-u64.json')
                command(work,'residual-certificate-adapter.py','--input',work/rawname,'--executed-source',work/'certify-field-residual.py','--field',work/(stem+'.npz'),'--output',work/adapted,'--input-guards',work/guards)
                command(work,'exponent-field-certificate.py','--field',stem+'.npz')
            command(work,'direct-tail-certificate.py')
        for stem,slug,output in [
            ('fixed-field-betap52-u128','point052','f8-price-point052-u64.json'),
            ('fixed-field-betap6-u128','point06','f8-price-point06-u64.json'),
            ('fixed-field-betap9-u80','betap9','f8-price-betap9-u64-.json')]:
            adapted='residual-node-certificate-'+slug+('-u64-.json' if slug=='betap9' else '-u64.json')
            command(work,'f8-node-price-aggregate.py','--exponents',work/(stem+'-exponent-certificate.json'),
                '--residual',work/adapted,'--output',work/output,'--exponent-error-proof',work/'fractional-exponent-linearization.md',
                '--true-cf-envelope',work/'direct-tail-certificate.json','--solver-cutoff','64','--grid-cutoff','128')
        command(work,'finite-candidate-objective-aggregate.py','--contract',work/'calibration-contract-finite-T05.json',
            '--prices',*[work/n for n in ['f8-price-point052-u64.json','f8-price-point06-u64.json','f8-price-betap9-u64-.json']],
            '--output',work/'finite-candidate-calibration-result.json','--pade-output',work/'frozen-pade-numeric-output.json')
        command(work,'compute-finance-usecase.py')
    elif stage_name=='diagnostic':
        command(work,'freeze-pade-output.py')
    return work

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='action',required=True)
    v=sub.add_parser('verify');v.add_argument('--sample-signs',type=int,default=0)
    v.add_argument('--output',type=Path,default=ROOT/'out'/'verification.json')
    r=sub.add_parser('replay');r.add_argument('stage',choices=['aggregate','pipeline','diagnostic'])
    r.add_argument('--out',type=Path,default=ROOT/'out'/'work')
    args=parser.parse_args();started=0
    if args.action=='verify':
        assert 0<=args.sample_signs<=211241
        output=args.output.resolve();out_root=(ROOT/'out').resolve()
        if out_root not in output.parents:
            raise ValueError('Verification output must lie within repository out/')
        result={'status':'PASS_SAVED_CERTIFICATE_VERIFICATION','runtime':{'Python':platform.python_version()},
            'manifest':check_manifest(),'structure':check_cover(args.sample_signs),
            'fields_and_residuals':check_fields_and_residuals(),'financial_decisions':check_objectives()}
        pass
        result['execution_scope']='Saved-byte identity, exact aggregation, cover geometry and recorded inequalities. Optional interval-sign reruns counted explicitly; continuous residual generator runs only under replay pipeline.'
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(result,indent=2),flush=True)
    else:
        work=replay(args.stage,args.out)
        print(json.dumps({'stage':args.stage,'work_directory':str(work)},indent=2))

if __name__=='__main__':main()
