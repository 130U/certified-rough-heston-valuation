# Evidence and reproduction

The [`paper` release](https://github.com/130U/certified-rough-heston-valuation/releases/tag/paper) identifies the online article and the public files listed below. `SOURCE-MANIFEST.json` inventories the reading and verification files; `SCIENTIFIC-MANIFEST.json` binds the scientific inputs, source and retained numerical banks.

| Calculation | Inputs, results and verification procedures |
| --- | --- |
| Finite-history and continuous residual certificates | [Source](science/baseline/finite-history), [commands](COMMANDS.md#p1), [complete proof](ARTICLE.md#appendix-c-complete-propagation-proofs-and-analytic-variants) |
| Quarter-year full-reference price accounts | [Source](science/baseline/frontier), [reader commands](COMMANDS.md#q2), [experiment accounts](ARTICLE.md#appendix-e-complete-experiments-and-verification-duties) |
| Nearby candidates and actual-output controls | [Source](science/experiments), [candidate commands](COMMANDS.md#n1), [output commands](COMMANDS.md#c1), [public ledgers](audit-experiments) |
| Dissipative-kernel comparison | [Source](science/analysis/kernel), [generation and reader commands](COMMANDS.md#k1), [matched results](ARTICLE.md#7-matched-decisions-and-scientific-controls) |
| Secondary ledger and extension checks | [Audit source](science/analysis/audit), [ledger commands](COMMANDS.md#a1), [extension commands](COMMANDS.md#g1) |
| Public source identities | [Source manifest](SOURCE-MANIFEST.json), [checker](verify_source.py), [command](COMMANDS.md#source-identities) |

The complete numerical banks are retained in the author's local evidence archive. The public checkout contains the source, smaller ledgers and verification procedures, but cannot perform the full saved-bank reconstruction without those banks.

`SCIENTIFIC-CHECK.json` records the author's saved-bank acceptance checks. With the complete banks, `reproduce.py` reads the saved evidence and reconstructs downstream prices, objectives and decisions. `--full` also recomputes the original complete structural-sign cover; it does not regenerate every continuous residual derivative bound. [Appendix E](ARTICLE.md#appendix-e-complete-experiments-and-verification-duties) identifies the shared arithmetic and generator dependencies.

File-identity checks, saved-bank reconstruction and fresh continuous generation have different scopes. The reported checks are author-side records; external independent reproduction is a separate step.
