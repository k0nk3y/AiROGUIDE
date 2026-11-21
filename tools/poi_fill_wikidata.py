#!/usr/bin/env python3
"""A data/tour_pois.json hianyzo nyelveit tolti Wikipedia-nyelvlinkekbol (internet kell). Futtatas: python3 tools/poi_fill_wikidata.py
Mukodes: az angol cim alapjan az en.wikipedia 'langlinks' adja a de/es/fr/it/pl/ru/sk/zh cimet; ami nincs, azt hagyja (az angol nev marad)."""
import json, os, sys, time, urllib.parse, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "tour_pois.json")
LANGS = ["de", "es", "fr", "it", "pl", "ru", "sk", "zh"]
d = json.load(open(P, encoding="utf-8"))
pois = d["pois"]

def api(params):
    u = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(u, headers={"User-Agent": "AiROGUIDE-tools/1.0"})
    return json.load(urllib.request.urlopen(req, timeout=30))

names = [n for n in pois if any(l not in pois[n] for l in LANGS)]
print(len(names), "latnivalo hianyos")
for i in range(0, len(names), 20):
    chunk = names[i:i + 20]
    # az EN nev gyakran 'Hely, Telepules' alaku: a vesszo elotti resz is jo cim
    titles = {n: n for n in chunk}
    try:
        r = api({"action": "query", "format": "json", "redirects": 1, "prop": "langlinks", "lllimit": "500", "titles": "|".join(chunk)})
    except Exception as e:
        print("hiba", e); time.sleep(3); continue
    q = r.get("query", {})
    alias = {}
    for k in ("normalized", "redirects"):
        for x in q.get(k, []):
            alias[x["from"]] = x["to"]
    pg = {p["title"]: p for p in q.get("pages", {}).values()}
    for n in chunk:
        t = n
        for _ in range(2):
            t = alias.get(t, t)
        ll = {x["lang"]: x["*"] for x in (pg.get(t) or {}).get("langlinks", [])}
        for l in LANGS:
            if l in ll and l not in pois[n]:
                pois[n][l] = ll[l]
    print(i + len(chunk), "/", len(names))
    time.sleep(0.5)
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=0, separators=(",", ":"))
print("kesz")
