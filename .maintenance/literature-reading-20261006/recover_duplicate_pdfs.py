"""Rescue unavailable canonical PDFs from existing duplicate Zotero attachments."""
import json,sys
from inventory import ROOT
from prepare import process

sys.stdout.reconfigure(encoding='utf-8')
def main():
    path=ROOT/'prepared-inventory.json';data=json.loads(path.read_text(encoding='utf-8'))
    records={r['key']:r for r in data['records']};aliases={}
    for r in data['records']:
        if r['status']=='duplicate-record':aliases.setdefault(r['canonical_key'],[]).extend(r.get('pdf_attachments',[]))
    results=[]
    for key,attachments in aliases.items():
        canonical=records.get(key)
        if not canonical or canonical['status'] not in {'blocked-pdf-unavailable','blocked-main-pdf-identity','blocked-text-extraction'}:continue
        seen={a['key'] for a in canonical.get('pdf_attachments',[])}
        extra=[a for a in attachments if a['key'] not in seen]
        if not extra:continue
        candidate=dict(canonical,pdf_attachments=canonical.get('pdf_attachments',[])+extra)
        recovered=process(candidate)
        result={'key':key,'prior_status':canonical['status'],'new_status':recovered['status'],'extra_attachments':len(extra)}
        if recovered['status']=='ready':
            latest=json.loads(path.read_text(encoding='utf-8'));latest['records']=[recovered if r['key']==key else r for r in latest['records']]
            temporary=path.with_suffix('.json.tmp');temporary.write_text(json.dumps(latest,ensure_ascii=False,indent=2),encoding='utf-8');temporary.replace(path)
            result['main_attachment']=recovered['main_attachment_key']
        results.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
    (ROOT/'duplicate-PDF-rescue.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'checked_canonical_records':len(results),'rescued':sum(r['new_status']=='ready' for r in results)},ensure_ascii=False),flush=True)

if __name__=='__main__':main()
