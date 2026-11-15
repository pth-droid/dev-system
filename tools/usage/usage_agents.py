"""Token totals per sub-agent log. Prints numbers and the short task label only, never message content."""
import glob, json, os, sys
from datetime import datetime, timedelta, timezone
LOCAL = timezone(timedelta(hours=7))
PRICE = {"fable": (8, 40, 0.20, 16), "opus": (4, 20, 0.20, 8), "sonnet": (2, 10, 0.10, 4)}
def fam(model):
    m = (model or "").lower()
    for k in ("fable", "opus", "sonnet", "haiku"):
        if k in m:
            return k
    return m or "?"
rows = []
for path in sorted(glob.glob(os.path.join(sys.argv[1], "agent-*.jsonl"))):
    msgs = {}
    for line in open(path, encoding="utf-8"):
        try:
            o = json.loads(line)
        except Exception:
            continue
        m = o.get("message") if isinstance(o.get("message"), dict) else None
        if o.get("type") == "assistant" and m and isinstance(m.get("usage"), dict):
            msgs[m.get("id")] = (o.get("timestamp"), m.get("model"), m["usage"])
    if not msgs:
        continue
    ts = sorted(t for t, _, _ in msgs.values() if t)
    t0 = datetime.fromisoformat(ts[0].replace("Z", "+00:00")).astimezone(LOCAL)
    t1 = datetime.fromisoformat(ts[-1].replace("Z", "+00:00")).astimezone(LOCAL)
    models = sorted({fam(m) for _, m, _ in msgs.values()})
    s = {"in": 0, "out": 0, "read": 0, "write": 0}
    ctx = []
    usd = 0.0
    for _, model, u in msgs.values():
        i = u.get("input_tokens", 0) or 0; o_ = u.get("output_tokens", 0) or 0
        r = u.get("cache_read_input_tokens", 0) or 0; w = u.get("cache_creation_input_tokens", 0) or 0
        s["in"] += i; s["out"] += o_; s["read"] += r; s["write"] += w
        ctx.append(i + r + w)
        p = PRICE.get(fam(model))
        if p:
            usd += (i * p[0] + o_ * p[1] + r * p[2] + w * p[3]) / 1e6
    meta = {}
    mp = path.replace(".jsonl", ".meta.json")
    if os.path.exists(mp):
        try:
            meta = json.load(open(mp, encoding="utf-8"))
        except Exception:
            pass
    label = str(meta.get("description") or meta.get("agentType") or "")[:38]
    rows.append((t0, t1, os.path.basename(path)[6:14], "/".join(models), len(msgs), s, max(ctx), usd, label))
rows.sort()
print("start  end    id        model   reqs      output        read      write   max ctx     USD  label")
T = {"reqs": 0, "out": 0, "read": 0, "write": 0, "usd": 0.0}
for t0, t1, aid, model, n, s, mx, usd, label in rows:
    print("%s  %s  %s  %-6s %5d %11s %11s %10s %9s %7.2f  %s" % (
        t0.strftime("%H:%M"), t1.strftime("%H:%M"), aid, model, n, f"{s['out']:,}", f"{s['read']:,}",
        f"{s['write']:,}", f"{mx:,}", usd, label))
    T["reqs"] += n; T["out"] += s["out"]; T["read"] += s["read"]; T["write"] += s["write"]; T["usd"] += usd
print("TOTAL %d agents, %d requests, output %s, read %s, write %s, list-price USD %.2f" % (
    len(rows), T["reqs"], f"{T['out']:,}", f"{T['read']:,}", f"{T['write']:,}", T["usd"]))
