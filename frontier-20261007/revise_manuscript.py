"""Revise the frozen 50-page manuscript; all earlier sources stay unchanged."""
from pathlib import Path
import hashlib,json,re
HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'heston-nine-point-20261007'
RELEASE='https://github.com/130U/certified-rough-heston-valuation/releases/tag/v0.2.0-certification-20261007'
BASEZIP='https://github.com/130U/certified-rough-heston-valuation/releases/download/v0.2.0-certification-20261007/Theodore-Ouyang-Heston-Finite-History-Evidence-20261007.zip'
NEWZIP='https://github.com/130U/certified-rough-heston-valuation/releases/download/v0.2.0-certification-20261007/Theodore-Ouyang-Heston-Frontier-Evidence-20261007-v2.zip'

def portfolio_table(zh):
    if zh:
        s='以下定义固定全部28个方向。令 \\(K_i=3700+100i\\)，\\(0\\le i\\le11\\)，\\(e_i\\) 为第i个执行价的单位持仓向量；未列分量均为零。\n\n'
        s+='| 类别 | 个数 | 完整持仓定义 | 总绝对持仓 |\n|---|---|---|---|\n'
        rows=[('相邻价差','11',r'\(e_i-e_{i+1}\), \(i=0,\ldots,10\)','2'),('相邻蝶式','10',r'\(e_i-2e_{i+1}+e_{i+2}\), \(i=0,\ldots,9\)','4'),('宽价差','4',r'\(e_0-e_3,e_3-e_6,e_6-e_9,e_0-e_{11}\)','2'),('全执行价篮子','1',r'\(12^{-1}\sum_{i=0}^{11}e_i\)','1'),('低执行价篮子','1',r'\(6^{-1}\sum_{i=0}^{5}e_i\)','1'),('高执行价篮子','1',r'\(6^{-1}\sum_{i=6}^{11}e_i\)','1')]
    else:
        s='The following definitions specify all 28 directions. Let \\(K_i=3700+100i\\), \\(0\\le i\\le11\\), and let \\(e_i\\) denote one option unit at strike i; unspecified components are zero.\n\n'
        s+='| Portfolio family | Count | Complete position definition | Gross option units |\n|---|---|---|---|\n'
        rows=[('Adjacent spreads','11',r'\(e_i-e_{i+1}\), \(i=0,\ldots,10\)','2'),('Adjacent butterflies','10',r'\(e_i-2e_{i+1}+e_{i+2}\), \(i=0,\ldots,9\)','4'),('Wide spreads','4',r'\(e_0-e_3,e_3-e_6,e_6-e_9,e_0-e_{11}\)','2'),('All-strike basket','1',r'\(12^{-1}\sum_{i=0}^{11}e_i\)','1'),('Lower-strike basket','1',r'\(6^{-1}\sum_{i=0}^{5}e_i\)','1'),('Upper-strike basket','1',r'\(6^{-1}\sum_{i=6}^{11}e_i\)','1')]
    for row in rows:s+='| '+' | '.join(row)+' |\n'
    s+=('\n宽价差端点依次为3700/4000、4000/4300、4300/4600及3700/4800。每个价格单位是一份期权的指数点价格，表内权重为固定名义持仓；指数点到报告货币的乘数取1，不宣称交易所合约的美元名义本金。\\(c=C/(DF)\\)，本任务\\(DF=4221.86\\)。若全部持仓乘以\\(a\\)，绝对误差界乘以\\(|a|\\)，相同一点阈值的通过数可能改变。三个正篮子权重之和均为1；价差和蝶式没有额外归一化。完整逐方向JSON与本表逐项一致。\n\n' if zh else
        '\nThe wide endpoints are 3700/4000, 4000/4300, 4300/4600, and 3700/4800. Each option unit is priced in index points; the displayed weights are the fixed position notionals. The reporting currency multiplier is one currency unit per index point; no exchange-contract dollar notional is asserted. With \\(c=C/(DF)\\), this task has \\(DF=4221.86\\). Scaling every position by \\(a\\) scales its absolute-error bound by \\(|a|\\), so pass counts at a fixed one-point threshold can change. Each positive basket has total weight one; spreads and butterflies have no further normalization. The full direction-by-direction JSON agrees with this table.\n\n')
    return s

def main():
    receipts={}
    for lang in ['en','zh']:
        zh=lang=='zh';src=OLD/'manuscript'/f'merged-heston-{lang}.md'
        s=src.read_text(encoding='utf-8')
        if not zh:
            s=s.replace('Finite-history propagation certifies the original selected spread within one index point at the unchanged output, and 28 preselected portfolios compare shared-node and signed marginal bounds with complete budgets.',
                'Finite-history propagation reduces the selected complete bound from 1.397613 to 0.378599 index points at the unchanged output; time-local envelopes further give 0.367258782. Complete certification of 512 omitted frequencies, with a legally updated reference centre, then gives 0.115215934 points and certifies the quarter-point task at the same fast output. At matched radii and a half-point budget, the selected candidate certifies 28/28 preselected portfolios jointly versus 13/28 with signed marginal bounds. A complete quarter-year refinement gives 0.233318843 points jointly versus 0.252393939 marginally, separating the quarter-point decision. Earlier failed stages are retained. The positive fractional curve-kernel condition is stated explicitly.')
        else:
            # Append a compact result paragraph inside the abstract when the earlier
            # translation's precise phrasing differs.
            p=s.index('**关键词')
            s=s[:p]+'有限历史传播在同一快速输出下，将首选价差完整界从1.397613点收紧至0.378599点，逐时包络进一步至0.367258782点。新增512省略频率的完整认证和合法参考中心平移进一步给出0.115215934点，通过原快速输出的四分之一点任务。在相同新节点半径、0.5点预算下，联合方法通过28/28个预定组合，有符号边际通过13/28。第二个季度期限的完整改进取得联合0.233318843点、有符号边际0.252393939点，分别通过和未通过四分之一点预算，保留此前失败阶段；正分数阶曲线核条件明确。\n\n'+s[p:]
        s=s.replace('Unchanged-output one-point breakthrough; complete 28-portfolio comparisons','Unchanged-output quarter-point task after complete high-node certification and legal recentering; matched 28-portfolio comparisons')
        s=s.replace('同输出一点预算突破；完整28组合对照','同输出四分之一点任务、高频完整认证和合法中心平移；相同半径28组合对照')
        s=s.replace('Section 11.4','Section 11.3').replace('第11.4节','第11.3节')
        s=s.replace('### 11.3.','### 11.2.').replace('### 11.4.','### 11.3.').replace('### 11.5.','### 11.4.')
        p=s.index('\n\n',s.index('## 11.'))
        s=s[:p]+('\n\n### 11.1. 原价差与基线证书' if zh else '\n\n### 11.1. Original spread and baseline certificates')+s[p:]
        p=s.index('### 11.4.')
        s=s[:p]+portfolio_table(zh)+s[p:]
        # Correct migrated classical locations without altering their proofs.
        s=s.replace("main text's primal–dual witness",'primal-dual witness in Appendix D.2.4')
        s=s.replace('directly in the main text','directly in Appendix D.3.5')
        s=s.replace('主文的原始—对偶见证','附录D.2.4的原始—对偶见证').replace('主文的原始-对偶见证','附录D.2.4的原始-对偶见证')
        s=s.replace('直接在主文中','直接在附录D.3.5中')
        s=s.replace('正文的 primal–dual witness','附录D.2.4的 primal-dual witness')
        s=s.replace('可在正文中直接复核','可在附录D.3.5中直接复核')
        # The stronger assumption is replaced only in the new finite-history theorem.
        a=s.index('### 9.5.');b=s.index('## 10.');block=s[a:b]
        block=block.replace(r'\(\xi\in AC[0,T]\), \(\xi(0)=V_0\ge0\), and \(\xi\prime\ge0\)',r'\(\xi\in AC[0,T]\), \(\xi(0)=V_0\ge0\), and \(q_\alpha=(I^{1-\alpha}\xi)\prime\ge0\) almost everywhere')
        block=block.replace(r"\(\xi\in AC[0,T]\), \(\xi(0)=V_0\ge0\), and \(\xi'\ge0\)",r"\(\xi\in AC[0,T]\), \(\xi(0)=V_0\ge0\), and \(q_\alpha=(I^{1-\alpha}\xi)'\ge0\) almost everywhere")
        block=block.replace(r"\(\xi\in AC[0,T]\)、\(\xi(0)=V_0\ge0\)、\(\xi'\ge0\)",r"\(\xi\in AC[0,T]\)、\(\xi(0)=V_0\ge0\)，且\(q_\alpha=(I^{1-\alpha}\xi)'\ge0\)几乎处处")
        s=s[:a]+block+s[b:]
        theory=HERE/f'theory-section-{lang}.md'
        assert theory.exists(), 'Theory review must be completed before authoring final manuscript.'
        p=s.index('## 10.');s=s[:p]+theory.read_text(encoding='utf-8')+'\n\n'+s[p:]
        s+='\n\n[ElEuchRosenbaum2017v1] Omar El Euch and Mathieu Rosenbaum. Perfect hedging in rough Heston models. arXiv:1703.05049v1, 15 March 2017. https://arxiv.org/abs/1703.05049v1. Fractional forward-curve relations and their admissibility restrictions are prior results; the present decreasing curve is an analytical propagation example.\n'
        attribution=('有限期限传播复用全局连续残差，将首选候选完整上界从1.397612095收紧至0.378598956点，约收紧72.91%。逐时包络随后降至0.367258782点，增加约0.011340174点、相对约3.00%的改善。两项成本分别报告。共同误差结构的贡献用相同新节点半径的边际/联合比较辨识：α=.52在0.5点预算为13/28与28/28；α=.60在0.25点为1/28与10/28；α=.90在0.25点为13/28与20/28。一点预算下α=.52两种新方法均28/28，旧到新的整体改善不能全部归因于共同几何。\n\n' if zh else
            'Finite-horizon propagation reuses the global continuous residuals and reduces the selected complete bound from 1.397612095 to 0.378598956 points, approximately 72.91%. The time-local envelope then reduces it to 0.367258782 points, an additional approximately 0.011340174 points or 3.00%; their costs are reported separately. The contribution of shared geometry is isolated with matched new node radii: at alpha=.52 and a half-point budget the signed marginal/joint counts are 13/28 and 28/28; at alpha=.60 and a quarter-point budget, 1/28 and 10/28; and at alpha=.90 and a quarter-point budget, 13/28 and 20/28. At one point both new methods achieve 28/28 for alpha=.52, so the entire old-to-new improvement cannot be attributed to shared geometry.\n\n')
        p=s.index('### 11.4.');s=s[:p]+attribution+s[p:]
        for stem in ['omission','transfer']:
            section=HERE/f'{stem}-section-{lang}.md'
            if section.exists():
                p=s.index('## 12.');s=s[:p]+section.read_text(encoding='utf-8')+'\n\n'+s[p:]
        costs=HERE/'cold-acceptance.json'
        if costs.exists():
            r=json.loads(costs.read_text(encoding='utf-8'))
            assert r['status']=='PASS_COLD_FULL_ACCEPTANCE'
            memory=r['peak_job_committed_memory_bytes']
            ms=(f'{memory/2**20:.2f} MiB' if memory is not None else ('不可用' if zh else 'unavailable'))
            ct=(f"本轮冷启动验收采用新解释器、新解压副本和完整--full序列，{r['commands_passed']}项全部退出0。父进程总耗时{r['end_to_end_parent_wall_seconds']:.3f}秒；ZIP验证和解压另计{r['zip_crc_hash_and_extraction_seconds_separate']:.3f}秒，下载未计。Windows job记录整个验收进程树的峰值提交内存{ms}，此值不是峰值RSS。本机Intel Core Ultra7 155U，12核14逻辑处理器，Windows11 10.0.26200，可见物理内存约15.44GiB，Python3.12.14、NumPy2.3.5，向外算术100bit。这次运行OMP/MKL/OpenBLAS线程上限显式设1；旧历史耗时的线程和峰内存没有记录，不追溯填补。其他研究进程可能同时运行，因此这些观测不构成隔离加速测试。父进程计时包含输入哈希、工作副本、解释器启动、全部检查和输出验证；可选完整连续残差重生成另计。完整记录见cold-acceptance.json。\n\n" if zh else
                f"This revision executes a cold acceptance with a new interpreter, a fresh extraction, and the complete --full sequence: all {r['commands_passed']} commands exit zero. Parent-process elapsed time is {r['end_to_end_parent_wall_seconds']:.3f} seconds; ZIP validation and extraction take a separate {r['zip_crc_hash_and_extraction_seconds_separate']:.3f} seconds, and download is excluded. Windows job accounting records a process-tree peak of {ms} committed memory, not peak RSS. The machine has an Intel Core Ultra7 155U, 12 cores and 14 logical processors, Windows11 10.0.26200, approximately 15.44GiB visible physical memory, Python3.12.14, NumPy2.3.5, and 100-bit outward arithmetic. This run explicitly limits OMP/MKL/OpenBLAS threads to one; historical threads and peak memory were not recorded and are not filled retrospectively. Other research processes may run concurrently, so these observations are not an isolated acceleration benchmark. Parent timing includes input hashing, work-copy creation, interpreter startup, all checks and output validation; optional complete residual regeneration is separate. The complete record is cold-acceptance.json.\n\n")
            p=s.index('## 12.');s=s[:p]+ct+s[p:]
        download=(f'固定证据的公开入口为[版本页面]({RELEASE})，可直接下载[原有限历史ZIP]({BASEZIP})及[本轮扩展ZIP]({NEWZIP})。这里指上传的具名资产；GitHub自动生成的Source code归档不等同于完整证据包。原有限历史ZIP的SHA256为edc25d2ad86c1526f404ec1a46a02a283f0726602f259beaa97eb1219d22d299。扩展包逐文件SHA256和准确运行命令见FRONTIER-MANIFEST.json与README.md。本地重跑和多agent读回是作者侧验收，不能冒称外部审稿人已下载或独立通过。\n\n' if zh else
            f'The fixed supplement is available from the [versioned release]({RELEASE}), with direct downloads of the [original finite-history ZIP]({BASEZIP}) and the [current extension ZIP]({NEWZIP}). These are named uploaded assets; GitHub\'s autogenerated Source code archive is not the complete evidence supplement. The original ZIP SHA256 is edc25d2ad86c1526f404ec1a46a02a283f0726602f259beaa97eb1219d22d299. FRONTIER-MANIFEST.json and README.md give the extension file identities and exact commands. Local reruns and agent readbacks are author-side acceptance; they do not establish that an external referee has downloaded or independently accepted the supplement.\n\n')
        p=s.index('\n\n',s.index('## 12.'))+2;s=s[:p]+download+s[p:]
        current_command=('本轮完整扩展的单命令为 `python heston-frontier-20261007/run_frontier.py --full`。它先核验FRONTIER-MANIFEST、创建新工作副本，再执行旧完整验收、高频包络检查、完整中心和预算重算、高频独立读回、三候选新期限及全参考/逐时补充独立读回。可选 `--regenerate-full`重新生成新增512高频连续残差。保存包络核验与全连续导数重生成的范围分列。新增(FQ1)–(FQ6)是解析证明；(FQ7)–(FQ8)对应省略节点新中心与完整账本。\n\n' if zh else
            'For the current extension, the single command is `python heston-frontier-20261007/run_frontier.py --full`. It verifies FRONTIER-MANIFEST, creates a new work copy, and runs the earlier complete acceptance, high-node envelope checks, full centre and budget reconstruction, independent high-node readback, and complete three-candidate and full-reference/time-local maturity readers. Optional `--regenerate-full` regenerates the 512 newly certified high-frequency residuals. Saved-envelope verification and complete continuous-derivative regeneration are reported separately. Equations (FQ1)--(FQ6) are analytical results; (FQ7)--(FQ8) connect the changed reference to the full omitted-node ledger.\n\n')
        p=s.index('\n\n',s.index('## 12.'))+2;s=s[:p]+current_command+s[p:]
        s=s.replace('The fixed downloadable supplement is','The preceding fixed finite-history supplement is')
        conclusion=(
            '本稿的主推进是残差经完整有限历史进入价格指数和实际输出证书。原一点任务已通过；主要突破来自有限期限传播，逐时包络提供较小附加改善，相同半径的紧预算对照体现共同误差结构的价值。新增解析条件和期限任务仅在各自证明、合同和完整账本范围内成立。高频省略节点的新认证按实际输出重新计算中心，不能沿用旧冻结预算的下界作为所有认证方法的下界。完整证据已经提供准确下载入口、逐文件身份和可执行验收；后续外部独立运行仍是另一项证据。\n\n' if zh else
            'The principal advance connects complete finite-history residual propagation to the pricing exponent and a certificate at the actual output. The original one-point task is certified. Most of the breakthrough comes from finite-horizon propagation; time-local envelopes add a smaller improvement, while tighter-budget matched comparisons identify the benefit of shared error structure. The analytic extension and new maturity task retain their respective proof, contract, and full-ledger scope. New certification of omitted frequencies recomputes the centre at the actual output; the old fixed-budget floor is not a lower bound for every certification method. The supplement provides precise downloads, file identities, and executable acceptance. Subsequent external independent execution is a separate evidence milestone.\n\n')
        conclusion+=(
            '本轮原价差的最佳完整上界为0.115215934点，并取得四分之一点证书。改善来自对新增高频的完整认证和合法中心平移；边际方法在同一新参考下也通过该预算，故这一突破不能全部归因于共同几何。共同结构进一步降低相同半径的方向上界，其作用由匹配比较单独衡量。\n\n' if zh else
            'The strongest complete bound for the original spread is now 0.115215934 points, certifying the quarter-point task. This improvement comes from complete high-frequency certification and legal recentering. The matched marginal method also certifies that budget, so the breakthrough is not assigned entirely to shared geometry; its further directional reduction is measured separately at matched radii.\n\n')
        conclusion+=(
            '新期限T=1/4的单次另列逐时探索取得联合0.233318843点、有符号边际0.252393939点；在同一快速输出、新参考中心、半径和全部余项下，只有联合方向界通过四分之一点。此前全局阶段未通过的结果一并保留，因此该实例检验了方法迁移，也给出共同几何改变任务判定的实质证据。\n\n' if zh else
            'For the new maturity T=1/4, one separately recorded time-local exploration gives a complete joint bound of 0.233318843 points against 0.252393939 from matched signed marginals. Only the joint direction certifies the quarter-point budget at the same output, new reference centre, radii and complete remainder. The preceding global-stage failures remain visible. This supplies both a second-maturity instantiation and a task decision changed by shared geometry.\n\n')
        p=s.index('## Appendix A.' if not zh else '## 附录 A.');s=s[:p]+conclusion+s[p:]
        # No unrenderable Unicode minus in CJK prose; formulas retain LaTeX minus.
        s=s.replace('\u2212','-')
        target=HERE/'manuscript'/f'merged-heston-{lang}.md';target.write_text(s,encoding='utf-8')
        alias='rough-heston-source.md' if not zh else 'report-source.md'
        (HERE/'manuscript'/alias).write_text(s,encoding='utf-8')
        receipts[lang]={'baseline_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'new_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'bytes':target.stat().st_size}
    (HERE/'manuscript-revision.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipts,indent=2))

if __name__=='__main__':main()
