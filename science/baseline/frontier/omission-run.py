"""Optional complete scientific residual regeneration without personal telemetry."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,sys
HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'reference'
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--regenerate-full',action='store_true');args=parser.parse_args()
    assert args.regenerate_full,'Only complete scientific regeneration is retained.'
    p=HERE/'omission-residual-generator.py'
    spec=importlib.util.spec_from_file_location('omission_generator',p);module=importlib.util.module_from_spec(spec)
    sys.modules['omission_generator']=module;spec.loader.exec_module(module)
    out=module.certify(BASE/'code/frozen/fixed-field-betap52-u128.npz',__import__('fractions').Fraction(13,25),128.,4,32)
    assert len(out['u'])==512 and out['certified_closed_subintervals']==8189
    (HERE/'omission-residual-high.json').write_text(json.dumps(out,indent=2)+'\n')
    receipt={'mode':'full','return_code':0,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    (HERE/'omission-full-execution.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'frequency_nodes':512,'closed_time_cells':8189}))
if __name__=='__main__':main()
