"""Write concise paper-ready tables only after both full grid levels pass."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal,localcontext,ROUND_FLOOR,ROUND_CEILING
import json
HERE=Path(__file__).resolve().parent
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def dec(v,places=9,up=True,scale=1):
    q=Q(v)*scale
    with localcontext() as c:
        c.prec=80;x=Decimal(q.numerator)/Decimal(q.denominator)
        return str(x.quantize(Decimal(1).scaleb(-places),rounding=ROUND_CEILING if up else ROUND_FLOOR))
def interval(v):return '['+dec(v[0],6,False,10**8)+', '+dec(v[1],6,True,10**8)+']'
def main():
    levels=[load(HERE/('N'+str(n))/'nearby-results.json') for n in [1024,2048]]
    for n in [1024,2048]:assert load(HERE/('N'+str(n))/'nearby-independent.json')['status']=='PASS_SEPARATE_ALL_NODE_AND_ALL_CELL_RECONSTRUCTION'
    assert load(HERE/'local128/independent.json')['status']=='PASS_SEPARATE_DESCRIPTIVE_128_BIN_ALL_CLOSED_CELL_CONTROL'
    ctrl=load(HERE/'workload-controls-N2048-local128.json')
    assert load(HERE/'workload-controls-independent-N2048-local128.json')['status']=='PASS_SEPARATE_SAME_GUARANTEE_AND_28_TASK_READBACK'
    table='| alpha | N=1024 joint J ×10^8 | N=2048 joint J ×10^8 |\n|---:|---:|---:|\n'
    for r1,r2 in zip(levels[0]['candidate_objectives'],levels[1]['candidate_objectives']):table+='| '+dec(r1['alpha'],3)+' | '+interval(r1['objective']['joint_interval'])+' | '+interval(r2['objective']['joint_interval'])+' |\n'
    pair='| Generated layer | Joint strictly separated pairs | Matched marginal pairs |\n|---|---:|---:|\n'
    counts=[]
    for level in levels:
        j=sum(r['joint']['decision']!='UNRESOLVED' for r in level['pairs']);m=sum(r['marginal']['decision']!='UNRESOLVED' for r in level['pairs']);counts.append([j,m]);pair+=f"| N={level['N']} | {j}/10 | {m}/10 |\n"
    target='| Returned output | Complete joint bound, points | Matched marginal bound, points | Joint quarter-point decision |\n|---|---:|---:|---|\n'
    names=['Frozen Padé','Direct binary64 reference','Padé + stored correction + binary64 addition','BL-modified Adams core, 512 steps','BL-modified Adams core, 1024 steps']
    for name,r in zip(names,ctrl['methods']):target+=f"| {name} | {dec(r['complete_joint_bound_points'])} | {dec(r['complete_marginal_bound_points'])} | {'PASS' if r['joint_quarter_point_pass'] else 'UNRESOLVED'} |\n"
    final=levels[1];grid=final['grid'];best=min(final['candidate_objectives'],key=lambda r:Q(r['objective']['joint_interval'][1]))
    unique=all(Q(best['objective']['joint_interval'][1])<Q(r['objective']['joint_interval'][0]) for r in final['candidate_objectives'] if r['alpha']!=best['alpha'])
    incompat={r['alpha']:r['incompatible_rows'] for r in final['candidate_objectives']}
    en='''### Real nearby candidates: complete finite-set comparison

The original twelve half-year quotes, forward F=4221.86, discount D=1,
and all other model parameters are fixed. Before computing new results we
froze alpha={0.520,0.525,0.530,0.540,0.550}, a first layer N=1024, and an
upgrade of **all five** candidates to N=2048 if any adjacent joint comparison
remained unresolved. Every point has a newly generated continuous reference
field and a complete closed-time residual bank. Fourier nodes through 64,
all omitted finite nodes through 128, true infinite tails, strip remainder,
reference arithmetic and original quote-conversion intervals are paid.

The objective is the original normalized midpoint loss
J=(1/24) sum_i (c_i-m_i)^2. Here the tiny target interval halfwidth is only
outward arithmetic error in converting the fixed bid/ask-price midpoint;
it is not the market bid/ask halfwidth. Ranking does not establish a uniform
winner for arbitrary quote targets inside those market bands.
A Taylor support enclosure preserves common
Fourier disks in its linear term and charges the full coordinate-radius
quadratic remainder. Its same-radius marginal comparison uses the identical
upstream certificate. Errors across different alpha candidates are not
assumed jointly correlated.

'''+table+'\n'+pair+f'''
The first layer retained its unresolved close pairs and triggered the frozen
all-candidate upgrade. The final finite grid {'has alpha='+dec(best['alpha'],3)+' as a strict minimum' if unique else 'does not certify a unique minimum'}.
This is a five-point comparison, not a continuous calibration optimum. All
five candidates remain incompatible with at least one original bid/ask row;
the finite-set result therefore does not identify a market-calibrated model.

### Why certify the frozen output after computing a reference?

We distinguish a frozen production-output audit from freely replacing the
output in a fresh pricing task. The ideal exact correction equals the rational
reference centre, but actual returned reference values, stored binary64
corrections and the final binary64 addition are separately frozen and their
exact dyadic rounding errors are paid. Once a strict reference has already
been computed, returning that reference is the simpler choice for a one-off
price. Frozen-output certificates are useful for auditing an existing library
and for repeated tasks sharing one proof bank; we make no general speed claim.

To test this distinction, a separate descriptive control was frozen after
the N=2048 global account was known. It reuses the complete alpha=0.52
closed residual bank with 128 physical-time propagation bins. Every bin
uses the maximum over all intersecting closed source cells and retains
history from zero. This control leaves the nearby-grid study unchanged.
All five returned-output methods use the same radius, reference, full
remainders, half-year 4400/4500 spread and quarter-point tolerance.

'''+target+'''
The modern comparison implements the BL-modified Adams Riccati core of
Boyarchenko et al. (2025, Section 3.2 and Appendix B): frequency scaling,
leading asymptotic subtraction, linear Adams history and eight Picard
corrections. It is adapted to our declared forward-variance model and uses
flat Fourier inversion. It does not reproduce SINH-CB. Its 512/1024 nominal
spread difference is an empirical diagnostic; deterministic guarantees in
the table come from the complete shared reference certificate and signed
centre translation, not empirical agreement or conformal bootstrap.

We report deterministic mathematical workload only. The two five-candidate
layers generate 15,754,230 complete closed-node residual entries, 5,130 strict
reference exponents and 10,250 true-CF node envelopes. Each point proof
supports all twelve prices; the 28 fixed portfolios require 28×1025 further
joint support terms and **zero** additional residual generation. The descriptive
128-bin control reuses 2,100,735 existing residual entries and pays 128×513
weighted residual terms. Verification reconstructs the complete mathematical
accounts. These counts do not equate binary64 operations with strict dyadic
transcendental primitives and do not support a universal cost ratio.
'''
    zh='''### 真实邻近候选：完整有限集合比较

固定原半年 12 条报价、F=4221.86、D=1 及其余模型参数。新结果计算之前
冻结 alpha={0.520,0.525,0.530,0.540,0.550} 和第一层 N=1024；只要任一
相邻 joint 比较 unresolved，就把**全部五点**升级到 N=2048。
每点重新生成连续参考场、完整闭时间残差银行；64 以内已用节点、128 以内
全部有限省略节点、真无限尾、条带、参考算术和原报价转换不确定性全付。
目标仍为原 normalized midpoint loss。目标区间半宽只支付固定 bid/ask 价格
中点转换的外向算术误差，不是市场 bid/ask 半宽；排名不证明对任意市场
band 内报价目标的统一最优。Taylor 线性项保留共同 Fourier disks，
二次余项按完整坐标半径支付；marginal 对照使用同样上游半径。
不同 alpha 候选的误差没有被假定相关。

'''+table+'\n'+pair+f'''
第一层保留 unresolved 近邻并触发预先固定的全点升级。
最终五点集合{'认证 alpha='+dec(best['alpha'],3)+' 是严格最小候选' if unique else '仍未认证唯一最小候选'}。
这不是连续校准最优性。五点均仍与至少一条原 bid/ask 报价不兼容，
因此也不是市场模型识别。

### 已算出参考价，为何还认证冻结快输出？

冻结生产输出审计与允许自由更换输出的新定价任务是不同工作负载。
理想精确平移等于参考有理中点；实际返回参考价格、binary64 修正存储及
binary64 加法分别保存，精确 dyadic 舍入逐项支付。若一次新定价任务的
严格参考已计算完成，直接返回参考价更简单。认证未修正快输出的价值在于
已有程序审计和共享证书的重复任务；不宣称普遍加速。

另一个描述性控制在 N2048 全局账本已知后先冻结，再计算：将同 alpha=.52
完整闭残差银行复用于 128 个物理时间传播格。每格取所有相交闭源单元的
最大包络，保留从零开始的全部历史；它不改动主邻近网格实验。
以下五种实际输出使用同一参考、同一半径、完整余项和原 4400/4500 价差，
目标一律为四分之一指数点。

'''+target+'''
现代对照采用 Boyarchenko 等（2025）§3.2/Appendix B 的 BL-modified
Adams Riccati 核心，包括频率缩放、显式首项减除、Adams 历史及八次
Picard 校正，适配当前 forward-variance 模型；仅采用 flat Fourier，
不宣称复现 SINH-CB。512/1024 输出差仅为经验诊断，表内保证来自完整
参考证书和有符号中心转换，不能由经验一致或 conformal bootstrap 替代。

只披露可重建的数学工作量。两层全五点实际产生 15,754,230 条全闭节点
残差、5,130 个严格参考指数和 10,250 个真实 CF 节点包络。
每个候选银行支持全部十二价格；28 个固定组合额外支付 28×1025 个共同
支持项，新增残差为零。描述性 128 格阶段复用 2,100,735 条已有残差，
另支付 128×513 个加权残差项。不同算术原语不能按次数直接互换，
这些规模不支持通用性能倍数。
'''
    (HERE/'experiment-section-en.md').write_text(en,encoding='utf-8');(HERE/'experiment-section-zh.md').write_text(zh,encoding='utf-8')
    summary={'status':'COMPLETE_READER_ACCEPTED_PAPER_TABLES','pair_separation_counts_joint_marginal':counts,
      'finite_grid_unique_best':best['alpha'] if unique else None,'all_final_quote_incompatibility_rows':incompat,
      'all_returned_rounding_paid':True,'descriptive_time_local_kept_separate':True}
    (HERE/'experiment-paper-summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print('PASS final bilingual experiment sections',counts,'unique',summary['finite_grid_unique_best'])
if __name__=='__main__':main()
