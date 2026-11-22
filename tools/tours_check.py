#!/usr/bin/env python3
"""Tura-ellenorzo: ICAO-k, szakaszhosszak, az utpontok orszaga, a fo hely tavolsaga az utvonaltol, ido/sebesseg.
Hasznalat: python3 tools/tours_check.py [tura-id ...]   (alapbol az osszes)"""
import gzip, json, math, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISO = {"Serbia": "RS", "Philippines": "PH", "Malaysia": "MY", "Oman": "OM", "Kenya": "KE", "Rwanda": "RW", "Tunisia": "TN", "Madagascar": "MG", "Palau": "PW", "Colombia": "CO", "Georgia": "GE", "Puerto Rico": "PR", "Belize": "BZ", "Costa Rica": "CR", "Papua New Guinea": "PG", "Taiwan": "TW", "Caribbean Netherlands": "BQ", "Saint Barthélemy": "BL", "South Korea": "KR", "Bhutan": "BT", "Sri Lanka": "LK", "Bolivia": "BO", "Venezuela": "VE", "Mauritius": "MU", "Hungary": "HU", "Italy": "IT", "Switzerland": "CH", "Austria": "AT", "France": "FR", "Iceland": "IS", "India": "IN", "Nepal": "NP", "Cambodia": "KH", "Myanmar": "MM",
       "Germany": "DE", "Spain": "ES", "Portugal": "PT", "United Kingdom": "GB", "Ireland": "IE", "Norway": "NO", "Greece": "GR", "Croatia": "HR", "Czechia": "CZ", "Poland": "PL", "Turkey": "TR", "Sweden": "SE", "Denmark": "DK", "Finland": "FI", "Slovenia": "SI", "Malta": "MT", "Romania": "RO", "Montenegro": "ME", "Netherlands": "NL", "Belgium": "BE", "Slovakia": "SK", "Bulgaria": "BG", "Cyprus": "CY", "Faroe Islands": "FO", "United States": "US", "Peru": "PE", "Brazil": "BR", "South Africa": "ZA", "Egypt": "EG", "Tanzania": "TZ", "Australia": "AU", "New Zealand": "NZ", "Japan": "JP", "United Arab Emirates": "AE", "Hong Kong": "HK", "Canada": "CA", "Mexico": "MX", "Argentina": "AR", "Chile": "CL", "Ecuador": "EC", "Morocco": "MA", "Zimbabwe": "ZW", "French Polynesia": "PF", "Indonesia": "ID", "Singapore": "SG"}


MIN_MIN, MIN_KM = 15, 20


def hav(a, b, c, d):
    p = math.pi / 180
    x = math.sin((c - a) * p / 2) ** 2 + math.cos(a * p) * math.cos(c * p) * math.sin((d - b) * p / 2) ** 2
    return 12742 * math.asin(math.sqrt(x))


def brg(a, b):
    p = math.pi / 180
    y = math.sin((b[2] - a[2]) * p) * math.cos(b[1] * p)
    x = math.cos(a[1] * p) * math.sin(b[1] * p) - math.sin(a[1] * p) * math.cos(b[1] * p) * math.cos((b[2] - a[2]) * p)
    return (math.atan2(y, x) / p) % 360


def load_rings():
    out = []
    for ln in gzip.open(os.path.join(ROOT, "data", "countries.tsv.gz"), "rt", encoding="utf-8"):
        cc, _, b = ln.rstrip("\n").partition("\t")
        x = y = 0
        xs, ys = [], []
        for t in b.split(" "):
            dx, dy = t.split(",")
            x += int(dx); y += int(dy)
            xs.append(x / 500.0); ys.append(y / 500.0)
        out.append((cc, xs, ys, min(xs), max(xs), min(ys), max(ys)))
    return out


def country_at(R, lat, lon):
    for cc, xs, ys, x0, x1, y0, y1 in R:
        if lon < x0 or lon > x1 or lat < y0 or lat > y1:
            continue
        ins = False
        j = len(xs) - 1
        for i in range(len(xs)):
            if (ys[i] > lat) != (ys[j] > lat) and lon < (xs[j] - xs[i]) * (lat - ys[i]) / (ys[j] - ys[i]) + xs[i]:
                ins = not ins
            j = i
        if ins:
            return cc
    return None


def main():
    only = set(sys.argv[1:])
    ap = {}
    for ln in gzip.open(os.path.join(ROOT, "data", "airports_rwy.tsv.gz"), "rt", encoding="utf-8"):
        p = ln.split("\t")
        ap[p[0]] = (float(p[2]), float(p[3]), p[5])
    R = load_rings()
    d = json.load(open(os.path.join(ROOT, "data", "tours.json"), encoding="utf-8"))
    bad = warn = 0
    ids = set()
    for t in d["tours"]:
        if only and t["id"] not in only:
            continue
        if t["id"] in ids:
            print("HIBA", t["id"], "dupla azonosito"); bad += 1
        ids.add(t["id"])
        iso = ISO.get(t["country"]["en"])
        E = lambda m: print("HIBA", t["id"], m)
        W = lambda m: print("  figy", t["id"], m)
        for k in ("en", "hu"):
            if not t["name"].get(k) or not t["desc"].get(k):
                E("hianyzo szoveg (%s)" % k); bad += 1
        m = t["main"]
        allpts = []
        for v in t["variants"]:
            pts = []
            for p in v["pts"]:
                if isinstance(p, str):
                    if p not in ap:
                        E("%s: ismeretlen ICAO %s" % (v["id"], p)); bad += 1; continue
                    if ap[p][2] in ("closed", "heliport", "seaplane_base", "balloonport"):
                        E("%s: nem hasznalhato repter %s (%s)" % (v["id"], p, ap[p][2])); bad += 1
                    pts.append((p, ap[p][0], ap[p][1]))
                else:
                    pts.append((p[0], float(p[1]), float(p[2])))
            if len(pts) < 2:
                E("%s: kevesebb mint 2 pont" % v["id"]); bad += 1; continue
            allpts += pts
            tot = 0
            for a, b in zip(pts, pts[1:]):
                dd = hav(a[1], a[2], b[1], b[2]); tot += dd
                if dd > 220:
                    W("%s: hosszu szakasz %s -> %s: %.0f km" % (v["id"], a[0], b[0], dd)); warn += 1
                if dd < 0.8:
                    W("%s: majdnem azonos pontok %s / %s" % (v["id"], a[0], b[0])); warn += 1
            for a, b, c in zip(pts, pts[1:], pts[2:]):             # hajtukanyar / szoros cikcakk: repulovel nem repulheto
                tn = abs((brg(b, c) - brg(a, b) + 180) % 360 - 180)
                dm_ = min(hav(a[1], a[2], b[1], b[2]), hav(b[1], b[2], c[1], c[2]))
                if tn > 120:
                    E("%s: hajtukanyar (%.0f fok) a(z) %s pontnal" % (v["id"], tn, b[0])); bad += 1
                elif tn > 90 and dm_ < 8:
                    W("%s: szoros fordulo (%.0f fok, %.1f km szakasz) a(z) %s pontnal" % (v["id"], tn, dm_, b[0])); warn += 1
            mins = tot / 1.852 / v["kt"] * 60
            if mins < MIN_MIN or tot < MIN_KM:
                E("%s: tul rovid (%.0f perc, %.0f km; minimum %d perc es %d km)" % (v["id"], mins, tot, MIN_MIN, MIN_KM)); bad += 1
            elif mins > 150:
                W("%s: idotartam %.0f perc (%.0f km, %d kt)" % (v["id"], mins, tot, v["kt"])); warn += 1
            if v["kind"] == "loop" and hav(pts[0][1], pts[0][2], pts[-1][1], pts[-1][2]) > 3:
                E("%s: koruton a kezdo es a vegpont nem azonos" % v["id"]); bad += 1
            if iso:
                for n, la, lo in pts:
                    if n in ap or n.startswith("~"):
                        continue
                    c = country_at(R, la, lo)
                    if c and c != iso:
                        W("%s: %s (%.4f, %.4f) a(z) %s teruleten van, nem %s" % (v["id"], n, la, lo, c, iso)); warn += 1
                    if c is None:
                        W("%s: %s (%.4f, %.4f) tengeren / orszaghatar nelkul" % (v["id"], n, la, lo)); warn += 1
        if allpts:
            dm = min(hav(m["lat"], m["lon"], p[1], p[2]) for p in allpts)
            if dm > 25:
                E("a fo hely (%s) %.0f km-re van az utvonaltol" % (m.get("en"), dm)); bad += 1
        for n, la, lo in t.get("pois") or []:
            if allpts and min(hav(la, lo, p[1], p[2]) for p in allpts) > 12:
                W("pois: %s tul messze az utvonaltol (>12 km, nem jelenik meg)" % n); warn += 1
    print("kesz: %d tura, %d hiba, %d figyelmeztetes" % (len(ids), bad, warn))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
