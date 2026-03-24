import json, urllib.request, urllib.parse

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
image_token = 'QU9WbBlU8oJZEhxKJnYcevk8nVe'
block_id = 'CJv6dzY6qoHPHsxlNyvcQkBfnxd'

# Try extra as JSON string
extra_json = json.dumps({"doc_token": doc_token, "block_id": block_id})
encoded_extra = urllib.parse.quote(extra_json)

url = f'https://open.feishu.cn/open-apis/drive/v1/medias/{image_token}/download?extra={encoded_extra}'
req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
try:
    resp2 = urllib.request.urlopen(req2)
    print('Status:', resp2.status)
    data2 = resp2.read()
    print('Data length:', len(data2))
    print('Content-Type:', resp2.headers.get('Content-Type'))
except urllib.error.HTTPError as e:
    print('HTTP Error:', e.code)
    print('Body:', e.read().decode('utf-8', errors='replace')[:300])
except Exception as e:
    print('Error:', str(e)[:100])
