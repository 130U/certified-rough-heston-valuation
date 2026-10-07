"""Independently invoke the identified frozen Padé output algorithm.

The exact returned dyadics are pricing targets, never true-price inputs.
All arithmetic accuracy comes from the separate full reference certificates.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,importlib.util,json,sys
import numpy as np
HERE=Path(__file__).resolve().parent;SDK=HERE/'sdk';sys.dont_write_bytecode=True
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument('--N',type=int,required=True);args=p.parse_args()
    sp=importlib.util.spec_from_file_location('independent_fast_algorithm',SDK/'price-profile-diagnostic.py');fast=importlib.util.module_from_spec(sp);sp.loader.exec_module(fast)
    quote=[r for r in load(SDK/'normalized-quote-bands.json')['rows'] if Q(r['T_decimal_input'])==Q(1,2)]
    m=[float(Q(r['moneyness_fraction'])) for r in quote];u,w=fast.fourier_grid(8);rows=[]
    for a in load(HERE/'nearby-contract-execution.json')['candidate_alpha_exact']:
        file=HERE/('N'+str(args.N))/('candidate-'+a.replace('/','_')+'.json');r=load(file)
        exponent=fast.pade_exponent(float(Q(a)),u,.5,256);actual=fast.prices(np.exp(exponent),u,w,m)
        replay=[Q.from_float(float(v)) for v in actual];stored=[Q(v['actual_fast_output']) for v in r['price_rows']]
        assert replay==stored
        rows.append({'alpha':a,'returned_values_verified':12,'candidate_sha256':sha(file)})
    out={'status':'PASS_ALL_FIVE_ACTUAL_PADE_OUTPUT_REPLAYS','N':args.N,
       'fourier_nodes':len(u),'Jacobi_nodes_per_frequency':256,'records':rows,
       'executed_algorithm_sha256':sha(SDK/'price-profile-diagnostic.py'),'reader_sha256':sha(Path(__file__)),
       'qualification':'Exact stored-output replay on the executing arithmetic platform; not a claim of universal cross-platform bitwise identity or internal quadrature accuracy.'}
    (HERE/('nearby-fast-replay-N'+str(args.N)+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS five-candidate actual stored Padé output replay',flush=True)
if __name__=='__main__':main()
