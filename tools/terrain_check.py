#!/usr/bin/env python3
"""Terep-ellenorzo a turakhoz: a repulesi magassag (alt_ft, MSL) elegendo-e a gerincek felett.

Mukodes: az utvonalat ~1 km-enkent mintavetelezi, mindegyik pontnal a terepmagassagot is lekerdezi
oldalirányban +-LAT km-ig (a sav kozepen es szelen), es megnezi, hol van a terep a repulesi magassag
alatt kevesebb mint CLEAR labbal. Az eredmeny turankent/variansonkent a gyanus szakaszok hossza.

Magassagadat: Open-Meteo (Copernicus DEM, ~90 m), ingyenes, kulcs nelkul. Internet kell hozza;
a lekerdezett adatot a tools/.elev_cache.json fajlba menti, igy a masodik futas gyors.

Hasznalat:
  python3 tools/terrain_check.py              az osszes tura
  python3 tools/terrain_check.py everest ...  csak a megadott tura-azonositok
  python3 tools/terrain_check.py --csv ki.csv az eredmeny CSV-ben is (tura;variáns;km;gyanus_km;max_ft;...)
Beallitasok (kornyezeti valtozo): CLEAR (alap 500 ft), LAT (alap 1.5 km), STEP (alap 1.0 km)."""
import csv, gzip, json, math, os, sys, time, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "tools", ".elev_cache.json")
CLEAR = float(os.environ.get("CLEAR", 500))      # minimalis fuggoleges szabad hely a terep folott (ft)
LAT = float(os.environ.get("LAT", 1.5))          # oldalso savszelesseg a kozepvonaltol (km)
STEP = float(os.environ.get("STEP", 1.0))        # mintavetel (km)
M2FT = 3.28084
_cache = {}


def hav(a, b, c, d):
    p = math.pi / 180
    x = math.sin((c - a) * p / 2) ** 2 + math.cos(a * p) * math.cos(c * p) * math.sin((d - b) * p / 2) ** 2
    return 12742 * math.asin(math.sqrt(x))


def brg(a, b, c, d):
    p = math.pi / 180
    y = math.sin((d - b) * p) * math.cos(c * p)
    x = math.cos(a * p) * math.sin(c * p) - math.sin(a * p) * math.cos(c * p) * math.cos((d - b) * p)
    return math.atan2(y, x)


def dest(la, lo, br, km):
    p = math.pi / 180
    d = km / 6371.0
    la1, lo1 = la * p, lo * p
    la2 = math.asin(math.sin(la1) * math.cos(d) + math.cos(la1) * math.sin(d) * math.cos(br))
    lo2 = lo1 + math.atan2(math.sin(br) * math.sin(d) * math.cos(la1), math.cos(d) - math.sin(la1) * math.sin(la2))
    return la2 / p, lo2 / p


def key(la, lo):
    return "%.3f,%.3f" % (la, lo)


def elev_fetch(pts):
    """pts: [(la, lo)] -> a hianyzo pontok lekerdezese az Open-Meteo-tol, 100-asaval."""
    need = [p for p in dict.fromkeys(key(*q) for q in pts) if p not in _cache]
    for i in range(0, len(need), 100):
        ch = need[i:i + 100]
        la = ",".join(c.split(",")[0] for c in ch)
        lo = ",".join(c.split(",")[1] for c in ch)
        url = "https://api.open-meteo.com/v1/elevation?latitude=%s&longitude=%s" % (la, lo)
        for tr in range(4):
            try:
                with urllib.request.urlopen(url, timeout=30) as r:
                    el = json.load(r)["elevation"]
                break
            except Exception as e:
                if tr == 3:
                    sys.exit("Magassag-lekerdezes sikertelen (%s). Internet kell hozza." % e)
                time.sleep(2 + 3 * tr)
        for c, e in zip(ch, el):
            _cache[c] = e
        time.sleep(0.25)                          # udvarias maradjon az ingyenes API-val
    return [_cache[key(*q)] * M2FT for q in pts]


def load_pts(v, ap):
    out = []
    for p in v["pts"]:
        if isinstance(p, str):
            if p in ap:
                out.append((ap[p][0], ap[p][1]))
        else:
            out.append((float(p[1]), float(p[2])))
    return out


def sample(pts):
    """Az utvonal ~STEP km-es mintai: (la, lo, bal_la, bal_lo, jobb_la, jobb_lo, tavolsag_km)."""
    out, cum = [], 0.0
    for (a, b), (c, d) in zip(pts, pts[1:]):
        L = hav(a, b, c, d)
        if L < 0.05:
            continue
        br = brg(a, b, c, d)
        n = max(1, int(L / STEP))
        for i in range(n):
            f = i * L / n
            la, lo = dest(a, b, br, f)
            ll = dest(la, lo, br - math.pi / 2, LAT)
            rr = dest(la, lo, br + math.pi / 2, LAT)
            out.append((la, lo, ll[0], ll[1], rr[0], rr[1], cum + f))
        cum += L
    out.append((pts[-1][0], pts[-1][1], pts[-1][0], pts[-1][1], pts[-1][0], pts[-1][1], cum))
    return out, cum


def analyse(v, ap):
    pts = load_pts(v, ap)
    if len(pts) < 2:
        return None
    S, tot = sample(pts)
    flat = []
    for s in S:
        flat += [(s[0], s[1]), (s[2], s[3]), (s[4], s[5])]
    el = elev_fetch(flat)
    alt = float(v["alt_ft"])
    bad_km = 0.0
    worst = (-1e9, 0.0)
    runs, cur = [], None
    for i, s in enumerate(S):
        ter = max(el[3 * i], el[3 * i + 1], el[3 * i + 2])      # a sav legmagasabb pontja
        gap = alt - ter                                          # szabad hely (ft)
        if gap < CLEAR:
            bad_km += STEP
            if cur is None:
                cur = [s[6], s[6], gap]
            cur[1] = s[6]
            cur[2] = min(cur[2], gap)
        elif cur is not None:
            runs.append(cur); cur = None
        if ter - alt > worst[0]:
            worst = (ter - alt, s[6])
    if cur is not None:
        runs.append(cur)
    return {"km": tot, "bad": min(bad_km, tot), "worst": worst, "runs": runs, "max_ter": max(el[3 * i] for i in range(len(S)))}


def main():
    args = sys.argv[1:]
    csvp = None
    if "--csv" in args:
        i = args.index("--csv"); csvp = args[i + 1]; del args[i:i + 2]
    only = set(args)
    if os.path.exists(CACHE):
        _cache.update(json.load(open(CACHE)))
    ap = {}
    for ln in gzip.open(os.path.join(ROOT, "data", "airports_rwy.tsv.gz"), "rt", encoding="utf-8"):
        p = ln.split("\t")
        ap[p[0]] = (float(p[2]), float(p[3]))
    d = json.load(open(os.path.join(ROOT, "data", "tours.json"), encoding="utf-8"))
    rows = []
    try:
        for t in d["tours"]:
            if only and t["id"] not in only:
                continue
            for v in t["variants"]:
                r = analyse(v, ap)
                if not r:
                    continue
                share = 100.0 * r["bad"] / r["km"] if r["km"] else 0
                flag = "HIBA" if share >= 10 or r["worst"][0] > 1000 else ("figy" if share >= 2 or r["bad"] >= 3 else "ok")
                rows.append((t["id"], v["id"], r["km"], r["bad"], share, r["worst"][0], r["runs"], v["alt_ft"], flag))
                if flag != "ok":
                    print("%-5s %s/%s: %.0f km, ebbol %.0f km (%.0f%%) a terep %d ft-nal kozelebb van a %d ft-os magassaghoz; legmagasabb gerinc %+d ft a repulesi magassaghoz kepest (a %.0f. km-nel)"
                          % (flag, t["id"], v["id"], r["km"], r["bad"], share, CLEAR, v["alt_ft"], r["worst"][0], r["worst"][1]))
                    for a, b, g in r["runs"][:4]:
                        print("        %.0f-%.0f. km: legkisebb szabad hely %d ft" % (a, b, g))
                else:
                    print("ok    %s/%s" % (t["id"], v["id"]))
    finally:
        try:
            json.dump(_cache, open(CACHE, "w"))
        except Exception:
            pass
    if csvp:
        with open(csvp, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["tura", "variáns", "km", "gyanus_km", "gyanus_%", "legmagasabb_gerinc_ft_a_repmagassag_folott", "alt_ft", "minosites"])
            for r in rows:
                w.writerow([r[0], r[1], round(r[2]), round(r[3]), round(r[4]), round(r[5]), r[7], r[8]])
    n = sum(1 for r in rows if r[8] != "ok")
    print("\n%d variáns vizsgálva, %d gyanús (HIBA: >=10%% szakasz vagy >1000 ft-tal magasabb gerinc; figy: >=2%%)." % (len(rows), n))


if __name__ == "__main__":
    main()
