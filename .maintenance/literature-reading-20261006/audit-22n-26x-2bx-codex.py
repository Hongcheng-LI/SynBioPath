from pathlib import Path
p=Path(__file__).parent/'audit-5l-ld-codex.py'
s=p.read_text(encoding='utf-8').replace("['5LCZ6Y94','LDMEJZHN']","['22NXE44F','26XKNUT7','2BXAQGNW']").replace("if key=='5LCZ6Y94':","if key=='unused':").replace('codex-two-paper-integrity-5l-ld-20261008.json','codex-three-paper-integrity-22n-26x-2bx-20261008.json')
exec(compile(s,str(p),'exec'))
