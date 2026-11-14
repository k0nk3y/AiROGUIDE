#!/usr/bin/env python3
"""Repuloter+palya adatbazis epitese az OurAirports (kozkincs) CSV-kbol.
Hasznalat: python build_airports.py <ourairports-data mappa> <kimenet.tsv.gz>
Kimenet soronkent: ICAO, nev, lat, lon, elev_ft, tipus, orszag, telepules, palyak
palyak = ';'-vel elvalasztva: azon|hossz_ft|szeles_ft|felulet|vilagitas|lezart   (felulet: H kemeny, G fu, V kavics, D fold, W viz, S ho/jeg, U ismeretlen)"""
import csv, gzip, sys, os, re

def surf(s):
    s = (s or "").strip().upper()
    if not s or s in ("UNK", "UNKNOWN", "X", "N"):
        return "U"
    if re.search(r"WAT", s): return "W"
    if re.search(r"SNOW|ICE|^SNO", s): return "S"
    if re.search(r"PI.ARRA", s): return "V"
    if re.search(r"ASFALT|^HARD|HARD", s): return "H"
    if s in ("SAN", "CLA", "TER") or s.startswith("SAND"): return "D"
    if re.search(r"ASP|CON|BIT|TAR|PEM|PAVED|MAC|CEM|PSP|TARMAC|TAR|PER|ASPH|CONC", s) or s in ("C", "A", "B", "P"): return "H"
    if re.search(r"GRV|GRAV|GVL|COR|CRUSH|STONE|SHELL|PIC|SOD|ROCK|CINDER|LATER", s) and "SOD" not in s: return "V"
    if re.search(r"TURF|GRS|GRASS|GRE|SOD|GRAS|^G$|-G$", s): return "G"
    if re.search(r"DIRT|EARTH|SAND|CLAY|GROUND|LOAM|MUD|SOIL|DRT|^D$|^S$", s): return "D"
    return "U"

src, out = sys.argv[1], sys.argv[2]
rw = {}
for r in csv.DictReader(open(os.path.join(src, "runways.csv"), encoding="utf-8")):
    try:
        L = int(float(r["length_ft"] or 0)); W = int(float(r["width_ft"] or 0))
    except ValueError:
        L = W = 0
    if L <= 0:
        continue
    ident = "%s/%s" % (r["le_ident"], r["he_ident"]) if r["he_ident"] else r["le_ident"]
    rw.setdefault(r["airport_ident"], []).append("%s|%d|%d|%s|%s|%s" % (ident.replace("|", "").replace(";", ""), L, W, surf(r["surface"]), r["lighted"] or "0", r["closed"] or "0"))
n = 0
with gzip.open(out, "wt", encoding="utf-8") as f:
    for r in csv.DictReader(open(os.path.join(src, "airports.csv"), encoding="utf-8")):
        if r["type"] in ("closed",):
            continue
        ident = r["ident"]
        rws = rw.get(ident, [])
        if r["type"] in ("heliport", "balloonport") and not rws:
            continue
        if r["type"] == "seaplane_base" and not rws:
            rws = ["WATER|0|0|W|0|0"]
        try:
            el = int(float(r["elevation_ft"] or 0))
        except ValueError:
            el = 0
        f.write("\t".join([ident, r["name"].replace("\t", " "), r["latitude_deg"], r["longitude_deg"], str(el), r["type"], r["iso_country"], r["municipality"].replace("\t", " "), ";".join(rws)]) + "\n")
        n += 1
print(n, "repuloter")
