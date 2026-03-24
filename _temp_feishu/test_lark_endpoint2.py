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

# Try with open.larksuite.com but with feishu.cn auth
# The tenant_token from feishu.cn won't work with larksuite.com
# But let's check what data we got
internal_url2 = f'https://open.larksuite.com/space/api/box/stream/download/preview/?token={image_token}&preview_type=16'
req3 = urllib.request.Request(internal_url2, headers={
    'Authorization': 'Bearer ' + tenant_token,
    'Content-Type': 'application/json'
})
try:
    resp3 = urllib.request.urlopen(req3)
    data3 = resp3.read()
    print('Size:', len(data3))
    print('First 200 bytes:', data3[:200])
    # Check if it's an error JSON
    try:
        err_data = json.loads(data3.decode('utf-8'))
        print('JSON response:', json.dumps(err_data, ensure_ascii=False)[:300])
    except:
        print('Not JSON, might be binary image')
        with open('C:/Software/Data/03-GitHub/SynBioPath/_temp_feishu/test_larksuite.jpg', 'wb') as f:
            f.write(data3)
        print('Saved to test_larksuite.jpg')
except urllib.error.HTTPError as e:
    print('HTTP Error:', e.code)
    print('Body:', e.read().decode('utf-8', errors='replace')[:300])
except Exception as e:
    print('Error:', str(e)[:100])
