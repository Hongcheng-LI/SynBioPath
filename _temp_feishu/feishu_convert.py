import json
import urllib.request
import os
import uuid

# ===================== CONFIG =====================
config_path = r'C:\Users\lhc\.newmax\skills\feishu-doc-reader\reference\feishu_config.json'
with open(config_path) as f:
    config = json.load(f)
app_id = config['app_id']
app_secret = config['app_secret']

out_base = "C:/Software/Data/03-GitHub/SynBioPath"
temp_dir = f"{out_base}/_temp_feishu"
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

def fix_encoding(text):
    """Fix double-encoded GBK-in-UTF8 text"""
    if not text:
        return text
    try:
        fixed = text.encode('latin1').decode('gbk')
        return fixed
    except:
        return text

def get_text_from_elements(elements):
    """Extract text from text_run elements, fixing encoding"""
    parts = []
    for el in elements:
        tr = el.get('text_run', {})
        content = tr.get('content', '')
        style = tr.get('text_element_style', {})

        content = fix_encoding(content)

        if style.get('bold'):
            content = f'**{content}**'
        if style.get('italic'):
            content = f'*{content}*'
        if style.get('inline_code'):
            content = f'`{content}`'
        if style.get('strikethrough'):
            content = f'~~{content}~~'
        if style.get('underline'):
            content = f'<u>{content}</u>'

        if 'link' in tr:
            link = tr['link'].get('url', '')
            if link:
                content = f'[{content}]({link})'

        parts.append(content)
    return ''.join(parts)

def get_image_url(doc_token, image_token):
    """Get download URL for a Feishu image"""
    url = f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}/images/{image_token}/download'
    token = get_token()
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}'})
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    if data.get('code') == 0:
        return data.get('data', {}).get('url', '')
    return None

def download_image(url):
    """Download image bytes from URL"""
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    return resp.read()

def upload_to_picgo(image_bytes):
    """Upload image to PicGo and return URL"""
    boundary = uuid.uuid4().hex
    body = b'--' + boundary.encode() + b'\r\n'
    body += b'Content-Disposition: form-data; name="file"; filename="image.png"\r\n'
    body += b'Content-Type: image/png\r\n\r\n'
    body += image_bytes + b'\r\n'
    body += b'--' + boundary.encode() + b'--\r\n'

    req = urllib.request.Request(
        'http://127.0.0.1:36677/upload',
        data=body,
        headers={
            'Content-Type': f'multipart/form-data; boundary={boundary}'
        }
    )
    resp = urllib.request.urlopen(req, timeout=30)
    result = json.loads(resp.read())
    if result.get('code') == 0:
        return result.get('data', {}).get('url', '')
    return None

def convert_blocks_to_md(blocks_data, doc_token):
    """Convert Feishu blocks to markdown recursively"""
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
            elements = block.get('text', {}).get('elements', [])
            return get_text_from_elements(elements)

        if bt == 3:
            elements = block.get('heading1', {}).get('elements', [])
            return '## ' + get_text_from_elements(elements)
        if bt == 4:
            elements = block.get('heading2', {}).get('elements', [])
            return '## ' + get_text_from_elements(elements)
        if bt == 5:
            elements = block.get('heading3', {}).get('elements', [])
            return '### ' + get_text_from_elements(elements)
        if bt in (6, 7, 8, 9, 10, 11):
            prefix = '#' * (bt - 2)
            key = f'heading{bt}'
            elements = block.get(key, {}).get('elements', [])
            return prefix + ' ' + get_text_from_elements(elements)

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
            lang_str = f'```{lang}\n' if lang else '```\n'
            return lang_str + code_text + '\n```'

        if bt in (24, 25):
            elements = block.get('quote', {}).get('elements', [])
            return '> ' + get_text_from_elements(elements)

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
                return f'![]({url})'
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

# ===================== MAIN =====================
wiki_tokens = ['HBbnwt9AbinTQgkc4mucm3QMn5k', 'KXy1w4mjZiX2QHkhj0scbNl7nO5']

results = []
for wiki_token in wiki_tokens:
    blocks_file = f"{temp_dir}/feishu_blocks_{wiki_token}.json"
    with open(blocks_file, 'r', encoding='utf-8') as f:
        blocks_data = json.load(f)

    root = next((x for x in blocks_data.get('items', []) if x.get('block_type') == 1), None)
    doc_token = root.get('block_id', wiki_token) if root else wiki_token

    md = convert_blocks_to_md(blocks_data, doc_token)

    title = 'Untitled'
    for item in blocks_data.get('items', []):
        if item.get('block_type') in (2, 3, 4, 5):
            for key in ['text', 'heading1', 'heading2', 'heading3']:
                if key in item:
                    elements = item[key].get('elements', [])
                    if elements:
                        t = get_text_from_elements(elements)
                        t = fix_encoding(t).strip()
                        if t:
                            title = t
                            break
            if title != 'Untitled':
                break

    safe_title = ''.join(c if c.isalnum() or c in ' -_' else '_' for c in title)[:50]
    out_file = f"{out_base}/{safe_title}.md"

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(f'title: "{title}"\n')
        f.write(f'feishu_wiki_token: "{wiki_token}"\n')
        f.write(f'doc_token: "{doc_token}"\n')
        f.write('---\n\n')
        f.write(f'# {title}\n\n')
        f.write(md)

    print(f"Saved: {out_file}")
    results.append((title, out_file))

print("\nDone! Files:")
for title, path in results:
    print(f"  {title} -> {path}")