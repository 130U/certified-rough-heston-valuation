"""Separate descriptive time-local output-value control; grid study unchanged."""
from pathlib import Path
from fractions import Fraction as Q
import copy,hashlib,importlib.util,json,sys
import numpy as np
HERE=Path(__file__).resolve().parent;SDK=HERE/'sdk';OUT=HERE/'local128';OUT.mkdir(exist_ok=True);NU=Q(2897,10000);F=Q(211093,50);sys.dont_write_bytecode=True
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,o):p.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def exact(x):return Q.from_float(float(x))
def main():
    source=HERE/'N2048/candidate-13_25.json';base=load(source)
    contract={'status':'DESCRIPTIVE_DESIGN_FROZEN_AFTER_GLOBAL_CONTROL_BEFORE_LOCAL_RESULT',
      'alpha':'13/25','N':2048,'T':'1/2','bins':128,'edges':'T*j/128, j=0..128',
      'source_candidate_sha256':sha(source),'known_global_control_joint_reference_bound_points':base['correction_control']['actual_binary64_reference_joint_bound_points'],
      'target':'same frozen Padé, binary64 reference/correction and modern BL core outputs; same model/task/quarter-point tolerance',
      'rule':'maximum over ALL closed source cells intersecting each closed propagation bin, including crossed endpoints; unchanged full history from zero',
      'independence':'separate descriptive control only; initial nearby-candidate N1024/N2048 objective experiment and its outcomes remain untouched'}
    cp=OUT/'contract.json';encoded=json.dumps(contract,indent=2)+'\n'
    if cp.exists():assert cp.read_text(encoding='utf-8')==encoded
    else:cp.write_text(encoded,encoding='utf-8')
    spec=importlib.util.spec_from_file_location('local_output_component',SDK/'exponent-field-certificate.py');comp=importlib.util.module_from_spec(spec);spec.loader.exec_module(comp);mo,dy,I,S,C=comp.mo,comp.mo.dy,comp.I,comp.S,comp.C
    def iv(b):
        lo,hi=map(Q,b);return I((lo.numerator*S)//lo.denominator,-((-hi.numerator*S)//hi.denominator),True)
    def norm(c):return Q(c.norm2().sqrt().hi,S)
    bank={k:v for k,v in np.load(HERE/'N2048/field-13_25-residual-cells.npz').items()};edges=[Q(j,256) for j in range(129)]
    weights=[];cell_records=[];envelopes=[]
    for left,right in zip(edges[:-1],edges[1:]):
        w=mo.moments(Q(1,2)-left,64)[0]-mo.moments(Q(1,2)-right,64)[0];assert w.lo>0;weights.append(Q(w.hi,S))
        included=np.flatnonzero((bank['a']<=float(right))&(bank['b']>=float(left)));assert len(included)
        r=np.max(bank['bound'][included],axis=0);envelopes.append(list(map(exact,r)))
        cell_records.append({'left':str(left),'right':str(right),'strict_weight':w.bounds(),
            'first_closed_source_index':int(included[0]),'last_closed_source_index':int(included[-1]),
            'overlapping_closed_cell_count':len(included),'physical_residual_envelope':list(map(str,envelopes[-1]))})
    ex=load(HERE/'N2048/exponents-13_25.json')['rows'];out=copy.deepcopy(base);radii=[Q(0)]*12;coeffs=[]
    for j,node in enumerate(out['node_ledger']):
        if j<=512:
            eta=sum((w*r[j]/NU for w,r in zip(weights,envelopes)),Q(0));mag=iv(ex[j]['phi_modulus']);cap=I(min(S,mag.lo),min(S,mag.hi),True)
            eps=min(Q((cap*(dy.exp_positive(I(eta))-1)).hi,S),Q((I(Q(node['true_CF_modulus_upper']))+mag).hi,S))
            assert eps<=Q(base['node_ledger'][j]['epsilon_upper'])
            node['eta_upper']=str(eta);node['epsilon_upper']=str(eps)
        else:eps=Q(node['epsilon_upper'])
        cs=[C(iv(c['re']),iv(c['im'])) for c in node['coefficients']];coeffs.append(cs)
        for i in range(12):radii[i]+=eps*norm(cs[i])
    prices=out['price_rows']
    for i,r in enumerate(prices):
        rem=sum((Q(r[k]) for k in ['strip_remainder','true_infinite_tail_remainder','reference_arithmetic_remainder']),Q(0));radius=radii[i]+rem;centre=Q(r['strict_reference_centre'])
        r['complete_reference_radius']=str(radius);r['frozen_fast_absolute_error_upper']=str(abs(Q(r['centre_correction']))+radius)
        r['true_price_interval']=[str(max(Q(0),centre-radius)),str(min(Q(1),centre+radius))]
        r['actual_reference_complete_bound']=str(abs(Q(r['actual_reference_output_binary64'])-centre)+radius)
        r['actual_corrected_fast_complete_bound']=str(abs(Q(r['actual_corrected_fast_output_binary64'])-centre)+radius)
    jr=Q(0);mr=Q(0)
    for n,cs in zip(out['node_ledger'],coeffs):
        eps=Q(n['epsilon_upper']);jr+=eps*norm(cs[7]-cs[8]);mr+=eps*(norm(cs[7])+norm(cs[8]))
    rem=sum((Q(prices[i][k]) for i in [7,8] for k in ['strip_remainder','true_infinite_tail_remainder','reference_arithmetic_remainder']),Q(0));cs=out['correction_control'];centre=Q(cs['direct_reference_spread']);fast=Q(cs['actual_frozen_fast_spread']);shift=abs(centre-fast)
    cs.update(uncorrected_fast_joint_complete_bound_points=str((shift+jr+rem)*F),uncorrected_fast_marginal_complete_bound_points=str((shift+mr+rem)*F),
       direct_reference_and_corrected_joint_bound_points=str((jr+rem)*F),direct_reference_and_corrected_marginal_bound_points=str((mr+rem)*F))
    for label,field in [('reference','actual_reference_output_binary64'),('corrected_fast','actual_corrected_fast_output_binary64')]:
        returned=Q(prices[7][field])-Q(prices[8][field]);s=abs(returned-centre)
        cs['actual_binary64_'+label+'_joint_bound_points']=str((s+jr+rem)*F);cs['actual_binary64_'+label+'_marginal_bound_points']=str((s+mr+rem)*F)
    out['status']='DESCRIPTIVE_LOCAL128_OUTPUT_CONTROL_NOT_NEARBY_GRID_OBJECTIVE_RESULT'
    # Original objective result is explicitly removed to prevent mislabelling.
    out.pop('objective');out['source_candidate_sha256']=sha(source);out['descriptive_contract_sha256']=sha(cp)
    out['workload'].update(new_continuous_residual_node_cell_entries=0,source_continuous_residual_node_cell_entries=513*4095,
       propagation_bins=128,weighted_residual_terms=128*513,source_reused='identity-checked N2048 complete closed bank; all old source proofs and final remainders retained')
    save(OUT/'weights-and-envelopes.json',{'status':'COMPLETE_ALL_INTERSECTING_CLOSED_CELL_128_BIN_PROPAGATION',
        'contract_sha256':sha(cp),'source_bank_sha256':base['bank_sha256'],'records':cell_records})
    save(OUT/'candidate-13_25.json',out)
    print('PASS descriptive128 control','fast',float(Q(cs['uncorrected_fast_joint_complete_bound_points'])),'reference',float(Q(cs['actual_binary64_reference_joint_bound_points'])),flush=True)
if __name__=='__main__':main()
