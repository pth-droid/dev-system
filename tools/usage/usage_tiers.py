"""Replay builder requests under tiered prices. Assumption for every model: cache read = 0.05 x input, cache write = 2 x input."""
import json, os, sys
M = {  # name: (threshold, in_lo, out_lo, in_hi, out_hi)
    "Sonnet 5.5": (None, 2, 10, 2, 10),
    "Haiku 5.5": (100_000, 0.10, 0.50, 0.50, 2.50),
    "Sol 6.1": (272_000, 2, 10, 4, 15),
    "Terra 6.1": (272_000, 1, 5, 2, 7.5),
}
def cost(reqs, m, force_low=False):
    th, il, ol, ih, oh = M[m]; c = 0.0
    for i, o, r, w in reqs:
        hi = (th is not None) and (i + r + w > th) and not force_low
        pi, po = (ih, oh) if hi else (il, ol)
        c += (i * pi + r * pi * 0.05 + w * pi * 2 + o * po) / 1e6
    return c
allreq = []
for aid, label in (("ae4a32b7122cc5f45", "J201"), ("a5b4ea727ae41f681", "J204"), ("a379ce59ce2b6230c", "J202")):
    us = {}
    for line in open(os.path.join(sys.argv[1], "agent-%s.jsonl" % aid), encoding="utf-8"):
        o = json.loads(line); m = o.get("message") if isinstance(o.get("message"), dict) else None
        if o.get("type") == "assistant" and m and isinstance(m.get("usage"), dict):
            u = m["usage"]
            us[m.get("id")] = (u.get("input_tokens", 0) or 0, u.get("output_tokens", 0) or 0,
                               u.get("cache_read_input_tokens", 0) or 0, u.get("cache_creation_input_tokens", 0) or 0)
    reqs = list(us.values()); allreq += reqs
    ctx = sorted(i + r + w for i, o, r, w in reqs); n = len(ctx)
    print("%s: %d requests, context median %s, first %s; above 100K: %d (%.0f%%), above 272K: %d (%.0f%%)" % (
        label, n, f"{ctx[n//2]:,}", f"{(reqs[0][0]+reqs[0][2]+reqs[0][3]):,}",
        sum(c > 100_000 for c in ctx), 100 * sum(c > 100_000 for c in ctx) / n,
        sum(c > 272_000 for c in ctx), 100 * sum(c > 272_000 for c in ctx) / n))
print("\nall three builders, %d requests: USD as run / if every request stayed under the threshold" % len(allreq))
for m in M:
    print("  %-11s %6.2f / %6.2f" % (m, cost(allreq, m), cost(allreq, m, True)))
