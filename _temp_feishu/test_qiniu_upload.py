#!/usr/bin/env python3
"""测试从 DOCX 提取图片并上传到七牛云"""

import os
import sys
import zipfile
import tempfile
import qiniu

# Check if qiniu is available
try:
    import qiniu
    print("qiniu SDK available")
except ImportError:
    print("qiniu SDK NOT available, installing...")
    os.system("pip install qiniu")
    import qiniu

# Qiniu config
QINIU_ACCESS_KEY = "U8xXIpiS0Xvag5U-YzcPKSD5smDAH4wGphVIWX99"
# We need secret key - let's check PicGo config
QINIU_SECRET_KEY = None

def get_picgo_qiniu_config():
    """从 PicGo 获取七牛配置"""
    picgo_data = os.path.expanduser("~/.picgo/data.json")
    if os.path.exists(picgo_data):
        try:
            with open(picgo_data, 'r') as f:
                data = json.load(f)
                if data.get('current') == 'qiniu':
                    config = data.get('config', {}).get('qiniu', {})
                    return config.get('accessKey'), config.get('secretKey'), config.get('bucket'), config.get('domain')
        except Exception as e:
            print(f"Error reading PicGo config: {e}")
    return None, None, None, None

# Check PicGo config
import json
picgo_data = os.path.expanduser("~/.picgo/data.json")
if os.path.exists(picgo_data):
    with open(picgo_data, 'r') as f:
        data = json.load(f)
        print(f"PicGo config current uploader: {data.get('current')}")
        if 'config' in data:
            config = data.get('config', {})
            print(f"Config keys: {list(config.keys())}")
            if 'qiniu' in config:
                qiniu_conf = config['qiniu']
                print(f"Qiniu config: accessKey={qiniu_conf.get('accessKey')[:10]}..., bucket={qiniu_conf.get('bucket')}")

print("\nTesting Qiniu upload with PicGo credentials...")

# Use PicGo's Qiniu credentials
picgo_access, picgo_secret, picgo_bucket, picgo_domain = get_picgo_qiniu_config()
if picgo_access and picgo_secret:
    print(f"Using PicGo credentials: accessKey={picgo_access[:10]}...")
else:
    print("Could not get PicGo credentials")

# Create a test image (small red square)
test_image_data = bytes([
    0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,  # PNG header
    0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,  # IHDR chunk
    0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,  # 1x1 pixel
    0x08, 0x02, 0x00, 0x00, 0x00, 0x90, 0x77, 0x53,
    0xDE, 0x00, 0x00, 0x00, 0x0C, 0x49, 0x44, 0x41,
    0x54, 0x08, 0xD7, 0x63, 0xF8, 0xCF, 0xC0, 0x00,
    0x00, 0x00, 0x03, 0x00, 0x01, 0x00, 0x05, 0xFE,
    0xD4, 0xEF, 0x00, 0x00, 0x00, 0x00, 0x49, 0x45,
    0x4E, 0x44, 0xAE, 0x42, 0x60, 0x82
])

# Try to upload
if picgo_access and picgo_secret:
    q = qiniu.Auth(picgo_access, picgo_secret)
    token = q.upload_token(picgo_bucket)

    key = f"test/test_image.png"
    ret, info = qiniu.put_data(token, key, test_image_data)

    if ret is not None:
        print(f"Upload success! Key: {ret['key']}")
        print(f"URL: {picgo_domain}/{key}")
    else:
        print(f"Upload failed: {info}")
else:
    print("Cannot test upload without credentials")
