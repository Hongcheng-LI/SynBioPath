from pathlib import Path
p=Path(__file__).parent/'audit-5l-ld-codex.py'
s=p.read_text(encoding='utf-8').replace("['5LCZ6Y94','LDMEJZHN']","['5F27T5Y6','U7JJFWV8']").replace("if key=='5LCZ6Y94':","if key=='unused':").replace('codex-two-paper-integrity-5l-ld-20261008.json','codex-two-paper-integrity-5f27-u7-20261008.json')
exec(compile(s,str(p),'exec'))
