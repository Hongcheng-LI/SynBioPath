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

image_token = 'QU9WbBlU8oJZEhxKJnYcevk8nVe'

# Test 1: batch_get_tmp_download_url
url = f'https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url?file_tokens={image_token}'
req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
try:
    resp2 = urllib.request.urlopen(req2)
    data2 = json.loads(resp2.read().decode('utf-8'))
    print('batch_get_tmp_download_url:', json.dumps(data2, ensure_ascii=False))
    urls = data2.get('data', {}).get('tmp_download_urls', [])
    if urls:
        print('Download URL:', urls[0])
        # Try to download from the temp URL
        download_url = urls[0].get('url')
        if download_url:
            req3 = urllib.request.Request(download_url)
            try:
                resp3 = urllib.request.urlopen(req3)
                img_data = resp3.read()
                print('Image downloaded! Size:', len(img_data))
                # Save to file
                with open('C:/Software/Data/03-GitHub/SynBioPath/_temp_feishu/test_image.jpg', 'wb') as f:
                    f.write(img_data)
                print('Saved to test_image.jpg')
            except Exception as e:
                print('Download error:', e)
except urllib.error.HTTPError as e:
    print('HTTP Error:', e.code, e.read().decode('utf-8', errors='replace')[:300])

# Test 2: direct download
print('\n--- Direct download test ---')
url4 = f'https://open.feishu.cn/open-apis/drive/v1/medias/{image_token}/download'
req4 = urllib.request.Request(url4, headers={'Authorization': 'Bearer ' + tenant_token})
try:
    resp4 = urllib.request.urlopen(req4)
    img_data4 = resp4.read()
    print('Direct download success! Size:', len(img_data4))
    with open('C:/Software/Data/03-GitHub/SynBioPath/_temp_feishu/test_image_direct.jpg', 'wb') as f:
        f.write(img_data4)
    print('Saved to test_image_direct.jpg')
except urllib.error.HTTPError as e:
    print('HTTP Error:', e.code)
    print('Body:', e.read().decode('utf-8', errors='replace')[:300])
