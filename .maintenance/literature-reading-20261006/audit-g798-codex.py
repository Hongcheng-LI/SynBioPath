from pathlib import Path
p=Path(__file__).parent/'audit-73-codex.py'
source=p.read_text(encoding='utf-8').replace('73ZWPHQB','G798ZYDL').replace('codex-paper-integrity-73-20261008.json','codex-paper-integrity-g798-20261008.json')
exec(compile(source,str(p),'exec'))
