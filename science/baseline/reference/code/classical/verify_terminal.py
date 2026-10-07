"""Read the completed small certificate; no author import, profile/model or LP run."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import hashlib
import json
import time
import sys

BASE = Path(__file__).resolve().parent
OUT = BASE / 'terminal-validation.json'
FAIL = BASE / 'terminal-validation-failure.json'
NAMES = ['terminal767-input.json', 'terminal767-result.json', 'provenance.json']
checks = 0


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(test, name):
    global checks
    checks += 1
    if not test:
        raise AssertionError(name)


def inner(x, y):
    check(len(x) == len(y), 'dot dimensions')
    return sum((a * b for a, b in zip(x, y)), F(0))


def vec(x):
    return [F(v) for v in x]


def det3(m):
    ans = F(0)
    for p in permutations(range(3)):
        inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
        term = F((-1) ** inversions)
        for i in range(3):
            term *= m[i][p[i]]
        ans += term
    return ans


def main():
    began = 0
    before = {name: sha(BASE / name) for name in NAMES}
    provenance = json.loads((BASE / 'provenance.json').read_text())
    for name in NAMES[:2]:
        check(before[name] == provenance['files'][name]['portable_sha256'] == provenance['files'][name]['retained_scientific_input_sha256'], 'byte-identical retained scientific input')
    data = json.loads((BASE / 'terminal767-input.json').read_text(encoding='utf-8-sig'))
    res = json.loads((BASE / 'terminal767-result.json').read_text(encoding='utf-8-sig'))
    check(data['freeze_sha256'] == provenance['source_identities']['terminal-prefreeze'], 'input freeze identity')
    check(res['input_sha256'] == before['terminal767-input.json'], 'result input identity')
    check(res['source_sha256'] == provenance['source_identities']['terminal-generator'], 'archived result source identity')
    check(res['status'] == 'STRICT_ROW_SEPARATION' and res['gap_money'] is None, 'declared scope')
    check('failure' not in res, 'final certificate no failure')

    n = 102
    A = [vec(row) for row in data['P_A']]
    b = vec(data['P_b'])
    profiles = [vec(row) for row in data['profiles']]
    check(len(A) == len(b) == len(data['P_names']) == 22, 'all frozen P rows')
    check(all(len(row) == n for row in A), 'P dimensions')
    check(len(profiles) == 9 and all(len(row) == n for row in profiles), 'nine profiles')
    check(all(x >= 0 for row in profiles for x in row), 'profile nonnegative data')
    check(A[-2] == [F(1)] * n and b[-2] == 1, 'mass upper')
    check(A[-1] == [F(-1)] * n and b[-1] == -1, 'mass lower')
    details = data['details']
    check(len(details) == 9, 'profile metadata count')
    check(F(details[0]['p']) == F(-1, 48) and F(details[0]['w']) == 64, 'Asian original terminal mode')
    omegas = list(range(8, 121, 16))
    for w, item in zip(omegas, details[1:]):
        check(F(item['p']) == F(-1, 4) and F(item['w']) == -w, 'put original mode order')

    pa = vec(res['Asian']['pi'])
    pb = vec(res['put_direction']['pi'])
    y = vec(res['Asian']['dual'])
    check(len(pa) == len(pb) == n and len(y) == len(b), 'certificate dimensions')
    for name, p in [('Asian', pa), ('put direction', pb)]:
        check(all(v >= 0 for v in p), name + ' nonnegative')
        check(sum(p) == 1, name + ' exact mass')
        for row, rhs in zip(A, b):
            check(inner(row, p) <= rhs, name + ' each P inequality')
    check(all(v >= 0 for v in y), 'Asian dual nonnegative')
    c = profiles[0]
    reduced = [inner([row[j] for row in A], y) - c[j] for j in range(n)]
    check(all(v >= 0 for v in reduced), 'Asian dual inequalities')
    check(reduced == vec(res['Asian']['reduced']), 'all saved reduced costs')
    alpha = inner(c, pa)
    check(alpha == inner(b, y) == F(res['Asian']['value']), 'exact primal dual equality')
    check(all(yi * (rhs - inner(row, pa)) == 0 for yi, row, rhs in zip(y, A, b)), 'all complementary rows')
    support = [j for j, v in enumerate(pa) if v > 0]
    check(support == res['Asian']['support'] == [1, 2, 6], 'exact Asian support')
    check(all(reduced[j] > 0 for j in range(n) if j not in support), 'all outside support strictly excluded')
    positive_rows = [i for i, v in enumerate(y) if v > 0]
    check(len(positive_rows) == len(support) == 3, 'three forcing rows')
    forced_matrix = [[A[i][j] for j in support] for i in positive_rows]
    determinant = det3(forced_matrix)
    check(determinant != 0 and res['Asian']['rank'] == 3, 'independent determinant proves unique support solution')

    # Confirm the basis record without solving or optimizing anything.
    basis = res['Asian']['basis']
    check(len(basis) == len(b) and len(set(basis)) == len(b), 'Asian basis list')
    slack = [rhs - inner(row, pa) for row, rhs in zip(A, b)]
    full = pa + slack
    check(all(full[j] == 0 for j in range(n + len(b)) if j not in basis), 'nonbasic primal entries zero')
    for i, rhs in enumerate(b):
        check(sum(((A[i][j] if j < n else F(i == j - n)) * full[j] for j in basis), F(0)) == rhs, 'each basic equation')

    # The recovery is solely a feasible witness. Verify its recorded finite arithmetic.
    recovery = res['put_direction']['recovery']
    basis_p = res['put_direction']['basis']
    raw = vec(recovery['raw_basic'])
    check(len(raw) == len(basis_p) == len(b), 'put raw basis dimensions')
    for i, rhs in enumerate(b):
        check(sum(((A[i][j] if j < n else F(i == j - n)) * x for j, x in zip(basis_p, raw)), F(0)) == rhs, 'put raw basic equation')
    clipped = [F(0)] * n
    for j, x in zip(basis_p, raw):
        if j < n:
            clipped[j] = max(F(0), x)
    mass = sum(clipped)
    check(mass > 0, 'clipped mass positive')
    normalized = [v / mass for v in clipped]
    anchor = [F(0)] * n
    check(recovery['anchor_index'] == 5, 'fixed anchor index')
    anchor[5] = F(1)
    check(all(inner(row, anchor) <= rhs for row, rhs in zip(A, b)), 'anchor exactly feasible')
    eps = F(recovery['epsilon'])
    check(0 <= eps <= 1, 'convex mixing coefficient')
    check(pb == [(1 - eps) * p + eps * aa for p, aa in zip(normalized, anchor)], 'recorded repair identity')

    direction = [v - u for u, v in zip(pa, pb)]
    parts = res['put_direction']['components']
    check(len(parts) == 8, 'all eight weights retained')
    low = high = F(0)
    component_report = []
    for w, h, item in zip(omegas, profiles[1:], parts):
        check(item['omega'] == w, 'original weight frequency')
        x = inner(h, pa)
        change = inner(h, direction)
        check(x == F(item['x']) and x > 0, 'positive radicand and recorded value')
        check(change == F(item['change']), 'recorded exact profile direction')
        dl, du = vec(item['derivative'])
        D = (F(w * w) + F(1, 16)) * (F(w * w) + F(25, 16))
        check(0 < dl <= du, 'positive derivative coefficient interval')
        # The exact coefficient is 1/(2*sqrt(D*x)); no sqrt or author primitive is called.
        check(4 * dl * dl * D * x <= 1 <= 4 * du * du * D * x, 'independent root direction by exact squares')
        l, u = (dl * change, du * change) if change >= 0 else (du * change, dl * change)
        low += l
        high += u
        component_report.append({'omega': w, 'change_sign': (change > 0) - (change < 0), 'lower': str(l), 'upper': str(u)})
    saved_lo, saved_hi = vec(res['put_direction']['derivative'])
    check(saved_lo <= low <= high <= saved_hi, 'complete signed outward derivative enclosure')
    check(low > 0 and saved_lo > 0, 'strict full row derivative')
    after = {name: sha(BASE / name) for name in NAMES}
    check(before == after, 'all read targets unchanged')

    output = {
        'status': 'PASS_PORTABLE_TERMINAL767_EXACT_ROW_CERTIFICATE',
        'review_author_is_root': False,
        'review_role': 'Portable exact-arithmetic adaptation of the archived adjacent-author checker; not external peer review.',
        'inputs': before,
        'checker_sha256': sha(Path(__file__)),
        'checks': checks,
        'Asian_unique_support': support,
        'positive_dual_rows': positive_rows,
        'forcing_determinant_exact': str(determinant),
        'Asian_value_exact': str(alpha),
        'directional_lower_exact': str(low),
        'directional_upper_exact': str(high),
        'saved_directional_interval': [str(saved_lo), str(saved_hi)],
        'components': component_report,
        'recovery_epsilon_exact': str(eps),
        'raw_basic_negative_entries': sum(v < 0 for v in raw),
        'conclusion': 'The saved effective P/profiles and unchanged exact eight weights have no common price-row maximum at j=767.',
        'actual_money_gap': None,
        'profile_or_model_recomputations': 0,
        'LP_or_SOC_solver_calls': 0,
        'Gamma_or_author_function_calls': 0,
        'P_and_profile_generation_scope': 'This checker reads effective inputs. verify_input_bounds.py separately regenerates all 22 probability rows and 918 profile entries with exact outward arithmetic.',
        
    }
    if '--write' in sys.argv:
        with OUT.open('w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
    print(json.dumps({'status': output['status'], 'checks': checks, 'support': support, 'saved_lower_exact': str(saved_lo)}, ensure_ascii=False))


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        if '--write' in sys.argv and not FAIL.exists():
            with FAIL.open('w', encoding='utf-8') as f:
                json.dump({'status': 'FAILED_SAVED_CERTIFICATE_READBACK', 'checks': checks, 'error': repr(err)}, f, ensure_ascii=False, indent=2)
        raise
