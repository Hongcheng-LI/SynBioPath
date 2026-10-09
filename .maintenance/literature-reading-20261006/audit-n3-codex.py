from pathlib import Path
p=Path(__file__).parent/'audit-wk-codex.py'
s=p.read_text(encoding='utf-8').replace('WKPAY6CE','N3NBXMFA').replace('codex-paper-integrity-wk-20261008.json','codex-paper-integrity-n3-20261008.json')
exec(compile(s,str(p),'exec'))
