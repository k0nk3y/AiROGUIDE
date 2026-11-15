#!/usr/bin/env python3
"""AiROGUIDE WT: repuloter-alaprajzok (taxik, kotok, epuletek) elore letoltese az OpenStreetMap-bol (Overpass).

Hasznalat (a program mappajabol, a csomagolt Pythonnal vagy barmelyik Python 3.8+-szal):
    python tools/build_layouts.py                      # a nagy repuloterek (large_airport)
    python tools/build_layouts.py --types large_airport,medium_airport --limit 500
    python tools/build_layouts.py --icao LHBP,BIKF,LZIB

Az eredmeny: data/airport_layouts.json.gz (ICAO -> elemlista). A program ezt hasznalja eloszor.
A letoltes megszakithato es folytathato (a reszeredmenyek az airoguide_adlayout mappaban maradnak).
"""
import argparse, gzip, json, math, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MIRRORS = ["https://overpass-api.de/api/interpreter", "https://overpass.openstreetmap.fr/api/interpreter", "https://overpass.kumi.systems/api/interpreter",
           "https://overpass.private.coffee/api/interpreter", "https://maps.mail.ru/osm/tools/overpass/api/interpreter", "https://overpass.nchc.org.tw/api/interpreter"]
KINDS = ("runway", "taxiway", "taxilane", "apron", "terminal", "hangar", "helipad")


def load_airports():
    out = {}
    with gzip.open(os.path.join(ROOT, "data", "airports_rwy.tsv.gz"), "rt", encoding="utf-8") as f:
        for ln in f:
            p = ln.rstrip("\n").split("\t")
            if len(p) < 9:
                continue
            cs = []
            for r in p[8].split(";"):
                q = r.split("|")
                if len(q) >= 10 and q[6] and q[9]:
                    try:
                        cs += [(float(q[6]), float(q[7])), (float(q[8]), float(q[9]))]
                    except ValueError:
                        pass
            out[p[0]] = {"icao": p[0], "type": p[5], "lat": float(p[2]), "lon": float(p[3]), "cs": cs}
    return out


def bbox(a):
    la, lo = a["lat"], a["lon"]
    cs = a["cs"] or [(la, lo)]
    mla = 800 / 111320.0
    mlo = 800 / (111320.0 * max(0.2, math.cos(math.radians(la))))
    return "%.5f,%.5f,%.5f,%.5f" % (min(c[0] for c in cs) - mla, min(c[1] for c in cs) - mlo, max(c[0] for c in cs) + mla, max(c[1] for c in cs) + mlo)


def parse(js):
    out = []
    for e in (js or {}).get("elements", []):
        if e.get("type") != "way":
            continue
        t = e.get("tags") or {}
        k = t.get("aeroway") or ""
        if k not in KINDS or k == "runway":
            continue
        p = [[round(x["lat"], 5), round(x["lon"], 5)] for x in (e.get("geometry") or []) if "lat" in x and "lon" in x]
        if len(p) < 2:
            continue
        if len(p) > 400:
            p = p[::max(1, len(p) // 400)]
        out.append({"k": k, "r": str(t.get("ref") or "")[:6], "p": p})
    return out


def fetch(a, tries=6):
    q = "[out:json][timeout:60];(" + "".join('way["aeroway"="%s"](%s);' % (k, bbox(a)) for k in KINDS if k != "runway") + ");out geom qt;"
    body = urllib.parse.urlencode({"data": q}).encode()
    last = ""
    for i in range(tries):
        u = MIRRORS[i % len(MIRRORS)]
        try:
            rq = urllib.request.Request(u, data=body, headers={"User-Agent": "AiROGUIDE/WT build_layouts", "Content-Type": "application/x-www-form-urlencoded"})
            with urllib.request.urlopen(rq, timeout=90) as r:
                return parse(json.loads(r.read().decode("utf-8")))
        except Exception as ex:
            last = u.split("/")[2] + ": " + repr(ex)[:100]
            time.sleep(4 + 4 * i)
    raise RuntimeError(last)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--types", default="large_airport")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--icao", default="")
    ap.add_argument("--pause", type=float, default=2.0, help="szunet a lekerdezesek kozott (mp)")
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "airport_layouts.json.gz"))
    a = ap.parse_args()
    A = load_airports()
    if a.icao:
        todo = [A[i] for i in a.icao.upper().split(",") if i in A]
    else:
        ty = set(a.types.split(","))
        todo = sorted([x for x in A.values() if x["type"] in ty], key=lambda x: x["icao"])
        if a.limit:
            todo = todo[:a.limit]
    part = os.path.join(ROOT, "airoguide_adlayout", "_build_partial.json")
    res = {}
    try:
        with open(part, encoding="utf-8") as f:
            res = json.load(f)
    except Exception:
        pass
    # a mar meglevo (programbol letoltott) alaprajzokat is felhasznaljuk
    for x in todo:
        fp = os.path.join(ROOT, "airoguide_adlayout", x["icao"] + ".json")
        if x["icao"] not in res and os.path.exists(fp):
            try:
                with open(fp, encoding="utf-8") as f:
                    d = json.load(f)
                if isinstance(d.get("items"), list):
                    res[x["icao"]] = d["items"]
            except Exception:
                pass
    os.makedirs(os.path.dirname(part), exist_ok=True)
    fail = 0
    for n, x in enumerate(todo, 1):
        if x["icao"] in res:
            continue
        try:
            res[x["icao"]] = fetch(x)
            print("%d/%d %s: %d elem" % (n, len(todo), x["icao"], len(res[x["icao"]])), flush=True)
        except Exception as ex:
            fail += 1
            print("%d/%d %s: HIBA %s" % (n, len(todo), x["icao"], ex), flush=True)
        if n % 10 == 0:
            with open(part, "w", encoding="utf-8") as f:
                json.dump(res, f, separators=(",", ":"))
        time.sleep(a.pause)
    with open(part, "w", encoding="utf-8") as f:
        json.dump(res, f, separators=(",", ":"))
    res = {k: v for k, v in res.items() if v}                      # az ures (nincs adat) repuloterek kimaradnak: a program elo lekerdezessel probalja
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with gzip.open(a.out, "wt", encoding="utf-8", compresslevel=9) as f:
        json.dump(res, f, separators=(",", ":"))
    print("Kesz: %d repuloter, %.1f MB, hibas: %d -> %s" % (len(res), os.path.getsize(a.out) / 1048576.0, fail, a.out))


if __name__ == "__main__":
    main()
