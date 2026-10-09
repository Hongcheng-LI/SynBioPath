import json
from pathlib import Path
import worker as w
for name in ['codex-source-review.json','publication.json']:
 p=w.ROOT/'sources'/'MFLGZ2V3'/name
 obj=json.loads(p.read_text(encoding='utf-8'))
 container=obj if name=='codex-source-review.json' else obj['source_review']
 for claim in container['verified_claims']:
  claim['evidence']=claim['evidence'].replace('mathchecked549? actual547.4and946.7','mathchecked547.4and946.7')
 w.write_json(p,obj)
p=Path(__file__).parent/'audit-5l-ld-codex.py';source=p.read_text(encoding='utf-8').replace("['5LCZ6Y94','LDMEJZHN']","['MFLGZ2V3','QWTYVVCT','UZJ6VLEJ']").replace("if key=='5LCZ6Y94':","if key=='unused':").replace('codex-two-paper-integrity-5l-ld-20261008.json','codex-three-paper-integrity-mf-qw-uz-20261008.json')
exec(compile(source,str(p),'exec'))
