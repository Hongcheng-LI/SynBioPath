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

image_token = 'QU9WbBlU8oJZEhxKJnYcevk8nVe'

# Try the URL that feishu-docx generates
url = f'https://internal-api-drive-stream.feishu.com/space/api/box/stream/download/v2/cover/{image_token}'

# Try with tenant token in Authorization header
req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
try:
    resp2 = urllib.request.urlopen(req2)
    data = resp2.read()
    print(f'Success with Bearer token! Size: {len(data)}')
    with open('C:/Software/Data/03-GitHub/SynBioPath/_temp_feishu/test_feishu_cdn.jpg', 'wb') as f:
        f.write(data)
    print('Saved!')
except urllib.error.HTTPError as e:
    print(f'Bearer Error: {e.code}')
    print('Body:', e.read().decode('utf-8', errors='replace')[:300])

# Try without auth
req3 = urllib.request.Request(url)
try:
    resp3 = urllib.request.urlopen(req3)
    data = resp3.read()
    print(f'Success without auth! Size: {len(data)}')
except urllib.error.HTTPError as e:
    print(f'No-auth Error: {e.code}')
    print('Body:', e.read().decode('utf-8', errors='replace')[:300])

# Try with the feishu.com domain (international)
url4 = f'https://internal-api-drive-stream.feishu.com/space/api/box/stream/download/preview/?token={image_token}&preview_type=16'
req4 = urllib.request.Request(url4)
try:
    resp4 = urllib.request.urlopen(req4)
    data = resp4.read()
    print(f'Preview URL success! Size: {len(data)}')
except urllib.error.HTTPError as e:
    print(f'Preview Error: {e.code}')
    print('Body:', e.read().decode('utf-8', errors='replace')[:300])
