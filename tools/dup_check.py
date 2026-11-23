#!/usr/bin/env python3
"""Duplikacio-ellenorzo: az uj turak (ids a parancssorban) latnivalo-pontjait veti ossze a tobbi tura pontjaival (<=6 km): kozos pontok, azonos nevek, azonos reptér.
Hasznalat: python3 tools/dup_check.py <tura-id ...>"""
import json, math, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open(os.path.join(ROOT, "data", "tours.json"), encoding="utf-8"))
new = set(sys.argv[1:])
def hav(a, b, c, e):
    p = math.pi / 180
    x = math.sin((c - a) * p / 2) ** 2 + math.cos(a * p) * math.cos(c * p) * math.sin((e - b) * p / 2) ** 2
    return 12742 * math.asin(math.sqrt(x))
def pts(t):
    o = []
    for v in t["variants"]:
        for p in v["pts"]:
            if not isinstance(p, str) and not p[0].startswith("~"):
                o.append((p[0], p[1], p[2], v["id"]))
    return o
def apts(t):
    return {p for v in t["variants"] for p in v["pts"][:1] + v["pts"][-1:] if isinstance(p, str)}
bad = 0
for t in d["tours"]:
    if t["id"] not in new:
        continue
    A = pts(t)
    for u in d["tours"]:
        if u["id"] in new and u["id"] >= t["id"] or u["id"] == t["id"]:
            continue
        B = pts(u)
        sh = set()
        for a in A:
            for b in B:
                if a[0] == b[0] or hav(a[1], a[2], b[1], b[2]) < 6:
                    sh.add((a[0], b[0]))
        ap = apts(t) & apts(u)
        if len(sh) >= 2 or (ap and sh):
            bad += 1
            print("ATFEDES %s <-> %s: %d kozos pont %s reptér=%s" % (t["id"], u["id"], len(sh), sorted(sh)[:4], sorted(ap)))
        elif ap:
            print("  azonos reptér (nincs kozos pont): %s <-> %s %s" % (t["id"], u["id"], sorted(ap)))
print("atfedo parok:", bad)
