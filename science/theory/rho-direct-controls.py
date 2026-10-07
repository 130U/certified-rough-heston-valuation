"""Additional semantic and missing-cell controls for the continuous supplement."""
from pathlib import Path
import gzip, hashlib, importlib.util, json
HERE=Path(__file__).resolve().parent
def load(name):return json.loads(gzip.decompress((HERE/name).read_bytes()))
direct=load('rho-direct.json.gz');prior=load('rho-cover.json.gz')
expected=dict(alpha=['13/25','3/5'],rho=['-744501/1000000','-744499/1000000'],kappa='0',eta=['0','1'])
def check_parameters(params):assert params==expected
check_parameters(direct['parameters'])
tests=[]
for name,field,value in [
    ('broader_alpha_claim','alpha',['51/100','3/5']),
    ('nonzero_mean_reversion_claim','kappa','1'),
    ('widened_correlation_claim','rho',['-744501/1000000','-744498/1000000']),
    ('missing_low_frequency_boundary','eta',['1/1024','1'])]:
    corrupt=dict(direct['parameters']);corrupt[field]=value
    tests.append((name,lambda corrupt=corrupt:check_parameters(corrupt)))
spec=importlib.util.spec_from_file_location('independent_splice',HERE/'rho-direct-check.py')
reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
first=direct['accepted'][0]['source_unresolved_leaf']
cells=[reader.keys(r) for r in direct['accepted'] if r['source_unresolved_leaf']==first]
root=reader.keys(prior['unresolved'][first])
reader.partition(root,cells,18)
tests.append(('missing_direct_closed_cell',lambda:reader.partition(root,cells[1:],18)))
negative={}
for name,test in tests:
    try:test()
    except AssertionError:negative[name]='REJECTED'
    else:raise AssertionError('accepted semantic negative control '+name)
result=dict(status='PASS_CONTINUOUS_RHO_SEMANTIC_NEGATIVE_CONTROLS',
            complete_parameter_statement_checked=True,
            valid_splice_checked=True,negative_controls=negative,
            checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            independent_splice_reader_sha256=hashlib.sha256((HERE/'rho-direct-check.py').read_bytes()).hexdigest())
(HERE/'rho-direct-controls.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
