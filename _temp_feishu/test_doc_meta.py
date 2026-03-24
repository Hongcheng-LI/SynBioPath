import json, urllib.request, urllib.error

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

# Get full document metadata
url = f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}'
req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
try:
    resp2 = urllib.request.urlopen(req2)
    data2 = json.loads(resp2.read().decode('utf-8'))
    print('Full doc metadata:')
    print(json.dumps(data2, ensure_ascii=False, indent=2))
except urllib.error.HTTPError as e:
    print('Error:', e.code, e.read().decode('utf-8', errors='replace')[:300])

# Also check wiki node for domain info
wiki_token = 'HBbnwt9AbinTQgkc4mucm3QMn5k'
url3 = f'https://open.feishu.cn/open-apis/wiki/v2/spaces/get_node?token={wiki_token}'
req3 = urllib.request.Request(url3, headers={'Authorization': 'Bearer ' + tenant_token})
try:
    resp3 = urllib.request.urlopen(req3)
    data3 = json.loads(resp3.read().decode('utf-8'))
    print('\nWiki node info:')
    print(json.dumps(data3, ensure_ascii=False, indent=2))
except urllib.error.HTTPError as e:
    print('Wiki error:', e.code, e.read().decode('utf-8', errors='replace')[:300])
