from pathlib import Path
p=Path(__file__).parent/'audit-5l-ld-codex.py'
source=p.read_text(encoding='utf-8').replace("['5LCZ6Y94','LDMEJZHN']","['WKPAY6CE']").replace("if key=='5LCZ6Y94':","if key=='unused':").replace("len(re.findall(r'^# ',body,re.M))==8","len(re.findall(r'^# ',body,re.M))==4").replace('codex-two-paper-integrity-5l-ld-20261008.json','codex-paper-integrity-wk-20261008.json')
exec(compile(source,str(p),'exec'))
