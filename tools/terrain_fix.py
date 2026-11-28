#!/usr/bin/env python3
"""Automatikus javaslat a terepmiatt nem repulheto turaszakaszokra (a terrain_check.py folytatasa).

Minden olyan variansra, amit a terrain_check HIBA/figy-nek jelolt, szakaszonkent:
  1. megnezi, hol vezet a szakasz a terep ala/koze (a repulesi magassag - CLEAR ft alatt),
  2. a szakasz kore (+-CORR km) magassag-racsot kerd le, es keres egy volgyet/atjarot, ami
     az adott magassagon vegig szabad (A* keresessel, kevés fordulóval),
  3. ha nincs ilyen, 1000 ft-os lepesekben emeli a magassagot (legfeljebb MAX_ALT-ig),
  4. ha igy sem, kiirja, hogy kezzel kell megoldani (pont athelyezese / a szakasz elhagyasa).
A javaslatot NEM irja at az eredeti fajlban: data/tours_javaslat.json + terrain_javaslat.txt.
Ezutan a javitott varianst a sajat szigorubb (1 km-es) ellenorzesevel is ujra megnezi.

Hasznalat: tools/terrain_fix.bat (dupla kattintas), vagy: python tools/terrain_fix.py [tura-id ...]
Kornyezeti valtozok: CLEAR (500 ft), CORR (12 km), CELL (1.5 km), MAX_ALT (20000 ft), MAXTURN (100 fok)."""
import hashlib, heapq, json, math, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import terrain_check as tc

ROOT = tc.ROOT
CLEAR = tc.CLEAR
CORR = float(os.environ.get("CORR", 12))
CELL = float(os.environ.get("CELL", 1.5))
MAX_ALT = float(os.environ.get("MAX_ALT", 20000))
MAXTURN = float(os.environ.get("MAXTURN", 100))
FREE = 3.0                                    # a vegpontok koruli ennyi km-en belul nem tiltott (a latnivalo maga lehet hegy)


def leg_bad(a, b, alt):
    """True, ha az a->b szakasz (savval) barhol kevesebb mint CLEAR szabad helyet hagy."""
    S, _ = tc.sample([a, b])
    flat = []
    for s in S:
        flat += [(s[0], s[1]), (s[2], s[3]), (s[4], s[5])]
    el = tc.elev_fetch(flat)
    worst = max(max(el[3 * i], el[3 * i + 1], el[3 * i + 2]) for i in range(len(S)))
    return worst + CLEAR > alt, worst


def corridor(a, b):
    """Racs a szakasz korul: (u: a szakasz menten, v: oldalirany) -> (la, lo)."""
    L = tc.hav(a[0], a[1], b[0], b[1])
    br = tc.brg(a[0], a[1], b[0], b[1])
    nu = int(L / CELL) + 1
    nv = int(CORR / CELL)
    grid = {}
    for i in range(nu + 1):
        la0, lo0 = tc.dest(a[0], a[1], br, min(i * CELL, L))
        for j in range(-nv, nv + 1):
            grid[(i, j)] = tc.dest(la0, lo0, br + math.pi / 2, j * CELL) if j else (la0, lo0)
    return grid, nu, nv, L


def astar(grid, nu, nv, el, alt, L):
    ok = {}
    for k in grid:
        i, j = k
        near_end = abs(j) * CELL < FREE and (i * CELL < FREE or (L - i * CELL) < FREE)
        ok[k] = near_end or el[k] + CLEAR <= alt
    start, goal = (0, 0), (nu, 0)
    ok[start] = ok[goal] = True
    edge = set(k for k in ok if ok[k] and any(not ok.get((k[0] + x, k[1] + y), True) for x in (-1, 0, 1) for y in (-1, 0, 1)))
    dirs = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (2, 1), (2, -1), (1, 2), (1, -2)]
    s0 = (start, None)
    pq = [(0.0, 0.0, s0)]
    best = {s0: 0.0}
    prev = {}
    while pq:
        f, g, st = heapq.heappop(pq)
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
            if not ok.get(n):
                continue
            if abs(dd[0]) == 2 and not ok.get((cur[0] + 1, cur[1] + (dd[1] > 0) - (dd[1] < 0) * 0)):
                continue
            if abs(dd[1]) == 2 and not ok.get((cur[0], cur[1] + (1 if dd[1] > 0 else -1))):
                continue
            step = math.hypot(dd[0], dd[1]) * CELL
            turn = 0.0
            if pd is not None:
                t = abs(math.degrees(math.atan2(dd[1], dd[0]) - math.atan2(pd[1], pd[0])))
                t = min(t, 360 - t)
                if t > MAXTURN:
                    continue
                turn = (t / 45.0) ** 2 * CELL * 0.6
            ng = g + step + turn + abs(n[1]) * 0.02 * CELL + (1.5 * CELL if n in edge else 0)    # tartson tavolsagot a hegyoldaltol
            ns = (n, dd)
            if ng < best.get(ns, 1e18):
                best[ns] = ng
                prev[ns] = st
                heapq.heappush(pq, (ng + math.hypot(goal[0] - n[0], goal[1] - n[1]) * CELL, ng, ns))
    return None


def simplify(pts, tol):
    """Douglas-Peucker a racs-uton (u, v km-ben)."""
    if len(pts) < 3:
        return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    nrm = math.hypot(dx, dy) or 1e-9
    dm, im = 0, 0
    for i in range(1, len(pts) - 1):
        d = abs(dy * pts[i][0] - dx * pts[i][1] + x2 * y1 - y2 * x1) / nrm
        if d > dm:
            dm, im = d, i
    if dm > tol:
        return simplify(pts[:im + 1], tol)[:-1] + simplify(pts[im:], tol)
    return [pts[0], pts[-1]]


def fix_leg(a, b, alt):
    """-> (uj_magassag, [koztes pontok (la, lo)]) vagy None."""
    grid, nu, nv, L = corridor(a, b)
    keys = list(grid)
    el = dict(zip(keys, tc.elev_fetch([grid[k] for k in keys])))
    a_alt = alt
    while a_alt <= MAX_ALT:
        path = astar(grid, nu, nv, el, a_alt, L)
        if path:
            uv = [(i * CELL, j * CELL) for i, j in path]
            simp = simplify(uv, CELL * 0.9)
            return a_alt, [grid[(round(u / CELL), round(v / CELL))] for u, v in simp[1:-1]]
        a_alt += 1000
    return None


def main():
    only = set(x for x in sys.argv[1:] if not x.startswith("-"))
    if os.path.exists(tc.CACHE):
        tc._cache.update(json.load(open(tc.CACHE)))
    ap = {}
    import gzip
    for ln in gzip.open(os.path.join(ROOT, "data", "airports_rwy.tsv.gz"), "rt", encoding="utf-8"):
        p = ln.split("\t")
        ap[p[0]] = (float(p[2]), float(p[3]))
    src = os.path.join(ROOT, "data", "tours.json")
    d = json.load(open(src, encoding="utf-8"))
    out = json.loads(json.dumps(d))
    rep = []
    try:
        for ti, t in enumerate(d["tours"]):
            if only and t["id"] not in only:
                continue
            for vi, v in enumerate(t["variants"]):
                pts_raw = v["pts"]
                pts = []
                for p in pts_raw:
                    if isinstance(p, str):
                        if p in ap:
                            pts.append((p, ap[p][0], ap[p][1]))
                    else:
                        pts.append((p[0], float(p[1]), float(p[2])))
                if len(pts) < 2:
                    continue
                alt = float(v["alt_ft"])
                newpts, newalt, notes, hard = [pts_raw[0]], alt, [], False
                for k in range(len(pts) - 1):
                    a, b = pts[k], pts[k + 1]
                    while True:
                        try:
                            bad, worst = leg_bad((a[1], a[2]), (b[1], b[2]), newalt)
                            break
                        except tc.Stop as e:
                            print("\n" + str(e) + " Egy ora mulva ujraprobalom (ablakot hagyd nyitva).")
                            time.sleep(3600)
                    if bad:
                        res = None
                        while True:
                            try:
                                res = fix_leg((a[1], a[2]), (b[1], b[2]), newalt)
                                break
                            except tc.Stop as e:
                                print("\n" + str(e) + " Egy ora mulva ujraprobalom (ablakot hagyd nyitva).")
                                time.sleep(3600)
                        if res:
                            na, via = res
                            if na > newalt:
                                notes.append("%s -> %s: a gerinc miatt a magassag %d -> %d ft" % (a[0], b[0], newalt, na)); newalt = na
                            if via:
                                notes.append("%s -> %s: %d uj terelo pont (volgyet koveti)" % (a[0], b[0], len(via)))
                            for la, lo in via:
                                newpts.append(["~", round(la, 4), round(lo, 4)])
                        else:
                            notes.append("%s -> %s: KEZZEL KELL MEGOLDANI (%d ft-ig sincs szabad atjaro; tegyel at pontot vagy hagyd el a szakaszt)" % (a[0], b[0], MAX_ALT)); hard = True
                    newpts.append(pts_raw[k + 1])
                if notes:
                    out["tours"][ti]["variants"][vi]["pts"] = newpts
                    out["tours"][ti]["variants"][vi]["alt_ft"] = int(newalt)
                    rep.append((t["id"], v["id"], notes, hard))
                    print("%s/%s:" % (t["id"], v["id"]))
                    for n in notes:
                        print("   " + n)
                    json.dump(out, open(os.path.join(ROOT, "data", "tours_javaslat.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
                    with open(os.path.join(ROOT, "terrain_javaslat.txt"), "w", encoding="utf-8") as f:
                        for r in rep:
                            f.write("%s/%s%s\n" % (r[0], r[1], "  [KEZI MUNKA KELL]" if r[3] else ""))
                            for n in r[2]:
                                f.write("   " + n + "\n")
                    try:
                        json.dump(tc._cache, open(tc.CACHE, "w"))
                    except Exception:
                        pass
    finally:
        try:
            json.dump(tc._cache, open(tc.CACHE, "w"))
        except Exception:
            pass
    print("\nKESZ. %d variáns kapott javaslatot. Fajlok: data/tours_javaslat.json, terrain_javaslat.txt" % len(rep))
    print("A javaslatot nezd at (kuld el nekem), mielott az eredeti data/tours.json helyere kerul.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nLeallitva.")
    except Exception as e:
        import traceback; traceback.print_exc()
    if os.name == "nt":
        input("\nNyomj Entert a bezarashoz...")
