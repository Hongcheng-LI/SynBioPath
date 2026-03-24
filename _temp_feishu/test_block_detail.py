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

doc_token = 'EIsyd1JZ8oF0koxvQNRc92wFnSh'

# Get full blocks response (not just the simplified version)
url = f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}/blocks?page_size=50&text_format=true'
req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
resp2 = urllib.request.urlopen(req2)
raw = resp2.read()
text = raw.decode('utf-8', errors='replace')
data = json.loads(text)

blocks = data.get('data', {}).get('items', [])
for b in blocks:
    if b.get('block_type') == 27:  # Image block
        print('Full image block:')
        print(json.dumps(b, ensure_ascii=False, indent=2))
        print()
        # Check if there are any extra fields
        img = b.get('image', {})
        for key in img:
            print(f'  Image field: {key} = {img[key]}')
