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
image_token = 'QU9WbBlU8oJZEhxKJnYcevk8nVe'

# Try batch_get_tmp_download_url with the docx document token
base_url = 'https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url'

# Test with document token
for name, token in [('doc_token', doc_token), ('image_token', image_token), ('both', doc_token + ',' + image_token)]:
    url = f'{base_url}?file_tokens={token}'
    req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
    try:
        resp2 = urllib.request.urlopen(req2)
        data2 = json.loads(resp2.read().decode('utf-8'))
        urls = data2.get('data', {}).get('tmp_download_urls', [])
        print(f'{name}: {len(urls)} URLs')
        for u in urls[:3]:
            print(f'  {json.dumps(u, ensure_ascii=False)[:200]}')
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        print(f'{name}: HTTP {e.code} - {body[:200]}')

# Also try docx specific media API - looking at what other docx media endpoints exist
# Check if there is any API that lists media in a docx
url3 = f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}/media'
req3 = urllib.request.Request(url3, headers={'Authorization': 'Bearer ' + tenant_token})
try:
    resp3 = urllib.request.urlopen(req3)
    data3 = json.loads(resp3.read().decode('utf-8'))
    print('media list:', json.dumps(data3, ensure_ascii=False, indent=2)[:1000])
except urllib.error.HTTPError as e:
    body = e.read().decode('utf-8', errors='replace')
    print(f'media list: HTTP {e.code} - {body[:200]}')
except Exception as e:
    print(f'media list: {str(e)[:100]}')
