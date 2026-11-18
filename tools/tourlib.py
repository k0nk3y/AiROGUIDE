#!/usr/bin/env python3
"""Kozos segedek a tura-csomagokhoz (tours.json bovitese; ujrafuttathato: a meglevo azonositokat frissiti)."""
import json, os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "tours.json")
T = []


def tour(id, country, name, main, tags, desc, pois, variants, cont="EU"):
    T.append({"id": id, "continent": cont, "country": {"en": country[0], "hu": country[1]}, "name": {"en": name[0], "hu": name[1]},
              "main": {"en": main[0], "hu": main[1], "lat": main[2], "lon": main[3]}, "tags": tags, "desc": {"en": desc[0], "hu": desc[1]},
              "variants": [dict(id=v[0], kind=v[1], kt=v[2], alt_ft=v[3], stol=False, label={"en": v[4][0], "hu": v[4][1]}, desc={"en": v[5][0], "hu": v[5][1]}, pts=v[6]) for v in variants],
              "pois": pois})




def save():
    d = json.load(open(P, encoding="utf-8"))
    have = {t["id"]: i for i, t in enumerate(d["tours"])}
    for t in T:
        if t["id"] in have:
            d["tours"][have[t["id"]]] = t
        else:
            d["tours"].append(t)
    json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(T), "tura, osszesen", len(d["tours"]))
