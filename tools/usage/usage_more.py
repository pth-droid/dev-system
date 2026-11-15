"""Second pass: cold starts, per-hour cost, sub-agent totals quoted in notifications. Numbers only."""
import json, re, sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
LOCAL = timezone(timedelta(hours=7))
P = (8, 40, 0.20, 16)  # Fable: input, output, read, write 1h
msgs = {}
agents = set()
with open(sys.argv[1], encoding="utf-8") as fh:
    for line in fh:
        for m in re.finditer(r'total_tokens\D{1,12}(\d+)\D{1,40}?tool_uses\D{1,12}(\d+)\D{1,40}?duration_ms\D{1,12}(\d+)', line):
            agents.add(tuple(int(x) for x in m.groups()))
        o = json.loads(line)
        m = o.get("message") if isinstance(o.get("message"), dict) else None
        if o.get("type") == "assistant" and m and isinstance(m.get("usage"), dict) and o.get("timestamp"):
            t = datetime.fromisoformat(o["timestamp"].replace("Z", "+00:00")).astimezone(LOCAL)
            msgs[m.get("id")] = (t, m["usage"])
rows = sorted(msgs.values(), key=lambda r: r[0])
def usd(u):
    return (u.get("input_tokens", 0) * P[0] + u.get("output_tokens", 0) * P[1]
            + u.get("cache_read_input_tokens", 0) * P[2] + u.get("cache_creation_input_tokens", 0) * P[3]) / 1e6
prev = None
cold = []; big = []
for t, u in rows:
    w = u.get("cache_creation_input_tokens", 0) or 0
    gap = (t - prev).total_seconds() / 60 if prev else 0
    if w > 50_000:
        big.append((t.strftime("%m-%d %H:%M"), round(gap), w, u.get("cache_read_input_tokens", 0)))
    prev = t
print("requests with a cache write above 50k tokens (time, minutes since previous request, written, read):")
tw = 0
for b in big:
    tw += b[2]
    print("  %s  gap %4d min  wrote %9s  read %9s" % (b[0], b[1], f"{b[2]:,}", f"{b[3]:,}"))
allw = sum((u.get("cache_creation_input_tokens", 0) or 0) for _, u in rows)
print("  these %d requests wrote %s of %s tokens (%.0f%% of all writes), USD %.2f" % (len(big), f"{tw:,}", f"{allw:,}", 100 * tw / allw, tw * P[3] / 1e6))
hours = defaultdict(lambda: [0, 0.0, 0])
for t, u in rows:
    k = t.strftime("%m-%d %H")
    hours[k][0] += 1; hours[k][1] += usd(u); hours[k][2] += u.get("output_tokens", 0) or 0
print("\nper hour (local): requests, list-price USD, output tokens")
for k in sorted(hours):
    print("  %s  %4d  %7.2f  %9s" % (k, hours[k][0], hours[k][1], f"{hours[k][2]:,}"))
outs = sorted((u.get("output_tokens", 0) or 0) for _, u in rows)
n = len(outs)
print("\noutput per request: median %d, p90 %d, max %d; top 10%% of requests hold %.0f%% of output" % (
    outs[n // 2], outs[int(n * 0.9)], outs[-1], 100 * sum(outs[int(n * 0.9):]) / sum(outs)))
print("\nsub-agent totals quoted in notifications (total_tokens, tool_uses, minutes):")
s = 0
for a in sorted(agents, key=lambda x: -x[0]):
    s += a[0]
    print("  %10s  %4d  %6.1f" % (f"{a[0]:,}", a[1], a[2] / 60000))
print("  sum", f"{s:,}", "count", len(agents))
