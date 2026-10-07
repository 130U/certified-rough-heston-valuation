"""Build a self-contained fixed extension without modifying the original ZIP."""
from pathlib import Path
import hashlib,json,shutil,zipfile
HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'heston-nine-point-20261007'/'Theodore-Ouyang-Heston-Finite-History-Evidence-20261007.zip'
STAGE=HERE/'bundle-v2-fixed'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    assert sha(BASE)=='edc25d2ad86c1526f404ec1a46a02a283f0726602f259beaa97eb1219d22d299'
    STAGE.mkdir(exist_ok=True)
    with zipfile.ZipFile(BASE) as z:
        assert z.testzip() is None
        for n in z.namelist():assert (STAGE/n).resolve().is_relative_to(STAGE.resolve())
        z.extractall(STAGE)
    # The transfer reader authenticates this original source as provenance.
    # It was not a member of the earlier finite-history-only supplement.
    original=HERE.parent/'english-heston-release/manuscript/rough-heston.md'
    assert sha(original)=='9ea6200ae8977c234cadc5eb849869df5e476a8d33260853dc564e187b9f8885'
    target=STAGE/'english-heston-release/manuscript/rough-heston.md'
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(original,target)
    selected=[]
    for f in sorted(HERE.rglob('*')):
        if not f.is_file():continue
        rel=f.relative_to(HERE)
        if any(x in ['cold-acceptance-extracted','download-readback','verification-work','rendered','.cache','__pycache__'] or x.startswith(('frontier-verification-work','bundle-')) for x in rel.parts):continue
        if f.suffix not in ['.py','.md','.json','.npz','.pdf','.txt','.cjs','.log'] and f.name!='.gitattributes':continue
        if f.name in ['FRONTIER-MANIFEST.json','frontier-bundle-receipt.json','frontier-execution-receipt.json','public-frontier-download.json','publication-frontier.json']:continue
        target=STAGE/'heston-frontier-20261007'/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(f,target)
        selected.append('heston-frontier-20261007/'+rel.as_posix())
    # The baseline README is retained byte-for-byte: its original manifest remains valid.
    shutil.copyfile(HERE/'README.md',STAGE/'README-FRONTIER.md')
    rows=[]
    for f in sorted(STAGE.rglob('*')):
        if not f.is_file() or f.name=='FRONTIER-MANIFEST.json':continue
        rel=f.relative_to(STAGE).as_posix()
        if any(x.startswith('frontier-verification-work') or x=='verification-work' for x in f.relative_to(STAGE).parts):continue
        rows.append({'path':rel,'bytes':f.stat().st_size,'sha256':sha(f)})
    # Fail rather than silently inheriting an obsolete file from a prior build.
    actual_new={r['path'] for r in rows if r['path'].startswith('heston-frontier-20261007/')}
    assert actual_new==set(selected),actual_new.symmetric_difference(selected)
    manifest=STAGE/'FRONTIER-MANIFEST.json'
    manifest.write_text(json.dumps({'version':'20261007-frontier-packaging-v2','baseline_zip_sha256':sha(BASE),'files':rows},indent=2)+'\n',encoding='utf-8')
    path=HERE/'Theodore-Ouyang-Heston-Frontier-Evidence-20261007-v2.zip'
    with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for rel in ['FRONTIER-MANIFEST.json']+[r['path'] for r in rows]:z.write(STAGE/rel,rel)
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        assert set(z.namelist())=={'FRONTIER-MANIFEST.json'}|{r['path'] for r in rows}
        for r in rows:assert hashlib.sha256(z.read(r['path'])).hexdigest()==r['sha256'],r['path']
    result={'status':'PASS_FIXED_FRONTIER_ZIP_ALL_BLOB_READBACK','archive':path.name,'bytes':path.stat().st_size,'sha256':sha(path),'files':len(rows),'manifest_sha256':sha(manifest)}
    (HERE/'frontier-bundle-receipt.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
