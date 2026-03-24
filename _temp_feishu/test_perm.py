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

# Check if the docx image token could be a drive file
# Try batch meta query with the image token
image_token = 'QU9WbBlU8oJZEhxKJnYcevk8nVe'
doc_token = 'EIsyd1JZ8oF0koxvQNRc92wFnSh'

# batch_query_meta
url = 'https://open.feishu.cn/open-apis/drive/v1/files/batch_query_meta'
payload = {"request_docs": [{"doc_token": doc_token, "docs": [{"doc_id": image_token}]}]}
req2 = urllib.request.Request(url,
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Authorization': 'Bearer ' + tenant_token,
        'Content-Type': 'application/json'
    })
try:
    resp2 = urllib.request.urlopen(req2)
    data2 = json.loads(resp2.read().decode('utf-8'))
    print('batch_query_meta:', json.dumps(data2, ensure_ascii=False, indent=2)[:1000])
except urllib.error.HTTPError as e:
    print('HTTP Error:', e.code)
    print('Body:', e.read().decode('utf-8', errors='replace')[:500])
except Exception as e:
    print('Error:', str(e)[:200])

# Also try the docx blocks API with a user token approach - use the wiki owner info
# Let's try to get the document meta to see owner
url3 = f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}'
req3 = urllib.request.Request(url3, headers={'Authorization': 'Bearer ' + tenant_token})
try:
    resp3 = urllib.request.urlopen(req3)
    data3 = json.loads(resp3.read().decode('utf-8'))
    print('Doc meta:', json.dumps(data3, ensure_ascii=False, indent=2)[:500])
except Exception as e:
    print('Error doc meta:', e)
    if hasattr(e, 'read'):
        print(e.read().decode('utf-8', errors='replace')[:300])
