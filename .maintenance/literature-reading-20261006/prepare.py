import concurrent.futures, json, re, hashlib, traceback
from pathlib import Path
from urllib.parse import urlparse, unquote
from collections import Counter
import fitz, requests
from inventory import ROOT, VAULT, norm

def resolve(key):
    s = requests.Session(); s.trust_env = False
    r = s.get(f'http://127.0.0.1:23119/api/users/0/items/{key}/file/view/url', timeout=60)
    r.raise_for_status()
    raw = r.text.strip().strip('"')
    if not raw.startswith('file:'):
        raise RuntimeError('Attachment file URL missing')
    part = unquote(urlparse(raw).path)
    if re.match(r'^/[A-Za-z]:', part): part = part[1:]
    return Path(part)

def process(rec):
    r = dict(rec)
    directory = ROOT / 'sources' / r['key']; directory.mkdir(parents=True, exist_ok=True)
    candidates = []; errors = []
    for attachment in r['pdf_attachments']:
        try:
            path = resolve(attachment['key'])
            with fitz.open(path) as doc:
                pages = [page.get_text('text', sort=False) for page in doc]
                first = '\n'.join(pages[:2])
                si = bool(re.search(r'supporting information|supplementary information|supplemental information|supplementary material', first[:1500], re.I))
                # ACS main articles contain a "Supporting Information" website button.
                # A button is not evidence that the PDF itself is SI.
                filename_si = bool(re.search(r'(?:_si_\d+|suppinfo|supplement|supporting)',path.name,re.I))
                if re.search(r'\babstract\b|\bintroduction\b',first[:7000],re.I) and not filename_si:
                    si = False
                match = norm(r['title']) in norm(first[:12000])
                doi_match = bool(r['doi']) and r['doi'].lower() in first.lower()
                score = (100 if match else 0) + (70 if doi_match else 0) + (0 if si else 20)
                if re.search(r'\b(support|supplement|supinfo|[sS][iI]\.pdf)\b', str(path.name), re.I): score -= 60
                candidates.append({'key': attachment['key'], 'path': str(path), 'pages':len(pages), 'texts': pages,
                                   'score':score, 'is_supplement':si, 'title_match':match, 'doi_match':doi_match})
        except Exception as e:
            errors.append({'key':attachment['key'], 'error':type(e).__name__ + ': ' + str(e)[:300]})
    if not candidates:
        r.update(status='blocked-pdf-unavailable', errors=errors)
        return r
    candidates.sort(key=lambda x:x['score'], reverse=True)
    selected = candidates[0]
    first = '\n'.join(selected['texts'][:3])
    if selected['is_supplement'] or selected['score'] < 20:
        r.update(status='blocked-main-pdf-identity', attachment_checks=[{k:v for k,v in x.items() if k!='texts'} for x in candidates])
        return r
    if re.search(r'博士学位论文|硕士学位论文|学位论文', first[:5000]):
        r.update(status='excluded-thesis-pdf')
        return r
    if len(re.findall(r'[\u4e00-\u9fff]', first)) > max(150, len(re.findall(r'[A-Za-z]', first))*0.25):
        r.update(status='excluded-chinese-pdf')
        return r
    source = '\n\n'.join(f'\n[PDF physical page {i+1}]\n{text}' for i,text in enumerate(selected['texts']))
    if len(source) < 2500:
        r.update(status='blocked-text-extraction', main_pdf=selected['path'])
        return r
    (directory/'main-text.txt').write_text(source,encoding='utf-8')
    si_text = '\n\n'.join(f'[Attachment {x["key"]}; PDF page {i+1}]\n{txt}'
                            for x in candidates[1:] for i,txt in enumerate(x['texts']))
    if si_text: (directory/'other-attachments.txt').write_text(si_text,encoding='utf-8')
    # Full caption blocks and their page coordinates form a source-located checklist.
    graphics = []; seen = set()
    with fitz.open(selected['path']) as doc:
        for page_no,page in enumerate(doc):
            for block in page.get_text('blocks'):
                text = block[4].strip()
                m = re.match(r'^(Fig(?:ure)?\.?|Table|Scheme)\s*(\d+)\b', text, re.I)
                if not m: continue
                kind = 'Figure' if m[1].lower().startswith('fig') else m[1].title()
                label = kind + ' ' + m[2]
                key = (label,page_no+1)
                if key in seen: continue
                seen.add(key)
                graphics.append({'label':label,'kind':kind,'number':int(m[2]),'page':page_no+1,
                                 'caption':text,'caption_bbox':list(block[:4])})
    r.update(status='ready', main_pdf=selected['path'], main_attachment_key=selected['key'],
             main_pdf_sha256=hashlib.sha256(Path(selected['path']).read_bytes()).hexdigest(),
             pdf_pages=selected['pages'], source_text=str(directory/'main-text.txt'),
             supplements=[{k:v for k,v in x.items() if k not in {'texts','score'}} for x in candidates[1:]],
             figure_candidates=graphics, pdf_identity={'title_match':selected['title_match'],'doi_match':selected['doi_match']})
    (directory/'prepared.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
    return r

def main():
    data = json.loads((ROOT/'inventory.json').read_text(encoding='utf-8'))
    seen = {}; unique = []; records = data['records']
    for r in records:
        if r['status'] == 'already-interpreted':
            seen[r['doi'].lower() or norm(r['title'])] = r['key']
    for r in records:
        if r['status'] != 'pending-pdf-check': continue
        identity = r['doi'].lower() or norm(r['title'])
        if identity in seen:
            r.update(status='duplicate-record', canonical_key=seen[identity])
        else:
            seen[identity] = r['key']; unique.append(r)
    done = {}; total = len(unique)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        jobs = {pool.submit(process,r):r['key'] for r in unique}
        for n,f in enumerate(concurrent.futures.as_completed(jobs),1):
            key = jobs[f]
            try: done[key] = f.result()
            except Exception as e: done[key] = dict(next(r for r in unique if r['key']==key),status='blocked-preparation',error=str(e))
            if n % 50 == 0 or n == total:
                print(f'PDF preparation {n}/{total}: {dict(Counter(x["status"] for x in done.values()))}',flush=True)
    data['records'] = [done.get(r['key'],r) for r in records]
    data['summary']['prepared_counts'] = dict(Counter(x['status'] for x in data['records']))
    (ROOT/'prepared-inventory.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(data['summary'],ensure_ascii=False,indent=2),flush=True)

if __name__=='__main__': main()
