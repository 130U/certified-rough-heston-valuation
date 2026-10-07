"""Semantic negative controls on in-memory copies, after byte-identity checks.

These tests intentionally bypass hashes: rejection must follow from mathematics.
"""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
import copy, gzip, importlib.util, json, sys, time
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
from audit_paths import release_root
RELEASE=release_root(HERE)

def load_module(name,path):
    sp=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(sp)
    sys.modules[name]=mod;sp.loader.exec_module(mod);return mod

def structural_records(data):
    assert len(data['cover'])==data['cells']==211241,'required leaf missing'
    area=Q(0)
    for row in data['cover']:
        a,b=map(Q,row['alpha']);c,d=map(Q,row['eta'])
        assert Q(13,25)<=a<b<=Q(3,5) and 0<=c<d<=1,'out-of-domain rectangle'
        assert all(Q(x)>0 for x in row['B_lower']+row['negative_D_lower']),'nonpositive sign margin'
        assert Q(row['delta_norm2_lower'])>0,'determinant not separated'
        area+=(b-a)*(d-c)
    assert area==Q(2,25),'incomplete or excess area'

def terminal_primal_dual(data,result):
    A=[list(map(Q,row)) for row in data['P_A']];b=list(map(Q,data['P_b']))
    p=list(map(Q,result['Asian']['pi']));y=list(map(Q,result['Asian']['dual']))
    c=list(map(Q,data['profiles'][0]));n=len(p)
    assert len(A)==len(b)==22 and n==102
    assert all(x>=0 for x in p) and sum(p)==1,'primal probability'
    for a,bi in zip(A,b):assert sum((x*z for x,z in zip(a,p)),Q(0))<=bi,'primal constraint direction'
    assert all(x>=0 for x in y),'dual multiplier sign'
    assert all(sum((row[j]*yy for row,yy in zip(A,y)),Q(0))>=c[j] for j in range(n)),'dual feasibility'
    assert sum((ci*pi for ci,pi in zip(c,p)),Q(0))==sum((bi*yi for bi,yi in zip(b,y)),Q(0)),'primal dual equality'

def main():
    result={'status':'RUNNING','tests':[]};started=0
    def test(name,fn,should_fail=False):
        t=0
        try:fn();rejected=False;reason=None
        except (AssertionError,KeyError,ValueError) as exc:rejected=True;reason=str(exc)
        passed=rejected if should_fail else not rejected
        result['tests'].append({'name':name,'deliberate_corruption':should_fail,'semantic_rejection':rejected,
                                'status':'PASS' if passed else 'FAIL','reason':reason})
        print(json.dumps(result['tests'][-1]),flush=True)
    with gzip.open(RELEASE/'code'/'frozen'/'compact-rough-layer-certificate.json.gz','rt',encoding='utf-8') as stream:data=json.load(stream)
    test('valid_structure_records',lambda:structural_records(data))
    dropped=dict(data);dropped['cover']=data['cover'][:-1]
    test('delete_necessary_leaf',lambda:structural_records(dropped),True)
    old=data['cover'][0]['B_lower'][0];data['cover'][0]['B_lower'][0]='-1'
    test('flip_strict_leaf_sign',lambda:structural_records(data),True);data['cover'][0]['B_lower'][0]=old
    gen=load_module('sample_signs',RELEASE/'code'/'src'/'compact-halfplane-certificate-partial.py')
    indices=[j*(len(data['cover'])-1)//63 for j in range(64)]
    times=[]
    for index in indices:
        row=data['cover'][index];t=0
        record,reason=gen.check(*map(Q,row['alpha']),*map(Q,row['eta']))
        assert record==row,(index,reason);times.append(0-t)
    result['additional_structure_sign_regeneration']={'leaves':64,'indices':indices,
        
        
        
        'scope':'A sample-based cost estimate, not a verified runtime guarantee or full sign verification.'}
    inflated=copy.deepcopy(data['cover'][0]);inflated['B_lower'][0]=str(Q(inflated['B_lower'][0])+1)
    def regenerated_leaf_reject():
        record,_=gen.check(*map(Q,inflated['alpha']),*map(Q,inflated['eta']))
        assert record==inflated,'strictly positive but inflated margin differs from generated interval evidence'
    test('inflate_positive_margin',regenerated_leaf_reject,True)
    del data
    cbase=RELEASE/'code'/'classical'
    inp=json.loads((cbase/'terminal767-input.json').read_text(encoding='utf-8-sig'))
    res=json.loads((cbase/'terminal767-result.json').read_text(encoding='utf-8-sig'))
    test('valid_terminal_primal_dual',lambda:terminal_primal_dual(inp,res))
    changed=copy.deepcopy(inp);changed['P_A'][-1]=['1']*102 # keep b=-1: impossible altered mass row
    test('flip_probability_constraint_direction',lambda:terminal_primal_dual(changed,res),True)
    changed_res=copy.deepcopy(res);idx=next(i for i,v in enumerate(changed_res['Asian']['dual']) if Q(v)>0)
    changed_res['Asian']['dual'][idx]=str(-Q(changed_res['Asian']['dual'][idx]))
    test('wrong_dual_multiplier_sign',lambda:terminal_primal_dual(inp,changed_res),True)
    shared=load_module('new_joint_support',HERE/'shared_fourier_spread.py')
    p=shared.load('f8-price-point052-u64.json')
    test('valid_shared_frequency_cover',lambda:shared.validate_cover(p))
    changed=copy.deepcopy(p);changed['node_error_cover'].pop(512)
    test('delete_shared_finite_node',lambda:shared.validate_cover(changed),True)
    changed=copy.deepcopy(p);changed['node_error_cover'][0]['true_CF_minus_stored_CF_modulus_upper']='-1'
    test('negative_CF_disk_radius',lambda:shared.validate_cover(changed),True)
    changed=copy.deepcopy(p);del changed['rows'][0]['budgets']['true_discrete_tail']
    test('delete_true_infinite_tail_budget',lambda:shared.validate_cover(changed),True)
    result['status']='PASS_ALL_SEMANTIC_NEGATIVE_CONTROLS' if all(r['status']=='PASS' for r in result['tests']) else 'FAIL'
    result['hashes_bypassed_for_negative_controls']=True
    result['generator_scope']='Reused executed raw polynomial interval generator for 64 evenly spaced leaves; portable downstream semantic checks contain no hash assertions.'
    pass
    (HERE/'adversarial-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result['additional_structure_sign_regeneration'],indent=2),flush=True)
    assert result['status']=='PASS_ALL_SEMANTIC_NEGATIVE_CONTROLS', 'Semantic negative-control suite failed'

if __name__=='__main__':main()
