"""Token profile of one Claude Code session transcript. Prints numbers only, never message content.
usage: python -X utf8 usage_profile.py <transcript.jsonl>
"""
import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone

path = sys.argv[1]
LOCAL = timezone(timedelta(hours=7))
# USD per million tokens: input, output, cache read, cache write 5m, cache write 1h
PRICE = {
    "fable": (8, 40, 0.20, 10, 16),
    "opus": (4, 20, 0.20, 5, 8),
    "sonnet": (2, 10, 0.10, 2.5, 4),
}


def family(model):
    m = (model or "").lower()
    for k in PRICE:
        if k in m:
            return k
    return m or "unknown"


msgs = {}          # message id -> (model, day, usage)
agent_results = []  # sub-agent totals reported back in tool results
result_keys = defaultdict(int)
lines = bad = 0
with open(path, encoding="utf-8") as fh:
    for line in fh:
        lines += 1
        try:
            o = json.loads(line)
        except Exception:
            bad += 1
            continue
        m = o.get("message") if isinstance(o.get("message"), dict) else None
        if o.get("type") == "assistant" and m and isinstance(m.get("usage"), dict):
            ts = o.get("timestamp") or ""
            try:
                day = datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(LOCAL).strftime("%m-%d")
            except Exception:
                day = "?"
            msgs[m.get("id") or lines] = (m.get("model"), day, m["usage"], bool(o.get("isSidechain")))
        r = o.get("toolUseResult")
        if isinstance(r, dict):
            for k in r:
                result_keys[k] += 1
            if "totalTokens" in r:
                agent_results.append(r)

print("lines", lines, "unparsed", bad, "assistant requests", len(msgs))

tot = defaultdict(lambda: defaultdict(float))
by_day = defaultdict(lambda: defaultdict(float))
ctx = []
for mid, (model, day, u, side) in msgs.items():
    fam = family(model) + ("/sidechain" if side else "")
    cc = u.get("cache_creation") or {}
    w1h = cc.get("ephemeral_1h_input_tokens", 0) or 0
    w5m = cc.get("ephemeral_5m_input_tokens", 0) or 0
    wtot = u.get("cache_creation_input_tokens", 0) or 0
    if not (w1h or w5m):
        w1h = wtot
    vals = {
        "requests": 1,
        "input": u.get("input_tokens", 0) or 0,
        "write_1h": w1h,
        "write_5m": w5m,
        "read": u.get("cache_read_input_tokens", 0) or 0,
        "output": u.get("output_tokens", 0) or 0,
    }
    for k, v in vals.items():
        tot[fam][k] += v
        by_day[day][k] += v
    p = PRICE.get(family(model))
    if p:
        usd = (vals["input"] * p[0] + vals["output"] * p[1] + vals["read"] * p[2]
               + vals["write_5m"] * p[3] + vals["write_1h"] * p[4]) / 1e6
        tot[fam]["usd"] += usd
        by_day[day]["usd"] += usd
        for k, price in (("input", p[0]), ("output", p[1]), ("read", p[2]), ("write_5m", p[3]), ("write_1h", p[4])):
            tot[fam]["usd_" + k] += vals[k] * price / 1e6
    if not side:
        ctx.append(vals["input"] + vals["read"] + vals["write_1h"] + vals["write_5m"])

for fam, t in tot.items():
    print("\n==", fam)
    for k in ("requests", "input", "write_1h", "write_5m", "read", "output"):
        print("  %-9s %15s" % (k, f"{int(t[k]):,}"))
    if t.get("usd"):
        print("  list-price USD %.2f" % t["usd"])
        for k in ("input", "output", "read", "write_5m", "write_1h"):
            print("    %-9s %8.2f  %5.1f%%" % (k, t["usd_" + k], 100 * t["usd_" + k] / t["usd"]))

print("\n== by local day (requests, output, read, write_1h, USD)")
for day in sorted(by_day):
    d = by_day[day]
    print("  %s %6d %12s %15s %12s %8.2f" % (day, d["requests"], f"{int(d['output']):,}", f"{int(d['read']):,}",
                                              f"{int(d['write_1h']):,}", d.get("usd", 0)))

if ctx:
    ctx.sort()
    n = len(ctx)
    print("\n== context per main-session request: median %s, p90 %s, max %s" % (
        f"{ctx[n // 2]:,}", f"{ctx[int(n * 0.9)]:,}", f"{ctx[-1]:,}"))
    big = sum(1 for c in ctx if c > 500_000)
    print("   requests above 500k context: %d of %d" % (big, n))

print("\n== tool result keys that look like sub-agent totals")
for k in ("totalTokens", "totalToolUseCount", "totalDurationMs", "usage", "agentId", "model", "status"):
    print("  ", k, result_keys.get(k, 0))
print("sub-agent results with totalTokens:", len(agent_results))
tt = 0
for r in agent_results:
    u = r.get("usage") or {}
    tt += r.get("totalTokens", 0) or 0
    print("   total %10s  tools %4s  min %6.1f  out %9s  read %12s  write %10s  in %8s" % (
        f"{r.get('totalTokens', 0):,}", r.get("totalToolUseCount", "?"),
        (r.get("totalDurationMs", 0) or 0) / 60000,
        f"{u.get('output_tokens', 0):,}", f"{u.get('cache_read_input_tokens', 0):,}",
        f"{u.get('cache_creation_input_tokens', 0):,}", f"{u.get('input_tokens', 0):,}"))
print("sum of sub-agent totalTokens:", f"{tt:,}")
