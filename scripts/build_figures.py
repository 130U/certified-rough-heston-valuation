"""Draw the figures of the paper from the saved banks.

Each figure is written as a vector PDF for the typeset paper and as a PNG for the online article.
The curves evaluate formulas of the paper in binary64 from stored exact radii; they illustrate the
certificates and are not themselves certificates.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import math

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'figures'
F = 4221.86
STEP = 1 / 8
STRIKES = np.array([3700 + 100 * i for i in range(12)], dtype=float)
INK, BLUE, RUST, GREY = '#1a1a1a', '#1f4e79', '#b5541c', '#9a9a9a'

plt.rcParams.update({
    'font.family': 'serif', 'font.serif': ['cmr10'], 'mathtext.fontset': 'cm', 'axes.formatter.use_mathtext': True,
    'font.size': 11, 'axes.linewidth': 0.6, 'axes.edgecolor': INK, 'axes.labelcolor': INK, 'text.color': INK,
    'xtick.color': INK, 'ytick.color': INK, 'xtick.direction': 'out', 'ytick.direction': 'out',
    'xtick.major.width': 0.6, 'ytick.major.width': 0.6, 'axes.spines.top': False, 'axes.spines.right': False,
    'legend.frameon': False, 'pdf.fonttype': 42, 'savefig.bbox': 'tight', 'savefig.pad_inches': 0.04,
    'axes.unicode_minus': False,
})


def load(relative):
    return json.loads((ROOT/relative).read_text(encoding='utf-8'))


def save(fig, name):
    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT/(name + '.pdf'), metadata={'CreationDate': None, 'ModDate': None})
    fig.savefig(OUT/(name + '.png'), dpi=220, metadata={'Software': None})
    plt.close(fig)


def mittag_leffler(a, b, z, terms=90):
    return sum(z ** n / math.gamma(a * n + b) for n in range(terms))


def damped_curve(t, lam, alpha=0.52, alpha0=0.5286, v0=0.0262, theta=0.0721, lam_xi=0.5037, outer=40):
    """Forward variance under mean-reversion speed lam: the derivative of the series (3.9)."""
    if t == 0:
        return v0
    total = 0.0
    for n in range(outer):
        total += (-lam) ** n * t ** (n * alpha) * (theta / math.gamma(1 + n * alpha)
                                                   + (v0 - theta) * mittag_leffler(alpha0, 1 + n * alpha, -lam_xi * t ** alpha0))
    return total


def residual_kernel():
    horizon, lam = 0.5, 0.5 * 0.7445 * 0.2897
    s = np.linspace(0.0, horizon, 241)
    plain = np.array([damped_curve(horizon - x, 0.0) for x in s])
    tilted = np.array([damped_curve(horizon - x, lam) for x in s])
    fig, ax = plt.subplots(figsize=(5.6, 3.3))
    ax.fill_between(s, tilted, plain, color=BLUE, alpha=0.12, linewidth=0)
    ax.plot(s, plain, color=INK, linewidth=1.3, label=r'pricing measure, $\xi(T-s)$')
    ax.plot(s, tilted, color=BLUE, linewidth=1.3, linestyle=(0, (5, 2)), label=r'half-share measure, $\xi^{\lambda_*}(T-s)$')
    ax.set_xlabel(r'time to maturity $s$ at which the residual occurs (years)')
    ax.set_ylabel('weight on a unit residual')
    ax.set_xlim(0, horizon)
    ax.set_ylim(0.02, 0.045)
    ax.legend(loc='upper right')
    save(fig, 'residual-kernel')


def modulus(weights, u):
    m = STRIKES / F
    loads = np.asarray(weights, dtype=float) * np.sqrt(m)
    phases = np.exp(-1j * np.outer(u, np.log(m)))
    return np.abs(phases @ loads), np.abs(loads).sum(), math.sqrt((loads ** 2).sum()) / np.abs(loads).sum()


def netting_ratio():
    radii = np.array([float(Q(x)) for x in load('science/baseline/finite-history/finite-history-nodes-alpha-13_25.json')['all_node_radii']])
    nodes = np.arange(1025) * STEP
    charge = radii / (nodes ** 2 + 0.25)
    charge[0] *= 0.5
    edges = np.arange(0, 129, 4)
    share = np.array([charge[(nodes >= a) & (nodes < b)].sum() for a, b in zip(edges[:-1], edges[1:])])
    share[-1] += charge[-1]
    share /= charge.sum()
    u = np.linspace(0, 128, 2049)
    spread = np.zeros(12); spread[7], spread[8] = 1, -1
    fly = np.zeros(12); fly[6], fly[7], fly[8] = 1, -2, 1
    basket = np.full(12, 1 / 12)
    fig, ax = plt.subplots(figsize=(5.9, 3.5))
    shade = ax.twinx()
    shade.bar(edges[:-1], share, width=4, align='edge', color=GREY, alpha=0.28, linewidth=0)
    shade.set_ylim(0, 0.5)
    shade.set_yticks([0, 0.1, 0.2])
    shade.set_ylabel('share of node charge', color=GREY)
    shade.yaxis.set_label_coords(1.09, 0.2)
    shade.tick_params(axis='y', colors=GREY)
    shade.spines['right'].set_visible(True)
    shade.spines['right'].set_color(GREY)
    for weights, colour, style, label in [(spread, INK, '-', 'call spread 4400/4500'), (fly, BLUE, (0, (5, 2)), 'butterfly 4300/4400/4500'),
                                          (basket, RUST, (0, (1, 1.2)), 'equal-weight basket, twelve strikes')]:
        value, gross, herfindahl = modulus(weights, u)
        ax.plot(u, value / gross, color=colour, linewidth=1.25, linestyle=style, label=label)
        ax.plot([120, 128], [herfindahl, herfindahl], color=colour, linewidth=2.2, solid_capstyle='butt')
    ax.set_zorder(shade.get_zorder() + 1)
    ax.patch.set_visible(False)
    ax.set_xlim(0, 128)
    ax.set_ylim(0, 1.0)
    ax.set_xticks([0, 32, 64, 96, 128])
    ax.set_xlabel(r'frequency $u$')
    ax.set_ylabel(r'netting ratio $\chi_w(u)$')
    ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.17), ncol=1, fontsize=9.5, handlelength=2.6, labelspacing=0.25)
    save(fig, 'netting-ratio')


def joint_error_set():
    nodes = load('science/baseline/frontier/transfer-time-local-nodes.json')['nodes']
    u = np.array([float(Q(n['u'])) for n in nodes])
    radius = np.array([float(Q(n['time_CF_radius_upper'])) for n in nodes])
    m = np.array([4400.0, 4500.0]) / F
    omega = np.ones_like(u); omega[0] = 0.5
    coefficient = -(STEP * omega / math.pi / (u ** 2 + 0.25))[:, None] * np.sqrt(m)[None, :] * np.exp(-1j * np.outer(u, np.log(m)))
    scaled = coefficient * radius[:, None] * F
    angles = np.linspace(0, 2 * math.pi, 1441)
    points = []
    for angle in angles:
        direction = np.array([math.cos(angle), math.sin(angle)])
        b = scaled @ direction
        phase = np.where(np.abs(b) > 0, np.conj(b) / np.maximum(np.abs(b), 1e-300), 0)
        points.append((scaled * phase[:, None]).real.sum(axis=0))
    points = np.array(points)
    half = np.abs(scaled).sum(axis=0)
    joint = np.abs(scaled @ np.array([1.0, -1.0])).sum()
    stored = float(sum(Q(n['joint_node_support_exact']) for n in nodes)) * F
    assert abs(joint - stored) < 1e-9 and abs(half.sum() - float(sum(Q(n['signed_marginal_node_support_exact']) for n in nodes)) * F) < 1e-9
    fig, ax = plt.subplots(figsize=(4.6, 4.4))
    ax.fill(points[:, 0], points[:, 1], color=BLUE, alpha=0.16, linewidth=0)
    ax.plot(points[:, 0], points[:, 1], color=BLUE, linewidth=1.3)
    ax.plot([-half[0], half[0], half[0], -half[0], -half[0]], [-half[1], -half[1], half[1], half[1], -half[1]], color=INK, linewidth=0.9, linestyle=(0, (4, 2)))
    span = 1.62 * max(half)
    for offset, colour, style, label in [(joint, BLUE, '-', f'joint support of the spread, {joint:.4f}'),
                                         (half.sum(), INK, (0, (4, 2)), f'leg-by-leg support, {half.sum():.4f}')]:
        ax.plot([-span, span], [-span - offset, span - offset], color=colour, linewidth=0.7, linestyle=style, label=label)
    ax.annotate('joint set', xy=(0.0, 0.0), ha='center', va='center', color=BLUE, fontsize=10)
    ax.annotate('bounding box', xy=(-half[0], half[1]), xytext=(0, 5), textcoords='offset points', color=INK, fontsize=10)
    ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=9, handlelength=2.4, borderaxespad=0.2)
    ax.set_xlim(-span, span)
    ax.set_ylim(-span, span)
    ax.set_aspect('equal')
    ax.set_xlabel('error of the 4400 call (index points)')
    ax.set_ylabel('error of the 4500 call (index points)')
    ticks = [-0.03, 0, 0.03]
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    save(fig, 'joint-error-set')


def pass_counts():
    rows = load('audit-experiments/portfolio-budget-counts.json')['threshold_rows']
    curves = {}
    for r in rows:
        curves.setdefault((r['configuration_id'], r['alpha'], r['method']), []).append(float(Q(r['exact_threshold_points'])))
    panels = [('13/25', r'$\alpha=0.52$', [('H0', GREY), ('H1', INK)]), ('3/5', r'$\alpha=0.60$', [('H0', GREY), ('H1', INK)]),
              ('9/10', r'$\alpha=0.90$', [('H0', GREY), ('H1', INK)]), ('13/25', r'$\alpha=0.52$, regenerated fields', [('N1', GREY), ('N2', RUST), ('N2L', BLUE)])]
    fig, axes = plt.subplots(2, 2, figsize=(6.4, 4.9), sharex=True, sharey=True)
    budgets = np.linspace(0, 2, 801)
    for ax, (alpha, title, banks) in zip(axes.flat, panels):
        for bank, colour in banks:
            for method, style in [('joint', '-'), ('marginal', (0, (3.5, 2)))]:
                values = np.sort(np.array(curves[bank, alpha, method]))
                assert len(values) == 28
                ax.step(budgets, np.searchsorted(values, budgets, side='right'), where='post', color=colour, linewidth=1.15, linestyle=style,
                        label=bank if method == 'joint' else None)
        for level in (0.25, 0.5, 1.0):
            ax.axvline(level, color=GREY, linewidth=0.4, alpha=0.6)
        ax.set_title(title, fontsize=10.5, loc='left', pad=4)
        ax.set_xlim(0, 2)
        ax.set_ylim(0, 29)
        ax.set_yticks([0, 7, 14, 21, 28])
        ax.set_xticks([0, 0.25, 0.5, 1, 1.5, 2])
        ax.set_xticklabels(['0', '', '0.5', '1', '1.5', '2'])
        ax.legend(loc='lower right', fontsize=9, handlelength=1.8)
    for ax in axes[1]:
        ax.set_xlabel('tolerance (index points)')
    for ax in axes[:, 0]:
        ax.set_ylabel('positions certified')
    fig.tight_layout(h_pad=1.2, w_pad=1.4)
    save(fig, 'pass-counts')


def main():
    residual_kernel()
    netting_ratio()
    joint_error_set()
    pass_counts()
    print('PASS figures', sorted(p.name for p in OUT.iterdir()))


if __name__ == '__main__':
    main()
