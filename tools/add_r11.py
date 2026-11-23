#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""11. kor: 8 uj tura. Sorrend: add_r11 -> tours_order <r11_ids> -> dup_check -> poi_registry -> tours_kw -> tours_img -> tours_check"""
from tourlib import *
import json, os
C = lambda e, h: (e, h)
ES = C("Spain", "Spanyolország"); GB = C("United Kingdom", "Egyesült Királyság"); SE = C("Sweden", "Svédország"); IS = C("Iceland", "Izland"); TR = C("Turkey", "Törökország")
KZ = C("Kazakhstan", "Kazahsztán"); MN = C("Mongolia", "Mongólia"); JP = C("Japan", "Japán"); CN = C("China", "Kína"); LB = C("Lebanon", "Libanon"); IN = C("India", "India"); ID = C("Indonesia", "Indonézia")
US = C("United States", "Egyesült Államok"); VI = C("US Virgin Islands", "Amerikai Virgin-szigetek"); MX = C("Mexico", "Mexikó"); GT = C("Guatemala", "Guatemala")
PE = C("Peru", "Peru"); UY = C("Uruguay", "Uruguay"); AR = C("Argentina", "Argentína"); MA = C("Morocco", "Marokkó"); NZ = C("New Zealand", "Új-Zéland"); AU = C("Australia", "Ausztrália"); CK = C("Cook Islands", "Cook-szigetek")
AQ = C("Antarctica", "Antarktisz"); AZ = C("Azerbaijan", "Azerbajdzsán"); RU = C("Russia", "Oroszország"); KE = C("Kenya", "Kenya"); MY = C("Malaysia", "Malajzia"); BR = C("Brazil", "Brazília")
CONT = {}
POI = {}


def add(cont, *a):
    a = list(a)
    a.insert(6, [])
    tour(*a); CONT[a[0]] = cont


def Pt(n, hu, kw, la, lo):
    POI[n] = (hu, kw)
    return [n, la, lo]


add("AF", "lamu", KE, ("Lamu Archipelago", "Lamu-szigetcsoport"), ("Lamu Old Town", "Lamu óvárosa", -2.2717, 40.9020), ["island", "coast", "culture", "unesco"],
    ("The Swahili stone town of Lamu, where donkeys are the traffic, the endless dunes of Shela Beach, the ruins of Takwa and the ancient trading port of Pate Island.", "Lamu szuahéli kővárosa, ahol a szamarak a közlekedés, a Shela-part végtelen dűnéi, Takwa romjai és Pate-sziget ősi kereskedővárosa."),
    [("loop", "loop", 100, 2500, ("Swahili coast loop", "Szuahéli part-kör"), ("Takwa ruins, Lamu Old Town, Shela Beach and Pate.", "Takwa romjai, Lamu óvárosa, a Shela-part és Pate."),
      ["HKLU", Pt("Lamu Old Town", "Lamu óvárosa", "Lamu óváros szuahéli", -2.2717, 40.9020), Pt("Shela Beach", "Shela-part", "Shela strand Lamu", -2.2900, 40.9100), ["~", -2.32, 40.94], ["~", -2.18, 41.12], Pt("Pate Town", "Pate", "Pate sziget város", -2.1230, 41.0600), Pt("Takwa Ruins", "Takwa romjai", "Takwa romok Manda sziget", -2.2400, 40.9800), "HKLU"])])
add("AS", "langkawi", MY, ("Langkawi", "Langkawi"), ("Langkawi Sky Bridge", "Langkawi Sky Bridge", 6.3860, 99.6650), ["island", "coast", "mountain", "jungle"],
    ("A jungle archipelago of 99 islands: the curved Sky Bridge on Mount Mat Cincang, Pantai Cenang beach, the marble lake of Dayang Bunting and the mangrove Kilim Geoforest.", "99 szigetből álló dzsungel szigetvilág: az ívelt Sky Bridge a Mat Cincang-hegyen, a Pantai Cenang-part, a Dayang Bunting márvány-tava és a mangrove Kilim Geopark."),
    [("loop", "loop", 100, 2500, ("Langkawi loop", "Langkawi-kör"), ("Pantai Cenang, the Sky Bridge, Kilim and Dayang Bunting.", "Pantai Cenang, a Sky Bridge, Kilim és Dayang Bunting."),
      ["WMKL", Pt("Pantai Cenang", "Pantai Cenang", "Pantai Cenang Langkawi strand", 6.2900, 99.7200), Pt("Langkawi Sky Bridge", "Langkawi Sky Bridge", "Langkawi Sky Bridge Mat Cincang", 6.3860, 99.6650), Pt("Kilim Geoforest", "Kilim Geopark", "Kilim Karst Geoforest Park Langkawi", 6.4200, 99.8500), Pt("Dayang Bunting", "Dayang Bunting", "Dayang Bunting tó Langkawi", 6.2260, 99.8010), "WMKL"])])
add("AS", "kota-kinabalu", MY, ("Kota Kinabalu and Mount Kinabalu", "Kota Kinabalu és a Kinabalu-hegy"), ("Mount Kinabalu", "Kinabalu-hegy", 6.0750, 116.5580), ["mountain", "island", "jungle", "unesco"],
    ("The 4,095 m granite summit of Mount Kinabalu, the highest peak of Borneo, rising behind the sunset city of Kota Kinabalu and the coral islands of Tunku Abdul Rahman Park.", "A Kinabalu 4095 méteres gránitcsúcsa, Borneó legmagasabb hegye a naplementés Kota Kinabalu és a Tunku Abdul Rahman Park korallszigetei mögött."),
    [("loop", "loop", 100, 6000, ("Borneo summit loop", "Borneói csúcs-kör"), ("The City Mosque, Mount Kinabalu, Poring and Gaya Island.", "A Városi mecset, a Kinabalu-hegy, Poring és a Gaya-sziget."),
      ["WBKK", Pt("Kota Kinabalu City Mosque", "Kota Kinabalu Városi mecset", "Kota Kinabalu City Mosque", 5.9600, 116.0620), Pt("Mount Kinabalu", "Kinabalu-hegy", "Kinabalu hegy Borneó", 6.0750, 116.5580), Pt("Poring Hot Springs", "Poring forrásai", "Poring Hot Springs Kinabalu", 6.0430, 116.7050), Pt("Gaya Island", "Gaya-sziget", "Gaya sziget Tunku Abdul Rahman Park", 5.9930, 115.9900), "WBKK"])])
add("AS", "baku", AZ, ("Baku and Gobustan", "Baku és Gobusztán"), ("Flame Towers", "Lángtornyok", 40.3600, 49.8260), ["city", "culture", "unesco"],
    ("The Flame Towers above the Caspian shore, the walled Old City, the Zoroastrian fire temple of Ateshgah, the ever-burning hillside of Yanar Dag and the rock art of Gobustan.", "A Lángtornyok a Káspi-tenger partja felett, a falakkal övezett óváros, az Ateshgah tűztemplom, a Yanar Dag örökké égő lejtője és Gobusztán sziklarajzai."),
    [("loop", "loop", 100, 3000, ("Land of Fire loop", "Tűz földje kör"), ("The Flame Towers, Ateshgah, Yanar Dag and Gobustan.", "A Lángtornyok, az Ateshgah, a Yanar Dag és Gobusztán."),
      ["UBBB", Pt("Flame Towers", "Lángtornyok", "Baku Flame Towers", 40.3600, 49.8260), Pt("Ateshgah", "Ateshgah tűztemplom", "Ateshgah Baku tűztemplom", 40.4170, 50.0120), Pt("Yanar Dag", "Yanar Dag", "Yanar Dag égő hegy", 40.5000, 50.1700), Pt("Gobustan", "Gobusztán", "Gobustan sziklarajzok", 40.1100, 49.3830), "UBBB"])])
add("AS", "lake-baikal", RU, ("Lake Baikal", "Bajkál-tó"), ("Lake Baikal", "Bajkál-tó", 53.2000, 107.3400), ["coast", "island", "mountain", "unesco"],
    ("The deepest and oldest lake on Earth: the shore town of Listvyanka, the Circum-Baikal mountains, the shamanic rock of Olkhon Island and the vast frozen blue expanse.", "A Föld legmélyebb és legöregebb tava: a parti Listvjanka, a Bajkál-hegyek, az Olhon-sziget sámánsziklája és a végtelen kék víztükör."),
    [("long", "loop", 120, 6000, ("Baikal loop", "Bajkál-kör"), ("Listvyanka, Port Baikal and Olkhon Island.", "Listvjanka, Port Bajkal és az Olhon-sziget."),
      ["UIII", Pt("Listvyanka", "Listvjanka", "Listvyanka Bajkál", 51.8500, 104.8700), Pt("Olkhon Island", "Olhon-sziget", "Olkhon sziget Khuzhir Bajkál", 53.2000, 107.3400), Pt("Cape Khoboy", "Hoboj-fok", "Khoboy fok Olkhon", 53.4200, 107.7500), "UIII"])])
add("AS", "kamchatka", RU, ("Kamchatka Volcanoes", "Kamcsatkai vulkánok"), ("Avachinsky Volcano", "Avacsinszkij-vulkán", 53.2560, 158.8300), ["volcano", "mountain", "coast"],
    ("The land of fire and ice: the twin cones of Avachinsky and Koryaksky above Petropavlovsk, Vilyuchinsky and the steaming crater of Mutnovsky.", "A tűz és jég földje: az Avacsinszkij és Korjakszkij ikerkúpjai Petropavlovszk felett, a Vilucsinszkij és a gőzölgő Mutnovszkij-kráter."),
    [("loop", "loop", 110, 9000, ("Volcano ring", "Vulkán-gyűrű"), ("Koryaksky, Avachinsky, Mutnovsky and Vilyuchinsky.", "A Korjakszkij, az Avacsinszkij, a Mutnovszkij és a Vilucsinszkij."),
      ["UHPP", Pt("Koryaksky", "Korjakszkij-vulkán", "Korjakszkij vulkán Kamcsatka", 53.3200, 158.7120), Pt("Avachinsky Volcano", "Avacsinszkij-vulkán", "Avacsinszkij vulkán Kamcsatka", 53.2560, 158.8300), Pt("Mutnovsky", "Mutnovszkij", "Mutnovsky vulkán Kamcsatka", 52.4500, 158.2000), Pt("Vilyuchinsky", "Vilucsinszkij", "Vilyuchinsky vulkán Kamcsatka", 52.7000, 158.2800), "UHPP"])])
add("EU", "galicia", ES, ("Galicia and Santiago de Compostela", "Galícia és Santiago de Compostela"), ("Santiago de Compostela Cathedral", "Santiago de Compostela-i katedrális", 42.8806, -8.5446), ["coast", "culture", "unesco"],
    ("The pilgrim cathedral of Santiago, the wild Costa da Morte, the lighthouse cape of Fisterra and the white-sand Cíes Islands of the Atlantic Rías Baixas.", "A zarándok-katedrális Santiagóban, a vad Costa da Morte, Fisterra világítótornyos foka és az Atlanti Rías Baixas fehér homokú Cíes-szigetei."),
    [("loop", "loop", 100, 3500, ("Atlantic Galicia loop", "Atlanti Galícia kör"), ("Santiago, Muxía, Fisterra and the Cíes Islands.", "Santiago, Muxía, Fisterra és a Cíes-szigetek."),
      ["LEST", Pt("Santiago Cathedral", "Santiago-i katedrális", "Santiago de Compostela katedrális", 42.8806, -8.5446), Pt("Muxía", "Muxía", "Muxia Costa da Morte", 43.1070, -9.2170), Pt("Cape Finisterre", "Fisterra-fok", "Fisterra világítótorony fok", 42.8830, -9.2730), Pt("Cíes Islands", "Cíes-szigetek", "Cies szigetek Vigo", 42.2250, -8.9060), "LEST"])])
add("SA", "fernando-de-noronha", BR, ("Fernando de Noronha", "Fernando de Noronha"), ("Morro do Pico", "Morro do Pico", -3.8340, -32.4290), ["island", "coast", "unesco"],
    ("A volcanic Atlantic archipelago of dolphins and turquoise bays: the 323 m phonolite spire of Morro do Pico, the Baía do Sancho and the twin rocks of Dois Irmãos.", "Vulkáni atlanti szigetcsoport delfinekkel és türkizkék öblökkel: a Morro do Pico 323 méteres kőtornya, a Baía do Sancho és a Dois Irmãos ikersziklái."),
    [("loop", "loop", 70, 2000, ("Archipelago loop", "Szigetcsoport-kör"), ("Praia do Leão, Baía do Sancho, Dois Irmãos and Morro do Pico.", "Praia do Leão, a Baía do Sancho, Dois Irmãos és a Morro do Pico."),
      ["SBFN", ["~", -3.9, -32.5], ["~", -3.95, -32.45], Pt("Praia do Leão", "Praia do Leão", "Praia do Leao Fernando de Noronha", -3.8750, -32.4170), Pt("Baía do Sancho", "Baía do Sancho", "Baia do Sancho Fernando de Noronha", -3.8530, -32.4460), Pt("Dois Irmãos", "Dois Irmãos", "Dois Irmaos Fernando de Noronha", -3.8310, -32.4480), Pt("Morro do Pico", "Morro do Pico", "Morro do Pico Fernando de Noronha", -3.8340, -32.4290), "SBFN"])])
for t in T:
    t["continent"] = CONT[t["id"]]
NEW = [t["id"] for t in T]
save()
d = json.load(open(P, encoding="utf-8"))
REV = set(open(os.path.join(os.path.dirname(P), "..", "tools", "reviewed.txt"), encoding="utf-8").read().split())
for t in d["tours"]:
    if t["id"] in NEW and t["id"] not in REV:
        t["new"] = True
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
here = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(here, "r11_ids.txt"), "w").write(" ".join(NEW))
with open(os.path.join(here, "poi_r11.py"), "w", encoding="utf-8") as f:
    f.write('# -*- coding: utf-8 -*-\n"""A 11. kor latnivaloi: EN nev -> (magyar nev, extra kereso szavak). Az add_r10.py generalja."""\nNEW = {\n')
    for k, (h, x) in POI.items():
        f.write("%r: (%r, %r),\n" % (k, h, x))
    f.write("}\n")
print(len(NEW), "tura,", len(POI), "latnivalo")
