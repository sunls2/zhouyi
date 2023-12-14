import os

DOCS_DIR = "docs"

# 获取脚本所在的路径
script_dir = os.path.dirname(os.path.abspath(__file__))
work_dir = os.path.join(script_dir, DOCS_DIR)

content = []
for root, _, files in os.walk(work_dir):
    for file in files:
        if not str(file).endswith(".md"):
            continue
        path = os.path.join(root, file)
        with open(path, "r+") as f:
            lines = f.readlines()
            if len(lines) == 0:
                continue
            if lines[0].startswith("---"):
                continue
            lines.insert(0, "---\nhide:\n  - navigation\n---\n")
            f.seek(0)
            f.writelines(lines)
            f.truncate()
