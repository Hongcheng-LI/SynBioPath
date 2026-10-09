import json,datetime
from collections import Counter
import worker as w
excluded={
 '2E5UEWNP':'用户明确排除本篇；庚糖经ALPK1触发免疫识别为核心问题',
 'C7DANW9B':'多糖糖缀合疫苗与免疫保护为核心；已有原笔记保留',
 'ZHD6M25V':'ADP庚糖免疫识别前体的合成酶分布研究，按相关方向排除',
 'CX9ZXZYB':'以免疫识别PAMP庚糖为对象的合成酶表征，按相关方向排除',
 '45CM6P5E':'糖基化疫苗佐剂QS21及其免疫刺激为核心，按相关方向排除'}
policy={'date':'2026-10-08','user_instruction':'所有文献库中跟糖免疫相关的文献都不需要读；继续其他文献','excluded':[], 'screening':'Read titles and Zotero abstracts across personal library; candidate lexical matches reviewed for actual research focus. Future papers rechecked before reading.','retained_examples':{'XFLD4TVL':'septacidin糖表异构酶，实际目标天然产物生物合成而非糖免疫','YCFFKWFD':'septacidin抗生素生物合成而非糖免疫','RAUUZENZ':'核苷酸糖生产平台，免疫原性仅背景','3GN4WT7S':'天然产物糖基化代谢综述，免疫原性仅背景','AK9B4YFU':'二十五碳萜结构/NO抑制，LPS为细胞模型刺激剂，非糖免疫研究','TBC2IX6G':'MelLec识别萘并吡喃酮/黑色素，实际配体非糖，保留化学工具研究'}}
for name in ['prepared-inventory.json','inventory.json']:
 p=w.ROOT/name;data=json.loads(p.read_text(encoding='utf-8'))
 for r in data['records']:
  if r['key'] not in excluded:continue
  old=r['status'];r['scope_excluded']=True;r['scope_exclusion_reason']=excluded[r['key']]
  if old not in ['already-interpreted','excluded-thesis','excluded-chinese','excluded-non-paper','excluded-chinese-pdf']:
   r.setdefault('status_before_scope_exclusion',old);r['status']='excluded-user-sugar-immunity'
  if name=='prepared-inventory.json':
   policy['excluded'].append({'key':r['key'],'title':r['title'],'status':r['status'],'previous_status':old,'reason':excluded[r['key']]})
   prep=w.ROOT/'sources'/r['key']/'prepared.json'
   if prep.exists():
    obj=json.loads(prep.read_text(encoding='utf-8'));obj.update(scope_excluded=True,scope_exclusion_reason=excluded[r['key']],status=r['status']);w.write_json(prep,obj)
 data['summary']['scope']='entire personal library; exclude Chinese papers, theses and sugar-immunity literature; local readable PDFs first'
 data['summary']['user_scope_exclusions']=len(excluded)
 data['summary']['prepared_counts' if name=='prepared-inventory.json' else 'counts']=dict(Counter(r['status'] for r in data['records']))
 w.write_json(p,data)
w.write_json(w.ROOT/'user-scope-exclusions.json',policy)
d=w.ROOT/'sources'/'2E5UEWNP'
if (d/'publication.json').exists():raise RuntimeError('Unexpected excluded paper already published')
w.write_json(d/'scope-excluded.json',{'key':'2E5UEWNP','status':'excluded-user-sugar-immunity','reason':excluded['2E5UEWNP'],'draft_only':True,'images_uploaded':False,'formal_note_created':False})
w.record_result({'key':'2E5UEWNP','title':policy['excluded'][0]['title'],'time':datetime.datetime.now().isoformat(),'status':'excluded-user-sugar-immunity','reason':excluded['2E5UEWNP'],'note_created':False,'images_uploaded':0})
print(json.dumps(policy,ensure_ascii=False))
