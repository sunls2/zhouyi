import os

DOCS_DIR = "docs/other"

# 获取脚本所在的路径
script_dir = os.path.dirname(os.path.abspath(__file__))
work_dir = os.path.join(script_dir, DOCS_DIR)

content = []
for root, _, files in os.walk(work_dir):
    for file in files:
        if not str(file).endswith(".md"):
            continue
        path = os.path.join(root, file)
        with open(path) as f:
            lines = f.readlines()
        if len(lines) == 0:
            continue
        # 从第7行开始为标题
        desc = lines[6].strip()
        basename = os.path.basename(root)
        content.append(f"|[{basename}](other/{basename}/)|{desc}|")
content.sort()
print("\n".join(content))
