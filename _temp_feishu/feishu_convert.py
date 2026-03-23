import json
import urllib.request
import os
import uuid

config_path = r'C:\Users\lhc\.newmax\skills\feishu-doc-reader\reference\feishu_config.json'
with open(config_path) as f:
    config = json.load(f)
app_id = config['app_id']
app_secret = config['app_secret']

out_base = "C:/Software/Data/03-GitHub/SynBioPath"
temp_dir = out_base + "/_temp_feishu"
os.makedirs(temp_dir, exist_ok=True)

TOKEN_CACHE = None

def get_token():
    global TOKEN_CACHE
    if TOKEN_CACHE:
        return TOKEN_CACHE
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
    data = json.dumps({'app_id': app_id, 'app_secret': app_secret}).encode()
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    resp = urllib.request.urlopen(req)
    TOKEN_CACHE = json.loads(resp.read())['tenant_access_token']
    return TOKEN_CACHE

def safe_json_loads(data):
    """Load JSON with UTF-8 lenient decoding (replaces invalid sequences instead of failing)"""
    if isinstance(data, bytes):
        text = data.decode('utf-8', errors='replace')
        return json.loads(text)
    return json.loads(data)

def get_doc_title(doc_token):
    """Get document title from API - returns correctly encoded text"""
    url = 'https://open.feishu.cn/open-apis/docx/v1/documents/' + doc_token
    req = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + get_token()})
    resp = urllib.request.urlopen(req)
    data = safe_json_loads(resp.read())
    if data.get('code') == 0:
        return data.get('data', {}).get('document', {}).get('title', 'Untitled')
    return 'Untitled'

def get_doc_blocks(doc_token):
    """Get document blocks with lenient UTF-8 decoding"""
    url = 'https://open.feishu.cn/open-apis/docx/v1/documents/' + doc_token + '/blocks?page_size=500'
    req = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + get_token()})
    resp = urllib.request.urlopen(req)
    data = safe_json_loads(resp.read())
    if data.get('code') == 0:
        return data.get('data', {})
    return {}

def get_wiki_doc_token(wiki_token):
    """Get underlying docx token from wiki token"""
    url = 'https://open.feishu.cn/open-apis/wiki/v2/spaces/get_node?token=' + wiki_token
    req = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + get_token()})
    resp = urllib.request.urlopen(req)
    data = safe_json_loads(resp.read())
    if data.get('code') == 0:
        return data.get('data', {}).get('node', {}).get('obj_token', '')
    return ''

def get_text_from_elements(elements):
    parts = []
    for el in elements:
        tr = el.get('text_run', {})
        content = tr.get('content', '')
        style = tr.get('text_element_style', {})
        if style.get('bold'):
            content = '**' + content + '**'
        if style.get('italic'):
            content = '*' + content + '*'
        if style.get('inline_code'):
            content = '`' + content + '`'
        if style.get('strikethrough'):
            content = '~~' + content + '~~'
        if style.get('underline'):
            content = '<u>' + content + '</u>'
        if 'link' in tr:
            link = tr['link'].get('url', '')
            if link:
                content = '[' + content + '](' + link + ')'
        parts.append(content)
    return ''.join(parts)

def get_image_url(doc_token, image_token):
    url = 'https://open.feishu.cn/open-apis/docx/v1/documents/' + doc_token + '/images/' + image_token + '/download'
    req = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + get_token()})
    resp = urllib.request.urlopen(req)
    data = safe_json_loads(resp.read())
    if data.get('code') == 0:
        return data.get('data', {}).get('url', '')
    return None

def download_image(url):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    return resp.read()

def upload_to_picgo(image_bytes):
    boundary = uuid.uuid4().hex
    body = b'--' + boundary.encode() + b'\r\n'
    body += b'Content-Disposition: form-data; name="file"; filename="image.png"\r\n'
    body += b'Content-Type: image/png\r\n\r\n'
    body += image_bytes + b'\r\n'
    body += b'--' + boundary.encode() + b'--\r\n'
    req = urllib.request.Request(
        'http://127.0.0.1:36677/upload', data=body,
        headers={'Content-Type': 'multipart/form-data; boundary=' + boundary}
    )
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        result = json.loads(resp.read())
        if result.get('code') == 0:
            return result.get('data', {}).get('url', '')
    except:
        pass
    return None

def convert_blocks_to_md(blocks_data, doc_token):
    items = blocks_data.get('items', [])
    children_map = {}
    for item in items:
        pid = item.get('parent_id', '')
        if pid not in children_map:
            children_map[pid] = []
        children_map[pid].append(item)

    image_cache = {}

    def render_block(block, indent=0):
        bt = block.get('block_type')
        block_id = block.get('block_id')

        if bt == 2:
            return get_text_from_elements(block.get('text', {}).get('elements', []))

        if bt == 3:
            return '## ' + get_text_from_elements(block.get('heading1', {}).get('elements', []))
        if bt == 4:
            return '## ' + get_text_from_elements(block.get('heading2', {}).get('elements', []))
        if bt == 5:
            return '### ' + get_text_from_elements(block.get('heading3', {}).get('elements', []))
        if bt in (6, 7, 8, 9, 10, 11):
            key = 'heading' + str(bt)
            prefix = '#' * (bt - 2)
            return prefix + ' ' + get_text_from_elements(block.get(key, {}).get('elements', []))

        if bt in (12, 14, 18):
            prefix = ' ' * indent + '- '
            content = get_text_from_elements(block.get('text', {}).get('elements', []))
            child_parts = []
            for child_id in children_map.get(block_id, []):
                child_block = next((x for x in items if x['block_id'] == child_id), None)
                if child_block:
                    child_md = render_block(child_block, indent + 2)
                    if child_md:
                        child_parts.append(child_md)
            result = prefix + content
            if child_parts:
                result += '\n' + '\n'.join(child_parts)
            return result

        if bt in (13, 15, 17):
            prefix = ' ' * indent + '1. '
            content = get_text_from_elements(block.get('text', {}).get('elements', []))
            child_parts = []
            for child_id in children_map.get(block_id, []):
                child_block = next((x for x in items if x['block_id'] == child_id), None)
                if child_block:
                    child_md = render_block(child_block, indent + 2)
                    if child_md:
                        child_parts.append(child_md)
            result = prefix + content
            if child_parts:
                result += '\n' + '\n'.join(child_parts)
            return result

        if bt == 16:
            code = block.get('code', {}).get('elements', [])
            lang = block.get('code', {}).get('style', {}).get('language', '')
            code_text = get_text_from_elements(code)
            lang_str = '```' + lang + '\n' if lang else '```\n'
            return lang_str + code_text + '\n```'

        if bt in (24, 25):
            return '> ' + get_text_from_elements(block.get('quote', {}).get('elements', []))

        if bt == 26:
            return '---'

        if bt == 27:
            image_token = block.get('image', {}).get('token', '')
            if image_token not in image_cache:
                img_url = get_image_url(doc_token, image_token)
                picgo_url = None
                if img_url:
                    img_bytes = download_image(img_url)
                    picgo_url = upload_to_picgo(img_bytes)
                image_cache[image_token] = picgo_url if picgo_url else (img_url if img_url else None)
            url = image_cache.get(image_token)
            if url:
                return '![]( ' + url + ')'
            return ''

        if bt == 19:
            rows = []
            for child_id in children_map.get(block_id, []):
                child_block = next((x for x in items if x['block_id'] == child_id), None)
                if child_block and child_block.get('block_type') == 32:
                    row_cells = []
                    for cell_id in children_map.get(child_id, []):
                        cell_block = next((x for x in items if x['block_id'] == cell_id), None)
                        if cell_block:
                            cell_text = get_text_from_elements(cell_block.get('tableCell', {}).get('elements', []))
                            row_cells.append(cell_text)
                    if row_cells:
                        rows.append('| ' + ' | '.join(row_cells) + ' |')
            if rows:
                col_count = len(rows[0].split('|')) - 2
                sep = '| ' + ' | '.join(['---'] * col_count) + ' |'
                return '\n'.join([rows[0], sep] + rows[1:])
            return ''

        for key in ['text', 'paragraph']:
            if key in block:
                elements = block[key].get('elements', [])
                if elements:
                    return get_text_from_elements(elements)
        return ''

    root = next((x for x in items if x.get('block_type') == 1), None)
    if not root:
        return ""
    root_id = root.get('block_id')

    md_parts = []
    for child_id in children_map.get(root_id, []):
        child_block = next((x for x in items if x['block_id'] == child_id), None)
        if child_block:
            md = render_block(child_block)
            if md:
                md_parts.append(md)

    return '\n\n'.join(md_parts)

def sanitize_filename(s):
    import re
    return re.sub(r'[<>:"/\\|?*]', '_', s)[:60]

wiki_tokens = ['HBbnwt9AbinTQgkc4mucm3QMn5k', 'KXy1w4mjZiX2QHkhj0scbNl7nO5']

results = []
for wiki_token in wiki_tokens:
    doc_token = get_wiki_doc_token(wiki_token)
    if not doc_token:
        print('Failed to get doc token for wiki:', wiki_token)
        continue

    title = get_doc_title(doc_token)
    print('Title: ' + title)

    blocks_data = get_doc_blocks(doc_token)
    items = blocks_data.get('items', [])
    print('Blocks: ' + str(len(items)))

    md_content = convert_blocks_to_md(blocks_data, doc_token)

    safe_title = sanitize_filename(title)
    out_file = out_base + '/' + safe_title + '.md'

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write('title: "' + title + '"\n')
        f.write('feishu_wiki_token: "' + wiki_token + '"\n')
        f.write('feishu_doc_token: "' + doc_token + '"\n')
        f.write('source: feishu_wiki\n')
        f.write('---\n\n')
        f.write('# ' + title + '\n\n')
        f.write(md_content)

    print('Saved: ' + out_file)
    results.append((title, out_file))

print('\nAll done!')
for t, p in results:
    print('  ' + t)
    print('    -> ' + p)