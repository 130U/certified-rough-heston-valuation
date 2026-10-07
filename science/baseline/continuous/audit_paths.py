"""Locate unchanged upstream evidence for local and published audit layouts."""
from pathlib import Path
def release_root(script_directory):
    """Local sibling, repo/code/merged, or repo/revision-YYYYMMDD/code.

    This only discovers paths; it does not alter any source or frozen input.
    """
    here=Path(script_directory).resolve()
    candidates=[here.parent/'reference',here.parent.parent,here.parent,here]
    for candidate in candidates:
        if (candidate/'code'/'frozen'/'calibration-contract-finite-T05.json').is_file() and (candidate/'code'/'src'/'interval-pade-certificate.py').is_file():
            return candidate
    raise FileNotFoundError('Cannot locate upstream release code/frozen and code/src from '+str(here))

def evidence_directory(script_directory):
    """Published revision scripts write beside code/, under evidence/."""
    here=Path(script_directory).resolve()
    if here.name=='code' and here.parent.name.startswith('revision-'):
        out=here.parent/'evidence';out.mkdir(parents=True,exist_ok=True);return out
    return here


def paper_source(script_directory):
    """Resolve the single authoritative English proof source."""
    for parent in [Path(script_directory).resolve(),*Path(script_directory).resolve().parents]:
        candidate=parent/"manuscript"/"merged-heston-en.md"
        if candidate.is_file():return candidate
    raise FileNotFoundError("The current English manuscript must accompany the scientific extraction.")
