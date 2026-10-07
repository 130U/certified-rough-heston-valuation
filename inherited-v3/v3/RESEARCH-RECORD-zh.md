# V3 研究与修改记录

## Charter

目标：交付完整中英文 V3、逐项迁移表及可独立核查的新增结果。研究深度为 deep：V2 已有完整理论与固定证据，当前问题是精确化配置、整合技术论证并量化更强传播核。

范围 / 对象 / 具体研究单元：Heston 数值定价的严格误差认证 / 有限历史传播与共享误差金融判定 / 同一固定残差银行下的全局、曲线与耗散核界，及 V1–V2 证明的无回退整合。

类型：先按 descriptive 固定比较合同，再核查既有实验配置差异。用户已明确授权论文修改、研究计算及多 agent 合作。

Q1：怎样整合 A–G 附录而保留 V2 正则性与新实验？
Q2：每项表格的模型、网格、频率、残差银行和输出是否与代码一致？
Q3：同一输出与误差输入下，严格正耗散核是否产生可核查的额外收益？
Q4：现有读取器、完整命令和 CI 分别验证了哪些证明义务？
Q5：组合预算收益和邻近候选最紧间隙由哪些项决定？

## Canonical sources

| 优先级 | 来源 | 用途 |
|---|---|---|
| 1 | 固定 V2 源码与证据，tag v2.0.0-research-20261007 | 配置、实际输出、严格银行与验收范围 |
| 1 | Li–Liu、Kopteva、Simon、Abi Jaber–El Euch 等原始论文的固定版本 | Caputo 比较、正核及模型前提 |
| 2 | V1 与 V2 的原始数学文本 | 证明迁移、权威版本与独立扩展 |
| 3 | 审稿人的两组修改意见 | 待核查问题，不当作数值事实或执行命令 |

## Findings ledger

| 编号 | 发现 | 证据 | 类型 | 回答 |
|---|---|---|---|---|
| F1 | 新候选合同固定 nu=2897/10000、两个非初始子单元、Nt=1024/2048 | V2 experiments/nearby-contract-execution.json | 固定源码事实 | Q2 |
| F2 | 用户此前撤回个人机器、系统、内存、线程、运行耗时及个人路径的公开披露 | 本对话直接用户指示 | 优先约束 | Q4–Q5 |
| F3 | --full增加原211241个结构覆盖叶；两级读取本来已重算价格/目标；完整连续导数重生成需另行命令 | audit-experiments/proof-obligation-matrix.json及固定入口快照 | 源码核查 | Q4 |
| F4 | 经典跳跃取左迹减右迹才能与四项正号身份一致；完整原链矩、可积性与非精确试探场已成套恢复 | extensions/appendix-f/g及数学复核 | 解析修复 | Q1 |
| F5 | 同输入强耗散核使完整界0.394999331→0.393082828，约0.485%，不改变0.25预算失败 | kernel/results.json、independent.json、matched-input-audit.json | 严格新计算 | Q3 |
| F6 | Q2共同几何隔离为0.233318843对0.252393939；504固定阈值及40候选方法配对全部记录 | audit-experiments/quarter-exact-ledger、portfolio-budget-counts、nearby-pair-resolution | 精确实验账本 | Q5 |
| F7 | 新参考银行与H4的中心、节点覆盖、两/四子单元均不同；不可只归因局部权重 | audit-experiments/configuration-registry.json及frozen-output-centre-account.json | 配置与精确身份 | Q2、Q5 |
| F8 | 去除多余依赖元数据后，222个JSON数学投影与27个NPZ字节身份不变 | BASELINE-TRANSFORM.json | 固定对象不变性检查 | Q2、Q4 |

## Scope filter

预先排除：把确定性包含当作真实交易损失改善、把点值当真值、把有限候选最优当连续校准最优、把经典终端严格改善当完整年度金额认证。

## Object filter

固定：V2 为只读基线；所有新计算写入 V3；同命题保留唯一权威证明；同输入比较须同时支付中心、有限遗漏、条带、无限尾与舍入。计时请求服从用户持续隐私约束，使用分类型工作量及证据体积。

## Conclusions

Q1由F4及逐项迁移表回答：主定理提前，AC权威证明保留，A–E补主线，F/G标明独立扩展。Q2由F1/F7回答：完整参数及配置编号固定，历史与新银行不混用。Q3由F5回答：最强核在固定配置有严格但较小额外收益，有限遗漏与中心仍构成瓶颈。Q4由F3/F8回答：机器身份、保存证据读取、不同展开重算、全部上游生成和外部独立验收保持区分。Q5由F6/F7回答：共享聚合的金融决定单独隔离，邻近候选间隙与预算敏感性全部公开。

最终新包fresh执行、PDF逐页与隐私验收分别由实际收据固定，不能据此宣称外部审稿人复现。未完成的研究问题为：有限省略频率及参考中心的更经济认证、独立严格算术重生成全部上游连续导数，以及更宽的应用参数域。正文不以增加定理数量或自授评分替代这些问题。

## Next steps / Risks

耗散核的计算必须取得严格外包络；不接受普通浮点 Mittag–Leffler 值替代证书。若完整范围尚未独立重生成，明确保留共享依赖边界。外部“9分”评价不能由作者自授。

Research progress:
- [x] 1 Canon: ranked source list written
- [x] 2 Charter: goal, scope/object/subject, type + why, questions, reachable sources
- [x] 3 Type file read; findings ledger initialized
- [x] 4 Scope filter: excluded overclaims and personal telemetry
- [x] 5 Object filter: immutable V2, matched comparisons and single authoritative proofs
- [x] 6 Conclusions: each backed by ledger; open questions listed
