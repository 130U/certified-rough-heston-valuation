# Explicit delivery and source preparation

These helpers do not publish, invoke Git, or modify any existing scientific or manuscript input. Each invocation requires a new output directory. They retain only relative source names, bytes and hashes; ZIP member dates are fixed to the format minimum. No execution measurements or personal host metadata are collected.

The root editor must review and supply the allowlist. Example schema (paths are relative to the V3 research root):

```json
{
  "version": "v3.0.0-research-20261007",
  "scientific_manifest": "evidence-v3/SCIENTIFIC-MANIFEST.json",
  "expected_release_arrays": 27,
  "fresh_receipt": {
    "source": "evidence-v3/FRESH-ACCEPTANCE.json",
    "path": "FRESH-ACCEPTANCE.json"
  },
  "pdf_assets": [
    {
      "source": "paper/Theodore-Ouyang-Merged-Heston-EN.pdf",
      "name": "Theodore-Ouyang-Merged-Heston-EN.pdf"
    },
    {
      "source": "paper/Theodore-Ouyang-Merged-Heston-ZH.pdf",
      "name": "Theodore-Ouyang-Merged-Heston-ZH.pdf"
    }
  ],
  "extra_files": [
    {"source": "manuscript/merged-heston-en.md", "path": "manuscript/merged-heston-en.md"},
    {"source": "manuscript/merged-heston-zh.md", "path": "manuscript/merged-heston-zh.md"},
    {"source": "qa/theory-final-review.md", "path": "qa/theory-final-review.md"}
  ]
}
```

This is a schema example, not the completed release allowlist. The editor must explicitly add final PDF QA, privacy and any additional delivery documents or receipts. The fresh receipt is listed once via `fresh_receipt`, and the final two PDFs once via `pdf_assets`; do not repeat them in `extra_files`. A scientific manifest containing old PDFs with these same basenames must be corrected before fresh acceptance and sealing, rather than silently deleting or replacing a bound object during sealing.

Run from the V3 research directory after review:

```text
python delivery-tools/seal_delivery.py --root . --allowlist delivery-allowlist.json --output delivery-v3
python delivery-tools/prepare_publication.py --root . --delivery delivery-v3/DELIVERY-MANIFEST.json --output publication-v3
python publication-v3/verify_source.py
```

The sealer checks every scientific object against its fixed manifest, checks the retained complete fresh receipt's tested-science, driver and step source identities, then assembles only the explicit members. It rejects traversal, case collisions, verification trees, caches and temporary names. It checks the ZIP CRC, exact member order/set, every size and SHA256, fixed dates and unchanged input identities after sealing. The two standalone PDFs have exactly the same bytes as their respective ZIP members. `SHA256SUMS.txt` binds the two PDFs and the named evidence ZIP. The delivery manifest is also available beside the four assets and as the final ZIP member; its self-identity is not recursively listed.

Source preparation reads that manifest, copies all listed non-NPZ objects from their identified sources, retains all 27 array identities as release-only rows, and adds a generated source verifier and a CI workflow. It also binds the delivery manifest bytes and verifies complete scientific and delivery coverage. The copied source tree remains unchanged by an identity check. CI checks SHA256/size identities and the retained fresh acceptance binding; it does not rerun scientific arithmetic, continuous derivative generation or the large arrays. The named release archive and its reproduction command serve that separate purpose.

If preparation fails after creating its new output directory, preserve that failed stage for diagnosis and use a different empty output name for a new attempt. These helpers never delete an existing stage.
