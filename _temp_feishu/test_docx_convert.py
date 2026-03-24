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

# Try the docx convert API to convert docx to other formats
convert_url = f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}/convert'

# Try HTML format
payload = {
    "target_type": "html"
}

req2 = urllib.request.Request(convert_url,
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Authorization': 'Bearer ' + tenant_token,
        'Content-Type': 'application/json'
    })
try:
    resp2 = urllib.request.urlopen(req2)
    data2 = json.loads(resp2.read().decode('utf-8'))
    print('Convert to HTML:', json.dumps(data2, ensure_ascii=False, indent=2))
except urllib.error.HTTPError as e:
    print('Convert HTTP Error:', e.code)
    print('Body:', e.read().decode('utf-8', errors='replace')[:500])

# Also try the raw_content with text_format to see if it includes image URLs
url3 = f'https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}/raw_content'
req3 = urllib.request.Request(url3, headers={'Authorization': 'Bearer ' + tenant_token})
try:
    resp3 = urllib.request.urlopen(req3)
    data3 = json.loads(resp3.read().decode('utf-8'))
    content = data3.get('data', {}).get('content', '')
    print('\nRaw content length:', len(content))
    # Check if content has any URL references
    import re
    urls = re.findall(r'https?://[^\s\'"]+', content)
    print('URLs found in raw_content:', len(urls))
    for u in urls[:5]:
        print(' ', u[:100])
except Exception as e:
    print('Raw content error:', e)
