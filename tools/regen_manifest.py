"""Recompute bytes/sha256 for every file listed in MANIFEST.json, set the version, check internal links.
usage: python -X utf8 regen_manifest.py <package dir> <version>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
version = sys.argv[2]
mpath = root / "MANIFEST.json"
m = json.loads(mpath.read_text(encoding="utf-8"))
changed = []
for rel, meta in m["files"].items():
    data = (root / rel).read_bytes()
    new = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    if new != {"bytes": meta.get("bytes"), "sha256": meta.get("sha256")}:
        changed.append(rel)
    meta.update(new)
m["version"] = version
mpath.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("version", version, "files", len(m["files"]), "changed", changed)

links = broken = 0
for rel in m["files"]:
    if not rel.endswith(".md"):
        continue
    text = (root / rel).read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
        if re.match(r"[a-z]+://", target):
            continue
        links += 1
        if not ((root / rel).parent / target).exists():
            broken += 1
            print("BROKEN", rel, "->", target)
print("links", links, "broken", broken)
