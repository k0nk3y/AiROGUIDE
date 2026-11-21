#!/usr/bin/env python3
"""Velence es Dolomitok szetvalasztasa: a Dolomitok csak a ket Bolzano-kor, Velence kap egy rovid varos-lagunas kort."""
import json, os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "tours.json")
d = json.load(open(P, encoding="utf-8"))
idx = {t["id"]: t for t in d["tours"]}
dol = idx["dolomites"]
dol["variants"] = [v for v in dol["variants"] if v["id"] != "ab"]
dol["name"] = {"en": "The Dolomites", "hu": "A Dolomitok"}
dol["tags"] = ["mountain", "unesco"]
dol["desc"] = {"en": "The pale rock towers of the Dolomites from Bolzano: Rosengarten, Sassolungo, Marmolada, the Tre Cime and Lago di Braies.",
               "hu": "A Dolomitok világos sziklatornyai Bolzanóból: Catinaccio, Sassolungo, Marmolada, a Tre Cime és a Braies-tó."}
ven = idx["venice"]
v = dict(id="city", kind="loop", kt=95, alt_ft=1800, stol=False,
         label={"en": "Venice highlights", "hu": "Velence látnivalói"},
         desc={"en": "A short loop over Torcello, Burano, St Mark's, the Lido and Murano, circling the southern lagoon.",
               "hu": "Rövid kör Torcello, Burano, a Szent Márk tér, a Lido és Murano felett, a déli lagúnát megkerülve."},
         pts=["LIPZ", ["Torcello", 45.4975, 12.4177], ["Burano", 45.485, 12.417], ["St Mark's Basilica", 45.434, 12.3397],
              ["Lido di Venezia", 45.4033, 12.367], ["~", 45.3317, 12.3117], ["~", 45.36, 12.21], ["~", 45.44, 12.26],
              ["Murano", 45.459, 12.353], "LIPZ"])
ven["variants"] = [w for w in ven["variants"] if w["id"] != "city"]
ven["variants"].insert(0, v)
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
dol["pois"] = []
dol["new"] = ven["new"] = True
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
