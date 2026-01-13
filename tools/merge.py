import os
import re

SRC_DIR = "src"
OUT_FILE = "build/game.bf"

include_pattern = re.compile(r"<include\s+(.+?)>")

def load_file(path, visited=None):
    if visited is None:
        visited = set()

    full_path = os.path.normpath(path)
    if full_path in visited:
        raise RuntimeError(f"Circular include detected: {full_path}")
    visited.add(full_path)

    with open(full_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output = []
    for line in lines:
        match = include_pattern.search(line)
        if match:
            inc = match.group(1).strip()
            inc_path = os.path.join(SRC_DIR, inc)
            output.append(load_file(inc_path, visited))
        else:
            output.append(line)

    return "".join(output)

os.makedirs("build", exist_ok=True)
merged = load_file(os.path.join(SRC_DIR, "main.bf"))

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(merged)

print(f"[merge] wrote {OUT_FILE}")
