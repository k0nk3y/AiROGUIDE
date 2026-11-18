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




V = []


def addvar(tid, vid, kind, kt, alt, label, desc, pts):
    """Uj / frissitett valtozat egy meglevo turahoz. pts: ICAO, ["nev", lat, lon] vagy "@Nev" (a tura mar ismert pontja)."""
    V.append((tid, dict(id=vid, kind=kind, kt=kt, alt_ft=alt, stol=False, label={"en": label[0], "hu": label[1]}, desc={"en": desc[0], "hu": desc[1]}, pts=pts)))


def save_vars():
    d = json.load(open(P, encoding="utf-8"))
    idx = {t["id"]: t for t in d["tours"]}
    for tid, v in V:
        t = idx[tid]
        known = {}
        for w in t["variants"]:
            for p in w["pts"]:
                if isinstance(p, list):
                    known[p[0]] = p
        known.update({p[0]: p for p in t.get("pois") or []})
        pts = []
        for p in v["pts"]:
            if isinstance(p, str) and p.startswith("@"):
                if p[1:] not in known:
                    raise SystemExit("ismeretlen pont: %s (%s)" % (p, tid))
                pts.append(list(known[p[1:]]))
            else:
                pts.append(p)
        v = dict(v, pts=pts)
        for i, w in enumerate(t["variants"]):
            if w["id"] == v["id"]:
                t["variants"][i] = v
                break
        else:
            t["variants"].append(v)
    json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(V), "valtozat")


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
