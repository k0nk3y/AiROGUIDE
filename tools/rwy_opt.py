#!/usr/bin/env python3
"""Kifutohoz igazitott korok: felszallas/leszallas a kifuto tengelyen (indulo ~= pont a kifuto iranyaban, erkezo ~= pont a megkozelitesi oldalon),
a koztes pontok sorrendje optimalizalva (kevesebb kanyar, nincs keresztezes). Hasznalat: rwy_opt.py tura-id ... [--apply]"""
import gzip, itertools, json, math, os, sys
from tours_check import hav, brg, ROOT
from tours_order import dest

def rwys(ic):
    for ln in gzip.open(os.path.join(ROOT, "data", "airports_rwy.tsv.gz"), "rt", encoding="utf-8"):
        p = ln.split("\t")
        if p[0] == ic:
            lat, lon = float(p[2]), float(p[3]); out = []
            for r in p[8].strip().split(";"):
                f = r.split("|")
                if len(f) < 4 or f[3] not in ("H", "A", "C", "P", "") : continue
                try: n = int(f[0].split("/")[0].rstrip("LRC")) * 10
                except: continue
                if int(f[1] or 0) < 2500: continue
                out.append((f[0], n, (n + 180) % 360))
            return (lat, lon), out
    raise SystemExit("nincs repter " + ic)

def tn(a, b): return (b - a + 180) % 360 - 180

def cross(p1, p2, p3, p4):
    def o(a, b, c): return (b[1]-a[1])*(c[0]-a[0]) - (b[0]-a[0])*(c[1]-a[1])
    return o(p1,p2,p3)*o(p1,p2,p4) < 0 and o(p3,p4,p1)*o(p3,p4,p2) < 0

def pl(P):    # [(name,lat,lon)] -> x,y km
    la0, lo0 = P[0][1], P[0][2]; k = math.cos(math.radians(la0))
    return [((p[2]-lo0)*111.32*k, (p[1]-la0)*111.32) for p in P]

def cost(P, hd0, hdN):
    X = pl(P); c = 0.0; n = len(P)
    hs = [hd0] + [brg(P[i], P[i+1]) for i in range(n-1)] + [hdN]
    for i in range(1, len(hs)):
        t = abs(tn(hs[i-1], hs[i])); c += max(0, t - 45) ** 2 * (4 if t > 100 else 1)
    c += 0.15 * sum(hav(P[i][1],P[i][2],P[i+1][1],P[i+1][2]) for i in range(n-1))
    for i in range(n-1):
        for j in range(i+2, n-1):
            if cross(X[i], X[i+1], X[j], X[j+1]): c += 2e5
    return c

def run(t, v, dkm=7.0, fkm=10.0):
    ic = v["pts"][0]; (alat, alon), rw = rwys(ic)
    mids = [p for p in v["pts"][1:-1] if not str(p[0]).startswith("~")]
    A = (ic, alat, alon)
    best = None
    for (d_nm, d_hd, _) in rw:
        for (l_nm, _, l_hd) in rw:           # leszallas az l_nm pontra: iranya l_hd, a megkozelites az l_hd+180 oldalrol
            for ud in (0, 1):
                for ul in (0, 1):
                    D = dest(A, d_hd, dkm) if ud else None
                    F = dest(A, (l_hd + 180) % 360, fkm) if ul else None
                    for m in itertools.permutations(mids):
                        seq = [A] + ([("~=", D[0], D[1])] if D else []) + [(x, x[1], x[2]) for x in m] + ([("~=", F[0], F[1])] if F else []) + [A]
                        c = cost(seq, d_hd if ud else brg(A, seq[1]) , l_hd) + (0 if ud else 400) + (0 if ul else 400)
                        if best is None or c < best[0]: best = (c, seq, d_nm, l_nm, ud, ul)
    return best

def fmt(seq, ic):
    out = [ic]
    for s in seq[1:-1]:
        out.append(["~=", round(s[1], 4), round(s[2], 4)] if s[0] == "~=" else s[0])
    out.append(ic); return out

if __name__ == "__main__":
    ids = [a for a in sys.argv[1:] if not a.startswith("--")]
    d = json.load(open(os.path.join(ROOT, "data", "tours.json"), encoding="utf-8"))
    for t in d["tours"]:
        if t["id"] in ids:
            for v in t["variants"]:
                if v.get("kind") != "loop": continue
                b = run(t, v); ic = v["pts"][0]
                print(t["id"], "cost %.0f" % b[0], "fel", b[2], "le", b[3], [s[0][0] if s[0] != "~=" else "~=" for s in b[1]])
                v["pts"] = fmt(b[1], ic)
    if "--apply" in sys.argv:
        json.dump(d, open(os.path.join(ROOT, "data", "tours.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
