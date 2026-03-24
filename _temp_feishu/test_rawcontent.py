import json, urllib.request, re

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

# Get raw_content and check the actual content string for image references
url = f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}/raw_content'
req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
resp2 = urllib.request.urlopen(req2)
data2 = json.loads(resp2.read().decode('utf-8'))
content_str = data2.get('data', {}).get('content', '')

print('Raw content length:', len(content_str))

# Write to file instead of printing to avoid encoding issues
with open('C:/Software/Data/03-GitHub/SynBioPath/_temp_feishu/raw_content_preview.txt', 'w', encoding='utf-8') as f:
    f.write(content_str[:5000])
print('Written to raw_content_preview.txt')

# Search for image-related patterns
patterns = ['image', 'img', 'token', 'url', 'http', 'pic', 'photo']
for p in patterns:
    idx = content_str.lower().find(p)
    if idx >= 0:
        print(f'Found "{p}" at {idx}: ...{repr(content_str[max(0,idx-20):idx+50])}...')
