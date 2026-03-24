import json
from feishu_docx import FeishuExporter

# Read credentials
with open('C:/Users/lhc/.newmax/skills/feishu-doc-reader/reference/feishu_config.json', 'r') as f:
    config = json.load(f)

app_id = config['app_id']
app_secret = config['app_secret']

# Initialize exporter
exporter = FeishuExporter(app_id=app_id, app_secret=app_secret)

# Try to export the document to a temp directory
wiki_url = "https://synbiopath.feishu.cn/wiki/HBbnwt9AbinTQgkc4mucm3QMn5k"
output_dir = "C:/Software/Data/03-GitHub/SynBioPath/_temp_feishu/feishu_docx_output"

try:
    result = exporter.export(wiki_url, output_dir)
    print('Export result:', result)
except Exception as e:
    print('Export error:', e)
    import traceback
    traceback.print_exc()
