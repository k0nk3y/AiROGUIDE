# -*- coding: utf-8 -*-
"""Kezzel rajzolt turak "ra-igazitasa" a terepre.

A rajzolt utvonal (a tours.json-ban "drawn": true jelzesu valtozatok) fixen megmarad (a megnevezett pontok es az iranyvonal), de
szakaszonkent a terep szerint finomodik: ahol a vonal a repulesi magassaghoz kozeli magassagu hegyre / gerincre csuszott,
a program a vonal korul (+/- SNAP_CORR km) keres egy jobb utat, amely
  - a keményen tiltott teruleteken (terep + CLEAR > magassag) nem megy at,
  - a magas teruletektol (magassag - COMFORT felett) lehetoleg tavol marad (puha buntetes), tehat a volgyet kovetve repul,
  - a rajzolt vonalhoz kozel marad.
Eredmeny: data/tours_javaslat.json + terrain_javaslat.txt (kuldd el atnezesre; az eredeti nem valtozik).

Hasznalat:  py tools\\terrain_snap.py [tura-azonosito ...]       (nelkule: minden "drawn" valtozat)
Beallitasok (kornyezeti valtozo): SNAP_CORR (alap 4 km), COMFORT (alap 2500 ft), PEN (alap 4), CELL (alap 0.5 km), CLEAR (alap 500 ft)."""
import os
import sys
import json
import math
import heapq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import terrain_check as tc
import terrain_fix as f

SNAP_CORR = float(os.environ.get("SNAP_CORR", 4.0))
COMFORT = float(os.environ.get("COMFORT", 2500))
PEN = float(os.environ.get("PEN", 4.0))
CELL = float(os.environ.get("CELL", 0.5))
CLEAR = tc.CLEAR


def corridor(a, b):
    L = tc.hav(a[0], a[1], b[0], b[1])
    br = tc.brg(a[0], a[1], b[0], b[1])
    nu = max(1, int(L / CELL))
    nv = max(1, int(SNAP_CORR / CELL))
    step = L / nu
    grid = {}
    for i in range(nu + 1):
        la0, lo0 = tc.dest(a[0], a[1], br, i * step)
        for j in range(-nv, nv + 1):
            grid[(i, j)] = tc.dest(la0, lo0, br + math.pi / 2, j * CELL) if j else (la0, lo0)
    return grid, nu, nv, L, step


def search(grid, nu, nv, el, alt, step):
    """Koltseg-alapu A*: szabad cella (terep + CLEAR <= alt); a COMFORT feletti magassag puha buntetes; oldaleltérés kis buntetes."""
    thr = alt - COMFORT
    blocked = {k: (el[k] + CLEAR > alt) for k in grid}
    start, goal = (0, 0), (nu, 0)
    blocked[start] = blocked[goal] = False
    dirs = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (2, 1), (2, -1), (1, 2), (1, -2)]
    pq = [(0.0, 0.0, (start, None))]
    best = {(start, None): 0.0}
    prev = {}
    while pq:
        fg, g, st = heapq.heappop(pq)
        if g > best.get(st, 1e18) + 1e-9:
            continue
        cur, pd = st
        if cur == goal:
            path = [cur]
            while st in prev:
                st = prev[st]
                path.append(st[0])
            return path[::-1]
        for dd in dirs:
            n = (cur[0] + dd[0], cur[1] + dd[1])
            if n not in blocked or blocked[n]:
                continue
            turn = 0.0
            if pd is not None:
                t = abs(math.degrees(math.atan2(dd[1], dd[0]) - math.atan2(pd[1], pd[0])))
                t = min(t, 360 - t)
                if t > 100:
                    continue
                turn = (t / 45.0) ** 2 * CELL * 0.5
            h = max(0.0, el[n] - thr) / 1000.0
            ng = g + math.hypot(dd[0] * step, dd[1] * CELL) * (1.0 + PEN * h) + turn + abs(n[1]) * 0.04 * CELL
            ns = (n, dd)
            if ng < best.get(ns, 1e18):
                best[ns] = ng
                prev[ns] = st
                heapq.heappush(pq, (ng + math.hypot((goal[0] - n[0]) * step, goal[1] * CELL), ng, ns))
    return None


def snap_leg(a, b, alt):
    """-> [koztes pontok] (lehet ures), vagy None ha nincs szabad ut"""
    grid, nu, nv, L, step = corridor(a, b)
    keys = list(grid)
    el = dict(zip(keys, tc.elev_fetch([grid[k] for k in keys])))
    path = search(grid, nu, nv, el, alt, step)
    if not path:
        return None
    uv = [(i * step, j * CELL) for i, j in path]
    simp = f.simplify(uv, CELL * 1.2)
    return [grid[(round(u / step), round(v / CELL))] for u, v in simp[1:-1]]


def main():
    only = set(x for x in sys.argv[1:] if not x.startswith("-"))
    if os.path.exists(tc.CACHE):
        tc._cache.update(json.load(open(tc.CACHE)))
    ap = {}
    import gzip
    for ln in gzip.open(os.path.join(f.ROOT, "data", "airports_rwy.tsv.gz"), "rt", encoding="utf-8"):
        p = ln.split("\t")
        ap[p[0]] = (float(p[2]), float(p[3]))
    d = json.load(open(os.path.join(f.ROOT, "data", "tours.json"), encoding="utf-8"))
    out = json.loads(json.dumps(d))
    rep = []
    try:
        for ti, t in enumerate(d["tours"]):
            if only and t["id"] not in only:
                continue
            for vi, v in enumerate(t["variants"]):
                if not v.get("drawn") and not only:
                    continue
                pts = []
                for p in v["pts"]:
                    if isinstance(p, str):
                        pts.append((p, ap[p][0], ap[p][1]) if p in ap else None)
                    else:
                        pts.append((p[0], float(p[1]), float(p[2])))
                if None in pts:
                    continue
                alt = float(v["alt_ft"])
                newpts, notes = [v["pts"][0]], []
                for k in range(len(pts) - 1):
                    a, b = pts[k], pts[k + 1]
                    via = f.retry(snap_leg, (a[1], a[2]), (b[1], b[2]), alt)
                    if via is None:
                        notes.append("%s -> %s: NINCS SZABAD UT a rajzolt vonal korul (magassag %d ft) - kezi munka" % (a[0], b[0], alt))
                    elif via:
                        notes.append("%s -> %s: %d igazito pont" % (a[0], b[0], len(via)))
                        for la, lo in via:
                            newpts.append(["~", round(la, 4), round(lo, 4)])
                    newpts.append(v["pts"][k + 1])
                out["tours"][ti]["variants"][vi]["pts"] = newpts
                rep.append((t["id"], v["id"], notes))
                print("%s/%s" % (t["id"], v["id"]))
                for n in notes:
                    print("   " + n)
                json.dump(out, open(os.path.join(f.ROOT, "data", "tours_javaslat.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
                with open(os.path.join(f.ROOT, "terrain_javaslat.txt"), "w", encoding="utf-8") as fh:
                    for q in rep:
                        fh.write("%s/%s\n" % (q[0], q[1]))
                        for n in q[2]:
                            fh.write("   " + n + "\n")
    finally:
        try:
            json.dump(tc._cache, open(tc.CACHE, "w"))
        except Exception:
            pass
    print("\nKESZ. %d valtozat igazitva. Fajlok: data/tours_javaslat.json, terrain_javaslat.txt - kuldd el atnezesre." % len(rep))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nLeallitva.")
    except Exception:
        import traceback
        traceback.print_exc()
    if os.name == "nt":
        input("\nNyomj Entert a bezarashoz...")
