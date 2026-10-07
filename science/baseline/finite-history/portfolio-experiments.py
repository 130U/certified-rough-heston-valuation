"""Systematic complete same-output portfolio certificates on frozen real data.

No numerical solver or residual generator is called. Coefficients are prepared
once and reused for every direction and candidate. Proof endpoints use exact
Fraction arithmetic and the released 100-bit outward integer intervals.
"""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
import argparse,hashlib,importlib.util,json,platform,sys,time
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;RELEASE=HERE.parent/'reference'
FROZEN=RELEASE/'code'/'frozen';SRC=RELEASE/'code'/'src'
def load(name):return json.loads((FROZEN/name).read_text(encoding='utf-8'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def pair(lo,hi):return [str(lo),str(hi)]
def absolute(interval):return max(map(abs,interval))
def dot(w,v):return sum((wi*vi for wi,vi in zip(w,v)),Q(0))
def weighted_interval(w,rows):
    lo=hi=Q(0)
    for wi,(a,b) in zip(w,rows):
        lo+=wi*(a if wi>=0 else b);hi+=wi*(b if wi>=0 else a)
    return lo,hi

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--finite-history',action='store_true');args=parser.parse_args()
    start=0;contract_bytes=(HERE/'portfolio-contract.json').read_bytes();contract=json.loads(contract_bytes)
    for name,value in contract['source_sha256'].items():assert sha(FROZEN/name)==value,'input differs from frozen contract'
    sp=importlib.util.spec_from_file_location('portfolio_primitives',SRC/'exponent-field-certificate.py')
    comp=importlib.util.module_from_spec(sp);sp.loader.exec_module(comp);mo=comp.mo;I,C,S=mo.I,mo.dy.C,mo.S
    pade=load('frozen-pade-numeric-output.json')
    candidate_names=['f8-price-point052-u64.json','f8-price-point06-u64.json','f8-price-betap9-u64-.json']
    data=[load(n) for n in candidate_names];scale=Q(contract['discount_D'])*Q(contract['forward_F'])
    m=[Q(r['m']) for r in data[0]['rows']];h=Q(data[0]['h']);nodes=[Q(r['u']) for r in data[0]['node_error_cover']]
    assert len(nodes)==1025 and nodes==[j*h for j in range(1025)]
    assert all([Q(r['m']) for r in d['rows']]==m and [Q(n['u']) for n in d['node_error_cover']]==nodes for d in data)
    read_seconds=0-start
    preparation=0;coeff=[]
    for mi in m:
        k=mo.log_endpoint(mi);pref=I(mi).sqrt()/mo.dy.PI;row=[]
        for index,u in enumerate(nodes):
            phase=-u*k;factor=-h*pref*(2 if index==0 else 1/(u*u+Q(1,4)))
            row.append(C(comp.trig(phase,True),comp.trig(phase))*C(factor))
        coeff.append(row)
    coefficient_seconds=0-preparation
    coefficient_digest=hashlib.sha256(json.dumps([[[c.re.bounds(),c.im.bounds()] for c in row] for row in coeff],separators=(',',':')).encode()).hexdigest()
    records=[];primary_node_accounts=[];candidate_diagnostics=[]
    for name,d in zip(candidate_names,data):
        alpha=Q(d['alpha_lower']);assert alpha==Q(d['alpha_upper'])
        rows=d['rows'];refs=[sum(map(Q,r['stored_field_price']))/2 for r in rows]
        arith=[(Q(r['stored_field_price'][1])-Q(r['stored_field_price'][0]))/2 for r in rows]
        grid=[Q(r['budgets']['grid'][1]) for r in rows];tails=[Q(r['budgets']['true_discrete_tail'][1]) for r in rows]
        remainders=[a+g+t for a,g,t in zip(arith,grid,tails)]
        fast=[Q(r['normalized_call_exact_dyadic']) for p in pade['cover'] if Q(p['alpha'])==alpha for r in p['rows']]
        shifts=[a-b for a,b in zip(refs,fast)]
        price_boxes=[tuple(map(Q,r['true_normalized_price'])) for r in rows]
        eps=[Q(n['true_CF_minus_stored_CF_modulus_upper']) for n in d['node_error_cover']]
        upgraded_receipt=None;coordinate_upgrade_seconds=0
        if args.finite_history:
            p=HERE/('finite-history-nodes-alpha-'+str(alpha).replace('/','_')+'.json')
            upgraded_receipt={'file':p.name,'sha256':sha(p)}
            e_new=list(map(Q,json.loads(p.read_text())['all_node_radii']))
            assert len(e_new)==len(eps) and all(0<=new<=old for new,old in zip(e_new,eps))
            eps=e_new;t=0;tightened=[]
            for i in range(12):
                coordinate_support=I(0)
                for j in range(1025):coordinate_support+=coeff[i][j].norm2().sqrt()*eps[j]
                radius=Q(coordinate_support.hi,S)+remainders[i]
                old_lo,old_hi=price_boxes[i]
                lo=max(old_lo,refs[i]-radius,max(Q(0),1-m[i]));hi=min(old_hi,refs[i]+radius,Q(1))
                assert lo<=hi; tightened.append((lo,hi))
            price_boxes=tightened;coordinate_upgrade_seconds=0-t
        error_boxes=[(lo-f,hi-f) for (lo,hi),f in zip(price_boxes,fast)]
        assert all(x>=0 for x in eps)
        for direction in contract['directions']:
            w=list(map(Q,direction['weights']));active=[i for i,wi in enumerate(w) if wi]
            t=0;symmetric=sum((abs(wi)*absolute(ei) for wi,ei in zip(w,error_boxes)),Q(0))
            marginal=weighted_interval(w,error_boxes);best=absolute(marginal)
            marginal_seconds=0-t
            t=0;support=I(0);low_nodes=I(0);omitted_nodes=I(0);node_entries=[]
            for j,u in enumerate(nodes):
                z=C(0)
                for i in active:z+=coeff[i][j]*C(w[i])
                term=z.norm2().sqrt()*eps[j];support+=term
                if u<=Q(d['solver_cutoff']):low_nodes+=term
                else:omitted_nodes+=term
                node_entries.append((Q(term.hi,S),u))
            node_seconds=0-t
            t=0;center=dot(w,shifts)
            components={'certified_reference_nodes':Q(low_nodes.hi,S),'omitted_finite_nodes':Q(omitted_nodes.hi,S),
                        'analytic_strip_grid':sum((abs(wi)*gi for wi,gi in zip(w,grid)),Q(0)),
                        'true_infinite_tail':sum((abs(wi)*ti for wi,ti in zip(w,tails)),Q(0)),
                        'reference_arithmetic':sum((abs(wi)*ai for wi,ai in zip(w,arith)),Q(0))}
            remainder=components['analytic_strip_grid']+components['true_infinite_tail']+components['reference_arithmetic']
            radius=Q(support.hi,S)+remainder;joint=(center-radius,center+radius);joint_abs=absolute(joint)
            final_price_bound=dot(w,fast)
            if direction['kind'] in ['adjacent_spread','wide_spread']:
                assert len(active)==2 and w[active[0]]==1 and w[active[1]]==-1
                payoff=(Q(0),m[active[1]]-m[active[0]])
            elif direction['kind']=='adjacent_butterfly':
                assert len(active)==3 and m[active[1]]-m[active[0]]==m[active[2]]-m[active[1]]
                assert [w[i] for i in active]==[1,-2,1]
                payoff=(Q(0),m[active[1]]-m[active[0]])
            else:
                assert all(wi>=0 for wi in w)
                payoff=(sum((wi*max(Q(0),1-mi) for wi,mi in zip(w,m)),Q(0)),sum(w))
            payoff_error=(payoff[0]-final_price_bound,payoff[1]-final_price_bound)
            intersection=(max(marginal[0],joint[0],payoff_error[0]),min(marginal[1],joint[1],payoff_error[1]))
            assert intersection[0]<=intersection[1],'empty mathematical intersection is a contradiction, not a successful result'
            intersect_abs=absolute(intersection)
            extra_seconds=0-t
            bounds={'symmetric_marginal':symmetric,'best_signed_marginal':best,'shared_Fourier':joint_abs,
                    'legal_directional_intersection':intersect_abs}
            decisions=[{'budget_index_points':b,'result':{key:('CERTIFIED' if value*scale<=Q(b) else 'NOT_CERTIFIED') for key,value in bounds.items()}} for b in contract['point_budgets']]
            record={'alpha':str(alpha),'direction_id':direction['id'],'kind':direction['kind'],'weights':direction['weights'],
                    'gross_units':direction['gross_units'],'signed_center':str(center),'full_joint_radius':str(radius),
                    'upgraded_node_receipt':upgraded_receipt,
                    'node_support_interval':support.bounds(),'radius_account':{key:str(value) for key,value in components.items()},
                    'best_signed_marginal_error_interval':pair(*marginal),'joint_error_interval':pair(*joint),
                    'payoff_price_bounds':pair(*payoff),'payoff_error_interval':pair(*payoff_error),
                    'legal_directional_intersection_error_interval':pair(*intersection),
                    'absolute_error_bounds_normalized':{key:str(value) for key,value in bounds.items()},
                    'absolute_error_bounds_index_points':{key:str(value*scale) for key,value in bounds.items()},
                    'reduction_fraction_joint_vs_best_signed':str(1-joint_abs/best),
                    'reduction_fraction_intersection_vs_best_signed':str(1-intersect_abs/best),
                    'joint_interval_inside_marginal':joint[0]>=marginal[0] and joint[1]<=marginal[1],
                    'intersection_strictly_improves_joint':intersect_abs<joint_abs,
                    'decisions':decisions,
                    'largest_node_contributions':[{'u':str(u),'upper':str(value)} for value,u in sorted(node_entries,reverse=True)[:8]]}
            records.append(record)
            if direction['id']=='adjacent-spread-4400-4500':
                primary_node_accounts.append({'alpha':str(alpha),'direction_id':direction['id'],
                    'nodes':[{'u':str(u),'support_upper':str(v)} for v,u in node_entries],
                    'required_radius_for_one_point':str(Q(1)/scale-abs(center)),
                    'current_radius':str(radius),'required_relative_radius_reduction':str(1-(Q(1)/scale-abs(center))/radius)})
        candidate_diagnostics.append({'alpha':str(alpha),
                                      'upgraded_node_receipt':upgraded_receipt})
        print(json.dumps({'alpha':str(alpha),'portfolios':len(contract['directions']),'completed_records':len(records)}),flush=True)
    summary=[]
    for alpha in contract['candidates']:
        subset=[r for r in records if r['alpha']==alpha]
        kinds=[]
        for kind in ['adjacent_spread','adjacent_butterfly','wide_spread','positive_basket']:
            sample=[r for r in subset if r['kind']==kind];reductions=[Q(r['reduction_fraction_joint_vs_best_signed']) for r in sample]
            kinds.append({'kind':kind,'count':len(sample),'minimum_reduction_fraction':str(min(reductions)),
                          'maximum_reduction_fraction':str(max(reductions)),
                          'median_reduction_fraction':str(sorted(reductions)[len(reductions)//2]),
                          'intersection_strict_improvement_count':sum(r['intersection_strictly_improves_joint'] for r in sample)})
        summary.append({'alpha':alpha,'kinds':kinds,'point_budget_counts':[{'budget_index_points':b,
                        'certified_counts':{key:sum(next(x for x in r['decisions'] if x['budget_index_points']==b)['result'][key]=='CERTIFIED' for r in subset)
                                            for key in contract['comparisons']}} for b in contract['point_budgets']],
                        'all_joint_intervals_inside_signed_marginal':all(r['joint_interval_inside_marginal'] for r in subset)})
    result={'status':'PASS_SYSTEMATIC_COMPLETE_PORTFOLIO_CERTIFICATES' if not args.finite_history else 'PASS_SYSTEMATIC_ARITHMETIC_CONDITIONAL_ON_FINITE_HISTORY_THEOREM',
            'scenario':'original_upstream_radii' if not args.finite_history else 'finite_history_all_eligible_radii',
            'finite_history_proof_dependency':None if not args.finite_history else {'required':'eta <= delta_F * J0(T), continuous approximate half-plane and positive exponent-kernel hypotheses',
                                                                                  'proof_file':'theory-research.md','arithmetic_does_not_validate_this_theorem':True},
            'contract_sha256':hashlib.sha256(contract_bytes).hexdigest(),
            'source_sha256':contract['source_sha256'],'implementation_sha256':sha(Path(__file__)),
            'python':platform.python_version(),'arithmetic':'100-bit outward dyadic intervals and exact Fraction decisions',
            
            'prepared_coefficients':{'strikes':12,'nodes':1025,'coefficients':12300,'exact_interval_cache_sha256':coefficient_digest},
            'records':records,'summary':summary,'candidate_diagnostics':candidate_diagnostics,'primary_original_spread_node_accounts':primary_node_accounts,
            
            'scope':'Single original half-year maturity, three actual frozen candidates, 28 fixed directions each; all finite omitted nodes and true tails. No new solver/residual generation, actual-error measurement, or exact intersection-support optimization.'}
    assert (HERE/'portfolio-contract.json').read_bytes()==contract_bytes,'contract changed during run'
    assert all(sha(FROZEN/n)==v for n,v in contract['source_sha256'].items()),'input changed during run'
    output='portfolio-results-finite-history.json' if args.finite_history else 'portfolio-results.json'
    if not args.finite_history and (HERE/output).exists():raise FileExistsError('Baseline already recorded; do not overwrite it.')
    (HERE/output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'records':len(records),},indent=2))
if __name__=='__main__':main()
