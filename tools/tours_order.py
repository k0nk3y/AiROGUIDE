#!/usr/bin/env python3
"""Utpontok sorrendjenek optimalizalasa: hajtukanyar (>~90 fok) nelkuli, rovid utvonal. A kezdo- es vegpont (repulo) marad.
Futtatas: add_eu1 -> add_eu2 -> add_var_eu -> tours_order (a tours.json-t modositja)."""
import gzip, itertools, json, math, os, sys
from tours_check import hav, brg, ROOT


def cost(pts):
    km = turn = 0.0
    for a, b in zip(pts, pts[1:]):
        km += hav(a[1], a[2], b[1], b[2])
    for a, b, c in zip(pts, pts[1:], pts[2:]):
        t = abs((brg(b, c) - brg(a, b) + 180) % 360 - 180)
        turn += max(0.0, t - 60) ** 2
    return turn + 0.3 * km


def dest(a, brg_deg, km):
    """Pont `km` tavolsagra a(z) a pontbol a megadott iranyban."""
    p = math.pi / 180
    la1, lo1, b = a[1] * p, a[2] * p, brg_deg * p
    d = km / 6371.0
    la2 = math.asin(math.sin(la1) * math.cos(d) + math.cos(la1) * math.sin(d) * math.cos(b))
    lo2 = lo1 + math.atan2(math.sin(b) * math.sin(d) * math.cos(la1), math.cos(d) - math.sin(la1) * math.sin(la2))
    return round(la2 / p, 4), round(lo2 / p, 4)


PASS_KM = 3.0      # ha egy utpont ennyin belul van a szomszedait osszekoto egyenestol (vagy a repulotertol), nem kell kulon odamenni: latnivalo (t["pois"]) marad, utpont nem


def xtrack(a, b, c):
    """Az `a` pont tavolsaga (km) a b-c szakasztol (sikkozelites)."""
    kx = 111.32 * math.cos(math.radians(a[1]))
    ax, ay = (a[2] - b[2]) * kx, (a[1] - b[1]) * 111.32
    cx, cy = (c[2] - b[2]) * kx, (c[1] - b[1]) * 111.32
    L2 = cx * cx + cy * cy
    u = 0.0 if L2 == 0 else max(0.0, min(1.0, (ax * cx + ay * cy) / L2))
    return math.hypot(ax - u * cx, ay - u * cy)


def passby(P, t):
    """Az also lepes: a nevesitett kozbenso pontot, ami PASS_KM-en belul van a szomszedait osszekoto szakasztol, kivesszuk az utvonalbol (t["pois"]-ba kerul)."""
    m = t.get("main") or {}
    while len(P) > 3:
        best = None
        for i in range(1, len(P) - 1):
            p = P[i][0]
            if isinstance(p, str) or str(p[0]).startswith("~"):
                continue
            if abs(p[1] - m.get("lat", 99)) < 1e-6 and abs(p[2] - m.get("lon", 99)) < 1e-6:
                continue
            x = xtrack(P[i], P[i - 1], P[i + 1])
            if x < PASS_KM and (best is None or x < best[0]):
                best = (x, i)
        if not best:
            break
        p = P[best[1]][0]
        ps = t.setdefault("pois", [])
        if not any(str(e[0]) == str(p[0]) for e in ps):
            ps.append(list(p))
        print("  utpont -> latnivalo:", t["id"], p[0], "(%.1f km)" % best[0])
        P = P[:best[1]] + P[best[1] + 1:]
    return P


def swing(P):
    """Ahol egy fordulo >120 fok (hajtukanyar), ott egy 'atmeneti' (nem latnivalo) pont kerul a fordulo utan: a fordulo ket szelid lepesben tortenik. Nevuk '~'-vel kezdodik."""
    out = [P[0]]
    for i in range(1, len(P) - 1):
        a, b, c = out[-1], P[i], P[i + 1]
        out.append(b)
        h1, h2 = brg(a, b), brg(b, c)
        sg = (h2 - h1 + 180) % 360 - 180
        if abs(sg) > 120:
            L = max(4.0, min(12.0, 0.25 * min(hav(a[1], a[2], b[1], b[2]), hav(b[1], b[2], c[1], c[2]))))
            if abs(sg) > 170:
                sg = 170.0 if sg >= 0 else -170.0
            la, lo = dest(b, (h1 + sg / 2.0) % 360, L)
            out.append((["~", la, lo], la, lo))
    out.append(P[-1])
    return out


FIXED = set(open(os.path.join(ROOT, "tools", "fixed_order.txt"), encoding="utf-8").read().split()) if os.path.exists(os.path.join(ROOT, "tools", "fixed_order.txt")) else set()   # tura/valtozat: a megadott sorrend marad


def main():
    ap = {}
    for ln in gzip.open(os.path.join(ROOT, "data", "airports_rwy.tsv.gz"), "rt", encoding="utf-8"):
        p = ln.split("\t")
        ap[p[0]] = (float(p[2]), float(p[3]))
    path = os.path.join(ROOT, "data", "tours.json")
    d = json.load(open(path, encoding="utf-8"))
    ch = 0
    only = set(sys.argv[1:])             # megadott tura-azonositok: csak azokat rendezi (a tobbi erintetlen)
    for t in d["tours"]:
        if only and t["id"] not in only:
            continue
        for v in t["variants"]:
            raw = [p for p in v["pts"] if isinstance(p, str) or not str(p[0]).startswith("~") or str(p[0]).startswith("~=")]   # "~=": kezzel megadott alakito pont, marad
            v["pts"] = raw
            P = [(p, ap[p][0], ap[p][1]) if isinstance(p, str) else (p, p[1], p[2]) for p in raw]
            mid = P[1:-1]
            if v.get("kind") == "loop" and 2 <= len(mid) <= 8 and "%s/%s" % (t["id"], v["id"]) not in FIXED:          # A->B turaknal a haladasi sorrend marad
                best = min(itertools.permutations(mid), key=lambda m: cost([P[0]] + list(m) + [P[-1]]))
                if cost([P[0]] + list(best) + [P[-1]]) < cost(P) - 1:
                    P = [P[0]] + list(best) + [P[-1]]
                    ch += 1
                    print("atrendezve:", t["id"], v["id"])
            if "%s/%s" % (t["id"], v["id"]) not in FIXED:
                P = passby(P, t)                         # a lathato/kozeli pontok nem kapnak kulon kitero-kanyart: latnivalo marad, utpont nem
            P2 = swing(P)
            for _ in range(3):                      # ha a bevezetett pont utan is >120 fok marad, meg egy
                P3 = swing(P2)
                if len(P3) == len(P2):
                    break
                P2 = P3
            v["pts"] = [x[0] for x in P2]
            if len(P2) != len(P):
                print("  atmeneti pont:", t["id"], v["id"], len(P2) - len(P))
    rev = set(open(os.path.join(ROOT, "tools", "reviewed.txt"), encoding="utf-8").read().split())      # mar atnezett turak; a tobbi "Uj" jelolest kap
    for t in d["tours"]:
        if only:
            continue
        if t["id"] in rev:
            t.pop("new", None)
        else:
            t["new"] = True
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(ch, "valtozat atrendezve")


if __name__ == "__main__":
    main()
