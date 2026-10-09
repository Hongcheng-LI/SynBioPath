from pathlib import Path
p=Path(__file__).parent/'audit-5l-ld-codex.py'
source=p.read_text(encoding='utf-8').replace("['5LCZ6Y94','LDMEJZHN']","['KAXHEABT','W4IHDLC6']").replace("==8,'no_unresolved_figure_markers'","==(4 if draft['paper_type']=='review' else 8),'no_unresolved_figure_markers'").replace("if key=='5LCZ6Y94':","if key=='unused':").replace('codex-two-paper-integrity-5l-ld-20261008.json','codex-two-paper-integrity-kax-w4-20261008.json')
exec(compile(source,str(p),'exec'))
