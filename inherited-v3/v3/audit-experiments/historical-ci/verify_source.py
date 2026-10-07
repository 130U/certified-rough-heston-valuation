from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
data=json.loads((root/'SOURCE-MANIFEST.json').read_text(encoding='utf-8'))
for row in data['source_files']:
    p=root/row['path']
    assert p.resolve().is_relative_to(root.resolve()) and p.is_file()
    assert p.stat().st_size==row['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],row['path']
receipt=json.loads((root/'FRESH-ACCEPTANCE.json').read_text(encoding='utf-8'))
assert receipt['status']=='PASS_FRESH_COMPLETE_SCIENTIFIC_ACCEPTANCE'
assert receipt['tested_scientific_manifest_sha256']==hashlib.sha256((root/'SCIENTIFIC-MANIFEST.json').read_bytes()).hexdigest()
science=json.loads((root/'SCIENTIFIC-MANIFEST.json').read_text(encoding='utf-8'))['files']
identities={r['path']:r for r in data['source_files']+data['large_data_supplied_in_named_release_archive']}
for row in science:assert identities[row['path']]==row,row['path']
print('PASS source identity and retained fresh acceptance receipt; large bank acceptance is the release command.')
