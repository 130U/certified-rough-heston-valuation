# 第二轮集中修订与瓶颈研究

## Charter

目标：交付修订合稿、精确组合表、公开可下载的固定证据包及实际验收记录；完成一项针对新瓶颈或可迁移性的完整新结果。知识深度：已有证明和冻结账本为深入；新省略节点与第二期限证书尚未验收。

范围 / 对象 / 主题：Rough Heston 完整定价误差认证 / 当前合稿和误差机制 / 原期限省略节点、正核条件、第二期限及验收包。

类型：首先对既有结果开展实验型证据核查；新计算单独采用事前固定的描述型实验合同。不会将事后已知结果标成事前注册。

Q1：原主要结论能否完整重跑、固定字节核验并公开下载？

Q2：省略频率的非零参考能否在保持同一实际快速输出、合法更新中心的情况下改善完整界？

Q3：正核条件是否可精确放宽，并给出显式常曲线解释？

Q4：另一期限的完整误差和成本是否可认证？若缺少必要证据，保留失败或未验收状态。

Q5：修订文字是否准确分离传播改善、联合结构、动作数和实际成本？

既有改善的候选原因：有限历史权重改变；逐时包络进一步收紧；相同上游半径下的共同傅里叶方向相消。判别方法是固定其他项的匹配比较。新省略节点与新期限是另外的合同，不能混入旧改善的归因。

预先分组：期限、alpha、组合权重、传播方式、参考节点范围、预算阈值、执行阶段。原结果已知；新合同注明固定时间和已知信息。

## Canonical sources

1. 原始数学论文全文（Caputo 凸性、分数阶残差比较、Volterra 仿射模型），用于工具归属和适用条件。
2. 用户评审原文及作者冻结的原始证据，版本为 heston-nine-point-20261007，原文件全部保留。
3. GitHub 官方 release/API 文档，用于实际公开证据交付。
4. 本轮源码、精确有理账本、运行日志与 PDF 渲染，直接检查实际行为。

外部文献只用原始来源；检索界限不构成排除所有先行工作的证明。

## Findings ledger

| 编号 | 主张 | 证据 | 等级 | 问题 |
|---|---|---|---|---|
| F1 | 评审尚未取得证据 ZIP；这不证明文件错误或不存在 | 用户本轮完整中文评审，第五部分 | 1 | Q1 |
| F2 | 旧组合合同确实包含完整28方向，但PDF仅概述类别 | ../heston-nine-point-20261007/portfolio-contract.json；manuscript/merged-heston-en.md §11.4 | 1/3 | Q5 |
| F3 | 本轮初始快照：PR1仍是旧45页修订，FH包尚未作为release asset提供 | GitHub connector，2026-10-07，PR1 head54c0167，release列表仅v1.0.0 | 3 | Q1 |
| F4 | GitHub release支持单个文件小于2GiB，现有约187MB包适用 | https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases ，全文读取2026-10-07 | 2 | Q1 |
| F5 | 本机CPU为Intel Core Ultra7 155U，12核14逻辑处理器 | 本轮只读Win32_Processor查询 | 3 | Q5 |
| F6 | 固定ZIP公开无凭据下载成功，243文件全部SHA256读回一致 | public-finite-download.json；公开v0.2.0-certification-20261007具名资产 | 3 | Q1 |
| F7 | 最终固定ZIP的完整冷启动18项验收全部通过，总父进程221.018秒，峰job提交内存697569280字节 | cold-acceptance.json，tested manifest fcd4c4ea...，完整cold-acceptance.log | 3 | Q1/Q5 |
| F8 | q非负条件、常曲线显式界及合法参考平移有条件证明；下降解析例不认证随机模型 | theory-proof-zh.md TQ1–TQ26；theory-evidence-ledger.json；theory-section-en.md FQ1–FQ8 | 1/3 | Q3 |
| F9 | 新512高频全部8189闭单元实际生成；原快速输出不变，新中心支付后原任务完整上界0.115215934点、通过¼ | omission-full-execution.json；omission-results.json；independent-omission.json，8项负控；omission-verification.json，6项负控 | 3 | Q2 |
| F10 | 新T=1/4三候选初始完整联合界1.207557898、0.801202097、0.497738795；所有初始¼均未认证 | transfer-results.json；independent-transfer.json；三候选新输出/指数/尾重新计算 | 3 | Q4 |
| F11 | T=1/4 α=.52 full128全局参考上界0.351318692点，仍¼未认证；该阶段后才冻结单次128bin探索 | transfer-supplement-contract.json；transfer-supplement-results.json；transfer-time-local-contract.json | 3 | Q4 |
| F12 | 同一季度full128参考/输出/中心/余项，128bin联合0.233318843点认证¼，而匹配边际0.252393939未认证 | transfer-time-local-results.json；independent-transfer-supplement.json的time_local_verification；transfer-execution-receipt.json | 3 | Q4/Q5 |

| F13 | 最终双语数学源读回通过；英文58页/中文47页，194展示公式每语，0字形页边界异常，全部105页接触表及关键整页已实际视觉检查 | frontier-manuscript-review.json；qa/pdf-verification.json；qa/visual-inspection.json及分工关键整页检查 | 3 | Q5 |

| F14 | 首次扩展整包执行在原18项及新高频读回通过后因遗漏原稿身份依赖退出；49文件闭包仅缺88816字节原rough-heston.md，补入可变副本后两transfer --full均通过；数值未改变 | packaging-first-attempt.log；packaging-first-attempt-diagnostic.json；明确-v2包补入原9ea6200a...哈希文件 | 3 | Q1 |

整包单命令执行和公开读回收据将单独具名交付，以保持固定ZIP字节不变。没有证据的方向列为待解决问题。

## Scope filter

F1–F14无项删除。将“独立验收”限定为作者侧第二实现读回与新副本实际执行；外部审稿验收尚待其自行运行。q核条件属于条件式解析传播；先行Caputo凸性和正逆算子准确归属原论文。任何认证上界变化均不改写为真实误差或交易损失变化；单位动作最优性不改写为耗时最优性。

## Object filter

F1–F14无项删除。固定ZIP的公开下载和全18步骤验收仅涵盖其版本；新省略节点和第二期限另有完整账本。不同参考中心、输出、期限和菜单分别记账。F10的“¼均失败”限定为初始through64/global阶段；F12是读过F11之后才冻结的单次探索，不能改写成原始事前主检成功。F9不套用于新期限，F12不扩大为所有期限。公开release标注prerelease且保留旧release和main。

## Conclusions

1. 原50页阶段的缺口“无法取得固定证据ZIP”已补齐可用公开具名下载；实际公共下载和全文件哈希读回通过（F6）。
2. 同一固定ZIP从新解释器和新解压副本执行完整--full序列18/18通过；scope明确区分残差重新生成和保存包络的完整验证（F7）。
3. 正核条件可以作条件式放宽，并保留初值、物理尺度和完整历史；其解析曲线例不构成概率模型认证（F8）。

4. 原期限省略频率瓶颈已由完整新增连续认证、合法参考中心平移和独立金融账本闭合；原任务最佳完整上界0.115215934点（F9）。
5. 完成另一合法期限的价格任务和完整证据，不再只停留单一期限。新期限¼预算的最终匹配判定由联合结构改变；初始及全局失败未被删除（F10–F12）。

证据支持具体对象的认证与迁移实例，不支持实际交易损失降低、所有期限性能保证、未知动作成本最优性或排除所有先行工作。

## Next steps / Risks

保持旧冻结不变；新对象单独存放。若第二期限缺少合法strip/tail或上游半平面证据，不能仅复用旧数字。公开链接必须独立下载后核验字节。9分由后续评审判断，不预先宣布。
