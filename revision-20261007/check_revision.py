"""Check source identity, exact evidence scopes, and the review package."""
from pathlib import Path
import hashlib,importlib.util,json,re
ROOT=Path(__file__).resolve().parent
from audit_paths import release_root
BASE=release_root(ROOT)
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def main():
    manifest=load('MANIFEST.json')
    for row in manifest['artifacts']:
        p=ROOT/row['path'];assert p.is_file(),row['path']
        assert p.stat().st_size==row['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],row['path']
    source=(ROOT/'manuscript/merged-heston-source.md').read_text(encoding='utf-8')
    public=(ROOT/'manuscript/merged-heston.md').read_text(encoding='utf-8')
    tags=re.findall(r'\\tag\{([^}]+)\}',source)
    assert len(tags)==len(set(tags))==123
    assert re.findall(r'\\tag\{([^}]+)\}',public)==tags
    spec=importlib.util.spec_from_file_location('converter',BASE/'scripts/build_github_manuscripts.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    expected,records=module.build(source);assert expected==public
    assert len(records)==829
    for url in re.findall(r'\]\(([^)]+)\)',source):
        if not url.startswith(('http:','https:','mailto:','#')):assert (ROOT/'manuscript'/url).resolve().exists(),url
    assert load('full-structure-verification.json')['signs_recomputed']==211241
    assert load('full-structure-verification.json')['all_regenerated_records_identical'] is True
    assert load('verification.json')['status'].startswith('PASS_')
    assert load('near-tie-diagnostic.json')['status'].startswith('PASS_')
    build=load('qa/rough-heston-pdf-build.json')
    assert build['source_sha256']==hashlib.sha256((ROOT/'manuscript/merged-heston-source.md').read_bytes()).hexdigest()
    assert build['math_source_occurrences']==829 and build['vector_formulas'] is True
    pdf_path=Path(build['pdf'])
    if len(pdf_path.parts)==1:pdf_path=Path('paper')/pdf_path
    assert hashlib.sha256((ROOT/pdf_path).read_bytes()).hexdigest()==build['pdf_sha256']
    print(json.dumps({'status':'PASS_MERGED_REVISION','files':len(manifest['artifacts']),
        'formulas':len(records),'equation_tags':len(tags),'scope':'Bytes, canonical math presentation, source/PDF identities, and exact evidence completion; proofs remain in the manuscript.'}))
if __name__=='__main__':main()
