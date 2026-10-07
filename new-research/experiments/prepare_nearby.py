"""Create private-information-free arithmetic dependencies and frozen protocol.

Dependency changes remove reporting only; numerical algorithm statements remain.
No timings, host configuration, user directories, or operating-system metadata
are gathered in the new experiments.
"""
from pathlib import Path
import hashlib,json,re

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[1]/'heston-frontier-20261007/bundle-v2-fixed/english-heston-release'
SDK=HERE/'sdk';SDK.mkdir(parents=True,exist_ok=True)
NAMES=['interval-pade-certificate.py','combined-field-derivative.py',
       'exact-forward-moments.py','direct-tail-certificate.py',
       'solver-diagnostic.py','field-residual-diagnostic.py',
       'certify-field-residual-v3.py','exponent-field-certificate.py',
       'price-profile-diagnostic.py']
def sha(b):return hashlib.sha256(b).hexdigest()
records=[]
for name in NAMES:
    blob=(SOURCE/'code/src'/name).read_bytes();text=blob.decode('utf-8')
    # Remove time-reporting dependencies and diagnostic-only main entry points.
    text=text.split('\ndef main():')[0]
    text=re.sub(r', time\b|,time\b','',text)
    text=re.sub(r'\btime,\s*','',text)
    text=re.sub(r';?started=time\.monotonic\(\)','',text)
    text=re.sub(r"\s*if start%\(block\*16\)==0:print\([^\n]+\)", '', text)
    text=re.sub(r"'seconds':time\.monotonic\(\)-started,",'',text)
    if name=='price-profile-diagnostic.py':text=text.split('\ndef calculate(')[0]+'\n'
    if name=='field-residual-diagnostic.py':text=text.split('\ndef residuals(')[0]+'\n'
    if name=='solver-diagnostic.py':
        prefix=text.split('\ndef reference(')[0]
        jacobi='\ndef jacobi('+text.split('\ndef jacobi(',1)[1].split('\ndef residual(',1)[0]
        text=prefix+jacobi+'\n'
    # Retain all per-cell bounds for independent cover/max verification.
    if name=='certify-field-residual-v3.py':
        text=text.replace('aa=np.array(aa);bb=np.array(bb);cell=np.array(cell)',
                          'aa=np.array(aa);bb=np.array(bb);cell=np.array(cell); cell_bounds=[first[None,:]]; cell_re=[np.zeros((1,len(u)))]')
        text=text.replace('local=np.max(bound,axis=0);changed=local>maximum',
                          'cell_bounds.append(bound.copy());cell_re.append(real_upper.copy());local=np.max(bound,axis=0);changed=local>maximum')
        text=text.replace("return {'status':'OUTWARD_BINARY64_INTERVAL_POINT_RESIDUAL_CERTIFICATE',",
                          "bank=path.with_name(path.stem+'-residual-cells.npz');np.savez_compressed(bank, a=np.r_[0.,aa], b=np.r_[t[1],bb], bound=np.concatenate(cell_bounds), re_upper=np.concatenate(cell_re), u=u)\n    return {'status':'OUTWARD_BINARY64_INTERVAL_POINT_RESIDUAL_CERTIFICATE', 'bank':bank.name, 'bank_sha256':hashlib.sha256(bank.read_bytes()).hexdigest(),")
    compiled=compile(text,name,'exec')
    clean=text.encode('utf-8');(SDK/name).write_bytes(clean)
    records.append({'name':name,'original_sha256':sha(blob),'new_sha256':sha(clean),
        'change_scope':'main/clock reporting removed; residual module additionally stores already computed closed-cell bounds'})
quote=(SOURCE/'code/frozen/normalized-quote-bands.json').read_bytes()
(SDK/'normalized-quote-bands.json').write_bytes(quote)
ledger={'status':'DEPENDENCY_TRANSFORMATION_DISCLOSED','records':records,
        'quotes_sha256':sha(quote),'numerical_source_scope':'existing rigorous primitives, same arithmetic implementation; independent reader shares these primitives'}
(HERE/'dependency-provenance.json').write_text(json.dumps(ledger,indent=2)+'\n',encoding='utf-8')
protocol={'status':'FROZEN_BEFORE_NEW_CANDIDATE_RESULTS',
  'candidate_alpha_exact':['13/25','21/40','53/100','27/50','11/20'],
  'T':'1/2','F':'211093/50','D':'1','rho':'-1489/2000','nu':'2897/10000','kappa':'0',
  'selected_quote_row_ids':list(range(1,13)),'quotes_sha256':sha(quote),
  'field':'independently regenerated startup-corrected implicit product integration for every point alpha, interpreted as exact stored dyadics',
  'first_level_time_cells':1024,'second_level_time_cells':2048,
  'closed_subcells_per_nonstartup_cell':2,'reference_frequency_step':'1/8',
  'reference_frequency_upper':'64','complete_grid_upper':'128',
  'tail_time_partition':64,'moment_series_terms':64,'strict_exponent_bits':100,
  'upgrade_rule':'Run all five candidates at N=2048 if any adjacent pair remains UNRESOLVED at N=1024; no result-based candidate selection',
  'pair_scope':'all ten unordered pairs; candidate-specific errors are not assumed correlated across alpha',
  'objective':'J=(1/24)*sum_{i=1}^{12}(true_normalized_call_i-midquote_i)^2; interval-valued exact original midpoint conversion retained',
  'joint_objective':'Taylor support enclosure with full Fourier common disks and all coordinate remainders; intersect with exact same-radius marginal box objective',
  'quote_compatibility':'separate original bid/ask compatibility rejection; objective minimization is not market identification',
  'actual_output':'original Gauss-Legendre order 8 and Jacobi order 256 Padé binary64 returned values frozen as exact dyadics',
  'controls':'stored field/closed cover/startup/all-cell maxima/halfplane/tails/strict weights/reference coefficients/complete budgets/quote compatibility and six deliberate corruption controls',
  'cost_disclosure':'deterministic mathematical workload counts only; no clock, hardware, operating-system, memory, thread, or user-path metadata',
  'pilot':'N=64,U=2 at alpha=13/25 only; path/shape/cover test, excluded from scientific comparison',
  'dependency_ledger_name':'dependency-provenance.json'}
target=HERE/'nearby-contract-execution.json'
protocol['initial_protocol_sha256']=sha((HERE/'nearby-contract.json').read_bytes())
protocol['initial_protocol_note']='The original grid, workload, upgrade rule and target are unchanged; only the dependency provenance bookkeeping was corrected before pilot execution.'
protocol['dependency_ledger_sha256']=sha((HERE/'dependency-provenance.json').read_bytes())
if target.exists() and target.read_text(encoding='utf-8')!=json.dumps(protocol,indent=2)+'\n':raise RuntimeError('execution protocol already frozen')
target.write_text(json.dumps(protocol,indent=2)+'\n',encoding='utf-8')
print('PASS dependency preparation and fixed five-point protocol')
