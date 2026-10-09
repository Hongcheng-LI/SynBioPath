from pathlib import Path
p=Path(__file__).parent/'audit-g798-codex.py'
s=p.read_text(encoding='utf-8').replace('G798ZYDL','4B2ZIUEF').replace('audit-g798','audit-4b2')
exec(compile(s,str(p),'exec'))
