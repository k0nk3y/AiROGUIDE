#!/usr/bin/env python3
"""5. kor: STOL turak (rovid palyas, kulonleges repterek). Sorrend: add_r5 -> tours_order <r5_ids> -> poi_registry -> tours_kw -> tours_img -> tours_check"""
from tourlib import *
import json, os
C = lambda e, h: (e, h)
FR = C("France", "Franciaország"); UK = C("United Kingdom", "Egyesült Királyság"); CN_ = C("Caribbean Netherlands", "Karibi Hollandia"); BL = C("Saint Barthélemy", "Saint-Barthélemy"); US = C("United States", "Egyesült Államok")
CONT = {}


def add(cont, *a, **k):
    tour(*a, **k); CONT[a[0]] = cont


def Pt(n, la, lo): return [n, la, lo]


add("EU", "courchevel", FR, ("Courchevel and the Savoie Alps", "Courchevel és a savoyai Alpok"), ("Courchevel Altiport", "Courchevel altiport", 45.3975, 6.6350), ["mountain", "stol"],
    ("The most famous altiport in the world: a 537 m runway with an 18.5 % slope, a hop away from Val Thorens, the Grande Motte glacier and Mont Blanc.", "A világ leghíresebb altiportja: 537 méteres, 18,5 százalékos lejtésű pálya, karnyújtásnyira a Val Thorenstől, a Grande Motte gleccsertől és a Mont Blanctól."), [],
    [("short", "loop", 100, 12000, ("Three Valleys", "Három völgy"), ("From the Courchevel altiport over Val Thorens, the Grande Motte glacier and Mont Pourri.", "A courchevel-i altiportról Val Thorens, a Grande Motte gleccser és a Mont Pourri felett."),
      ["LFLJ", Pt("Val Thorens", 45.2979, 6.5800), Pt("Grande Motte", 45.4264, 6.9014), Pt("Mont Pourri", 45.5000, 6.8190), "LFLJ"]),
     ("long", "loop", 105, 14000, ("Mont Blanc round trip", "Mont Blanc-kör"), ("About an hour: Val Thorens, the Grande Motte, Mont Blanc and the Roselend lake.", "Kb. egy óra: Val Thorens, a Grande Motte, a Mont Blanc és a Roselend-tó."),
      ["LFLJ", Pt("Val Thorens", 45.2979, 6.5800), Pt("Grande Motte", 45.4264, 6.9014), Pt("Mont Blanc", 45.8326, 6.8652), Pt("Lac de Roselend", 45.7100, 6.6500), Pt("Méribel", 45.3970, 6.5650), "LFLJ"])])
add("EU", "barra-st-kilda", UK, ("Barra and St Kilda", "Barra és St Kilda"), ("Traigh Mhòr beach", "Traigh Mhòr strand", 57.0228, -7.4430), ["island", "coast", "unesco", "stol"],
    ("Land on the beach: the only airport in the world where the tide sets the schedule, with Mingulay's cliffs and the remote archipelago of St Kilda.", "Leszállás a strandon: az egyetlen repülőtér a világon, ahol az apály-dagály szabja az órarendet, Mingulay sziklafalaival és a távoli St Kilda-szigetcsoporttal."), [],
    [("loop", "loop", 100, 2500, ("St Kilda round trip", "St Kilda-kör"), ("From the beach airport to Mingulay, out over the Atlantic to St Kilda and back via Eaval on North Uist.", "A strandrepülőtérről Mingulay-hoz, az Atlanti-óceán felett St Kildára és vissza Észak-Uist Eaval-jánál át."),
      ["EGPR", Pt("Mingulay", 56.8040, -7.6370), Pt("St Kilda", 57.8140, -8.5860), Pt("Eaval", 57.6000, -7.1700), "EGPR"])])
add("NA", "saba-statia", CN_, ("Saba, Statia and St Kitts", "Saba, Statia és St Kitts"), ("Mount Scenery", "Mount Scenery", 17.6347, -63.2327), ["island", "volcano", "stol"],
    ("Takeoff from a 400 m runway on a cliff: the volcanic cones of Saba, The Quill on St Eustatius and Mount Liamuiga on St Kitts.", "Felszállás egy sziklaperemen álló 400 méteres pályáról: Saba vulkáni kúpja, a Quill St Eustatiuson és a Mount Liamuiga St Kittsen."), [],
    [("loop", "loop", 100, 3500, ("Three volcanoes", "Három vulkán"), ("From Saba over St Eustatius and St Kitts and back past Brimstone Hill.", "Sabáról St Eustatius és St Kitts felett, majd a Brimstone Hill mellett vissza."),
      ["TNCS", Pt("The Quill", 17.4770, -62.9610), Pt("Mount Liamuiga", 17.3700, -62.8010), Pt("Brimstone Hill Fortress", 17.3490, -62.8700), "TNCS"])])
add("NA", "st-barth", BL, ("St Barths and Maho Beach", "St Barth és Maho Beach"), ("Gustavia", "Gustavia", 17.8960, -62.8500), ["island", "coast", "stol"],
    ("A famously steep approach over a hill, white-sand coves and the jets skimming the beach at Maho on neighbouring Sint Maarten.", "Híresen meredek leszállás egy domb felett, fehér homokos öblök és a szomszédos Sint Maarten Maho strandja fölött suhanó utasszállítók."), [],
    [("loop", "loop", 95, 2000, ("St Barths and Sint Maarten", "St Barth és Sint Maarten"), ("Gustavia, the Île Fourchue, Maho Beach and Anguilla's Shoal Bay.", "Gustavia, az Île Fourchue, a Maho Beach és Anguilla Shoal Bay-e."),
      ["TFFJ", Pt("Gustavia", 17.8960, -62.8500), Pt("Île Fourchue", 17.9000, -62.9900), Pt("Maho Beach", 18.0410, -63.1090), Pt("Shoal Bay", 18.2150, -63.0100), "TFFJ"])])
add("NA", "mccarthy", US, ("Wrangell Mountains from McCarthy", "A Wrangell-hegység McCarthyból"), ("Kennecott Mine", "Kennecott bánya", 61.4838, -142.8886), ["mountain", "volcano", "unesco", "stol"],
    ("A gravel strip at the end of the road in Alaska's largest national park: the ghost mine of Kennecott, huge glaciers and the volcano Mount Wrangell.", "Kavicsos leszállópálya az alaszkai legnagyobb nemzeti park útjának végén: a Kennecott kísértetbánya, hatalmas gleccserek és a Wrangell vulkán."), [],
    [("long", "loop", 105, 12000, ("Mount Wrangell", "Mount Wrangell"), ("About an hour and a half: Kennecott, Mount Blackburn and the steaming volcano Mount Wrangell.", "Kb. másfél óra: Kennecott, a Mount Blackburn és a gőzölgő Wrangell vulkán."),
      ["PAMX", Pt("Kennecott Mine", 61.4838, -142.8886), Pt("Mount Blackburn", 61.7300, -143.4300), Pt("Mount Wrangell", 62.0050, -144.0190), Pt("Chitina", 61.5230, -144.4400), "PAMX"])])
add("NA", "telluride", US, ("Telluride and the San Juan Mountains", "Telluride és a San Juan-hegység"), ("Mount Sneffels", "Mount Sneffels", 38.0039, -107.7920), ["mountain", "stol"],
    ("One of the highest airports in the US at 9,070 ft, on a mesa above the town, with fourteeners all around and the 'Switzerland of America' at Ouray.", "Az Egyesült Államok egyik legmagasabban fekvő repülőtere, 2764 méteren, egy fennsík szélén a város fölött, körülötte tizennégyezresek és Ouray, „Amerika Svájca”."), [],
    [("loop", "loop", 110, 14500, ("San Juan loop", "San Juan-kör"), ("Over Lizard Head Pass, Silverton, Ouray and Mount Sneffels.", "A Lizard Head-hágó, Silverton, Ouray és a Mount Sneffels felett."),
      ["KTEX", Pt("Lizard Head", 37.8000, -107.9170), Pt("Silverton", 37.8120, -107.6640), Pt("Ouray", 38.0228, -107.6714), Pt("Mount Sneffels", 38.0039, -107.7920), "KTEX"])])

for t in T:
    t["continent"] = CONT[t["id"]]
    for v in t["variants"]:
        v["stol"] = True
NEW = [t["id"] for t in T]
save()
d = json.load(open(P, encoding="utf-8"))
REV = set(open(os.path.join(os.path.dirname(P), "..", "tools", "reviewed.txt"), encoding="utf-8").read().split())
for t in d["tours"]:
    if t["id"] in NEW and t["id"] not in REV:
        t["new"] = True
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(os.path.join(os.path.dirname(P), "..", "tools", "r5_ids.txt"), "w").write(" ".join(NEW))
print(len(NEW), "uj tura")
