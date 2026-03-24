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

# Get raw_content
url = f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}/raw_content'
req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
resp2 = urllib.request.urlopen(req2)
data2 = json.loads(resp2.read().decode('utf-8'))
content = data2.get('data', {}).get('content', {})

# Check the structure
print('Content type:', type(content))
if isinstance(content, dict):
    print('Keys:', list(content.keys())[:10])
    # Check for image-related keys
    for key in content:
        if 'image' in key.lower() or 'img' in key.lower() or 'media' in key.lower():
            print(f'Found key: {key}')
elif isinstance(content, list):
    print('Content is a list with', len(content), 'items')
    for item in content[:3]:
        print('Item type:', type(item), str(item)[:200])

# Search for image tokens in the raw content string
content_str = json.dumps(content)
img_matches = re.findall(r'token["\':\s]+([a-zA-Z0-9_-]{20,})', content_str)
print('Tokens found:', img_matches[:5])

# Also try to find image URLs
url_matches = re.findall(r'https?://[^\s"\']+', content_str)
print('URLs found:', [u for u in url_matches if 'image' in u.lower() or 'img' in u.lower() or 'feishu' in u.lower()][:5])
