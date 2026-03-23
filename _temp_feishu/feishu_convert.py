import json
import urllib.request
import os
import re
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

def get_wiki_doc_token(wiki_token):
    url = 'https://open.feishu.cn/open-apis/wiki/v2/spaces/get_node?token=' + wiki_token
    req = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + get_token()})
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    if data.get('code') == 0:
        return data.get('data', {}).get('node', {}).get('obj_token', '')
    return ''

def get_doc_title(doc_token):
    url = 'https://open.feishu.cn/open-apis/docx/v1/documents/' + doc_token
    req = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + get_token()})
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    if data.get('code') == 0:
        return data.get('data', {}).get('document', {}).get('title', 'Untitled')
    return 'Untitled'

def get_raw_content(doc_token):
    url = 'https://open.feishu.cn/open-apis/docx/v1/documents/' + doc_token + '/raw_content'
    req = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + get_token()})
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    if data.get('code') == 0:
        return data.get('data', {}).get('content', '')
    return ''

def get_image_tokens(doc_token):
    """Get all image tokens from document blocks"""
    url = 'https://open.feishu.cn/open-apis/docx/v1/documents/' + doc_token + '/blocks?page_size=500'
    req = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + get_token()})
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    if data.get('code') == 0:
        items = data.get('data', {}).get('items', [])
        image_tokens = []
        for item in items:
            if item.get('block_type') == 27:
                token = item.get('image', {}).get('token', '')
                if token:
                    image_tokens.append(token)
        return image_tokens
    return []

def get_image_url(doc_token, image_token):
    url = 'https://open.feishu.cn/open-apis/docx/v1/documents/' + doc_token + '/images/' + image_token + '/download'
    req = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + get_token()})
    try:
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read())
        if data.get('code') == 0:
            return data.get('data', {}).get('url', '')
    except:
        pass
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

def parse_raw_content_to_md(content, image_map):
    """Convert raw content text to markdown format"""
    lines = content.split('\n')
    md_lines = []
    i = 0
    image_idx = 0

    while i < len(lines):
        line = lines[i].strip()
        if not line:
            md_lines.append('')
            i += 1
            continue

        # Skip standalone image.png references at start (cover image)
        if line == 'image.png' and i <= 2:
            i += 1
            continue

        # Section headers: "一：", "二：", etc.
        if re.match(r'^[\u4e00-\u9fff]\u3001', line) or re.match(r'^[\u4e00-\u9fff]\uff1a', line):
            header_match = re.match(r'^([\u4e00-\u9fff]\uff1a)(.*)', line)
            if header_match:
                rest = header_match.group(2).strip()
                if rest:
                    md_lines.append('## ' + rest)
                else:
                    md_lines.append('## ' + line)
            else:
                md_lines.append('## ' + line)
            i += 1
            continue

        # Sub-headers: short Chinese text (research background, methods, etc.)
        if i > 0 and 2 <= len(line) <= 20 and re.match(r'^[\u4e00-\u9fff]+$', line):
            md_lines.append('### ' + line)
            i += 1
            continue

        # Key-value pairs: "文章题目：...", "文章 DOI 号：..."
        matched = False
        for sep in ['\uff1a']:
            idx = line.find(sep)
            if 0 < idx < 40:
                key = line[:idx].strip()
                value = line[idx+1:].strip()
                if value:
                    md_lines.append('**' + key + '：**' + value)
                    matched = True
                    break
        if not matched:
            md_lines.append(line)

        # Image references
        if line == 'image.png':
            if image_idx < len(image_map):
                img_data = image_map[image_idx]
                url = img_data.get('picgo_url') or img_data.get('original_url')
                if url:
                    md_lines.append(f'![]({url})')
                else:
                    md_lines.append(f'![image](image_{image_idx + 1}.png)')
                image_idx += 1
            i += 1
            continue

        # Figure captions: "Figure 2a: ..."
        fig_match = re.match(r'^(Figure|Figure\s+)(\d+[a-z]?)\s*[:\uff1a]\s*(.*)', line, re.IGNORECASE)
        if fig_match:
            caption = fig_match.group(3).strip()
            if caption:
                md_lines.append(f'*Figure {fig_match.group(2)}: {caption}*')
            else:
                md_lines.append(f'**Figure {fig_match.group(2)}**')
            i += 1
            continue

        fig_match2 = re.match(r'^(图|figure)\s*(\d+[a-z]?)\s*[:\uff1a]\s*(.*)', line, re.IGNORECASE)
        if fig_match2:
            caption = fig_match2.group(3).strip()
            if caption:
                md_lines.append(f'*{fig_match2.group(1).title()} {fig_match2.group(2)}: {caption}*')
            else:
                md_lines.append(f'**Figure {fig_match2.group(2)}**')
            i += 1
            continue

        # Bold lines (research highlights numbered items)
        bold_match = re.match(r'^(\d+\.)\s+(.*)', line)
        if bold_match:
            md_lines.append('**' + bold_match.group(1) + '** ' + bold_match.group(2))
            i += 1
            continue

        # Regular paragraphs
        if line not in md_lines[-1] if md_lines else False:
            md_lines.append(line)
        else:
            md_lines.append(line)
        i += 1

    return '\n'.join(md_lines)

def sanitize_filename(s):
    return re.sub(r'[<>:"/\\|?*]', '_', s)[:60]

def process_wiki_doc(wiki_token):
    doc_token = get_wiki_doc_token(wiki_token)
    if not doc_token:
        return None, 'Failed to get doc token'

    title = get_doc_title(doc_token)
    content = get_raw_content(doc_token)

    # Get image tokens
    image_tokens = get_image_tokens(doc_token)
    image_map = []
    for img_token in image_tokens:
        img_url = get_image_url(doc_token, img_token)
        picgo_url = None
        if img_url:
            try:
                img_bytes = download_image(img_url)
                picgo_url = upload_to_picgo(img_bytes)
            except Exception as e:
                pass
        # Store tuple (url, uploaded_url)
        image_map.append({'original_url': img_url, 'picgo_url': picgo_url})

    md_body = parse_raw_content_to_md(content, image_map)

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
        f.write(md_body)

    return title, out_file

# Main
wiki_tokens = ['HBbnwt9AbinTQgkc4mucm3QMn5k', 'KXy1w4mjZiX2QHkhj0scbNl7nO5']

results = []
for wiki_token in wiki_tokens:
    print('Processing:', wiki_token)
    title, result = process_wiki_doc(wiki_token)
    if title:
        print('  Title:', title)
        print('  Saved:', result)
        results.append((title, result))
    else:
        print('  Error:', result)

print('\nAll done!')
for t, p in results:
    print(' ', t)
    print('   ->', p)