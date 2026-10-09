from pathlib import Path
source=Path(__file__).with_name('audit-5l-ld-codex.py').read_text(encoding='utf-8')
source=source.replace('5LCZ6Y94','FZARD87N').replace('LDMEJZHN','RZNZCQRY').replace('codex-two-paper-integrity-5l-ld-20261008.json','codex-two-paper-integrity-fz-rz-20261008.json')
# The older audit's continuation-table conditions apply only to its older paper.
source=source.replace("if key=='FZARD87N':", "if key=='unused':")
exec(compile(source,str(Path(__file__)),'exec'))
