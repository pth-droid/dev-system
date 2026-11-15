"""Recompute bytes/sha256 for every file listed in MANIFEST.json, set the version, check internal links.

usage: python -X utf8 regen_manifest.py <package dir> <version>
       python -X utf8 regen_manifest.py <package dir> --check

--check is the verification step: it never writes. It exits 1 when a listed
file is missing, a byte count or hash differs, or an internal link is broken.
Regeneration also exits 1 without writing when a listed file is missing or a
link is broken, so a broken package never becomes the new canonical manifest.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
check_only = sys.argv[2] == "--check"
mpath = root / "MANIFEST.json"
m = json.loads(mpath.read_text(encoding="utf-8"))

missing, changed, fresh = [], [], {}
for rel, meta in m["files"].items():
    path = root / rel
    if not path.is_file():
        missing.append(rel)
        print("MISSING", rel)
        continue
    data = path.read_bytes()
    new = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    if new != {"bytes": meta.get("bytes"), "sha256": meta.get("sha256")}:
        changed.append(rel)
    fresh[rel] = new

links = broken = 0
for rel in m["files"]:
    if not rel.endswith(".md") or rel in missing:
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

if check_only:
    for rel in changed:
        print("MISMATCH", rel)
    ok = not (missing or changed or broken)
    print("check", "PASS" if ok else "FAIL", "missing", len(missing),
          "mismatch", len(changed), "broken", broken)
    sys.exit(0 if ok else 1)

if missing or broken:
    print("REFUSED: manifest not written; fix missing files and broken links first")
    sys.exit(1)

for rel, new in fresh.items():
    m["files"][rel].update(new)
m["version"] = sys.argv[2]
mpath.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("version", m["version"], "files", len(m["files"]), "changed", changed)
