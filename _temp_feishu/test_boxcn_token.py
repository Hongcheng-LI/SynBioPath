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

# Test with a boxcn token from feishu2md test data
boxcn_token = 'boxcnbK20aJ9pePyziodIvjXTce'

# Test batch_get_tmp_download_url
url = f'https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url?file_tokens={boxcn_token}'
req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
try:
    resp2 = urllib.request.urlopen(req2)
    data2 = json.loads(resp2.read().decode('utf-8'))
    print('batch_get_tmp_download_url:', json.dumps(data2, ensure_ascii=False))
except urllib.error.HTTPError as e:
    print('batch HTTP Error:', e.code, e.read().decode('utf-8', errors='replace')[:200])

# Test direct download
url3 = f'https://open.feishu.cn/open-apis/drive/v1/medias/{boxcn_token}/download'
req3 = urllib.request.Request(url3, headers={'Authorization': 'Bearer ' + tenant_token})
try:
    resp3 = urllib.request.urlopen(req3)
    data3 = resp3.read()
    print('Direct download success! Size:', len(data3))
    with open('C:/Software/Data/03-GitHub/SynBioPath/_temp_feishu/test_boxcn.jpg', 'wb') as f:
        f.write(data3)
    print('Saved to test_boxcn.jpg')
except urllib.error.HTTPError as e:
    print('Direct HTTP Error:', e.code, e.read().decode('utf-8', errors='replace')[:200])
