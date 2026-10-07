"""Render bilingual manuscript tables from exact audit records."""
from pathlib import Path
from fractions import Fraction as Q
import json,re
HERE=Path(__file__).resolve().parent
def load(n):return json.loads((HERE/n).read_text(encoding='utf-8'))
def write(n,t):
 if n.endswith('-en.md'):
  replacements={'allremainders':'all remainders','allconfiguration':'all configuration','Allconfiguration':'All configuration','allthreshold':'all threshold','allten':'all ten','allfive':'all five','allpoint':'all point','allcontinuous':'all continuous','allstructural':'all structural','allobjective':'all objective','all28':'all 28','all40':'all 40','all3075':'all 3075','all1025':'all 1025','all513':'all 513','allhigh':'all high','all12':'all 12','nooutside':'no outside','every five-point':'each five-point','The joint complete bound is0.':'The joint complete bound is 0.','versus0.':'versus 0.','difference0.':'difference 0.','the0.':'the 0.','through80':'through 80','through128':'through 128','through64':'through 64','have2049':'have 2049','have1430':'have 1430','have8189':'have 8189','has8189':'has 8189','has1025':'has 1025','and1025':'and 1025','for513':'for 513','and512':'and 512','only513':'only 513','with2047':'with 2047','of128':'of 128','the28':'the 28','No28':'No 28','all40pair-mode':'all 40 pair-mode','has2049':'has 2049','the0–2':'the 0–2','the0-2':'the 0-2'}
  # Only ordinary English spacing is edited; scientific tokens and values stay fixed.
  replacements.pop('every alpha',None)
  for old,new in replacements.items():t=t.replace(old,new)
  for old,new in {'descriptive128':'descriptive 128','quarter4400':'quarter 4400','half-year4400':'half-year 4400','and0.':'and 0.','of7.':'of 7.','versus.':'versus .','to128':'to 128','toH':'to H','toN':'to N','40pair':'40 pair','512high':'512 high','512low':'512 low','128bin':'128 bin','plotted0':'plotted 0','nohost':'no host','with28':'with 28','only513':'only 513','all128':'all 128','all1539':'all 1539','rebuilds513':'rebuilds 513','with1025':'with 1025','newly513':'newly 513','original513':'original 513','every513':'every 513','full512':'full 512','complete128':'complete 128'}.items():t=t.replace(old,new)
  t=re.sub(r'([,;])(?=[A-Za-z0-9])',r'\1 ',t)
 (HERE/n).write_text(t.strip()+'\n',encoding='utf-8')
def v(q,n=9):return f'{float(Q(q)):.{n}f}'
def up(q,n=9):
 x=Q(q);scale=10**n;integer=-((-x.numerator*scale)//x.denominator);return str(integer//scale)+'.'+str(integer%scale).zfill(n)
def science(q):return f'{float(Q(q)):.12e}'
def table(headers,rows):return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+'\n'.join('| '+' | '.join(map(str,r))+' |' for r in rows)
def main():
 reg=load('configuration-registry.json');quarter=load('quarter-exact-ledger.json');pairs=load('nearby-pair-resolution.json');centres=load('frozen-output-centre-account.json');cdf=load('portfolio-budget-counts.json');matrix=load('proof-obligation-matrix.json')
 rows=[]
 for r in reg['configurations']:
  nt=r['reference_time_cells'];nt='2048 / 2048 / 1024' if r['configuration_id'] in ['H0','H1'] else ('1429 / 1352 / 549' if r['configuration_id']=='Q0' else str(nt))
  rows.append([r['configuration_id'],r['T'],', '.join(r['alphas']),nt,r['reference_nonzero_nodes'],r['finite_zero_nodes'],r['closed_subcells_per_nonstartup_cell'],r['history_bins']])
 headers_en=['ID','T','alpha','N_t source cells','nonzero ref nodes','zero finite nodes','subcells','history bins']
 headers_zh=['ID','T','alpha','N_t 源时间单元','非零参考节点','有限零置节点','子单元','历史分区']
 cfg_en='''All experiments use model parameter $\\nu=0.2897$, $\\rho=-0.7445$, Riccati mean reversion zero, Fourier step $1/8$, a finite reference/error grid through 128 (1025 nodes), 100-bit outward dyadic arithmetic and 64 forward-moment series terms. The actual Padé output uses composite Gauss–Legendre order 8 through 200 (352 nodes) and Jacobi order 256; its Fourier cutoff is distinct from the certificate cutoff. $N_t$ counts source time cells. The number of frequency nodes is written explicitly to avoid confusing it with $\\nu$.

'''+table(headers_en,rows)+'''

H0 uses the old uniform-state propagation; H1 uses finite-horizon global propagation on the identical field. H2 retains the original low-frequency 128-bin bank. H3/H4 expand the same reference centre through 128, retaining that low bank and adding the newly certified high bank with global/128-bin propagation. Q0/Q1/Q2 keep full history from zero and use exact quarter-terminal interpolation of the original half-year field: Q0 has 1430/1353/550 time knots, and Q1/Q2 have 1430 knots. Their larger-horizon continuous banks are reused; quarter moments, output and tails are recomputed. The original alpha=.9 source field has 1025 time knots and 641 stored frequencies through80; only513 are nonzero reference nodes in H0/H1/Q0. The .52/.60 original fields have2049 knots and1025 stored frequencies through128.

N1/N2 regenerate every five-point field and its continuous residual bank, with two nonstartup subcells (2047/4095 closed cells). N2L is a separately frozen descriptive128-bin reuse of N2 at alpha=.52; it does not replace the nearby-grid objective experiment. The old low and high banks each have8189 closed cells (four nonstartup subcells), for513 and512 frequencies respectively. Thus the0.115215934-point H4 certificate and0.394999331-point N2L certificate concern different reference centres, node coverage and residual banks. Their difference cannot be attributed solely to128-bin propagation. BL-core512/1024 are nominal history-stepping controls whose complete guarantees use the explicitly identified N1/N2/N2L reference bank.
'''
 cfg_zh='''全部实验使用模型参数 $\\nu=0.2897$、$\\rho=-0.7445$、Riccati 均值回复为零、Fourier 步长 $1/8$、截至128的有限参考/误差网格（1025节点）、100位向外舍入二进有理算术及64项前向曲线矩级数。实际 Padé 输出采用截至200的8阶复合 Gauss–Legendre（352节点）和256阶 Jacobi；输出截断与证书截断不同。$N_t$ 表示源时间单元数，频率节点数直接列出，以免与 $\\nu$ 混淆。

'''+table(headers_zh,rows)+'''

H0是旧全时统一状态传播；H1在同一参考场上使用有限期限全局传播。H2保留旧低频128分区bank。H3/H4将同一参考场的参考中心扩至128，保留低频bank，并分别对新增高频bank采用全局/128分区传播。Q0/Q1/Q2均从初始时刻保留完整历史，在旧半年场上精确插值得到季度终点：Q0有1430/1353/550个时间结点，Q1/Q2有1430个。它们复用较长期限的连续残差bank，重新计算季度矩、输出与尾部。旧 alpha=.9 源场有1025个时间结点、截至80的641个存储频率，H0/H1/Q0实际只用其中513个非零参考节点；.52/.60旧场有2049个时间结点、截至128的1025个存储频率。

N1/N2为每个五点候选分别重新生成场和完整连续残差bank，非初始时间单元分成两个闭子单元（2047/4095闭单元）。N2L是事先单独冻结的、alpha=.52下复用N2的描述性128分区对照，不替换邻近网格目标实验。旧低频、高频bank均有8189个闭时间单元（四个非初始子单元），对应513、512个频率。因此H4的0.115215934点与N2L的0.394999331点涉及不同参考中心、参考节点覆盖和残差bank，不能仅归因于128分区传播。BL-core512/1024是名义历史步进对照，其完整保证继承明确标注的N1/N2/N2L参考bank。
'''
 write('config-main-en.md',cfg_en);write('config-main-zh.md',cfg_zh)
 components={r['component']:r for r in quarter['rows']}
 selected=['signed_reference_minus_actual_fast','absolute_centre_charge','used_reference_node_support','finite_zero_node_support','strip','true_infinite_tail','reference_arithmetic','absolute_error_upper']
 names_en=['Signed centre','Absolute centre charge','Used-node support','Finite omitted-node support','Strip remainder','True infinite-tail remainder','Reference arithmetic','Complete upper bound']
 names_zh=['有符号中心','中心绝对值支出','已用节点支持','有限遗漏节点支持','条带余项','真实无限尾余项','参考算术','完整上界']
 def qrows(names):
  rows=[]
  for key,name in zip(selected,names):
   display=science if key=='reference_arithmetic' else up if key=='absolute_error_upper' else lambda x:v(x,12)
   rows.append([name,display(components[key]['joint_index_points_exact']),display(components[key]['marginal_index_points_exact'])])
  return rows
 near=pairs['nearest_pair'];gaprows=near['parts']
 pointcounts=[]
 for cid,a in [('H0','13/25'),('H1','13/25'),('H1','3/5'),('H1','9/10'),('N1','13/25'),('N2','13/25'),('N2L','13/25')]:
  for budget in ['1/4','1/2','1']:
   rr=[r for r in cdf['counts'] if r['configuration_id']==cid and r['alpha']==a and Q(r['exact_budget_points'])==Q(budget)]
   d={r['method']:r['passed_count'] for r in rr};pointcounts.append([cid,a,budget,str(d['marginal'])+'/28',str(d['joint'])+'/28'])
 cr=[[r['configuration_id'],v(r['signed_centre_points']),v(r['complete_radius_points']),up(r['complete_bound_points'])] for r in centres['rows']]
 near_table=[]
 for n in [1024,2048]:
  for mode in ['joint','marginal']:
   unresolved=[r for r in pairs['unresolved'] if r['level']==n and r['mode']==mode]
   near_table.append([n,mode,str(10-len(unresolved))+'/10',', '.join('('+v(r['alpha_a'],3)+','+v(r['alpha_b'],3)+')' for r in unresolved) or 'none'])
 audit_en='''### 7.7. Matched ledgers and certificate resolution

The quarter-maturity decision is attributable to shared aggregation. Q2 uses identical actual output, reference centre,1025 node radii and allremainders in both columns. Finite omitted-node support is zero because every finite node has a nonzero reference. Values below are in index points; exact fractions are retained in quarter-exact-ledger.json.

'''+table(['Component','Joint','Signed marginal'],qrows(names_en))+'''

The joint complete bound is0.233318843 points versus0.252393939 points for signed marginal aggregation; only the joint certificate passes the0.25-point budget. The difference0.019075095 points is entirely the node-support aggregation difference. Complete-bound displays are rounded upward to nine decimal places; component/centre and gap displays are approximate. Every decision and ledger identity uses exact fractional endpoints. Tiny reference arithmetic is displayed separately, and the signed centre is a locator, not an extra additive charge on top of its absolute value.

Every portfolio curve uses the28 originally fixed and fully specified directions. Exact endpoints, allthreshold breakpoints and pass counts are supplied in portfolio-exact-thresholds.csv and portfolio-budget-counts.json. Certification uses the complete rational endpoint condition $B\\leq\\tau$, including equality. Between-bank plots show descriptive changes; joint versus signed marginal within one bank uses matched radii. No28-direction quarterly dataset is inferred from the single quarter spread.

'''+table(['Bank','alpha','Budget points','Marginal','Joint'],pointcounts)+'''

The two nearby levels retain allten unordered pairs, including unresolved ones:

'''+table(['N_t','Method','Separated pairs','Complete unresolved list'],near_table)+'''

The closest N2 joint separation, alpha=.520 versus.525, is an exact positive gap of'''+science(near['strict_gap_exact'])+''' in normalized squared-midpoint loss. Its endpoint identity is $J_{0,B}-J_{0,A}-H_B-H_A-Q_A$ plus any box-intersection endpoint adjustment. The gap decomposition, including used nodes, finite zero nodes, reference strip/tail/arithmetic and midpoint-conversion arithmetic, is recorded exactly in nearby-pair-resolution.json. This is a fixed original midpoint-loss ranking. The midpoint-conversion arithmetic interval does not represent the market bid/ask width; allfive candidates remain separately bid/ask-incompatible.

The unchanged actual half-year4400–4500 output admits the following complete centre accounting:

'''+table(['Bank','Signed centre points','Complete radius points','Complete bound points'],cr)+'''

Expanding H2 toH3 changes the absolute centre charge as well as the paid reference radius; H3 toH4 retains that new centre. N2 toN2L retains its own reference centre and fullremainders. H4 toN2L is a descriptive cross-bank identity, not an ablation. These transitions are exact in frozen-output-centre-account.json, which also reports the common strict-reference certificate floor as a fraction of each BL-core bound. A dominant floor limits what this comparison can establish about intrinsic solver accuracy. When replacement is permitted and the strict reference is already available, returning that reference directly is the simpler workload; frozen-output audit and free replacement answer different tasks.
'''
 audit_zh='''### 7.7. 匹配账本与证书分辨率

季度任务中是否通过预算的改变可以归于共同聚合。Q2两列使用完全相同的实际输出、参考中心、1025个节点半径及全部余项；每个有限节点已有非零参考，有限遗漏节点支持为零。下表单位为指数点；quarter-exact-ledger.json保留精确有理数。

'''+table(['分项','联合','有符号边际'],qrows(names_zh))+'''

联合完整上界为0.233318843点，有符号边际为0.252393939点；仅联合通过0.25点预算。差值0.019075095点完全来自节点支持的聚合方式。完整上界展示值向上舍入至9位小数，分项/中心及间隙只作近似显示；所有决定和账本恒等式均使用精确有理端点。极小参考算术单列；有符号中心用于定位，其绝对值才是对称预算中的一次支出。

全部组合曲线使用原先冻结且权重明确定义的28个方向。portfolio-exact-thresholds.csv和portfolio-budget-counts.json给出精确端点、全部阈值断点和通过数。认证条件是完整有理端点 $B\\leq\\tau$，包含等号。不同bank的曲线属于描述性变化，同bank联合/有符号边际则使用匹配半径。季度单价差不会被扩写成没有计算的28方向数据集。

'''+table(['Bank','alpha','预算点','边际','联合'],pointcounts)+'''

邻近两层完整保留10个无序对，包括未分离结果：

'''+table(['N_t','方法','已分离对数','完整未分离名单'],near_table)+'''

N2中最近的alpha=.520与.525联合严格间隙为'''+science(near['strict_gap_exact'])+'''（归一化平方中点损失）。精确端点分解为 $J_{0,B}-J_{0,A}-H_B-H_A-Q_A$，再加坐标盒交集产生的端点调整。nearby-pair-resolution.json分别列清已用节点、有限零置节点、条带/无限尾/参考算术、固定报价中点换算算术。排名针对原固定中点损失；中点换算的算术区间不是市场bid/ask宽度，五个候选均另行保留原bid/ask不兼容结论。

实际半年4400–4500输出保持不变时，完整中心支出如下：

'''+table(['Bank','有符号中心点','完整半径点','完整上界点'],cr)+'''

H2扩至H3同时改变中心绝对值支出与付清后的参考半径；H3至H4保留新中心。N2至N2L保留其自身参考中心和全部余项。H4至N2L是不同bank的描述性恒等式，不是消融。frozen-output-centre-account.json给出精确转移，还列明共同严格参考证书底座占每个BL-core完整界的比例。底座占主导会限制对求解器内在精度的解释；当允许替换输出、且严格参考已经可得时，直接返回参考价是更简单的工作负载，冻结输出审计与自由替换任务需要分别评价。
'''
 write('audit-main-en.md',audit_en);write('audit-main-zh.md',audit_zh)
 matrixrows=[[r['id'],r['proof_obligation'],r['verification_command'],r['recomputed_scope'],r['inherited_scope']+'; '+r['shared_dependencies']] for r in matrix['obligations']]
 gap_table=[[r['component'],science(r['signed_gap_contribution'])] for r in gaprows]
 floors=[[r['configuration_id'],r['method'],v(r['ideal_reference_certificate_floor_points']),v(r['BL_translation_points']),f"{100*float(Q(r['ideal_floor_fraction_of_BL_bound'])):.6f}%"] for r in centres['BL_reference_floor_shares']]
 en='''### E.2. Numerical identities, scope and evidence map

Allconfiguration IDs and mathematical dimensions are fixed in configuration-registry.json. The following table states the actual reader obligation. Shared elementary interval primitives, shared continuous-derivative generator, reused fixed scientific input and an independently written assembly are distinct types of dependence. These are author-side acceptance checks; nooutside referee execution is presumed.

'''+table(['ID','Obligation','Verification command','Recomputed','Inherited / shared'],matrixrows)+'''

Exact generation commands, their empty-tree versus retained-input behavior, source hashes and boundary notes are in proof-obligation-matrix.json. Run commands in a disposable relative work copy to preserve the fixed packet. In particular, nearby_generate.py regenerates missing fields/residuals, but retains identity-matched components when present. nearby_independent.py can use an identity-matched per-point cache; the top-level fresh acceptance driver deletes every such cache before invocation.

For the explicitly retained V2 entrypoint source snapshots, the complete --full distinction is:

'''+table(['Entry point','Additional executed obligation','Outside that command'],[[r['entry'],r['newly_executes'],r['does_not_execute']] for r in matrix['flag_semantics']])+'''

Thus the retained V2 reproduce.py --full adds structural-sign regeneration. It does not regenerate allcontinuous residual derivatives. Its source SHA is not imposed on the new V3 top-level driver. The original low continuous generator requires run_evidence.py --regenerate-continuous; the high-frequency generator requires run_frontier.py --regenerate-full, which uses a distinct reconstruction clone and preserves the fixed transfer input receipts. The historical CI checks source identities and the retained acceptance receipt binding; it does not perform the large-bank interval replay. A stored PASS receipt, byte identities, executed recomputation and a mathematical theorem remain separately identifiable evidence.

The exact closest-pair gap equals the sum of the following signed contributions; scientific notation is a display only:

'''+table(['Gap contribution','Normalized loss contribution'],gap_table)+'''

The quarterly account has zero finite omissions; its infinite tail beyond128 remains paid. The unused-node term in the nearby/global controls is nonzero and cannot be dropped by borrowing the quarter full-reference result. Exact ledger fractions and all40pair-mode records are delivered with independent secondary readback and intentional corruption controls.

Common ideal strict-reference floor in the BL-core complete bound:

'''+table(['Bank','Nominal output','Reference floor points','Translation points','Floor / complete bound'],floors)+'''

The separate returned-reference ratio also pays binary64 return rounding and is retained in the machine ledger. A small BL512/1024 nominal difference is an empirical comparison; its complete guarantee uses the same reference floor plus exact output translation. These floor fractions do not establish an intrinsic BL error estimate.

portfolio-pass-counts.svg and portfolio-pass-counts.pdf show the exact-endpoint pass-count step functions for the original three candidates and the regenerated alpha=.52 controls. Coordinates are converted to display decimals only after exact counting. The plotted0–2-point range is stated explicitly; allthresholds are retained in the CSV/JSON. Cross-bank curves are descriptive and within-bank methods share radii. Only typed scientific work counts, evidence bytes and version/hash identities are used; nohost or duration measurements are part of this audit.
'''
 zh='''### E.2. 数值恒等式、证明范围与证据对应

configuration-registry.json固定全部配置ID和数学规模。下表以源码实际行为区分读取器义务。共同基础区间原语、共同连续导数生成器、复用固定科学输入与独立编写聚合，是不同种类的依赖。本轮是作者侧验收，不能表述为外部审稿人已经执行。

'''+table(['ID','证明义务','验证命令','重新计算范围','继承/共享'],matrixrows)+'''

proof-obligation-matrix.json列出精确生成命令、空输出目录与现存输入时的行为、源码哈希和边界。命令应在相对路径的可丢弃工作副本运行，以保持冻结包。nearby_generate.py只生成缺失的场/残差；已有且身份匹配的部件会复用。nearby_independent.py可使用身份匹配的逐点缓存；顶层fresh验收会在调用前删除这些缓存。

以下入口表对应明确留存的V2源码快照；--full与连续重生成必须区分：

'''+table(['入口','实际新增执行','该命令不覆盖'],[[r['entry'],r['newly_executes'],r['does_not_execute']] for r in matrix['flag_semantics']])+'''

因此留存的V2 reproduce.py --full增加结构符号重生成，不重算全部连续残差导数；不会用其源码SHA冒验新V3顶层driver。旧低频连续生成需run_evidence.py --regenerate-continuous；高频生成需run_frontier.py --regenerate-full，后者使用独立重建副本，保持固定季度证据输入。历史CI检查源码身份及已留存验收收据的绑定，不执行大型bank区间重读。留存PASS收据、字节身份、真正重新计算与数学定理是分别识别的证据。

最近邻严格间隙等于以下有符号贡献之和；科学计数法只用于展示：

'''+table(['间隙分项','归一化损失贡献'],gap_table)+'''

季度分账的有限遗漏为零，但截至128之后的无限尾仍完整支付。邻近/全局控制的有限零置项非零，不能借用季度全参考结果删掉。交付精确有理账本和全部40条pair-mode记录，并有独立二次重读及有意义的故意破坏负控。

BL-core完整界中的共同理想严格参考底座：

'''+table(['Bank','名义输出','参考底座点','平移点','底座/完整界'],floors)+'''

机器账本另行记录付清binary64返回舍入的参考价比例。BL512/1024名义差是经验比较；其完整保证仍为共同参考底座加实际输出的精确平移。这些比例不能给出BL算法的内在误差估计。

portfolio-pass-counts.svg及portfolio-pass-counts.pdf展示旧三候选和重新生成alpha=.52控制的精确端点通过数阶梯。先用有理数计数，再转换展示坐标。绘图明示0–2点范围，CSV/JSON保留全部阈值。跨bank曲线是描述性比较，同bank方法半径匹配。审计只使用明确类型的科学工作量、证据字节和版本/哈希身份，不纳入设备信息和执行计时。
'''
 write('appendix-e-en.md',en);write('appendix-e-zh.md',zh)
 print('PASS six bilingual manuscript fragments from exact ledgers')
if __name__=='__main__':main()
