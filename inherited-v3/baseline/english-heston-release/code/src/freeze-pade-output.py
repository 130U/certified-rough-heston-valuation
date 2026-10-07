"""Freeze the actually executed GR [3/3] price algorithm, not true prices.

Each returned IEEE binary64 is regarded as an exact dyadic number. A separate
true-model price enclosure is needed before making any accuracy claim.
"""
from pathlib import Path
from fractions import Fraction
import hashlib, importlib.util, json, platform, time
import numpy as np

BASE = Path(__file__).parent
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    started = 0
    contract_path = BASE / 'calibration-contract-finite-T05.json'
    quote_path = BASE / 'normalized-quote-bands.json'
    component = BASE / 'price-profile-diagnostic.py'
    solver_path = BASE / 'solver-diagnostic.py'
    sources = [Path(__file__), component, solver_path, contract_path, quote_path]
    initial_hashes = {p.name: sha(p) for p in sources}
    spec = importlib.util.spec_from_file_location('pade_price_algorithm', component)
    algorithm = importlib.util.module_from_spec(spec); spec.loader.exec_module(algorithm)
    contract = json.loads(contract_path.read_text(encoding='utf-8'))
    quoted = json.loads(quote_path.read_text(encoding='utf-8'))
    rows = [r for r in quoted['rows'] if r['row_id'] in contract['selected_row_ids']]
    k = np.array([float(Fraction(r['moneyness_fraction'])) for r in rows])
    u, weights = algorithm.fourier_grid(8)
    cover = []
    for alpha in contract['candidate_alpha_exact']:
        exponent = algorithm.pade_exponent(float(alpha), u, .5, 256)
        values = algorithm.prices(np.exp(exponent), u, weights, k)
        assert np.all(np.isfinite(values))
        cover.append({'alpha': alpha, 'rows': [
            {'row_id': row['row_id'],
             'normalized_call_exact_dyadic': str(Fraction.from_float(float(value))),
             'normalized_call_float_display_only': float(value)}
            for row, value in zip(rows, values)]})
        print('froze alpha', alpha, 'rows', len(values), flush=True)
    assert initial_hashes == {p.name: sha(p) for p in sources}
    out = {
        'status': 'FROZEN_PADE_NUMERIC_OUTPUT_EXACT_DYADICS_NOT_TRUE_PRICE_CERTIFICATE',
        'contract_sha256': initial_hashes[contract_path.name],
        'quotes_sha256': initial_hashes[quote_path.name],
        'executed_source_path': Path(__file__).name,
        'executed_source_sha256': initial_hashes[Path(__file__).name],
        'component_sources_sha256': {component.name: initial_hashes[component.name],
                                     solver_path.name: initial_hashes[solver_path.name]},
        'runtime_versions': {'Python': platform.python_version(), 'NumPy': np.__version__},
        'algorithm': {'Fourier': 'composite Gauss-Legendre order 8 on frozen cuts to 200',
                      'exponent': 'D-type fractional convolution, Jacobi order 256',
                      'rational': 'unchanged GR six-condition [3/3]',
                      'forward_curve': 'frozen alpha0=.5286, not candidate alpha'},
        'arithmetic_scope': 'stored binary64 outputs interpreted as exact dyadics; no true-price certificate in this file',
         'cover': cover}
    (BASE / 'frozen-pade-numeric-output.json').write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')

if __name__ == '__main__': main()
