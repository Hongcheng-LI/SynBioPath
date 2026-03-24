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

# Try to create an export task to export the docx as HTML (which includes images)
# The type field for docx is "docx"
payload = {
    "type": "docx",
    "token": doc_token,
    "file_extension": "html"
}

url = 'https://open.feishu.cn/open-apis/drive/v1/export_tasks'
req2 = urllib.request.Request(url,
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Authorization': 'Bearer ' + tenant_token,
        'Content-Type': 'application/json'
    })
try:
    resp2 = urllib.request.urlopen(req2)
    data2 = json.loads(resp2.read().decode('utf-8'))
    print('Export task created:', json.dumps(data2, ensure_ascii=False, indent=2))
except Exception as e:
    print('Error:', e)
    if hasattr(e, 'read'):
        print(e.read().decode('utf-8', errors='replace')[:500])
