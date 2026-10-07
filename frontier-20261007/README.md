# Heston认证：省略频率与第二期限扩展，2026-10-07

本版本保留旧冻结，并集中补齐评审要求：全部28组合的持仓尺度、公开固定证据、冷启动成本、正核条件、原快速输出的高频参考重认证及第二期限的完整误差账本。9分是后续评审目标，不是作者自评已获的外审分数。

[公开版本页面](https://github.com/130U/certified-rough-heston-valuation/releases/tag/v0.2.0-certification-20261007)提供具名资产。请下载上传的证据ZIP，GitHub自动Source code归档不包含全部原始数值数据。

本轮入口使用明确的 `-v2.zip` 包装修订。首次完整执行发现第一扩展ZIP漏收原始稿件身份依赖；该稿88816字节的精确SHA与原合同一致，已补入v2。原失败日志和49项依赖诊断保留，不改变任何定价数字。当前独立PDF资产名以 `-EN-v2.pdf`、`-ZH-v2.pdf` 结尾。

- [原有限历史证据ZIP](https://github.com/130U/certified-rough-heston-valuation/releases/download/v0.2.0-certification-20261007/Theodore-Ouyang-Heston-Finite-History-Evidence-20261007.zip)：SHA256 `edc25d2ad86c1526f404ec1a46a02a283f0726602f259beaa97eb1219d22d299`。
- [本轮完整扩展ZIP](https://github.com/130U/certified-rough-heston-valuation/releases/download/v0.2.0-certification-20261007/Theodore-Ouyang-Heston-Frontier-Evidence-20261007-v2.zip)：身份见同页 `frontier-bundle-receipt-v2.json` 及解压后的 `FRONTIER-MANIFEST.json`。

Python3.11+与NumPy2.3.5；本机已测Python3.12.14。数学验收不需联网、SciPy、TeX或PDF生成依赖。新包自带三个旧依赖目录和本轮目录，在解压根目录运行：

```text
python heston-frontier-20261007/run_frontier.py --full
```

该命令核验冻结字节，复制完整工作副本，然后运行旧18项完整序列、所有新增高频保存包络检查、参考指数与完整预算重算、另一套高频读回，以及第二期限完整独立读回。输出写入独立 `frontier-verification-work-*`，末尾再次核验原冻结身份。文件身份不代替证明；代码、原始包络、数学证明和独立读回共同支撑相应结论。

可选重新生成所有新增512个高频连续残差：

```text
python heston-frontier-20261007/run_frontier.py --full --regenerate-full
```

原513个已用节点的完整残差重生成仍由旧包的 `--regenerate-continuous` 命令提供。默认路径检查完整保存包络并重新计算传播、指数与金融账本，分别标注保存检查和新残差生成。

可选新生成放在第二个隔离副本并核查，后续transfer读回仍使用原固定副本，避免把新生成的计时元数据SHA误当作既有固定收据。两条证据路径和日志分别标识。

主要入口：

- `manuscript/merged-heston-en.md`、`merged-heston-zh.md`：完整可编辑合稿；`paper/`为矢量数学PDF。
- `theory-proof-zh.md`、`theory-section-*.md`：q核条件、常曲线推论、合法非零省略节点参考。
- `omission-contract.json`、`omission-*.json/npz`：高频完整证据及预先固定合同；`independent-omission.py`为独立读回。
- `transfer-contract.json`、`transfer-results.json`、`independent-transfer.py`：T=1/4，三候选、原4400/4500任务的全部结果与失败；`transfer-supplement-*`、`independent-transfer-supplement.py`提供明确另列的扩展参考和逐时账本。
- `cold-acceptance.json`、`cold-logs/`：同一原固定ZIP从新解释器和新解压副本运行的18/18完整验收；明确线程、物理硬件、内存定义与冷启动计时范围。
- `RESEARCH-RECORD-zh.md`：来源、证据表和适用边界；`REVIEW-RESPONSE-zh.md`：逐项评审回应。

范围：同一模型、曲线及指定任务的认证上界，不是实测真实误差或交易损失。参考改变后中心与算术同步重算；旧固定菜单下界不等于所有认证方法或真实误差的下界。新期限不提供新市场报价或连续校准结论。下降曲线是解析示例，未另行证明随机方差模型的可实现性。多agent与本地重跑属于作者侧验收；外部审稿人的独立运行仍由其自行确认。一般分数阶残差与成本分配的先行工具有明确归属，有限文献检索不支持绝对优先权主张。
