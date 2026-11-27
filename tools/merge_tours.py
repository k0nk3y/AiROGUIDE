#!/usr/bin/env python3
"""Egyszeri osszevonas: a STOL-turak utvonalai a velük azonos teruletu alap-tura variansai lesznek.
Futtatas: python3 tools/merge_tours.py   (ujrafuttatva nem csinal semmit). Kiirja az app.py-ba illeszto TOUR_MERGE szotarat."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "tours.json")
MERGE = [("everest", "stol-lukla", False), ("denali", "stol-kantishna", True), ("tenerife", "stol-la-gomera", True),
         ("belize-blue-hole", "stol-belize-bluehole", True), ("lake-malawi", "stol-lake-malawi", True), ("exumas", "stol-staniel", True),
         ("orkney", "stol-orkney", True), ("lord-howe", "stol-lord-howe", True), ("jungfrau", "stol-gstaad", True),
         ("milford-sound", "stol-milford", True), ("barra-st-kilda", "stol-barra", True), ("lofoten", "stol-roest", True),
         ("okavango", "stol-okavango-kiri", True), ("mccarthy", "stol-wrangell", True), ("iceland-south", "stol-heimaey", True),
         ("oahu", "stol-molokai", True), ("cornwall", "stol-scilly", True)]   # 3. elem: a STOL-tura utvonala megmarad (False = az alap-tura mar tartalmazza, elhagyjuk)
d = json.load(open(P, encoding="utf-8"))
T = {t["id"]: t for t in d["tours"]}
out = {}
for base, st, keep in MERGE:
    if st not in T:
        continue
    b, s = T[base], T[st]
    vids = {v["id"] for v in b["variants"]}
    for v in s["variants"]:
        if not keep:
            out[st + "/" + v["id"]] = None
            continue
        nid = st.replace("stol-", "", 1) if len(s["variants"]) == 1 else st.replace("stol-", "", 1) + "-" + v["id"]
        while nid in vids:
            nid += "x"
        vids.add(nid)
        out[st + "/" + v["id"]] = base + "/" + nid
        v["id"] = nid
        v["stol"] = True
        b["variants"].append(v)
    names = {p[0] for p in b.get("pois", [])}
    for p in s.get("pois", []):
        if p[0] not in names:
            b.setdefault("pois", []).append(p)
    for g in s.get("tags", []):
        if g not in b["tags"] and g != "stol":
            b["tags"].append(g)
    b["kw"] = (b.get("kw", "") + " " + s.get("kw", "")).strip()
    if s.get("new") and keep:
        b["new"] = True
    out[st] = base
    d["tours"] = [t for t in d["tours"] if t["id"] != st]
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
# a tools/fixed_order.txt sorrendfajl azonositoi
fo = os.path.join(ROOT, "tools", "fixed_order.txt")
L = open(fo, encoding="utf-8").read().split("\n")
res = []
for ln in L:
    k = ln.strip()
    if k in out and out[k] is None:
        continue
    res.append(out.get(k) if k in out and out[k] else ln)
open(fo, "w", encoding="utf-8").write("\n".join(res))
print(json.dumps({k: v for k, v in out.items()}, ensure_ascii=False))
