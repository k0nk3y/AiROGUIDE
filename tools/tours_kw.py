#!/usr/bin/env python3
"""A turak keresheto kulcsszavait (kw) irja a data/tours.json-ba: a tura latnivaloinak magyar (es egyeb) alias-ai. Futtatas: add_* / tours_order utan."""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from poi_hu import HU
P = os.path.join(ROOT, "data", "tours.json")
d = json.load(open(P, encoding="utf-8"))
miss = set()
for t in d["tours"]:
    names = []
    for v in t["variants"]:
        for p in v["pts"]:
            if not isinstance(p, str) and not p[0].startswith("~") and p[0] not in names:
                names.append(p[0])
    for p in t.get("pois") or []:
        n = p if isinstance(p, str) else p[0]
        if n not in names:
            names.append(n)
    kw = []
    for n in names:
        a = HU.get(n)
        if a is None:
            miss.add(n)
        elif a not in kw:
            kw.append(a)
    t["kw"] = " ".join(kw)
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("kw kesz:", len(d["tours"]), "tura; alias nelkul:", sorted(miss))
