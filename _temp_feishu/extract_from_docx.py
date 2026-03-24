#!/usr/bin/env python3
"""
从飞书导出的 DOCX 文件中提取图片，上传到七牛云，并生成带七牛云链接的 Markdown。

使用方法：
1. 在飞书 Web UI 中：文件 -> 导出 -> DOCX
2. 下载 DOCX 文件
3. 运行此脚本：
   python extract_from_docx.py <docx_file> [-o output.md]
"""

import os
import sys
import zipfile
import tempfile
import re
import json
import qiniu
from pathlib import Path

# Qiniu config
QINIU_ACCESS_KEY = "U8xXIpiS0Xvag5U-YzcPKSD5smDAH4wGphVIWX99"
QINIU_SECRET_KEY = ""  # Will try to get from PicGo config
QINIU_BUCKET = "synbiopath-1"
QINIU_DOMAIN = "https://synbiopath.online"


def get_qiniu_auth():
    """从 PicGo 配置获取七牛密钥"""
    picgo_config = os.path.expanduser("~/.picgo/config.json")
    if os.path.exists(picgo_config):
        with open(picgo_config, 'r') as f:
            config = json.load(f)
            # PicGo 可能把配置存在不同位置
            if 'data' in config:
                data = config['data']
                if isinstance(data, dict):
                    # Try qiniu section
                    for section_key in data:
                        section = data[section_key]
                        if isinstance(section, dict) and 'secretKey' in section:
                            return section.get('accessKey'), section.get('secretKey')
    return None, None


def upload_to_qiniu(image_data, filename):
    """上传图片到七牛云"""
    import qiniu

    # Try to get credentials
    access_key = QINIU_ACCESS_KEY
    secret_key = QINIU_SECRET_KEY

    # Try from PicGo if not set
    if not secret_key:
        picgo_access, picgo_secret = get_qiniu_auth()
        if picgo_access and picgo_secret:
            access_key = picgo_access
            secret_key = picgo_secret

    if not secret_key:
        print("Warning: No Qiniu secret key available, will use placeholder URL")
        return f"{QINIU_DOMAIN}/placeholder/{filename}"

    q = qiniu.Auth(access_key, secret_key)
    token = q.upload_token(QINIU_BUCKET)

    key = f"feishu_docx/{filename}"
    ret, info = qiniu.put_data(token, key, image_data)

    if ret is not None:
        return f"{QINIU_DOMAIN}/{key}"
    else:
        print(f"Warning: Upload failed for {filename}, using placeholder")
        return f"{QINIU_DOMAIN}/placeholder/{filename}"


def extract_images_from_docx(docx_path):
    """从 DOCX 文件中提取所有图片"""
    images = []

    with tempfile.TemporaryDirectory() as tmpdir:
        with zipfile.ZipFile(docx_path, 'r') as zf:
            # 列出所有文件
            media_files = [n for n in zf.namelist() if 'word/media/' in n]
            print(f"Found {len(media_files)} images in DOCX")

            for i, media_path in enumerate(media_files):
                # 提取图片
                data = zf.read(media_path)
                ext = os.path.splitext(media_path)[1] or '.png'
                filename = f"image_{i+1}{ext}"
                out_path = os.path.join(tmpdir, filename)

                with open(out_path, 'wb') as f:
                    f.write(data)

                images.append({
                    'index': i + 1,
                    'filename': filename,
                    'data': data,
                    'path': out_path,
                    'original_path': media_path
                })

    return images


def extract_text_from_docx(docx_path):
    """从 DOCX 中提取纯文本（用于参考）"""
    try:
        from docx import Document
        doc = Document(docx_path)
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return paragraphs
    except Exception as e:
        print(f"Error extracting text: {e}")
        return []


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    docx_path = sys.argv[1]
    output_md = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.exists(docx_path):
        print(f"Error: File not found: {docx_path}")
        sys.exit(1)

    print(f"Processing: {docx_path}")

    # 提取图片
    images = extract_images_from_docx(docx_path)

    if not images:
        print("No images found in DOCX")
        sys.exit(1)

    print(f"\nExtracted {len(images)} images")

    # 上传到七牛云
    qiniu_urls = []
    for img in images:
        print(f"  Uploading {img['filename']}...")
        url = upload_to_qiniu(img['data'], img['filename'])
        qiniu_urls.append(url)
        print(f"    -> {url}")

    # 生成报告
    print("\n" + "="*60)
    print("上传完成！图片 URL 列表：")
    print("="*60)
    for i, url in enumerate(qiniu_urls):
        print(f"  image_{i+1}: {url}")

    print("\n" + "="*60)
    print("下一步：")
    print("1. 使用 feishu-docx 工具导出 Markdown")
    print("2. 手动替换图片链接，或告诉我 feishu-docx 输出的文件路径")
    print("="*60)


if __name__ == "__main__":
    main()
