"""Read the classical model, moment, terminal and field certificates."""
from pathlib import Path
import subprocess, sys
sys.dont_write_bytecode=True
BASE=Path(__file__).resolve().parents[1]/'baseline/reference/code/classical'
for name in ['verify_package.py','verify_input_bounds.py','verify_terminal.py','verify_field_receipt.py']:
 result=subprocess.run([sys.executable,'-X','utf8','-B',str(BASE/name)],check=True)
print('PASS_CLASSICAL_MODEL_TERMINAL_AND_FIELD_READERS')
