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
import csv, gzip, hashlib, json, math, os, sys, time, urllib.error, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "tools", ".elev_cache.json")
CLEAR = float(os.environ.get("CLEAR", 500))      # minimalis fuggoleges szabad hely a terep folott (ft)
LAT = float(os.environ.get("LAT", 1.5))          # oldalso savszelesseg a kozepvonaltol (km)
STEP = float(os.environ.get("STEP", 0.5))        # mintavetel (km)
M2FT = 3.28084
_cache = {}


class Stop(Exception):
    pass


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


# ---- helyi magassag-csempek (SRTM "skadi", AWS nyilvanos adat): korlat nelkul, kulcs nelkul ----
DEM_DIR = os.path.join(ROOT, "tools", ".dem")
SOURCE = os.environ.get("ELEV", "tiles")          # "tiles" (alap, korlatlan) vagy "api" (Open-Meteo, napi keretes)
_tiles = {}


def _tile(la, lo):
    """Az 1x1 fokos csempe: (meret, array) vagy None (ocean / nincs adat). Letolti, ha kell (1-12 MB)."""
    import array
    la0, lo0 = math.floor(la), math.floor(lo)
    nm = "%s%02d%s%03d" % ("N" if la0 >= 0 else "S", abs(la0), "E" if lo0 >= 0 else "W", abs(lo0))
    if nm in _tiles:
        return _tiles[nm]
    path = os.path.join(DEM_DIR, nm + ".hgt.gz")
    if not os.path.exists(path):
        os.makedirs(DEM_DIR, exist_ok=True)
        url = "https://s3.amazonaws.com/elevation-tiles-prod/skadi/%s/%s.hgt.gz" % (nm[:3], nm)
        try:
            print("   csempe letoltese: %s ..." % nm, flush=True)
            req = urllib.request.Request(url, headers={"User-Agent": "AiROGUIDE-terrain-check"})
            with urllib.request.urlopen(req, timeout=120) as r, open(path + ".part", "wb") as f:
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    f.write(b)
            os.replace(path + ".part", path)
        except urllib.error.HTTPError as e:
            if e.code in (403, 404):                  # nincs ilyen csempe: tenger
                open(path, "wb").write(gzip.compress(b""))
            else:
                raise Stop("Csempe-letoltes sikertelen (%s): %s" % (nm, e))
        except Exception as e:
            raise Stop("Csempe-letoltes sikertelen (%s): %s. Internet kell hozza." % (nm, e))
    raw = gzip.open(path, "rb").read()
    if not raw:
        t = None
    else:
        a = array.array("h"); a.frombytes(raw)
        if sys.byteorder == "little":
            a.byteswap()                              # a .hgt big-endian
        n = int(round(math.sqrt(len(a))))
        t = (n, a)
    if len(_tiles) >= 6:
        _tiles.pop(next(iter(_tiles)))
    _tiles[nm] = t
    return t


def tile_elev(la, lo):
    """Terepmagassag (m), bilinearis; tenger/ures = 0."""
    t = _tile(la, lo)
    if not t:
        return 0.0
    n, a = t
    fy = (math.floor(la) + 1 - la) * (n - 1)          # a sorok eszakrol delre
    fx = (lo - math.floor(lo)) * (n - 1)
    y0, x0 = min(int(fy), n - 2), min(int(fx), n - 2)
    dy, dx = fy - y0, fx - x0
    v = [a[y0 * n + x0], a[y0 * n + x0 + 1], a[(y0 + 1) * n + x0], a[(y0 + 1) * n + x0 + 1]]
    v = [0 if x <= -1000 else x for x in v]           # -32768 = adathiany
    return (v[0] * (1 - dx) + v[1] * dx) * (1 - dy) + (v[2] * (1 - dx) + v[3] * dx) * dy


def elev_fetch(pts):
    if SOURCE == "tiles":
        return [tile_elev(la, lo) * M2FT for la, lo in pts]
    return elev_fetch_api(pts)


def elev_fetch_api(pts):
    """pts: [(la, lo)] -> a hianyzo pontok lekerdezese az Open-Meteo-tol, 100-asaval."""
    need = [p for p in dict.fromkeys(key(*q) for q in pts) if p not in _cache]
    for i in range(0, len(need), 100):
        ch = need[i:i + 100]
        la = ",".join(c.split(",")[0] for c in ch)
        lo = ",".join(c.split(",")[1] for c in ch)
        url = "https://api.open-meteo.com/v1/elevation?latitude=%s&longitude=%s" % (la, lo)
        el = None
        for tr in range(4):
            try:
                with urllib.request.urlopen(url, timeout=30) as r:
                    el = json.load(r)["elevation"]
                break
            except urllib.error.HTTPError as e:
                body = ""
                try:
                    body = e.read().decode("utf-8", "replace")
                except Exception:
                    pass
                if e.code == 429 and "aily" in body:
                    raise Stop("Az ingyenes napi keret elfogyott. A mar lekert adat el van mentve, holnap folytasd ugyanigy.")
                if tr == 3:
                    raise Stop("A szolgaltatas nem valaszol (HTTP %s %s)." % (e.code, body[:120]))
                print("   varakozas (%s), ujraprobalom..." % e.code); time.sleep(65 if e.code == 429 else 5)
            except Exception as e:
                if tr == 3:
                    raise Stop("Magassag-lekerdezes sikertelen (%s). Internet kell hozza." % e)
                time.sleep(3 + 4 * tr)
        for c, e in zip(ch, el):
            _cache[c] = e
        try:
            json.dump(_cache, open(CACHE, 'w'))
        except Exception:
            pass
        time.sleep(0.3)                           # udvarias maradjon az ingyenes API-val
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


def vkey(t, v):
    h = hashlib.md5(json.dumps(v["pts"], sort_keys=True).encode("utf-8")).hexdigest()[:10]
    return "%s/%s|%s|%s" % (t["id"], v["id"], v["alt_ft"], h)


def write_reports(rows, csvp, txtp, stop=None):
    rows = sorted(rows, key=lambda r: ({"HIBA": 0, "figy": 1, "ok": 2}[r[8]], -r[4]))
    with open(csvp, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["tura", "variáns", "km", "gyanus_km", "gyanus_%", "legmagasabb_gerinc_ft_a_repmagassag_folott", "alt_ft", "minosites"])
        for r in rows:
            w.writerow([r[0], r[1], round(r[2]), round(r[3]), round(r[4]), round(r[5]), r[7], r[8]])
    with open(txtp, "w", encoding="utf-8") as f:
        f.write("Terep-ellenorzes (%d variáns kész)%s\n\n" % (len(rows), "  - FOLYAMATBAN: " + stop if stop else ""))
        for r in rows:
            if r[8] == "ok":
                continue
            f.write("%s %s/%s: %.0f km, ebbol %.0f km (%.0f%%) gyanus; legmagasabb gerinc %+d ft a %d ft-os repmagassaghoz kepest\n" % (r[8], r[0], r[1], r[2], r[3], r[4], r[5], r[7]))
            for a, b, g in r[6][:6]:
                f.write("      %.0f-%.0f. km: legkisebb szabad hely %d ft\n" % (a, b, g))


def main():
    args = sys.argv[1:]
    only = set(a for a in args if not a.startswith("-"))
    if os.path.exists(CACHE):
        _cache.update(json.load(open(CACHE)))
    done = {}
    DONE = os.path.join(ROOT, "tools", ".terrain_done.json")
    if os.path.exists(DONE):
        done = json.load(open(DONE, encoding="utf-8"))
    csvp = os.path.join(ROOT, "terrain_eredmeny.csv")
    txtp = os.path.join(ROOT, "terrain_eredmeny.txt")
    ap = {}
    for ln in gzip.open(os.path.join(ROOT, "data", "airports_rwy.tsv.gz"), "rt", encoding="utf-8"):
        p = ln.split("\t")
        ap[p[0]] = (float(p[2]), float(p[3]))
    d = json.load(open(os.path.join(ROOT, "data", "tours.json"), encoding="utf-8"))
    todo = [(t, v) for t in d["tours"] if not only or t["id"] in only for v in t["variants"]]
    rows = []
    for t, v in todo:
        k = vkey(t, v)
        if k in done:
            rows.append(done[k])
    print("%d variáns, ebbol %d mar kesz. Az eredmeny menet kozben is mentodik:\n  %s\n  %s\n(Leallitas: Ctrl+C vagy az ablak bezarasa; ujrainditaskor ott folytatja.)\n" % (len(todo), len(rows), csvp, txtp))
    write_reports(rows, csvp, txtp)
    try:
        for t, v in todo:
            k = vkey(t, v)
            if k in done:
                continue
            while True:
                try:
                    r = analyse(v, ap)
                    break
                except Stop as e:
                    print("\n" + str(e) + "\n   Ujraprobalom egy ora mulva (az ablakot hagyd nyitva; az eddigi eredmeny mentve van).")
                    write_reports(rows, csvp, txtp, str(e))
                    time.sleep(3600)
            if not r:
                continue
            share = 100.0 * r["bad"] / r["km"] if r["km"] else 0
            flag = "HIBA" if share >= 10 or r["worst"][0] > 1000 else ("figy" if share >= 2 or r["bad"] >= 3 else "ok")
            row = [t["id"], v["id"], r["km"], r["bad"], share, r["worst"][0], [list(x) for x in r["runs"]], v["alt_ft"], flag]
            rows.append(row)
            done[k] = row
            json.dump(done, open(DONE, "w", encoding="utf-8"))
            write_reports(rows, csvp, txtp)
            print("%-5s %s/%s  (%d/%d)  gyanus: %.0f%%, legmagasabb gerinc %+d ft" % (flag, t["id"], v["id"], len(rows), len(todo), share, r["worst"][0]))
    finally:
        try:
            json.dump(_cache, open(CACHE, "w"))
        except Exception:
            pass
    n = sum(1 for r in rows if r[8] != "ok")
    print("\nKESZ: %d variáns, %d gyanus (HIBA: >=10%% szakasz vagy >1000 ft-tal magasabb gerinc; figy: >=2%%). Eredmeny: %s" % (len(rows), n, txtp))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nLeallitva. Ujrainditaskor ott folytatja.")
    except Exception as e:
        print("Hiba:", e)
    if os.name == "nt":
        input("\nNyomj Entert a bezarashoz...")
