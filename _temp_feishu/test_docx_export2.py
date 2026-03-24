import json, urllib.request, urllib.error, time

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

# Try the docx export task - let's check if it needs additional permissions
export_url = 'https://open.feishu.cn/open-apis/drive/v1/export_tasks'

# First try docx export
payload = {
    "type": "docx",
    "token": doc_token,
    "file_extension": "docx"
}

req2 = urllib.request.Request(export_url,
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Authorization': 'Bearer ' + tenant_token,
        'Content-Type': 'application/json'
    })
try:
    resp2 = urllib.request.urlopen(req2)
    data2 = json.loads(resp2.read().decode('utf-8'))
    print('Export task created:', json.dumps(data2, ensure_ascii=False, indent=2))

    # Get the task token and poll for completion
    task_token = data2.get('data', {}).get('task', {}).get('token')
    if task_token:
        print(f'Task token: {task_token}')
        # Poll for task completion
        for i in range(10):
            time.sleep(2)
            status_url = f'https://open.feishu.cn/open-apis/drive/v1/export_tasks/{task_token}'
            req3 = urllib.request.Request(status_url, headers={'Authorization': 'Bearer ' + tenant_token})
            try:
                resp3 = urllib.request.urlopen(req3)
                status_data = json.loads(resp3.read().decode('utf-8'))
                task = status_data.get('data', {}).get('task', {})
                print(f'Poll {i+1}: status={task.get("job_status")}, code={status_data.get("code")}')
                if task.get('job_status') == 2:  # Done
                    print('Export complete!')
                    print('Result:', json.dumps(status_data, ensure_ascii=False, indent=2))
                    break
                elif task.get('job_status') == 3:  # Failed
                    print('Export failed:', task.get('job_error_msg'))
                    break
            except Exception as e:
                print(f'Status poll error: {e}')
except urllib.error.HTTPError as e:
    print('Export HTTP Error:', e.code)
    print('Body:', e.read().decode('utf-8', errors='replace')[:500])
