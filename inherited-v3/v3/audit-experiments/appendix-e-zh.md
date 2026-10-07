### E.2. 数值恒等式、证明范围与证据对应

configuration-registry.json固定全部配置ID和数学规模。下表以源码实际行为区分读取器义务。共同基础区间原语、共同连续导数生成器、复用固定科学输入与独立编写聚合，是不同种类的依赖。本轮是作者侧验收，不能表述为外部审稿人已经执行。

| ID | 证明义务 | 验证命令 | 重新计算范围 | 继承/共享 |
| --- | --- | --- | --- | --- |
| S1 | Padé coefficient signs on the original parameter rectangle | python bc-merged-20261007/full_structure_verify.py | 211241 structural sign leaves and rectangle cover | model/parameter definitions; original strict interval algebra and generalized-power primitives |
| S2 | Startup Caputo residual and left-halfplane enclosure | python bc-merged-20261007/startup_independent.py | all513 frequencies for each of the three original startup cells | stored field dyadics and later-time continuous residuals; Gamma/power/dyadic outward primitives |
| R1 | Full original alpha=.52 low-frequency continuous residual cover | python heston-nine-point-20261007/check-time-envelope.py | 8189 closed cells x513 entries: cover, saved dyadic values and per-node maxima; startup audited separately | derivative inequalities in identified continuous generator; NumPy enclosure with proved dot-product error and strict scalar primitives |
| R2 | Full alpha=.52 high-frequency continuous residual cover | python heston-frontier-20261007/omission-verify.py | 8189 closed cells x512 entries: exact bank, startup/halfplane, saved-node maxima | identified Caputo derivative-generator inequalities; strict scalar primitives and original continuous generator |
| P1 | Global finite-history and low-frequency128-bin price accounts | python heston-nine-point-20261007/verify-finite-history-independent.py; python heston-nine-point-20261007/independent-time-local.py | forward masses, complete cell intersections, 513 tightened radii, all1025 finite terms and complete spread remainder | continuous residual theorem/validity and identified stored field; strict forward-moment, exponent and true-tail primitives |
| P2 | Expanded-reference frozen half-year output account | python heston-frontier-20261007/independent-omission.py | changed reference centre, all1025 support terms, old/new complete interval intersection, global/local high-frequency accounts | same actual fast output and continuous residual banks; original strict moment/scalar primitives |
| Q1 | Quarter-maturity used64 certificate and actual fast output | python heston-frontier-20261007/independent-transfer.py --full | all three exact terminal interpolations, 1539 restricted exponents, three original fast-output calculations, all3075 true finite CF/tail/price terms | larger-horizon continuous residuals and halfplane certificate; strict moment/trig/dyadic/true-tail libraries; original fast implementation used only for output replay |
| Q2 | Quarter full128 global and128-bin complete certificate | python heston-frontier-20261007/independent-transfer-supplement.py --full | all1025 restricted exponents, all1025 CF/tail/coefficient/radius terms, allhigh bank entries, all128 local weights and exact account | low/high continuous derivative validity; actual fast replay is separately performed by Q1; strict moment/trig/dyadic/true-tail libraries; path helpers of Q1 |
| N1 | Fresh fields/residuals at the five nearby alpha points | python nearby_independent.py --N 1024; python nearby_independent.py --N 2048 | all cells, startup, halfplane, 513 exponents and1025 CF/coefficient terms per point; allobjective/pair decisions | strict proof of continuous residual generator and final propagation theorem; declared sdk outward primitives, stored reference data |
| N2 | Descriptive128-bin reused-bank control, outside nearby objective grid | python local_output_independent.py | 128 exact positive weights, every intersecting closed-bank maximum,513 tightened radii, all12 prices and allactual output rounding | complete identity-matched N2048 point proof and continuous residual generator; same strict moment/trig/dyadic primitives |
| C1 | Same model and complete tolerance for frozen/direct/corrected/BL-core outputs | python workload_controls_independent.py --N 2048 --local128 | exact stored-output centre translation, allsame-reference remainder and28 portfolio supports; BL nominal-output metadata identity | reference certificate, BL nominal-output producer and its stored dyadics; same strict outward coefficient primitives |

proof-obligation-matrix.json列出精确生成命令、空输出目录与现存输入时的行为、源码哈希和边界。命令应在相对路径的可丢弃工作副本运行，以保持冻结包。nearby_generate.py只生成缺失的场/残差；已有且身份匹配的部件会复用。nearby_independent.py可使用身份匹配的逐点缓存；顶层fresh验收会在调用前删除这些缓存。

以下入口表对应明确留存的V2源码快照；--full与连续重生成必须区分：

| 入口 | 实际新增执行 | 该命令不覆盖 |
| --- | --- | --- |
| reproduce.py default | fixed-copy saved evidence readers; original frontier always requests bothquarter readers --full; new nearby reader point caches deleted by this top driver | allcontinuous residual generators or allstructural signs |
| reproduce.py --full | default plus all211241 original structural sign leaves | fresh low/high/new-nearby continuous derivative generation |
| baseline/.../run_evidence.py --regenerate-continuous | original alpha=.52 513-node low continuous generator and retained8189-cell bank | new five-alpha reference/residual generation |
| baseline/.../run_frontier.py --regenerate-full | separate-clone full512 high continuous generator plus fresh-bank audit | alter fixed quarter input receipts |
| nearby_generate.py --N N | missing field/residual/exponent components; otherwise reuses identified existing components | force regeneration over already retained scientific output |
| publication-v2 CI source.yml | source manifest identities and retained acceptance receipt binding | NumPy bank replay, interval arithmetic replay or residual generation |

因此留存的V2 reproduce.py --full增加结构符号重生成，不重算全部连续残差导数；不会用其源码SHA冒验新V3顶层driver。旧低频连续生成需run_evidence.py --regenerate-continuous；高频生成需run_frontier.py --regenerate-full，后者使用独立重建副本，保持固定季度证据输入。历史CI检查源码身份及已留存验收收据的绑定，不执行大型bank区间重读。留存PASS收据、字节身份、真正重新计算与数学定理是分别识别的证据。

最近邻严格间隙等于以下有符号贡献之和；科学计数法只用于展示：

| 间隙分项 | 归一化损失贡献 |
| --- | --- |
| reference_midpoint_objective_difference | 7.939186982887e-09 |
| used_node_support_both_candidates | -4.690368762320e-09 |
| finite_zero_support_both_candidates | -1.217354923855e-09 |
| strip_both_candidates | -1.855578458131e-12 |
| true_infinite_tail_both_candidates | -9.568024410400e-11 |
| reference_arithmetic_both_candidates | -6.928606526135e-23 |
| midpoint_conversion_arithmetic_both_candidates | -4.770477111773e-27 |
| candidate_a_quadratic_remainder | -1.195663126282e-09 |
| box_intersection_endpoint_adjustment | 0.000000000000e+00 |

季度分账的有限遗漏为零，但截至128之后的无限尾仍完整支付。邻近/全局控制的有限零置项非零，不能借用季度全参考结果删掉。交付精确有理账本和全部40条pair-mode记录，并有独立二次重读及有意义的故意破坏负控。

BL-core完整界中的共同理想严格参考底座：

| Bank | 名义输出 | 参考底座点 | 平移点 | 底座/完整界 |
| --- | --- | --- | --- | --- |
| N1 | BL modified-Adams core N=512 | 0.423484833 | 0.000853401 | 99.798887% |
| N1 | BL modified-Adams core N=1024 | 0.423484833 | 0.000305328 | 99.927953% |
| N2 | BL modified-Adams core N=512 | 0.261808768 | 0.000845646 | 99.678039% |
| N2 | BL modified-Adams core N=1024 | 0.261808768 | 0.000297572 | 99.886469% |
| N2L | BL modified-Adams core N=512 | 0.228237113 | 0.000845646 | 99.630856% |
| N2L | BL modified-Adams core N=1024 | 0.228237113 | 0.000297572 | 99.869791% |

机器账本另行记录付清binary64返回舍入的参考价比例。BL512/1024名义差是经验比较；其完整保证仍为共同参考底座加实际输出的精确平移。这些比例不能给出BL算法的内在误差估计。

portfolio-pass-counts.svg及portfolio-pass-counts.pdf展示旧三候选和重新生成alpha=.52控制的精确端点通过数阶梯。先用有理数计数，再转换展示坐标。绘图明示0–2点范围，CSV/JSON保留全部阈值。跨bank曲线是描述性比较，同bank方法半径匹配。审计只使用明确类型的科学工作量、证据字节和版本/哈希身份，不纳入设备信息和执行计时。
