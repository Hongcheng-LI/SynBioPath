from pathlib import Path
p=Path(__file__).parent/'audit-5l-ld-codex.py'
source=p.read_text(encoding='utf-8').replace("['5LCZ6Y94','LDMEJZHN']","['T653KQDL','A4UKNEHC','JJ77V5A7','A2J2FZZU']").replace("==8,'no_unresolved_figure_markers'","==(4 if draft['paper_type']=='review' else 8),'no_unresolved_figure_markers'").replace("if key=='5LCZ6Y94':","if key=='unused':").replace('codex-two-paper-integrity-5l-ld-20261008.json','codex-four-paper-integrity-t6-a4-jj-a2-20261008.json')
exec(compile(source,str(p),'exec'))
