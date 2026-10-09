from pathlib import Path
p=Path(__file__).parent/'audit-5l-ld-codex.py'
source=p.read_text(encoding='utf-8').replace("['5LCZ6Y94','LDMEJZHN']","['9BZH5GCC','BJCHTQFG']").replace("if key=='5LCZ6Y94':","if key=='unused':").replace('codex-two-paper-integrity-5l-ld-20261008.json','codex-two-paper-integrity-9b-bj-20261008.json')
exec(compile(source,str(p),'exec'))
