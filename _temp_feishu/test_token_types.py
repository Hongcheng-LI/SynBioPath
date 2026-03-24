import json, urllib.request

with open('C:/Users/lhc/.newmax/skills/feishu-doc-reader/reference/feishu_config.json', 'r') as f:
    feishu_config = json.load(f)
app_id = feishu_config['app_id']
app_secret = feishu_config['app_secret']

req = urllib.request.Request(
    'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal',
    data=json.dumps({'app_id': app_id, 'app_secret': app_secret}).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)
resp = urllib.request.urlopen(req)
tenant_token = json.loads(resp.read().decode('utf-8'))['tenant_access_token']

# Get all image tokens from our document
doc_token = 'EIsyd1JZ8oF0koxvQNRc92wFnSh'

url = f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}/blocks?page_size=50'
req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
resp2 = urllib.request.urlopen(req2)
raw = resp2.read()
text = raw.decode('utf-8', errors='replace')
data = json.loads(text)

blocks = data.get('data', {}).get('items', [])
image_tokens = []
for b in blocks:
    if b.get('block_type') == 27:
        img = b.get('image', {})
        token = img.get('token')
        if token:
            image_tokens.append(token)
            print(f'Image token: {token} (starts with: {token[:4]})')

print(f'\nTotal image tokens: {len(image_tokens)}')

# Check if any start with 'boxcn'
boxcn_tokens = [t for t in image_tokens if t.startswith('boxcn')]
qu9w_tokens = [t for t in image_tokens if t.startswith('QU9W')]
print(f'boxcn tokens: {len(boxcn_tokens)}')
print(f'QU9W tokens: {len(qu9w_tokens)}')

# Test each type with batch_get_tmp_download_url
for token_type, tokens in [('boxcn', boxcn_tokens), ('QU9W', qu9w_tokens)]:
    if tokens:
        test_token = tokens[0]
        url3 = f'https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url?file_tokens={test_token}'
        req3 = urllib.request.Request(url3, headers={'Authorization': 'Bearer ' + tenant_token})
        try:
            resp3 = urllib.request.urlopen(req3)
            data3 = json.loads(resp3.read().decode('utf-8'))
            urls = data3.get('data', {}).get('tmp_download_urls', [])
            if urls:
                print(f'{token_type}: GOT URL - {urls[0].get("tmp_download_url", "")[:80]}...')
            else:
                print(f'{token_type}: empty URL list')
        except Exception as e:
            print(f'{token_type}: Error - {e}')
