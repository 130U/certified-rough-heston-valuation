"""Software versions only; no system, device, path, timing or telemetry."""
from pathlib import Path
from importlib.metadata import version,PackageNotFoundError
import json,sys
HERE=Path(__file__).resolve().parent
record={'Python':'.'.join(str(getattr(sys.version_info,k)) for k in ['major','minor','micro'])}
for name in ['numpy','scipy','mpmath']:
    try:record[name]=version(name)
    except PackageNotFoundError:record[name]='NOT_INSTALLED'
record['required_by_experiments']=['Python','numpy']
record['not_required_by_new_experiments']=['scipy','mpmath']
record['arithmetic']='exact Fraction; 100 bit outward dyadic strict primitives; outward binary64 residual intervals'
(HERE/'software-identity.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
