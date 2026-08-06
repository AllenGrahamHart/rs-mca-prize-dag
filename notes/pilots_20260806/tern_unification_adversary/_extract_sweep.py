import json, sys
src = "/home/u2470931/.claude/projects/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/tool-results/toolu_01C6C3y68wJgCNAkmBSBAvwj.json"
with open(src) as f:
    d = json.load(f)
parts = []
def walk(o):
    if isinstance(o, dict):
        if o.get("type") == "text" and isinstance(o.get("text"), str):
            parts.append(o["text"])
        else:
            for v in o.values(): walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
walk(d)
out = "\n\n".join(parts)
dst = "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/tern_unification_adversary/_sweep_raw.md"
with open(dst, "w") as f:
    f.write(out)
print("wrote", dst, len(out), "chars", out.count("\n")+1, "lines")
