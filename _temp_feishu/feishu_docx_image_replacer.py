#!/usr/bin/env python3
"""
从飞书导出的 DOCX 中提取图片，上传到七牛云，并替换 Markdown 中的图片链接。

工作流程：
1. 运行 feishu-docx 导出飞书文档为 Markdown（会生成飞书 CDN 图片链接）
2. 用户从飞书 Web UI 导出同一文档为 DOCX
3. 运行此脚本，传入 DOCX 文件路径和 Markdown 文件路径
4. 脚本从 DOCX 提取图片，上传到七牛云，并替换 Markdown 中的链接

使用方法：
python feishu_docx_image_replacer.py <docx_file> <markdown_file> [-o output.md]
"""

import os
import sys
import json
import re
import zipfile
import tempfile
import qiniu
from pathlib import Path

# Qiniu credentials from PicGo
QINIU_ACCESS_KEY = "U8xXIpiS0Xvag5U-YzcPKSD5smDAH4wGphVIWX99"
QINIU_SECRET_KEY = "YXNOktuDay555JUDTJv2sU_rV6agqUVX3jGZbdZt"
QINIU_BUCKET = "synbiopath-1"
QINIU_DOMAIN = "https://synbiopath.online"


def upload_to_qiniu(image_data, filename):
    """上传图片到七牛云"""
    q = qiniu.Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)
    token = q.upload_token(QINIU_BUCKET)

    key = f"feishu_docx/{filename}"
    ret, info = qiniu.put_data(token, key, image_data)

    if ret is not None:
        return f"{QINIU_DOMAIN}/{key}"
    else:
        print(f"Warning: Upload failed for {filename}: {info}")
        return None


def extract_images_from_docx(docx_path):
    """从 DOCX 文件中提取所有图片，按顺序返回"""
    images = []

    with tempfile.TemporaryDirectory() as tmpdir:
        with zipfile.ZipFile(docx_path, 'r') as zf:
            media_files = sorted([n for n in zf.namelist() if 'word/media/' in n])
            print(f"Found {len(media_files)} images in DOCX")

            for i, media_path in enumerate(media_files):
                data = zf.read(media_path)
                ext = os.path.splitext(media_path)[1] or '.png'
                filename = f"image_{i+1}{ext}"

                images.append({
                    'index': i + 1,
                    'filename': filename,
                    'data': data,
                })

    return images


def extract_feishu_image_urls(markdown_content):
    """从 Markdown 中提取所有飞书 CDN 图片 URL"""
    pattern = r'!\[image\]\((https://internal-api-drive-stream\.feishu\.com/space/api/box/stream/download/v2/cover/[^)]+)\)'
    urls = re.findall(pattern, markdown_content)
    return urls


def replace_image_urls(markdown_content, qiniu_urls):
    """替换 Markdown 中的图片 URL 为七牛云 URL"""
    # 找到所有飞书 CDN URL 并按顺序替换
    pattern = r'!\[image\]\(https://internal-api-drive-stream\.feishu\.com/space/api/box/stream/download/v2/cover/[^)]+\)'

    def replace_func(match):
        if qiniu_urls:
            url = qiniu_urls.pop(0)
            return f'![]({url})'
        return match.group(0)

    result = re.sub(pattern, replace_func, markdown_content)
    return result


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    docx_path = sys.argv[1]
    md_path = sys.argv[2]
    output_md = sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == '-o' else None

    if not os.path.exists(docx_path):
        print(f"Error: DOCX file not found: {docx_path}")
        sys.exit(1)

    if not os.path.exists(md_path):
        print(f"Error: Markdown file not found: {md_path}")
        sys.exit(1)

    # 读取 Markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 提取飞书 CDN URL
    feishu_urls = extract_feishu_image_urls(md_content)
    print(f"Found {len(feishu_urls)} feishu CDN URLs in Markdown")

    if not feishu_urls:
        print("No feishu CDN URLs found in Markdown. Nothing to replace.")
        sys.exit(0)

    # 从 DOCX 提取图片
    images = extract_images_from_docx(docx_path)
    print(f"Extracted {len(images)} images from DOCX")

    if len(images) != len(feishu_urls):
        print(f"Warning: Number of images in DOCX ({len(images)}) doesn't match number of URLs in Markdown ({len(feishu_urls)})")

    # 上传到七牛云
    qiniu_urls = []
    print("\nUploading to Qiniu...")
    for img in images:
        print(f"  [{img['index']}] Uploading {img['filename']}...")
        url = upload_to_qiniu(img['data'], img['filename'])
        if url:
            qiniu_urls.append(url)
            print(f"       -> {url}")
        else:
            print(f"       -> FAILED")

    # 替换 Markdown 中的 URL
    print("\nReplacing URLs in Markdown...")
    new_md_content = replace_image_urls(md_content, qiniu_urls.copy())

    # 保存结果
    if output_md is None:
        output_md = md_path.replace('.md', '_qiniu.md')

    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(new_md_content)

    print(f"\nDone! Output saved to: {output_md}")
    print(f"Replaced {min(len(images), len(feishu_urls))} image URLs")


if __name__ == "__main__":
    main()
