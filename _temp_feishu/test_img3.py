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

image_token = 'QU9WbBlU8oJZEhxKJnYcevk8nVe'

# Try different ways to pass file_tokens array
tests = [
    # Method 1: comma-separated
    ('Comma sep', f'file_tokens={image_token}'),
    # Method 2: repeated params (handled by urllib automatically)
    ('Repeated params', None),
    # Method 3: JSON array in query
    ('JSON array', f'file_tokens={json.dumps([image_token])}'),
]

base_url = 'https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url'

for name, query in tests:
    if query:
        url = f'{base_url}?{query}'
    else:
        url = f'{base_url}?file_tokens={image_token}&file_tokens={image_token}'
    req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
    try:
        resp2 = urllib.request.urlopen(req2)
        data2 = json.loads(resp2.read().decode('utf-8'))
        print(f'{name}: {json.dumps(data2, ensure_ascii=False)[:200]}')
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        print(f'{name}: HTTP {e.code} - {body[:200]}')
    except Exception as e:
        print(f'{name}: {str(e)[:100]}')
