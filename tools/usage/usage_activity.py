"""Split each builder's requests by what the request did. Prints counts and sums only, never content."""
import glob, json, os, re, sys
from collections import defaultdict
TEST = re.compile(r"(^|[\/])tests?[\/]|test_|_test\.|ui_[a-z_]+\.mjs|fixture|spec\.", re.I)
P = (2, 10, 0.10, 4)  # Sonnet: input, output, read, write(1h)
def kind_of(blocks):
    kinds = set()
    for b in blocks:
        n = b.get("name"); i = b.get("input") or {}
        if n in ("Edit", "Write", "NotebookEdit"):
            kinds.add("edit_test" if TEST.search(i.get("file_path", "")) else "edit_code")
        elif n in ("Bash", "PowerShell"):
            c = i.get("command", "")
            kinds.add("run_checks" if re.search(r"pytest|run-tests|ui_\w+\.mjs|node --check|impeccable|bench ", c) else "run_other")
        elif n in ("Read", "Grep", "Glob"):
            kinds.add("read")
        elif n:
            kinds.add("other_tool")
    for k in ("edit_test", "edit_code", "run_checks", "run_other", "read", "other_tool"):
        if k in kinds:
            return k
    return "text_only"
for path in sys.argv[2:]:
    path = os.path.join(sys.argv[1], "agent-%s.jsonl" % path)
    usage = {}; blocks = defaultdict(list); chars = defaultdict(int)
    for line in open(path, encoding="utf-8"):
        o = json.loads(line)
        m = o.get("message") if isinstance(o.get("message"), dict) else None
        if o.get("type") != "assistant" or not m:
            continue
        mid = m.get("id")
        if isinstance(m.get("usage"), dict):
            usage[mid] = m["usage"]
        for b in m.get("content") or []:
            if isinstance(b, dict) and b.get("type") == "tool_use":
                blocks[mid].append(b)
                i = b.get("input") or {}
                if b.get("name") in ("Edit", "Write"):
                    k = "test" if TEST.search(i.get("file_path", "")) else "code"
                    chars[k] += len(i.get("new_string") or i.get("content") or "")
    agg = defaultdict(lambda: [0, 0, 0.0])
    tot = 0.0
    for mid, u in usage.items():
        k = kind_of(blocks.get(mid, []))
        c = ((u.get("input_tokens", 0) or 0) * P[0] + (u.get("output_tokens", 0) or 0) * P[1]
             + (u.get("cache_read_input_tokens", 0) or 0) * P[2] + (u.get("cache_creation_input_tokens", 0) or 0) * P[3]) / 1e6
        agg[k][0] += 1; agg[k][1] += u.get("output_tokens", 0) or 0; agg[k][2] += c; tot += c
    print("\n==", os.path.basename(path)[6:14], "total USD %.2f" % tot)
    for k in ("edit_test", "edit_code", "run_checks", "run_other", "read", "other_tool", "text_only"):
        if k in agg:
            a = agg[k]
            print("  %-11s reqs %4d  output %8s  USD %6.2f  %5.1f%%" % (k, a[0], f"{a[1]:,}", a[2], 100 * a[2] / tot))
    print("  characters written by Edit/Write: test files %s, other files %s" % (f"{chars['test']:,}", f"{chars['code']:,}"))
