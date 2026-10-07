"""Map source identities explicitly and compare every retained exact derivation."""
from pathlib import Path
import hashlib,json,copy
from audit_layout import HERE,resolve
def read(p):return json.loads(p.read_text(encoding='utf-8'))
FILES=['quarter-exact-ledger.json','nearby-pair-resolution.json','portfolio-budget-counts.json','frozen-output-centre-account.json','configuration-registry.json']
def normalize(name):
 prefix='research/heston-major-revision-20261007/'
 if name.startswith(prefix+'evidence-v2/baseline/'):return 'baseline/'+name[len(prefix+'evidence-v2/baseline/'):]
 if name.startswith(prefix+'experiments/'):return 'new-research/experiments/'+name[len(prefix+'experiments/'):]
 raise ValueError('Unknown original evidence source prefix.')
def main():
 initial=read(HERE/'source-identities-before-portable.json');current=read(HERE/'source-identities.json');original={normalize(k):v for k,v in initial['sources'].items()};assert original.keys()==current['sources'].keys()
 records=[]
 for name,r in current['sources'].items():
  p=resolve(name);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'];old=original[name];records.append({'source':name,'original_sha256':old['sha256'],'current_sha256':r['sha256'],'same_bytes':old==r,'original_evidence_bytes':old['evidence_bytes'],'current_evidence_bytes':r['evidence_bytes']})
 retained=HERE/'retained-scientific-derivations.json'
 values={name:read(HERE/name) for name in FILES}
 if not retained.exists():
  # This file is frozen before any rebasing to the final privacy-clean snapshot.
  retained.write_text(json.dumps({'status':'RETAINED_EXACT_PRE_REBASE_DERIVATIONS','objects':values},indent=2)+'\n',encoding='utf-8')
 originals=read(retained)['objects'];projection=copy.deepcopy(values);retained_projection=copy.deepcopy(originals);display_changes=[]
 for before,after in zip(retained_projection['configuration-registry.json']['configurations'],projection['configuration-registry.json']['configurations']):
  old_display=before.pop('reported_joint_bound_points');new_display=after.pop('reported_joint_bound_points')
  if old_display!=new_display:display_changes.append({'configuration_id':after['configuration_id'],'retained_display_label':old_display,'corrected_display_label':new_display,'boundary':'Display label only; exact endpoint calculations are independently reconstructed and checked.'})
 assert projection==retained_projection,'A scientific audit derivation changed across snapshots.'
 changes=[r for r in records if not r['same_bytes']]
 receipt={'status':'PASS_CANONICAL_SOURCE_IDENTITY_AND_RETAINED_EXACT_DERIVATIONS','records':records,'source_objects':len(records),'changed_source_identities':len(changes),'display_label_corrections':display_changes,'exact_derived_objects_checked':FILES,'retained_derivation_sha256':hashlib.sha256(retained.read_bytes()).hexdigest(),'boundary':'A changed SHA is disclosed, never ignored. Equality of allretained exact secondary derivations is checked. Approximate configuration display labels are excluded explicitly and any corrections listed; noexact numeric endpoint is excluded. Equivalence of changes to a shared mathematical generator requires its separate privacy/source-equivalence audit; this bridge does not claim to prove arbitrary code equivalence.'}
 (HERE/'snapshot-identity-bridge.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print('PASS canonical identity bridge',len(changes),'changed source identities; fiveexact derived objects invariant')
if __name__=='__main__':main()
