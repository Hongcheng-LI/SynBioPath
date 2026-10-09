from pathlib import Path
p=Path(__file__).parent/'audit-5l-ld-codex.py'
source=p.read_text(encoding='utf-8').replace("['5LCZ6Y94','LDMEJZHN']","['MFLGZ2V3','QWTYVVCT','UZJ6VLEJ','QIVCCQB8','K4UYREEP','V6BKYU8Q']").replace("if key=='5LCZ6Y94':","if key=='unused':").replace('codex-two-paper-integrity-5l-ld-20261008.json','codex-six-paper-integrity-20261008.json')
exec(compile(source,str(p),'exec'))
