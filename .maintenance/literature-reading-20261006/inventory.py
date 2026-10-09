import json, re, hashlib, html, time
from pathlib import Path
from collections import Counter, defaultdict
from difflib import SequenceMatcher
import requests

ROOT = Path(__file__).resolve().parent
VAULT = ROOT.parent.parent
S = requests.Session()
S.trust_env = False
API = 'http://127.0.0.1:23119/api/users/0'

def get(route):
    response = S.get(API + route, timeout=90)
    response.raise_for_status()
    return response.json()

def paged(route):
    output = []
    for start in range(0, 50000, 100):
        rows = get(f'{route}?limit=100&start={start}')
        output.extend(rows)
        print(f'{route}: {len(output)}', flush=True)
        if len(rows) < 100:
            return output
    raise RuntimeError('Pagination limit exceeded')

def norm(s):
    return re.sub(r'[^a-z0-9]', '', html.unescape(s).lower())

def doi_norm(s):
    return s.lower().rstrip('.,;:，。；）)]}')

def main():
    items = paged('/items')
    collections = paged('/collections')
    (ROOT / 'zotero-items.json').write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT / 'zotero-collections.json').write_text(json.dumps(collections, ensure_ascii=False, indent=2), encoding='utf-8')
    notes = []
    for p in VAULT.rglob('*.md'):
        if any(part in {'.git', '.obsidian', '.maintenance'} for part in p.relative_to(VAULT).parts):
            continue
        text = p.read_text(encoding='utf-8-sig')
        # Navigation/list pages are never evidence of an already interpreted paper.
        if re.search(r'^type:\s*(?!literature-reading)[a-z-]+', text, re.M):
            continue
        if len(text) < 1500 or not re.search(r'研究背景|内容深度解读|实验设计|研究方法|论文评价|关键问题', text):
            continue
        notes.append({'path': str(p.relative_to(VAULT)).replace('\\', '/'),
                      'text': text, 'norm': norm(text),
                      'dois': {doi_norm(x) for x in re.findall(r'10\.\d{4,9}/[^\s<>\"\[\]]+', text, re.I)},
                      'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    by_doi = defaultdict(list)
    for n in notes:
        for d in n['dois']:
            by_doi[d].append(n['path'])
    children = defaultdict(list)
    for item in items:
        d = item['data']
        if d.get('parentItem'):
            children[d['parentItem']].append(item)
    output = []
    for item in items:
        d = item['data']
        kind = d['itemType']
        if kind in {'attachment', 'note', 'annotation'} or d.get('parentItem'):
            continue
        title = d.get('title', '')
        record = {'key': item['key'], 'title': title, 'doi': d.get('DOI', ''),
                  'item_type': kind, 'language': d.get('language', ''),
                  'date': d.get('date', ''), 'journal': d.get('publicationTitle', ''),
                  'collections': d.get('collections', []),
                  'pdf_attachments': [{'key': x['key'], 'filename': x['data'].get('filename'),
                                       'title': x['data'].get('title', ''), 'linkMode': x['data'].get('linkMode'),
                                       'path': x['data'].get('path')}
                                      for x in children[item['key']]
                                      if x['data'].get('contentType') == 'application/pdf'],
                  'existing_notes': [], 'match_basis': []}
        if kind == 'thesis' or re.search(r'博士[学位毕业]*论文|硕士[学位毕业]*论文', title):
            record['status'] = 'excluded-thesis'
        elif re.match(r'^(zh|chi|chinese|中文)', d.get('language', ''), re.I) or (len(re.findall(r'[\u4e00-\u9fff]', title)) >= 4):
            record['status'] = 'excluded-chinese'
        elif kind not in {'journalArticle', 'preprint', 'conferencePaper'}:
            record['status'] = 'excluded-non-paper'
        else:
            doi = doi_norm(d.get('DOI', ''))
            if doi and doi in by_doi:
                record['existing_notes'].extend(by_doi[doi])
                record['match_basis'].append('DOI in substantive reading note')
            nt = norm(title)
            for n in notes:
                if len(nt) >= 25 and nt in n['norm']:
                    record['existing_notes'].append(n['path'])
                    record['match_basis'].append('exact normalized title in substantive reading note')
            for child in children[item['key']]:
                if child['data']['itemType'] == 'note':
                    plain = html.unescape(re.sub('<[^>]+>', ' ', child['data'].get('note', '')))
                    if len(plain) > 1800 and len(re.findall(r'[\u4e00-\u9fff]', plain)) > 600 and re.search(r'研究背景|实验设计|内容深度解读|论文评价', plain):
                        record['existing_notes'].append('zotero-note:' + child['key'])
                        record['match_basis'].append('substantive interpretation in Zotero child note')
            record['existing_notes'] = sorted(set(record['existing_notes']))
            record['match_basis'] = sorted(set(record['match_basis']))
            if record['existing_notes']:
                record['status'] = 'already-interpreted'
            elif record['pdf_attachments']:
                record['status'] = 'pending-pdf-check'
            else:
                record['status'] = 'blocked-no-pdf'
        output.append(record)
    summary = {'scope': 'entire personal library; exclude Chinese papers and theses',
               'vault': str(VAULT), 'live_items': len(items), 'parent_records': len(output),
               'substantive_vault_notes': len(notes), 'counts': dict(Counter(x['status'] for x in output))}
    (ROOT / 'inventory.json').write_text(json.dumps({'summary': summary, 'records': output}, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT / 'existing-note-hashes.json').write_text(json.dumps([{k:v for k,v in n.items() if k in {'path','sha256'}} for n in notes], ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)

if __name__ == '__main__':
    main()
