"""Koruttura-pontok sorrendjenek optimalizalasa: ahol a kor (a felszallo/leszallo palyahoz igazitva) tul eles kanyart tartalmaz,
kiprobalja a koztes latnivalo-pontok osszes sorrendjet (a kezi '~' segedpontokat elhagyva), es a legjobbat menti a data/tours.json-ba.
Hasznalat: python3 tools/tours_reorder.py [--apply] [--limit 118]"""
import importlib.util, itertools, json, math, os, sys, copy
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sp = importlib.util.spec_from_file_location("app", os.path.join(ROOT, "app.py"))
m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
ad = m._ad_load()
LIM = 118
for i, a in enumerate(sys.argv):
    if a == "--limit":
        LIM = float(sys.argv[i + 1])


def resolve(pts):
    o = []
    for p in pts:
        if isinstance(p, str):
            a = ad[p]; o.append((p, a["lat"], a["lon"]))
        else:
            o.append((str(p[0]), float(p[1]), float(p[2])))
    return o


def turns(q):
    r = []
    for i in range(1, len(q) - 1):
        b1 = m.bearing(q[i - 1][1], q[i - 1][2], q[i][1], q[i][2]); b2 = m.bearing(q[i][1], q[i][2], q[i + 1][1], q[i + 1][2])
        r.append(abs((b2 - b1 + 540) % 360 - 180))
    return r


def score(q):
    t = turns(q)
    return max(t or [0]) + 0.3 * sum(x for x in t if x > 90)


def evalp(pts):
    q = m._tour_rwy_ends(pts, ad)
    return score(q), m._route_len(q)


d = json.load(open(os.path.join(ROOT, "data", "tours.json"), encoding="utf-8"))
chg = 0
for t in d["tours"]:
    for v in t["variants"]:
        raw = v["pts"]
        if len(raw) < 5 or not isinstance(raw[0], str) or raw[0] != raw[-1] or v.get("kind", "loop") != "loop":
            continue
        pts = resolve(raw)
        s0, l0 = evalp(pts)
        if s0 <= LIM:
            continue
        mid = [(raw[i], pts[i]) for i in range(1, len(raw) - 1) if not (not isinstance(raw[i], str) and str(raw[i][0]).startswith("~"))]
        if len(mid) < 3 or len(mid) > 7:
            continue
        best = (s0, l0, None)
        for perm in itertools.permutations(range(len(mid))):
            if perm[0] > perm[-1]:
                continue                                  # a megforditott sorrendet a futasi ido maga is kiprobalja
            q = [pts[0]] + [mid[k][1] for k in perm] + [pts[-1]]
            sc, ln = evalp(q)
            pen = sc + 60 * max(0.0, ln / l0 - 1.05)
            if pen < best[0] - 12 and (best[2] is None or pen < best[3]):
                best = (sc, ln, perm, pen)
        if best[2] is not None:
            nr = [raw[0]] + [mid[k][0] for k in best[2]] + [raw[-1]]
            print("%s/%s: %.0f -> %.0f  (%.0f -> %.0f km)  %s" % (t["id"], v["id"], s0, best[0], l0, best[1], [x if isinstance(x, str) else x[0] for x in nr]))
            v["pts"] = nr; chg += 1
print("modosult:", chg)
if "--apply" in sys.argv and chg:
    json.dump(d, open(os.path.join(ROOT, "data", "tours.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("mentve")
