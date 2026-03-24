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

# Try the docx convert API - there's a convert document API
# Let's check if there's an HTML export option
# First, let's try to create export task with various formats
export_url = 'https://open.feishu.cn/open-apis/drive/v1/export_tasks'

# Try HTML format
payload = {
    "type": "docx",
    "token": doc_token,
    "file_extension": "html"
}

req2 = urllib.request.Request(export_url,
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Authorization': 'Bearer ' + tenant_token,
        'Content-Type': 'application/json'
    })
try:
    resp2 = urllib.request.urlopen(req2)
    data2 = json.loads(resp2.read().decode('utf-8'))
    print('HTML export:', json.dumps(data2, ensure_ascii=False, indent=2))
except urllib.error.HTTPError as e:
    print('HTML HTTP Error:', e.code)
    print('Body:', e.read().decode('utf-8', errors='replace')[:500])

# Try docx format (which we know works)
payload2 = {
    "type": "docx",
    "token": doc_token,
    "file_extension": "docx"
}

req3 = urllib.request.Request(export_url,
    data=json.dumps(payload2).encode('utf-8'),
    headers={
        'Authorization': 'Bearer ' + tenant_token,
        'Content-Type': 'application/json'
    })
try:
    resp3 = urllib.request.urlopen(req3)
    data3 = json.loads(resp3.read().decode('utf-8'))
    print('DOCX export:', json.dumps(data3, ensure_ascii=False, indent=2))
except urllib.error.HTTPError as e:
    print('DOCX HTTP Error:', e.code)
    print('Body:', e.read().decode('utf-8', errors='replace')[:500])
