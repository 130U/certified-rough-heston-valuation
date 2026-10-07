"""Separate all-cell/weight readback of the descriptive local-output control."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,importlib.util,json,sys
import numpy as np
HERE=Path(__file__).resolve().parent;SDK=HERE/'sdk';OUT=HERE/'local128';NU=Q(2897,10000);F=Q(211093,50);sys.dont_write_bytecode=True
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def exact(v):return Q.from_float(float(v))
def main():
    base=load(HERE/'N2048/candidate-13_25.json');point=load(HERE/'N2048/point-independent-13_25.json');candidate=load(OUT/'candidate-13_25.json');weights=load(OUT/'weights-and-envelopes.json');contract=load(OUT/'contract.json')
    assert point['candidate_sha256']==sha(HERE/'N2048/candidate-13_25.json') and point['status']=='PASS_COMPLETE_POINT_RECONSTRUCTION'
    assert candidate['source_candidate_sha256']==contract['source_candidate_sha256']==sha(HERE/'N2048/candidate-13_25.json')
    assert candidate['descriptive_contract_sha256']==weights['contract_sha256']==sha(OUT/'contract.json')
    assert weights['source_bank_sha256']==base['bank_sha256']==sha(HERE/'N2048/field-13_25-residual-cells.npz')
    bank={k:v for k,v in np.load(HERE/'N2048/field-13_25-residual-cells.npz').items()}
    sp=importlib.util.spec_from_file_location('ind_local_component',SDK/'exponent-field-certificate.py');comp=importlib.util.module_from_spec(sp);sp.loader.exec_module(comp);mo,dy,I,S,C=comp.mo,comp.mo.dy,comp.I,comp.S,comp.C
    def iv(b):
        lo,hi=map(Q,b);return I((lo.numerator*S)//lo.denominator,-((-hi.numerator*S)//hi.denominator),True)
    def norm(c):return Q(c.norm2().sqrt().hi,S)
    ws=[];envelopes=[]
    assert len(weights['records'])==128
    for k,r in enumerate(weights['records']):
        a,b=Q(k,256),Q(k+1,256);assert Q(r['left'])==a and Q(r['right'])==b
        w=mo.moments(Q(1,2)-a,64)[0]-mo.moments(Q(1,2)-b,64)[0]
        assert w.bounds()==r['strict_weight'] and w.lo>0;ws.append(Q(w.hi,S))
        cells=np.flatnonzero((bank['a']<=float(b))&(bank['b']>=float(a)))
        assert int(cells[0])==r['first_closed_source_index'] and int(cells[-1])==r['last_closed_source_index'] and len(cells)==r['overlapping_closed_cell_count']
        maxima=list(map(exact,np.max(bank['bound'][cells],axis=0)))
        assert maxima==list(map(Q,r['physical_residual_envelope']));envelopes.append(maxima)
    ex=load(HERE/'N2048/exponents-13_25.json')['rows'];radii=[Q(0)]*12;coeffs=[]
    for j,(r,old) in enumerate(zip(candidate['node_ledger'],base['node_ledger'])):
        assert r['u']==old['u'] and r['coefficients']==old['coefficients'] and r['true_CF_modulus_upper']==old['true_CF_modulus_upper']
        if j<=512:
            eta=sum((w*m[j]/NU for w,m in zip(ws,envelopes)),Q(0));mag=iv(ex[j]['phi_modulus']);cap=I(min(S,mag.lo),min(S,mag.hi),True)
            epsilon=min(Q((cap*(dy.exp_positive(I(eta))-1)).hi,S),Q((I(Q(old['true_CF_modulus_upper']))+mag).hi,S))
            assert eta==Q(r['eta_upper']) and epsilon==Q(r['epsilon_upper']) and epsilon<=Q(old['epsilon_upper'])
        else:epsilon=Q(old['epsilon_upper']);assert r==old
        cs=[C(iv(c['re']),iv(c['im'])) for c in r['coefficients']];coeffs.append(cs)
        for i in range(12):radii[i]+=epsilon*norm(cs[i])
    for i,(r,old) in enumerate(zip(candidate['price_rows'],base['price_rows'])):
        for key in ['strict_reference_centre','actual_fast_output','actual_reference_output_binary64','actual_signed_correction_binary64','actual_corrected_fast_output_binary64','reference_output_rounding_exact','correction_storage_rounding_exact','correction_addition_rounding_exact','strip_remainder','true_infinite_tail_remainder','reference_arithmetic_remainder']:assert r[key]==old[key]
        rem=sum((Q(old[k]) for k in ['strip_remainder','true_infinite_tail_remainder','reference_arithmetic_remainder']),Q(0));radius=radii[i]+rem;centre=Q(old['strict_reference_centre'])
        assert Q(r['complete_reference_radius'])==radius
        assert list(map(Q,r['true_price_interval']))==[max(Q(0),centre-radius),min(Q(1),centre+radius)]
        for kind,col in [('reference','actual_reference_output_binary64'),('corrected_fast','actual_corrected_fast_output_binary64')]:assert Q(r['actual_'+kind+'_complete_bound'])==abs(Q(r[col])-centre)+radius
    jr=sum((Q(r['epsilon_upper'])*norm(c[7]-c[8]) for r,c in zip(candidate['node_ledger'],coeffs)),Q(0));mr=sum((Q(r['epsilon_upper'])*(norm(c[7])+norm(c[8])) for r,c in zip(candidate['node_ledger'],coeffs)),Q(0));prices=candidate['price_rows'];rem=sum((Q(prices[i][k]) for i in [7,8] for k in ['strip_remainder','true_infinite_tail_remainder','reference_arithmetic_remainder']),Q(0));cs=candidate['correction_control'];centre=Q(cs['direct_reference_spread'])
    for kind,col in [('frozen_fast','actual_fast_output'),('reference','actual_reference_output_binary64'),('corrected_fast','actual_corrected_fast_output_binary64')]:
        shift=abs(Q(prices[7][col])-Q(prices[8][col])-centre)
        key='uncorrected_fast_' if kind=='frozen_fast' else 'actual_binary64_'+kind+'_'
        assert Q(cs[key+'joint_complete_bound_points' if kind=='frozen_fast' else key+'joint_bound_points'])==(shift+jr+rem)*F
        assert Q(cs[key+'marginal_complete_bound_points' if kind=='frozen_fast' else key+'marginal_bound_points'])==(shift+mr+rem)*F
    out={'status':'PASS_SEPARATE_DESCRIPTIVE_128_BIN_ALL_CLOSED_CELL_CONTROL',
       'bins':128,'source_closed_residual_entries':513*4095,'weighted_residual_terms_checked':128*513,
       'new_continuous_residual_entries_generated':0,'candidate_sha256':sha(OUT/'candidate-13_25.json'),
       'reader_sha256':sha(Path(__file__)),'main_grid_unchanged':True,
       'sharing_boundary':'inherits the separately validated entire N2048 point proof; independently rebuilds all 128 bin masses, all intersecting closed-cell maxima, 513 tightened radii, all price and returned-output bounds; same rigorous primitives'}
    (OUT/'independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS independent local-output complete account',flush=True)
if __name__=='__main__':main()
