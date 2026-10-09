from pathlib import Path
p=Path(__file__).parent/'audit-5l-ld-codex.py'
source=p.read_text(encoding='utf-8').replace("['5LCZ6Y94','LDMEJZHN']","['NEFNRZLY','YLHKWJ9W']").replace("if key=='5LCZ6Y94':","if key=='unused':").replace('codex-two-paper-integrity-5l-ld-20261008.json','codex-two-paper-integrity-ne-yl-20261008.json')
source=source.replace("'eight_main_chapters':len(re.findall(r'^# ',body,re.M))==8", "'expected_main_chapters':len(re.findall(r'^# ',body,re.M))==(8 if draft['paper_type']=='research' else 4)")
exec(compile(source,str(p),'exec'))
