#!/usr/bin/env python3
"""Automatikus javaslat a terepmiatt nem repulheto turaszakaszokra (a terrain_check.py folytatasa).

Szabalyok (variansonkent):
  1. Ha a legmagasabb gerinc + CLEAR legfeljebb 1000 ft-tal van a repulesi magassag folott (vagy a terep az egesz
     utvonalon a magassag korul jar, pl. fennsik), csak a magassagot emeli (500 ft-ra felkerekitve), utvonalat nem valtoztat.
  2. Kulonben a rossz szakaszokat kerul: a szakasz kore (+-CORR km) magassag-racsot olvas, es A* kereses talal egy szabad
     volgyet. A magas objektumoktol (csucsok, gerincek) lehetoleg DIL*CELL km tavolsagot tart (3 km, ha nem fer, kevesebbet).
     A hegyen levo latnivalot (nev marad) elobb a legkozelebbi szabad kilatpontra teszi (RELOC_MIN..RELOC km, alap 2..8 km).
     Egy valtozat magassaga legfeljebb MAX_JUMP (2000 ft)-tal emelkedhet, a "~" pontoknal > TURN_MAX (90 fok) forduloket kisimitja.
  3. Ha nincs atjaro, emeli a magassagot a szukseges szintre, legfeljebb MAX_ALT-ig (alap 15 000 ft).
  4. Az eredetileg MAX_ALT feletti turak (Everest, K2 ...) HI_ALT-ig (alap 20 000 ft) mehetnek, es kapnak egy
     "hi_alt": true jelzest: ezekhez magaslati repulesre alkalmas gep kell (a program figyelmeztetest mutat).
  5. Ha igy sem megy, "KEZZEL KELL MEGOLDANI" jelzes, a szukseges magassaggal egyutt.
Az eredeti data/tours.json-t NEM irja at: data/tours_javaslat.json + terrain_javaslat.txt.

Hasznalat: tools/terrain_fix.bat (dupla kattintas), vagy: python tools/terrain_fix.py [tura-id ...]
Kornyezeti valtozok: CLEAR (500 ft), CORR (12 km), CELL (1.5 km), MAX_ALT (15000), HI_ALT (20000), MAXTURN (100 fok)."""
import hashlib, heapq, json, math, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import terrain_check as tc

ROOT = tc.ROOT
CLEAR = tc.CLEAR
CORR = float(os.environ.get("CORR", 12))
CELL = float(os.environ.get("CELL", 1.5))
MAX_ALT = float(os.environ.get("MAX_ALT", 15000))
HI_ALT = float(os.environ.get("HI_ALT", 20000))
DIL = int(os.environ.get("DIL", 2))                # a magas teruletek koruli kerulo-sav (cella)
MAXTURN = float(os.environ.get("MAXTURN", 100))
RELOC = float(os.environ.get("RELOC", 8))        # a hegyen levo latnivalo legfeljebb ennyi km-re kerul arrebb (kilatopont)
RELOC_MIN = float(os.environ.get("RELOC_MIN", 2))
MAX_JUMP = float(os.environ.get("MAX_JUMP", 2000))  # ennel nagyobb magassag-emelest nem javasol, inkabb kezi munka
TURN_MAX = float(os.environ.get("TURN_MAX", 90))   # a "~" pontoknal ennel élesebb fordulot probal kisimitani
FREE = 3.0                                    # a vegpontok koruli ennyi km-en belul nem tiltott (a latnivalo maga lehet hegy)


def leg_bad(a, b, alt):
    """-> (rossz-e, legmagasabb terep (ft), a rossz mintak aranya 0..1)."""
    S, _ = tc.sample([a, b])
    flat = []
    for q in S:
        flat += [(q[0], q[1]), (q[2], q[3]), (q[4], q[5])]
    el = tc.elev_fetch(flat)
    m = [max(el[3 * i], el[3 * i + 1], el[3 * i + 2]) for i in range(len(S))]
    worst = max(m)
    frac = sum(1 for x in m if x + CLEAR > alt) / float(len(m))
    return worst + CLEAR > alt, worst, frac


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


def astar(grid, nu, nv, el, alt, L, dil=0):
    ok = {}
    for k in grid:
        i, j = k
        near_end = abs(j) * CELL < FREE and (i * CELL < FREE or (L - i * CELL) < FREE)
        ok[k] = near_end or el[k] + CLEAR <= alt
    if dil:
        blk = [k for k in ok if not ok[k]]
        for (i, j) in blk:
            for x in range(-dil, dil + 1):
                for y in range(-dil, dil + 1):
                    q = (i + x, j + y)
                    if q in ok and ok[q] and not (abs(q[1]) * CELL < FREE and (q[0] * CELL < FREE or (L - q[0] * CELL) < FREE)):
                        ok[q] = False
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
    """Kerulo ut az adott magassagon: [koztes pontok (la, lo)] (lehet ures), vagy None, ha nincs atjaro."""
    grid, nu, nv, L = corridor(a, b)
    keys = list(grid)
    el = dict(zip(keys, tc.elev_fetch([grid[k] for k in keys])))
    for dil in range(DIL, -1, -1):
        path = astar(grid, nu, nv, el, alt, L, dil)
        if path:
            uv = [(i * CELL, j * CELL) for i, j in path]
            simp = simplify(uv, CELL * 0.9)
            return [grid[(round(u / CELL), round(v / CELL))] for u, v in simp[1:-1]]
    return None


def _brg(a, b):
    p = math.pi / 180
    y = math.sin((b[1] - a[1]) * p) * math.cos(b[0] * p)
    x = math.cos(a[0] * p) * math.sin(b[0] * p) - math.sin(a[0] * p) * math.cos(b[0] * p) * math.cos((b[1] - a[1]) * p)
    return math.degrees(math.atan2(y, x)) % 360


def turn(a, b, c):
    d = abs(_brg(b, c) - _brg(a, b)) % 360
    return 360 - d if d > 180 else d


def point_max(la, lo):
    """a pont 1.5 km-es kornyezetenek legmagasabb terepe"""
    ps = [(la, lo)]
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ps.append((la + dy * 1.5 / 111.0, lo + dx * 1.5 / (111.0 * max(0.2, math.cos(math.radians(la))))))
    return max(tc.elev_fetch(ps))


def relocate(p, ref, alt, nxt=None):
    """Hegyen levo latnivalo -> szabad kilatopont (RELOC_MIN..RELOC km). Nem a legkozelebbit valasztja vakon, hanem azt, amelyik
    nem csinal hajtukanyart: a fordulo (elozo -> uj pont -> kovetkezo) ne legyen sokkal elesebb, mint eredetileg.
    -> (la, lo) vagy None"""
    la0, lo0 = p[1], p[2]
    kx = 111.0 * max(0.2, math.cos(math.radians(la0)))
    t0 = turn(ref, (la0, lo0), nxt) if nxt else 0
    lim = max(t0 + 15, 80)
    best = None
    r = RELOC_MIN
    while r <= RELOC + 1e-6:
        for k in range(24):
            ang = k * math.pi / 12
            c = (la0 + r * math.cos(ang) / 111.0, lo0 + r * math.sin(ang) / kx)
            if point_max(*c) > alt - CLEAR:
                continue
            tt = turn(ref, c, nxt) if nxt else 0
            sc = r + (0 if tt <= lim else 4.0 + (tt - lim) * 0.5) + 0.002 * tc.hav(c[0], c[1], ref[0], ref[1])
            if best is None or sc < best[0]:
                best = (sc, c, tt)
        r += 1.0
    return best[1] if best else None


def smooth(pts, alt, ap, notes):
    """A '~' terelopontokat, amelyeknel a fordulo > TURN_MAX fok, elhagyja, ha az igy kialakulo szakasz szabad maradt."""
    def xy(p):
        return (ap[p][0], ap[p][1]) if isinstance(p, str) else (p[1], p[2])
    pts = list(pts)
    changed = True
    while changed:
        changed = False
        for k in range(1, len(pts) - 1):
            p = pts[k]
            if isinstance(p, str) or p[0] != "~":
                continue
            if pts[k - 1] is None or (isinstance(pts[k - 1], str) and pts[k - 1] not in ap) or (isinstance(pts[k + 1], str) and pts[k + 1] not in ap):
                continue
            a, b, c = xy(pts[k - 1]), xy(p), xy(pts[k + 1])
            if turn(a, b, c) > TURN_MAX:
                bad, _, _ = retry(leg_bad, a, c, alt)
                if not bad:
                    del pts[k]
                    notes.append("eles fordulo (%d fok) kisimitva: egy '~' pont elhagyva" % turn(a, b, c))
                    changed = True
                    break
    return pts


def up500(x):
    return int(math.ceil(x / 500.0) * 500)


def retry(fn, *args):
    while True:
        try:
            return fn(*args)
        except tc.Stop as e:
            print("\n" + str(e) + " Egy ora mulva ujraprobalom (ablakot hagyd nyitva).")
            time.sleep(3600)


def process(v, ap):
    """-> (uj_pts, uj_alt, notes, hard, hi) vagy None, ha nincs mit javitani."""
    pts_raw = v["pts"]
    pts = []
    for p in pts_raw:
        if isinstance(p, str):
            if p in ap:
                pts.append((p, ap[p][0], ap[p][1]))
        else:
            pts.append((p[0], float(p[1]), float(p[2])))
    if len(pts) < 2:
        return None
    alt0 = float(v["alt_ft"])
    cap = HI_ALT if alt0 > MAX_ALT else MAX_ALT
    pre = []
    for k in range(1, len(pts) - 1):
        a, p = pts[k - 1], pts[k]
        if p[0] == "~" or p[0] in ap or isinstance(pts_raw[k], str):
            continue
        if retry(point_max, p[1], p[2]) > alt0 - CLEAR:
            q = retry(relocate, p, (a[1], a[2]), alt0, (pts[k + 1][1], pts[k + 1][2]))
            if q:
                d = tc.hav(p[1], p[2], q[0], q[1])
                pts[k] = (p[0], round(q[0], 4), round(q[1], 4))
                pre.append("%s: hegyen van -> kilatopont %.1f km-re (%.4f, %.4f)" % (p[0], d, q[0], q[1]))
    if pre:
        pts_raw = [pts_raw[0]] + [[x[0], x[1], x[2]] for x in pts[1:-1]] + [pts_raw[-1]] if len(pts) == len(pts_raw) else pts_raw
    legs = []
    for k in range(len(pts) - 1):
        a, b = pts[k], pts[k + 1]
        bad, worst, frac = retry(leg_bad, (a[1], a[2]), (b[1], b[2]), alt0)
        legs.append((a, b, bad, worst, frac))
    if not any(l[2] for l in legs):
        if pre:
            return (pts_raw, alt0, pre, False, alt0 > MAX_ALT)
        return (pts_raw, alt0, [], False, alt0 > MAX_ALT) if alt0 > MAX_ALT and not v.get("hi_alt") else None
    need = up500(max(l[3] for l in legs) + CLEAR)
    total = sum(tc.hav(a[1], a[2], b[1], b[2]) for a, b, _, _, _ in legs)
    badkm = sum(tc.hav(a[1], a[2], b[1], b[2]) * fr for a, b, _, _, fr in legs)
    notes, hard = list(pre), False
    # 1. csak magassag-emeles: kis tullogas, vagy a terep az egesz utvonalon a repulesi magassag korul jar
    if need <= cap and (need - alt0 <= 1000 or (badkm >= 0.45 * total and need - alt0 <= MAX_JUMP)):
        notes.append("magassag %d -> %d ft (a gerinc/fennsik miatt; utvonal valtozatlan)" % (alt0, need))
        return (pts_raw, float(need), notes, False, need > MAX_ALT)
    # 2. kerulo szakaszonkent
    newpts, fail = [pts_raw[0]], []
    pi = 0
    for k, (a, b, bad, worst, frac) in enumerate(legs):
        if bad:
            via = retry(fix_leg, (a[1], a[2]), (b[1], b[2]), alt0)
            if via is None:
                fail.append((a, b, worst))
            elif via:
                notes.append("%s -> %s: %d terelo pont (volgyet koveti, magas teruletektol tavol)" % (a[0], b[0], len(via)))
                for la, lo in via:
                    newpts.append(["~", round(la, 4), round(lo, 4)])
        newpts.append(pts_raw[k + 1] if len(pts_raw) == len(pts) else [pts[k + 1][0], round(pts[k + 1][1], 4), round(pts[k + 1][2], 4)])
    alt = alt0
    if fail:
        nf = up500(max(f[2] for f in fail) + CLEAR)
        if nf <= cap and nf - alt0 <= MAX_JUMP:
            alt = float(nf)
            notes.append("nincs atjaro %d szakaszon -> magassag %d -> %d ft" % (len(fail), alt0, nf))
        else:
            hard = True
            for a, b, w in fail:
                notes.append("%s -> %s: KEZZEL KELL MEGOLDANI (nincs atjaro; ehhez %d ft kellene, plafon %d ft, max. emeles %d ft)" % (a[0], b[0], up500(w + CLEAR), cap, MAX_JUMP))
    if not hard:
        newpts = smooth(newpts, alt, ap, notes)
    return (newpts, alt, notes, hard, alt > MAX_ALT)


def main():
    only = set(x for x in sys.argv[1:] if not x.startswith("-"))
    if os.path.exists(tc.CACHE):
        tc._cache.update(json.load(open(tc.CACHE)))
    ap = {}
    import gzip
    for ln in gzip.open(os.path.join(ROOT, "data", "airports_rwy.tsv.gz"), "rt", encoding="utf-8"):
        p = ln.split("\t")
        ap[p[0]] = (float(p[2]), float(p[3]))
    d = json.load(open(os.path.join(ROOT, "data", "tours.json"), encoding="utf-8"))
    out = json.loads(json.dumps(d))
    rep = []
    hi = []
    try:
        for ti, t in enumerate(d["tours"]):
            if only and t["id"] not in only:
                continue
            for vi, v in enumerate(t["variants"]):
                r = process(v, ap)
                if not r:
                    continue
                newpts, newalt, notes, hard, high = r
                ov = out["tours"][ti]["variants"][vi]
                ov["pts"] = newpts
                ov["alt_ft"] = int(newalt)
                if high:
                    ov["hi_alt"] = True
                    hi.append("%s/%s (%d ft)" % (t["id"], v["id"], newalt))
                if notes or high:
                    rep.append((t["id"], v["id"], notes, hard, high))
                    print("%s/%s:%s" % (t["id"], v["id"], "  [KEZI MUNKA KELL]" if hard else ""))
                    for n in notes:
                        print("   " + n)
                    json.dump(out, open(os.path.join(ROOT, "data", "tours_javaslat.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
                    with open(os.path.join(ROOT, "terrain_javaslat.txt"), "w", encoding="utf-8") as f:
                        for q in rep:
                            f.write("%s/%s%s%s\n" % (q[0], q[1], "  [KEZI MUNKA KELL]" if q[3] else "", "  [MAGASLATI GEP KELL]" if q[4] else ""))
                            for n in q[2]:
                                f.write("   " + n + "\n")
    finally:
        try:
            json.dump(tc._cache, open(tc.CACHE, "w"))
        except Exception:
            pass
    hardn = sum(1 for r in rep if r[3])
    print("\nKESZ. %d variáns kapott javaslatot, ebbol %d-nél kezi munka is kell; %d variáns magaslati (>%d ft) jelzest kapott." % (len(rep), hardn, len(hi), MAX_ALT))
    print("Fajlok: data/tours_javaslat.json, terrain_javaslat.txt. Kuldd el nekem atnezesre, mielott az eredeti helyere kerul.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nLeallitva.")
    except Exception:
        import traceback; traceback.print_exc()
    if os.name == "nt":
        input("\nNyomj Entert a bezarashoz...")
