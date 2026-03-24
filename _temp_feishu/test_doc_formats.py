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

# Try raw_content with different format options
test_urls = [
    # Normal raw_content
    (f'Normal raw_content', f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}/raw_content'),
    # Try with text_format parameter
    (f'Text format', f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}/raw_content?text_format=true'),
]

for name, url in test_urls:
    req2 = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + tenant_token})
    try:
        resp2 = urllib.request.urlopen(req2)
        raw = resp2.read()
        data = json.loads(raw.decode('utf-8'))
        content = data.get('data', {}).get('content', '')
        print(f'{name}: content length={len(content)}, type={type(content).__name__}')
        # Check if content looks like HTML
        if '<html' in content.lower() or '<!doctype' in content.lower():
            print('  -> Contains HTML!')
    except urllib.error.HTTPError as e:
        print(f'{name}: HTTP {e.code}')
    except Exception as e:
        print(f'{name}: Error - {e}')

# Also try to get document as HTML via the drive export with docx format then convert
# Or try the document view API
url3 = f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}'
req3 = urllib.request.Request(url3, headers={'Authorization': 'Bearer ' + tenant_token})
try:
    resp3 = urllib.request.urlopen(req3)
    data3 = json.loads(resp3.read().decode('utf-8'))
    print('\nDoc response keys:', list(data3.keys()))
    print('Document keys:', list(data3.get('data', {}).get('document', {}).keys()))
except Exception as e:
    print('Doc error:', e)
