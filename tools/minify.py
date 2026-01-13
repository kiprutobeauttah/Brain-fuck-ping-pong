BF_CHARS = set("+-<>[],.")

with open("build/game.bf", "r", encoding="utf-8") as f:
    src = f.read()

minified = "".join(c for c in src if c in BF_CHARS)

with open("build/game.min.bf", "w", encoding="utf-8") as f:
    f.write(minified)

print(f"[minify] reduced {len(src)} → {len(minified)} chars")
