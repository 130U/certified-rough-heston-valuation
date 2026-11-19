"""Bind the current proof source after checking the saved quarter-transfer inputs.

This checks an existing contract and existing fields. It is not a prospective
registration, a new residual calculation, or a mathematical proof checker.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse, hashlib, importlib.util, json, sys
import numpy as np

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('preflight_paths', HERE.parent/'continuous/audit_paths.py')
paths = importlib.util.module_from_spec(spec); spec.loader.exec_module(paths)
BASE = paths.release_root(HERE)
SRC, FROZEN = BASE/'code/src', BASE/'code/frozen'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

def build():
    contract_path = HERE/'transfer-contract.json'
    contract = load(contract_path)
    assert contract['maturity_exact'] == '1/4'
    assert contract['old_certificate_horizon_exact'] == '1/2'
    assert contract['candidate_alpha_exact'] == ['13/25', '3/5', '9/10']
    assert contract['strikes_exact'] == ['4400', '4500']
    assert contract['weights_exact'] == ['1', '-1']
    assert contract['model']['nu'] == '2897/10000'
    assert contract['model']['rho'] == '-1489/2000'
    assert contract['model']['Riccati_kappa'] == '0'
    trusted = {r['path']: r['sha256'] for r in load(BASE/'code/MANIFEST.json')['artifacts']}
    records, inputs = [], {}
    cases = [('13/25', 'fixed-field-betap52-u128', 'residual-node-certificate-point052-u64.json'),
             ('3/5', 'fixed-field-betap6-u128', 'residual-node-certificate-point06-u64.json'),
             ('9/10', 'fixed-field-betap9-u80', 'residual-node-certificate-betap9-u64-.json')]
    for alpha, stem, residual_name in cases:
        field, metadata, residual_path = FROZEN/(stem+'.npz'), FROZEN/(stem+'.json'), FROZEN/residual_name
        for p in [field, metadata, residual_path]:
            digest = sha(p)
            assert digest == trusted['code/frozen/'+p.name], p.name
            inputs['reference/code/frozen/'+p.name] = digest
        meta, residual = load(metadata), load(residual_path)
        assert sha(field) == meta['sha256'] == residual['field_sha256']
        assert field.stat().st_size == meta['bytes']
        assert Q(meta['beta_exact_decimal']) == Q(alpha)
        assert Q(meta['T']) == Q(1,2) and Q(meta['frequency_step']) == Q(1,8)
        assert meta['nu_exact'] == '2897/10000' and meta['rho_exact'] == '-1489/2000' and meta['kappa_exact'] == '0'
        assert residual['status'] == 'EXACT_CONTINUOUS_RESIDUAL_CERTIFICATE'
        assert Q(residual['T']) == Q(1,2) and Q(residual['alpha_lower']) == Q(residual['alpha_upper']) == Q(alpha)
        assert residual['residual_definition'] == 'D_C_t_alpha_Hhat_minus_nu_F'
        assert residual['proof_evidence']
        assert [Q(row['u']) for row in residual['cover']] == [Q(j,8) for j in range(513)]
        assert all(Q(row['delta_physical_upper']) >= 0 and Q(row['approx_halfplane_upper']) <= 0 for row in residual['cover'])
        with np.load(field, allow_pickle=False) as bank:
            t,u,A1,A2,LG = [bank[key] for key in ['t','u','A1','A2','LG']]
            assert all(np.all(np.isfinite(v)) for v in [t,u,A1,A2,LG])
            assert t[0] == 0 and t[-1] == .5 and np.all(np.diff(t) > 0)
            assert np.array_equal(u, np.arange(len(u))/8) and len(u) >= 513
            assert LG.shape == (len(t),len(u)) and A1.shape == A2.shape == u.shape
            assert np.all(LG[0] == 0)
            times = [Q.from_float(float(v)) for v in t]
        T = Q(1,4)
        assert T not in times
        left = max(j for j,value in enumerate(times) if value < T)
        assert times[left] < T < times[left+1]
        ratio = (T-times[left])/(times[left+1]-times[left])
        records.append({'alpha':alpha,'field':field.name,'residual':residual_name,
            'field_sha256':sha(field),'source_horizon':'1/2','quarter_original_knot':False,
            'terminal_cell_index':left,'terminal_cell_exact':[str(times[left]),str(times[left+1])],
            'terminal_interpolation_fraction':str(ratio),'retained_time_nodes_with_new_terminal':left+2,
            'used_frequencies':513})
    sources = {'reference/code/src/'+name:sha(SRC/name) for name in [
        'exact-forward-moments.py','exponent-field-certificate.py','direct-tail-certificate.py',
        'price-profile-diagnostic.py','solver-diagnostic.py']}
    sources['merged-heston-en.md'] = sha(paths.paper_source(HERE))
    return {'status':'PASS_CURRENT_TRANSFER_INPUT_BINDING','contract_sha256':sha(contract_path),
        'executed_checker_sha256':sha(Path(__file__)),'records':records,'source_sha256':sources,
        'saved_input_sha256':inputs,
        'scope':'Current input identity, complete saved-field shape and dyadic terminal interpolation checks for the existing quarter contract. The current manuscript is an identified proof dependency, not machine-verified by this check.',
        'continuous_derivatives_regenerated':False,
        'limitations':'Saved continuous residual validity and strict arithmetic theory remain inherited. Quarter output, exponent, tail and complete error accounts must be reconstructed and read independently; this is not a new prospective registration.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    result=build();target=HERE/'transfer-preflight.json'
    if args.check:
        assert load(target)==result,'current transfer input binding differs from saved record'
    else:
        target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(result['status'],len(result['records']),'fields; current proof',result['source_sha256']['merged-heston-en.md'])

if __name__=='__main__':
    main()
