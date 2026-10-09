import json, concurrent.futures, sys
from collections import Counter
from prepare import ROOT, process
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
data=json.loads((ROOT/'prepared-inventory.json').read_text(encoding='utf-8'))
targets=[r for r in data['records'] if r['status']=='blocked-main-pdf-identity']
results={}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    tasks={pool.submit(process,r):r['key'] for r in targets}
    for n,f in enumerate(concurrent.futures.as_completed(tasks),1):
        results[tasks[f]]=f.result()
        if n%50==0:print(f'Recheck {n}/{len(targets)}: {dict(Counter(r["status"] for r in results.values()))}',flush=True)
data['records']=[results.get(r['key'],r) for r in data['records']]
data['summary']['prepared_counts']=dict(Counter(r['status'] for r in data['records']))
(ROOT/'prepared-inventory.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(data['summary'],ensure_ascii=False,indent=2),flush=True)
