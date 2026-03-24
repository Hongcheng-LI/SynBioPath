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
doc_token = 'EIsyd1JZ8oF0koxvQNRc92wFnSh'

# Try the internal endpoint used by lark-doc-scraper
# /space/api/box/stream/download/preview/
internal_url = f'https://feishu.cn/space/api/box/stream/download/preview/?token={image_token}&preview_type=16'
req2 = urllib.request.Request(internal_url, headers={
    'Authorization': 'Bearer ' + tenant_token,
    'Content-Type': 'application/json'
})
try:
    resp2 = urllib.request.urlopen(req2)
    data2 = resp2.read()
    print('Internal endpoint success! Size:', len(data2))
    with open('C:/Software/Data/03-GitHub/SynBioPath/_temp_feishu/test_internal.jpg', 'wb') as f:
        f.write(data2)
    print('Saved to test_internal.jpg')
except urllib.error.HTTPError as e:
    print('Internal endpoint HTTP Error:', e.code)
    print('Body:', e.read().decode('utf-8', errors='replace')[:300])
except Exception as e:
    print('Internal endpoint error:', str(e)[:100])

# Also try the lark international version
internal_url2 = f'https://open.larksuite.com/space/api/box/stream/download/preview/?token={image_token}&preview_type=16'
req3 = urllib.request.Request(internal_url2, headers={
    'Authorization': 'Bearer ' + tenant_token,
    'Content-Type': 'application/json'
})
try:
    resp3 = urllib.request.urlopen(req3)
    data3 = resp3.read()
    print('Lark internal endpoint success! Size:', len(data3))
except urllib.error.HTTPError as e:
    print('Lark internal endpoint HTTP Error:', e.code)
    print('Body:', e.read().decode('utf-8', errors='replace')[:300])
except Exception as e:
    print('Lark internal endpoint error:', str(e)[:100])
