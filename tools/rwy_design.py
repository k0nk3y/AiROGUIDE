#!/usr/bin/env python3
"""Kezzel tervezett, kifutohoz igazitott korok (felszallas/leszallas a kifuto tengelyen). python3 rwy_design.py [--apply]"""
import json, math, os, sys
from tours_check import hav, brg, ROOT
from tours_order import dest, swing
from rwy_opt import rwys, tn, cross, pl

def F(ic, hd_land, km=10.0):          # megkozelitesi pont: a leszallo kifuto hosszabbitasaban, a kuszob elott
    (la, lo), _ = rwys(ic); p = dest((ic, la, lo), (hd_land + 180) % 360, km); return ["~=", round(p[0], 4), round(p[1], 4)]
def D(ic, hd_dep, km=7.0):
    (la, lo), _ = rwys(ic); p = dest((ic, la, lo), hd_dep, km); return ["~=", round(p[0], 4), round(p[1], 4)]

# tura: (kifuto-fel irany, [pontok: nev | ["~=",lat,lon] | ("F", leszallo_irany, km) | ("D", fel_irany, km) | ("~",)])
SPEC = {
 "asmara-massawa": (70, ["Asmara Modernist City", "Massawa", "Dahlak Kebir", "SW", "Qohaito", ("F", 300, 10)]),
 "sao-tome": (110, ["São Sebastião Fort", "Rolas Equator Monument", ["~", 0.0198, 6.4862], "Pico Cão Grande", "Lagoa Azul", ["~=", 0.49, 6.60], ("F", 110, 14)]),
 "alula": (300, ["Dadan", "Hegra", ["~", 26.8137, 38.0116], ["~=", 26.55, 38.32], ("F", 300, 12)]),
 "coxs-bazar": (170, ["Teknaf", "Saint Martin's Island", "Cox's Bazar Beach"]),
 "dunhuang": (260, ["Crescent Lake", "Dunhuang Yardang", ["~", 40.4541, 93.316], "Yumen Pass"]),
 "paraguay-jesuit": (20, ["Trinidad Mission", "Jesús de Tavarangue", "Itaipu Dam", "SW", "Yacyretá Reservoir", ("F", 20, 10)]),
 "vanuatu-tanna": (290, ["Hideaway Island", "SW", "Mount Yasur", ("F", 290, 10)]),
 "samoa-upolu": (260, ["Mount Matavanu", "SW", "Savai'i Lava Fields", "To Sua Ocean Trench", ("F", 260, 10)]),
}
def build(t, v, dep, spec):
    ic = v["pts"][0]; (la, lo), _ = rwys(ic)
    known = {}
    for p in v["pts"][1:-1] + [x for x in t.get("pois", [])]:
        if not isinstance(p, str) and not str(p[0]).startswith("~"): known[p[0]] = p
    out = [ic]
    for s in spec:
        if isinstance(s, str):
            if s == "SW": out.append("SW")
            else: out.append(list(known[s]))
        elif isinstance(s, tuple): out.append(F(ic, s[1], s[2]) if s[0] == "F" else D(ic, s[1], s[2]))
        else: out.append(s)
    out.append(ic); return out

def report(ic, pts):
    (la, lo), _ = rwys(ic); A = (ic, la, lo)
    P = [A] + [(p, p[1], p[2]) for p in pts[1:-1]] + [A]
    X = pl(P); hs = [brg(P[i], P[i+1]) for i in range(len(P)-1)]
    turns = [round(tn(hs[i], hs[i+1])) for i in range(len(hs)-1)]
    x = sum(1 for i in range(len(P)-1) for j in range(i+2, len(P)-1) if cross(X[i], X[i+1], X[j], X[j+1]))
    return turns, x

if __name__ == "__main__":
    d = json.load(open(os.path.join(ROOT, "data", "tours.json"), encoding="utf-8"))
    for t in d["tours"]:
        if t["id"] in SPEC:
            v = t["variants"][0]; dep, spec = SPEC[t["id"]]
            pts = build(t, v, dep, spec)
            # SW: swing lesz a tours_order-ben; itt a hajtukanyart 'SW' helyen szelidito ponttal oldjuk meg
            P = [pts[0]] + [p for p in pts[1:-1]] + [pts[-1]]
            res = []
            (la, lo), _ = rwys(pts[0]); A = (pts[0], la, lo)
            Q = [A]; 
            for p in P[1:-1]:
                if p == "SW":
                    a, b = Q[-1], None; Q.append("SW")
                else: Q.append((p, p[1], p[2]))
            # SW kitoltese: kovetkezo ponttal dontunk
            out = [Q[0]]
            for i in range(1, len(Q)):
                if Q[i] == "SW":
                    prev, nxt = out[-1], Q[i+1]
                    h1, h2 = brg(prev, nxt) if False else None, None
                    out.append("SW")
                else: out.append(Q[i])
            # egyszeru: a SW helyet a swing() adja a vegso listaban
            pts2 = [pts[0]] + [p for p in pts[1:-1] if p != "SW"] + [pts[-1]]
            PP = [A] + [(p, p[1], p[2]) for p in pts2[1:-1]] + [A]
            S = swing(PP)
            for _ in range(3):
                S2 = swing(S)
                if len(S2) == len(S): break
                S = S2
            if t["id"] == "dunhuang" and not any(str(e[0]) == "Mogao Caves" for e in t.get("pois", [])): t.setdefault("pois", []).append(["Mogao Caves", 40.138, 94.81])
            v["pts"] = [pts[0]] + [x[0] for x in S[1:-1]] + [pts[-1]]
            tr, x = report(pts[0], v["pts"])
            print(t["id"], "fordulok", tr, "keresztezes", x, "max", max(map(abs, tr)))
    if "--apply" in sys.argv:
        json.dump(d, open(os.path.join(ROOT, "data", "tours.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
