#!/usr/bin/env python3
"""1. csomag (Europa): tours.json bovitese. Ujrafuttathato: a meglevo azonositokat nem duplazza, a frissit."""
import json, os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "tours.json")
T = []


def tour(id, country, name, main, tags, desc, pois, variants, cont="EU"):
    T.append({"id": id, "continent": cont, "country": {"en": country[0], "hu": country[1]}, "name": {"en": name[0], "hu": name[1]},
              "main": {"en": main[0], "hu": main[1], "lat": main[2], "lon": main[3]}, "tags": tags, "desc": {"en": desc[0], "hu": desc[1]},
              "variants": [dict(id=v[0], kind=v[1], kt=v[2], alt_ft=v[3], stol=False, label={"en": v[4][0], "hu": v[4][1]}, desc={"en": v[5][0], "hu": v[5][1]}, pts=v[6]) for v in variants],
              "pois": pois})


tour("budapest", ("Hungary", "Magyarország"), ("Budapest and the Danube Bend", "Budapest és a Dunakanyar"), ("Hungarian Parliament", "Országház", 47.5072, 19.0456), ["city", "culture", "unesco"],
     ("The Danube through the Hungarian capital, then north to the river's great bend with Szentendre, the Visegrád citadel and Esztergom Basilica.",
      "A Duna Budapesten át, majd északra a folyó nagy kanyarjáig: Szentendre, a visegrádi fellegvár és az esztergomi bazilika."),
     [["Heroes' Square", 47.5149, 19.0780], ["Fisherman's Bastion", 47.5020, 19.0347], ["Margaret Bridge", 47.5155, 19.0452]],
     [("city", "loop", 100, 1800, ("Budapest city loop", "Budapesti városkör"), ("Short loop over the Budapest landmarks: Gellért Hill, Buda Castle, Parliament and Margaret Island.", "Rövid kör Budapest nevezetességei felett: a Gellért-hegy, a budai vár, az Országház és a Margitsziget."),
       ["LHBP", ["Gellért Hill", 47.4862, 19.0460], ["Buda Castle", 47.4961, 19.0396], ["Hungarian Parliament", 47.5072, 19.0456], ["Margaret Island", 47.5260, 19.0480], "LHBP"]),
      ("bend", "loop", 105, 2000, ("Danube Bend", "Dunakanyar"), ("The city landmarks plus the Danube Bend: Szentendre, the Visegrád citadel and Esztergom Basilica.", "A városi látnivalók és a Dunakanyar: Szentendre, a visegrádi fellegvár és az esztergomi bazilika."),
       ["LHBP", ["Gellért Hill", 47.4862, 19.0460], ["Buda Castle", 47.4961, 19.0396], ["Hungarian Parliament", 47.5072, 19.0456], ["Szentendre", 47.6694, 19.0756], ["Visegrád Citadel", 47.7889, 18.9686], ["Esztergom Basilica", 47.7993, 18.7390], "LHBP"])])

tour("balaton", ("Hungary", "Magyarország"), ("Lake Balaton", "Balaton"), ("Tihany Abbey", "Tihanyi apátság", 46.9136, 17.8885), ["coast", "culture"],
     ("Central Europe's largest lake from the air: the Hévíz thermal lake, Keszthely palace, the volcanic hills of Badacsony and the Tihany peninsula.",
      "Közép-Európa legnagyobb tava a levegőből: a hévízi tó, a keszthelyi kastély, a badacsonyi vulkáni hegyek és a Tihanyi-félsziget."),
     [["Balatonfüred", 46.9560, 17.8900], ["Szigliget Castle", 46.8000, 17.4300]],
     [("loop", "loop", 100, 2200, ("Balaton circuit", "Balaton-kör"), ("From Hévíz-Balaton Airport over Keszthely and Badacsony to Tihany and Siófok, and back.", "A Hévíz–Balaton repülőtérről Keszthely és Badacsony felett Tihanyba és Siófokra, majd vissza."),
       ["LHSM", ["Hévíz Lake", 46.7894, 17.1927], ["Festetics Palace, Keszthely", 46.7655, 17.2458], ["Badacsony", 46.7993, 17.5000], ["Tihany Abbey", 46.9136, 17.8885], ["Siófok", 46.9060, 18.0570], "LHSM"])])

tour("rome-naples", ("Italy", "Olaszország"), ("Rome to Naples classics", "Róma – Nápoly klasszikusok"), ("Colosseum", "Colosseum", 41.8902, 12.4922), ["city", "culture", "unesco", "volcano"],
     ("Ancient Rome, the Vatican, then south to Pompeii, Mount Vesuvius and the island of Capri.", "Az ókori Róma, a Vatikán, majd délre Pompeji, a Vezúv és Capri szigete."),
     [["Roman Forum", 41.8925, 12.4853], ["Trevi Fountain", 41.9009, 12.4833]],
     [("ab", "ab", 120, 3000, ("Rome to Naples", "Rómától Nápolyig"), ("One-way flight from Ciampino over the Colosseum and St Peter's, then Pompeii, Vesuvius and Capri to Naples.", "Egyirányú repülés Ciampinóból a Colosseum és a Szent Péter-bazilika felett Pompejibe, a Vezúvhoz és Capriba, Nápolyba."),
       ["LIRA", ["Colosseum", 41.8902, 12.4922], ["St Peter's Basilica", 41.9022, 12.4539], ["Pompeii", 40.7511, 14.4869], ["Mount Vesuvius", 40.8213, 14.4262], ["Capri", 40.5528, 14.2417], "LIRN"])])

tour("amalfi", ("Italy", "Olaszország"), ("Amalfi Coast and Capri", "Amalfi-part és Capri"), ("Positano", "Positano", 40.6281, 14.4850), ["coast", "island", "unesco"],
     ("The cliffs of the Amalfi Coast: Ravello, Amalfi, Positano and Sorrento, with Capri and Vesuvius on either side.", "Az Amalfi-part sziklái: Ravello, Amalfi, Positano és Sorrento, Capri és a Vezúv két oldalán."),
     [["Villa Rufolo, Ravello", 40.6490, 14.6119], ["Marina Piccola, Capri", 40.5437, 14.2430]],
     [("loop", "loop", 100, 2500, ("Amalfi loop", "Amalfi-kör"), ("From Naples over Vesuvius and Pompeii to Amalfi, Positano, Sorrento and Capri, back to Naples.", "Nápolyból a Vezúv és Pompeji felett Amalfiba, Positanóba, Sorrentóba és Capriba, majd vissza."),
       ["LIRN", ["Mount Vesuvius", 40.8213, 14.4262], ["Pompeii", 40.7511, 14.4869], ["Amalfi", 40.6340, 14.6027], ["Positano", 40.6281, 14.4850], ["Sorrento", 40.6263, 14.3758], ["Capri", 40.5528, 14.2417], "LIRN"])])

tour("tuscany", ("Italy", "Olaszország"), ("Tuscany hill towns", "Toszkána dombvárosai"), ("Florence Cathedral", "A firenzei dóm", 43.7731, 11.2560), ["culture", "unesco", "city"],
     ("Florence, the Leaning Tower of Pisa and the medieval towers of San Gimignano, Siena and Pienza in the Val d'Orcia.", "Firenze, a pisai ferde torony, San Gimignano és Siena középkori tornyai, valamint Pienza az Orcia-völgyben."),
     [["Monteriggioni", 43.3908, 11.2243], ["Pienza", 43.0766, 11.6793]],
     [("ab", "ab", 110, 3000, ("Florence to the Maremma", "Firenzétől a Maremmáig"), ("One-way flight from Florence via Pisa, San Gimignano and Siena to the Val d'Orcia and Grosseto.", "Egyirányú repülés Firenzéből Pisán, San Gimignanón és Sienán át az Orcia-völgyig és Grossetóig."),
       ["LIRQ", ["Florence Cathedral", 43.7731, 11.2560], ["Leaning Tower of Pisa", 43.7230, 10.3966], ["San Gimignano", 43.4677, 11.0432], ["Siena", 43.3186, 11.3306], ["Pienza", 43.0766, 11.6793], "LIRS"])])

tour("dolomites", ("Italy", "Olaszország"), ("Venice and the Dolomites", "Velence és a Dolomitok"), ("Tre Cime di Lavaredo", "Tre Cime di Lavaredo", 46.6186, 12.3028), ["mountain", "unesco", "city"],
     ("From the lagoon of Venice to the pale rock towers of the Dolomites: Cortina, the Tre Cime and the Marmolada glacier.", "A velencei lagúnától a Dolomitok világos sziklatornyaiig: Cortina, a Tre Cime és a Marmolada-gleccser."),
     [["Cortina d'Ampezzo", 46.5405, 12.1357]],
     [("ab", "ab", 130, 11000, ("Venice to Bolzano", "Velencétől Bolzanóig"), ("A one-way climb from Venice over the Dolomites to Bolzano; keep terrain clearance in mind.", "Egyirányú repülés Velencéből a Dolomitok felett Bolzanóba; figyelj a terep feletti magasságra."),
       ["LIPZ", ["St Mark's Basilica", 45.4343, 12.3388], ["Cortina d'Ampezzo", 46.5405, 12.1357], ["Tre Cime di Lavaredo", 46.6186, 12.3028], ["Marmolada", 46.4342, 11.8559], "LIPB"])])

tour("cinque-terre", ("Italy", "Olaszország"), ("Cinque Terre and the Ligurian coast", "Cinque Terre és a ligur tengerpart"), ("Vernazza", "Vernazza", 44.1350, 9.6836), ["coast", "unesco"],
     ("The colourful cliff villages of the Cinque Terre, Portovenere and Portofino on the way to Genoa.", "A Cinque Terre színes sziklafalu, Portovenere és Portofino, Genova felé."),
     [["Monterosso al Mare", 44.1460, 9.6540], ["Riomaggiore", 44.0990, 9.7380]],
     [("ab", "ab", 110, 2200, ("Pisa to Genoa", "Pisától Genováig"), ("Along the Ligurian coast from Pisa over the Cinque Terre and Portovenere to Portofino and Genoa.", "A ligur partvonal mentén Pisától a Cinque Terre és Portovenere felett Portofinóba és Genovába."),
       ["LIRP", ["Portovenere", 44.0525, 9.8344], ["Vernazza", 44.1350, 9.6836], ["Portofino", 44.3033, 9.2095], "LIMJ"])])

tour("matterhorn", ("Switzerland", "Svájc"), ("Matterhorn and the Bernese Alps", "Matterhorn és a Berni-Alpok"), ("Matterhorn", "Matterhorn", 45.9766, 7.6585), ["mountain", "unesco"],
     ("From the Rhône valley past the Matterhorn to the Aletsch glacier, the Jungfrau and the Eiger, ending at Bern.", "A Rhône-völgyből a Matterhorn mellett az Aletsch-gleccserhez, a Jungfrauhoz és az Eigerhez, Bernbe."),
     [["Zermatt", 46.0207, 7.7491], ["Interlaken", 46.6863, 7.8632]],
     [("ab", "ab", 110, 12500, ("Sion to Bern", "Sion – Bern"), ("A high-altitude one-way flight along the Valais Alps to the Bernese Oberland. High terrain: needs a capable aircraft.", "Magaslati egyirányú repülés a Wallisi-Alpok mentén a Berni-Oberlandig. Magas terep: megfelelő gép kell hozzá."),
       ["LSGS", ["Matterhorn", 45.9766, 7.6585], ["Zermatt", 46.0207, 7.7491], ["Aletsch Glacier", 46.4375, 8.0539], ["Jungfrau", 46.5368, 7.9626], ["Eiger", 46.5775, 8.0053], ["Interlaken", 46.6863, 7.8632], "LSZB"])])

tour("lucerne", ("Switzerland", "Svájc"), ("Lake Lucerne and the Rigi", "Luzerni-tó és a Rigi"), ("Chapel Bridge, Lucerne", "Luzerni fedett híd", 47.0516, 8.3075), ["mountain", "city", "coast"],
     ("A loop around Lake Lucerne: the Rigi, the old town of Lucerne with its Chapel Bridge, Mount Pilatus and Titlis.", "Kör a Luzerni-tó körül: a Rigi, Luzern óvárosa a fedett híddal, a Pilatus és a Titlis."),
     [["Rütli Meadow", 46.9772, 8.5906]],
     [("loop", "loop", 100, 8500, ("Lucerne loop", "Luzerni kör"), ("From Buochs over the Rigi, Lucerne, Pilatus and Titlis, back to the lake.", "Buochsból a Rigi, Luzern, a Pilatus és a Titlis felett vissza a tóhoz."),
       ["LSZC", ["Rigi Kulm", 47.0564, 8.4855], ["Chapel Bridge, Lucerne", 47.0516, 8.3075], ["Pilatus", 46.9788, 8.2527], ["Titlis", 46.7712, 8.4378], "LSZC"])])

tour("salzkammergut", ("Austria", "Ausztria"), ("Salzburg and the Salzkammergut", "Salzburg és a Salzkammergut"), ("Hallstatt", "Hallstatt", 47.5622, 13.6493), ["mountain", "culture", "unesco", "city"],
     ("Salzburg's fortress, then the lakes of the Salzkammergut: Mondsee, St Wolfgang and the UNESCO village of Hallstatt below the Dachstein.", "Salzburg erődje, majd a Salzkammergut tavai: a Mondsee, St. Wolfgang és a Dachstein alatti UNESCO-falu, Hallstatt."),
     [["Wolfgangsee", 47.7500, 13.4500]],
     [("loop", "loop", 100, 6500, ("Salzburg and the lakes", "Salzburg és a tavak"), ("From Salzburg over the lakes to Hallstatt and the Dachstein, and back.", "Salzburgból a tavak felett Hallstattba és a Dachsteinhez, majd vissza."),
       ["LOWS", ["Hohensalzburg Fortress", 47.7948, 13.0475], ["Mondsee", 47.8467, 13.3687], ["St. Wolfgang", 47.7397, 13.4469], ["Hallstatt", 47.5622, 13.6493], ["Dachstein", 47.4755, 13.6060], "LOWS"])])

tour("loire", ("France", "Franciaország"), ("Paris and the Loire châteaux", "Párizs és a Loire menti kastélyok"), ("Chambord Château", "Chambord-i kastély", 47.6161, 1.5170), ["culture", "unesco", "city"],
     ("The Eiffel Tower and Versailles, then south-west to the great Renaissance châteaux of the Loire.", "Az Eiffel-torony és Versailles, majd délnyugatra a Loire nagy reneszánsz kastélyaihoz."),
     [["Notre-Dame de Paris", 48.8530, 2.3499], ["Château d'Amboise", 47.4129, 0.9843]],
     [("ab", "ab", 120, 3000, ("Paris to Tours", "Párizstól Tours-ig"), ("One-way flight from Paris-Orly over the Eiffel Tower and Versailles to Chambord, Chenonceau and Amboise.", "Egyirányú repülés Párizs-Orlyből az Eiffel-torony és Versailles felett Chambordba, Chenonceau-ba és Amboise-ba."),
       ["LFPO", ["Eiffel Tower", 48.8584, 2.2945], ["Versailles", 48.8049, 2.1204], ["Château de Chambord", 47.6161, 1.5170], ["Château de Chenonceau", 47.3249, 1.0701], ["Château d'Amboise", 47.4129, 0.9843], "LFOT"])])

tour("golden-circle", ("Iceland", "Izland"), ("Reykjavik and the Golden Circle", "Reykjavík és az Aranykör"), ("Gullfoss", "Gullfoss", 64.3271, -20.1199), ["volcano", "unesco", "coast"],
     ("Iceland's classic circuit: the rift valley at Þingvellir, the Geysir geothermal field, the Gullfoss waterfall and the Blue Lagoon.", "Izland klasszikus körútja: a þingvellíri hasadékvölgy, a Geysir gejzírmező, a Gullfoss-vízesés és a Kék-lagúna."),
     [["Hallgrímskirkja", 64.1417, -21.9266]],
     [("loop", "loop", 100, 2500, ("Golden Circle", "Aranykör"), ("From Reykjavik over Þingvellir, Geysir and Gullfoss to Kerið and the Blue Lagoon.", "Reykjavíkból Þingvellir, Geysir és Gullfoss felett a Kerið-kráterhez és a Kék-lagúnához."),
       ["BIRK", ["Þingvellir", 64.2559, -21.1299], ["Geysir", 64.3104, -20.3024], ["Gullfoss", 64.3271, -20.1199], ["Kerið", 64.0411, -20.8853], ["Blue Lagoon", 63.8803, -22.4495], "BIRK"])])

d = json.load(open(P, encoding="utf-8"))
have = {t["id"]: i for i, t in enumerate(d["tours"])}
for t in T:
    if t["id"] in have:
        d["tours"][have[t["id"]]] = t
    else:
        d["tours"].append(t)
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(T), "tura, osszesen", len(d["tours"]))
