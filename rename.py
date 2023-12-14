import os
import re


def replace_links(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    # content = re.sub(r'(/[^/]+\.md/)', '/', content)
    content = re.sub(r'(\.\./)(\d)(\.)', r'\g<1>0\2\3', content)
    with open(file_path, 'w') as f:
        f.write(content)


TARGET_NAME = "index.md"
DOCS_DIR = "docs"

# 获取脚本所在的路径
script_dir = os.path.dirname(os.path.abspath(__file__))
work_dir = os.path.join(script_dir, DOCS_DIR)

# 遍历目录中的文件
for root, _, files in os.walk(work_dir):
    sp = str(root).split(".")
    if len(sp) == 2:
        dirname = os.path.dirname(sp[0])
        basename = os.path.basename(sp[0])
        if len(str(basename)) == 1:
            # 1 => 01 2 => 02
            basename = f"0{basename}.{sp[1]}"
            os.rename(root, os.path.join(dirname, basename))

    for file in files:
        if not file.endswith(".md"):
            continue
        path = os.path.join(root, file)
        replace_links(path)
        if file == TARGET_NAME:
            continue
        new_file = os.path.join(root, TARGET_NAME)
        os.rename(path, new_file)

print('done')
