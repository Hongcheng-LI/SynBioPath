import json, re, time, sys
from pathlib import Path
import requests

CFG = Path(r'C:\Users\lhc\.agents\skills\paper-interpret\config.json')

def call(content, system='', max_tokens=16000):
    cfg = json.loads(CFG.read_text(encoding='utf-8'))
    payload = {'model':cfg['llm_model'], 'temperature':0.2, 'max_tokens':max_tokens,'stream':True,'stream_options':{'include_usage':True},
               'messages':[{'role':'system','content':system},{'role':'user','content':content}]}
    session = requests.Session()
    # This process-local route bypasses an unstable proxy; no system settings change.
    session.trust_env = False
    response = session.post(cfg['llm_endpoint'], json=payload,stream=True,
                            headers={'Authorization':'Bearer '+cfg['llm_api_key']}, timeout=(30,600))
    if response.status_code != 200:
        raise RuntimeError('Configured LLM HTTP '+str(response.status_code))
    if 'text/event-stream' in response.headers.get('Content-Type',''):
        parts=[];usage={};finish=None
        for line in response.iter_lines():
            if not line.startswith(b'data:'):continue
            frame=line[5:].strip()
            if frame==b'[DONE]':break
            event=json.loads(frame)
            if event.get('usage'):usage=event['usage']
            if event.get('base_resp',{}).get('status_code',0):
                raise RuntimeError('Configured LLM provider code '+str(event['base_resp']['status_code']))
            for ch in event.get('choices',[]):
                delta=ch.get('delta',{}).get('content','')
                if delta:parts.append(delta)
                if ch.get('finish_reason'):finish=ch['finish_reason']
        if finish is None:raise RuntimeError('Configured LLM stream ended before completion')
        data={'choices':[{'message':{'content':''.join(parts)},'finish_reason':finish}],'usage':usage}
    else:
        data=response.json()
    if data.get('base_resp',{}).get('status_code',0):
        raise RuntimeError('Configured LLM provider code '+str(data['base_resp']['status_code']))
    if not data.get('choices'):
        raise RuntimeError('Configured LLM returned no choices')
    choice = data['choices'][0]
    if choice.get('finish_reason') == 'length':
        raise RuntimeError('Configured LLM output truncated')
    answer = choice.get('message',{}).get('content','')
    answer = re.sub(r'<think>[\s\S]*?</think>','',answer,flags=re.I).strip()
    if not answer: raise RuntimeError('Configured LLM empty answer')
    return answer, data.get('usage',{})

def json_answer(text):
    text = re.sub(r'^```(?:json)?\s*|\s*```$','',text.strip())
    try: return json.loads(text)
    except json.JSONDecodeError:
        # vendor2 holds a locally maintained json_repair; the original vendor
        # copy is unreadable on this machine and PyPI is unreachable.
        for p in (Path(__file__).parent/'vendor2', Path(__file__).parent/'vendor'):
            sys.path.insert(0,str(p))
        from json_repair import repair_json
        repaired=repair_json(text,return_objects=True,skip_json_loads=True)
        if not isinstance(repaired,dict): raise RuntimeError('json-repair-not-object')
        return repaired

if __name__=='__main__':
    answer,usage=call('只回答：OK。', '连通性测试', max_tokens=50)
    print(json.dumps({'answer':answer,'usage':usage},ensure_ascii=False),flush=True)
