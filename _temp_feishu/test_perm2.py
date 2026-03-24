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
data = json.loads(resp.read().decode('utf-8'))
tenant_token = data['tenant_access_token']
print('Token starts with:', tenant_token[:20])

# Test: Try getting tmp_download_url for a known public image token
# Test with a token from feishu2md testdata if available
# Or try other approaches

# 1. Try docx/image download via the correct endpoint
doc_token = 'EIsyd1JZ8oF0koxvQNRc92wFnSh'
image_token = 'QU9WbBlU8oJZEhxKJnYcevk8nVe'

# Try with the correct Feishu API endpoint format
# From Feishu docs: GET /open-apis/docx/v1/documents/{document_id}/images/{image_id}
# But we know this returns 404

# Let's try: maybe we need to use the user access token instead of tenant token?
# Or maybe the issue is that docs:document.media:download needs user token

# Try the drive media direct download with extra param as JSON string
import urllib.parse
extra = json.dumps({"doc_token": doc_token})
encoded_extra = urllib.parse.quote(extra)

tests = [
    # Method 1: direct media download
    (f'Media download (no extra)', f'https://open.feishu.cn/open-apis/drive/v1/medias/{image_token}/download'),
    # Method 2: media download with doc_token in extra
    (f'Media download + extra', f'https://open.feishu.cn/open-apis/drive/v1/medias/{image_token}/download?extra={encoded_extra}'),
    # Method 3: batch_get_tmp_download_url with array format
    (f'Batch URL', f'https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url?file_tokens={image_token}'),
    # Method 4: Try with user access token header
    (f'Media download (user)', f'https://open.feishu.cn/open-apis/drive/v1/medias/{image_token}/download'),
]

print('\n--- Testing with tenant_access_token ---')
for name, url in tests[:3]:
    req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
    try:
        resp2 = urllib.request.urlopen(req2)
        raw = resp2.read()
        print(f'{name}: Status {resp2.status}, Data len: {len(raw)}')
        if len(raw) < 500:
            print(f'  Data: {raw.decode("utf-8", errors="replace")[:200]}')
    except urllib.error.HTTPError as e:
        body = e.read()
        print(f'{name}: HTTP {e.code}, Body: {body.decode("utf-8", errors="replace")[:200]}')

# Try getting user access token - check if the app has user credentials
# Actually, let's check what scope the current token has
print('\n--- Checking token info ---')
url5 = 'https://open.feishu.cn/open-apis/auth/v3/token_info'
req5 = urllib.request.Request(url5, headers={
    'Authorization': 'Bearer ' + tenant_token,
    'Content-Type': 'application/json'
})
try:
    resp5 = urllib.request.urlopen(req5)
    data5 = json.loads(resp5.read().decode('utf-8'))
    print('Token info:', json.dumps(data5, ensure_ascii=False, indent=2))
except urllib.error.HTTPError as e:
    print('Token info error:', e.code, e.read().decode('utf-8', errors='replace')[:200])
except Exception as e:
    print('Error:', str(e))
