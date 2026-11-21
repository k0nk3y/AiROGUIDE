#!/usr/bin/env python3
"""1. kor, 2. resz: tura minden nem europai kontinensen (rovid ~20-30 perces es ~1 oras korok). Sorrend: add_r1 -> add_r2 -> tours_order <azonositok> -> tours_check"""
from tourlib import *
import json, os

US = ("United States", "Egyesült Államok"); CA = ("Canada", "Kanada"); MX = ("Mexico", "Mexikó"); AR = ("Argentina", "Argentína"); CL = ("Chile", "Chile"); EC = ("Ecuador", "Ecuador")
MA = ("Morocco", "Marokkó"); ZW = ("Zimbabwe", "Zimbabwe"); EG = ("Egypt", "Egyiptom"); TZ = ("Tanzania", "Tanzánia"); AU = ("Australia", "Ausztrália"); NZ = ("New Zealand", "Új-Zéland")
PF = ("French Polynesia", "Francia Polinézia"); ID = ("Indonesia", "Indonézia"); SG = ("Singapore", "Szingapúr")
CONT = {}

def add(cont, *a, **k):
    tour(*a, **k); CONT[a[0]] = cont

# ---------------- Eszak-Amerika ----------------
add("NA", "yellowstone", US, ("Yellowstone and the Tetons", "Yellowstone és a Teton-hegység"), ("Old Faithful", "Old Faithful", 44.4605, -110.8281), ["mountain", "volcano", "unesco"],
    ("Geysers, hot springs and the jagged Teton Range: America's first national park from above.", "Gejzírek, forró források és a csipkézett Teton-hegység: Amerika első nemzeti parkja felülről."), [],
    [("short", "loop", 110, 12500, ("Tetons short", "Teton rövid"), ("Short loop from Jackson Hole: the Grand Teton, Jackson Lake and the Snake River.", "Rövid kör Jackson Hole-ból: a Grand Teton, a Jackson-tó és a Snake River."),
      ["KJAC", ["Grand Teton", 43.7410, -110.8024], ["Jackson Lake", 43.8500, -110.6000], ["Oxbow Bend", 43.8650, -110.5200], ["Jenny Lake", 43.7550, -110.7230], "KJAC"]),
     ("full", "loop", 115, 12500, ("Yellowstone loop", "Yellowstone-kör"), ("About an hour and a half: the Tetons, Old Faithful, Grand Prismatic Spring and the Grand Canyon of the Yellowstone.", "Kb. másfél óra: a Tetonok, Old Faithful, a Grand Prismatic Spring és a Yellowstone Grand Canyonja."),
      ["KJAC", ["Grand Teton", 43.7410, -110.8024], ["Old Faithful", 44.4605, -110.8281], ["Grand Prismatic Spring", 44.5251, -110.8383], ["Yellowstone Falls", 44.7183, -110.4962], ["Yellowstone Lake", 44.4500, -110.3700], ["Jackson Lake", 43.8500, -110.6000], "KJAC"])])
add("NA", "las-vegas", US, ("Las Vegas and Hoover Dam", "Las Vegas és a Hoover-gát"), ("Las Vegas Strip", "Las Vegas Strip", 36.1147, -115.1728), ["city", "culture", "mountain"],
    ("The neon Strip, the Red Rock canyons, the Hoover Dam and the red sandstone of the Valley of Fire.", "A neonfényes Strip, a Red Rock-kanyon, a Hoover-gát és a Valley of Fire vörös homokköve."), [],
    [("short", "loop", 100, 5500, ("Vegas short", "Vegas rövid"), ("Short loop: the Strip, Red Rock Canyon and the Hoover Dam.", "Rövid kör: a Strip, a Red Rock-kanyon és a Hoover-gát."),
      ["KLAS", ["Las Vegas Strip", 36.1147, -115.1728], ["Red Rock Canyon", 36.1350, -115.4270], ["Hoover Dam", 36.0160, -114.7377], "KLAS"]),
     ("full", "loop", 110, 5500, ("Vegas loop", "Vegas-kör"), ("About an hour: the Strip, Red Rock, Hoover Dam, Lake Mead and the Valley of Fire.", "Kb. egy óra: a Strip, Red Rock, Hoover-gát, a Mead-tó és a Valley of Fire."),
      ["KLAS", ["Red Rock Canyon", 36.1350, -115.4270], ["Las Vegas Strip", 36.1147, -115.1728], ["Hoover Dam", 36.0160, -114.7377], ["Lake Mead", 36.2000, -114.3500], ["Valley of Fire", 36.4350, -114.5160], "KLAS"])])
add("NA", "yosemite", US, ("Yosemite", "Yosemite"), ("Half Dome", "Half Dome", 37.7459, -119.5332), ["mountain", "unesco"],
    ("Granite walls and waterfalls: Half Dome, El Capitan, Yosemite Falls and the high country of Tuolumne.", "Gránitfalak és vízesések: a Half Dome, az El Capitan, a Yosemite-vízesés és Tuolumne magasföldje."), [],
    [("loop", "loop", 110, 11500, ("Yosemite loop", "Yosemite-kör"), ("Yosemite Valley with El Capitan and Half Dome, Glacier Point and Tuolumne Meadows.", "A Yosemite-völgy az El Capitannal és a Half Dome-mal, Glacier Point és Tuolumne Meadows."),
      ["KMPI", ["El Capitan", 37.7340, -119.6377], ["Yosemite Falls", 37.7565, -119.5968], ["Half Dome", 37.7459, -119.5332], ["Glacier Point", 37.7305, -119.5740], ["Tuolumne Meadows", 37.8730, -119.3500], "KMPI"])])
add("NA", "banff", CA, ("Banff and Lake Louise", "Banff és a Lake Louise"), ("Lake Louise", "Lake Louise", 51.4254, -116.1773), ["mountain", "unesco"],
    ("Turquoise lakes under the Canadian Rockies: Lake Louise, Moraine Lake, Peyto Lake and the Bow Valley.", "Türkiz tavak a Kanadai-Sziklás-hegység alatt: Lake Louise, Moraine Lake, Peyto Lake és a Bow-völgy."), [],
    [("full", "loop", 115, 11500, ("Lakes loop", "Tó-kör"), ("About an hour: Mount Rundle, Banff, Lake Louise, Moraine Lake and Peyto Lake on the Icefields Parkway.", "Kb. egy óra: a Mount Rundle, Banff, Lake Louise, Moraine Lake és a Peyto-tó a Jégmező-úton."),
      ["CYBW", ["Mount Rundle", 51.1500, -115.5500], ["Banff", 51.1784, -115.5708], ["Lake Louise", 51.4254, -116.1773], ["Peyto Lake", 51.7240, -116.5170], ["Moraine Lake", 51.3217, -116.1860], "CYBW"])])
add("NA", "yucatan", MX, ("Cancún and the Maya coast", "Cancún és a maja part"), ("Chichén Itzá", "Chichén Itzá", 20.6843, -88.5678), ["culture", "coast", "unesco"],
    ("White beaches and Maya pyramids: Isla Mujeres, Tulum above the sea and the great pyramid of Chichén Itzá.", "Fehér strandok és maja piramisok: Isla Mujeres, a tenger felett álló Tulum és a chichén itzái nagy piramis."), [],
    [("short", "loop", 100, 2000, ("Cancún short", "Cancún rövid"), ("Short loop: Isla Mujeres, the hotel zone and Tulum.", "Rövid kör: Isla Mujeres, a szállodasor és Tulum."),
      ["MMUN", ["Isla Mujeres", 21.2310, -86.7300], ["Cancún Hotel Zone", 21.1250, -86.7500], ["Tulum", 20.2114, -87.4654], "MMUN"]),
     ("maya", "loop", 105, 2500, ("Maya ruins", "Maja romok"), ("About an hour: Tulum, Cobá and Chichén Itzá.", "Kb. egy óra: Tulum, Cobá és Chichén Itzá."),
      ["MMUN", ["Tulum", 20.2114, -87.4654], ["Cobá", 20.4950, -87.7360], ["Chichén Itzá", 20.6843, -88.5678], ["Isla Mujeres", 21.2310, -86.7300], "MMUN"])])

# ---------------- Del-Amerika ----------------
add("SA", "torres-del-paine", CL, ("Torres del Paine", "Torres del Paine"), ("Torres del Paine", "Torres del Paine", -50.9423, -73.4068), ["mountain", "unesco"],
    ("Granite towers, blue glaciers and turquoise lakes at the end of the world.", "Gránittornyok, kék gleccserek és türkiz tavak a világ végén."), [],
    [("loop", "loop", 100, 7500, ("Paine loop", "Paine-kör"), ("From Puerto Natales: the Torres, the Cuernos, Lake Pehoé and the Grey Glacier.", "Puerto Natalesből: a Torres, a Cuernos, a Pehoé-tó és a Grey-gleccser."),
      ["SCNT", ["Torres del Paine", -50.9423, -73.4068], ["Grey Glacier", -50.9625, -73.2000], ["Cuernos del Paine", -50.9540, -73.0640], ["Lake Pehoé", -51.0640, -73.0700], "SCNT"])])
add("SA", "perito-moreno", AR, ("Perito Moreno and Fitz Roy", "Perito Moreno és a Fitz Roy"), ("Perito Moreno Glacier", "Perito Moreno-gleccser", -50.4967, -73.1370), ["mountain", "unesco"],
    ("A glacier that calves into Lago Argentino and the sharp spires of Fitz Roy and Cerro Torre.", "A Lago Argentinóba törő gleccser, valamint a Fitz Roy és a Cerro Torre éles tornyai."), [],
    [("short", "loop", 105, 6500, ("Glacier short", "Gleccser rövid"), ("Short loop from El Calafate: Lago Argentino and the Perito Moreno Glacier.", "Rövid kör El Calafatéból: a Lago Argentino és a Perito Moreno-gleccser."),
      ["SAWC", ["Perito Moreno Glacier", -50.4967, -73.1370], ["Lago Argentino", -50.3500, -72.8000], ["Upsala Glacier", -50.0000, -73.2000], "SAWC"]),
     ("fitzroy", "loop", 110, 9500, ("Fitz Roy loop", "Fitz Roy-kör"), ("About an hour and a half: the glacier, Cerro Torre, Fitz Roy and Lake Viedma.", "Kb. másfél óra: a gleccser, a Cerro Torre, a Fitz Roy és a Viedma-tó."),
      ["SAWC", ["Perito Moreno Glacier", -50.4967, -73.1370], ["Cerro Torre", -49.2928, -73.0980], ["Fitz Roy", -49.2715, -72.9980], ["Lake Viedma", -49.6000, -72.6000], "SAWC"])])
add("SA", "galapagos", EC, ("Galápagos Islands", "Galápagos-szigetek"), ("Pinnacle Rock", "Pinnacle Rock", -0.2866, -90.5469), ["island", "volcano", "unesco"],
    ("Darwin's islands: volcanic cones, black lava coasts and the pinnacle of Bartolomé.", "Darwin szigetei: vulkáni kúpok, fekete lávapartok és a bartoloméi Pinnacle Rock."), [],
    [("loop", "loop", 100, 2500, ("Galápagos loop", "Galápagos-kör"), ("From Baltra: Daphne Major, Bartolomé, Sullivan Bay and Puerto Ayora.", "Baltráról: Daphne Major, Bartolomé, Sullivan Bay és Puerto Ayora."),
      ["SEGS", ["Daphne Major", -0.4180, -90.3500], ["Pinnacle Rock", -0.2866, -90.5469], ["Sullivan Bay", -0.2290, -90.5780], ["Puerto Ayora", -0.7430, -90.3130], "SEGS"])])
add("SA", "buenos-aires", AR, ("Buenos Aires and the Río de la Plata", "Buenos Aires és a Río de la Plata"), ("Obelisco", "Obeliszk", -34.6037, -58.3816), ["city", "culture", "coast"],
    ("The tango capital: Puerto Madero, La Boca, Recoleta and the brown Río de la Plata.", "A tangó fővárosa: Puerto Madero, La Boca, Recoleta és a barna Río de la Plata."), [],
    [("loop", "loop", 95, 1800, ("Buenos Aires loop", "Buenos Aires-kör"), ("The Obelisco, Puerto Madero, La Boca, Recoleta and Isla Martín García in the river.", "Az Obeliszk, Puerto Madero, La Boca, Recoleta és az Isla Martín García a folyón."),
      ["SABE", ["Obelisco", -34.6037, -58.3816], ["Puerto Madero", -34.6118, -58.3636], ["La Boca", -34.6356, -58.3647], ["Recoleta Cemetery", -34.5875, -58.3930], ["Isla Martín García", -34.1870, -58.2540], "SABE"])])

# ---------------- Afrika ----------------
add("AF", "marrakech-atlas", MA, ("Marrakech and the Atlas", "Marrakesh és az Atlasz"), ("Koutoubia Mosque", "Koutoubia-mecset", 31.6240, -7.9937), ["city", "culture", "mountain", "unesco"],
    ("The red city of Marrakech, the High Atlas around Toubkal and the mud-brick fortress of Aït Benhaddou.", "A vörös Marrakesh, a Magas-Atlasz a Toubkal körül és az Aït Benhaddou vályogerődje."), [],
    [("short", "loop", 105, 9500, ("Marrakech short", "Marrakesh rövid"), ("Short loop: Marrakech, Oukaïmeden and the foothills of the Atlas.", "Rövid kör: Marrakesh, Oukaïmeden és az Atlasz előhegyei."),
      ["GMMX", ["Koutoubia Mosque", 31.6240, -7.9937], ["Oukaïmeden", 31.2060, -7.8640], ["Imlil", 31.1360, -7.9190], "GMMX"]),
     ("atlas", "loop", 115, 14500, ("High Atlas and Aït Benhaddou", "Magas-Atlasz és Aït Benhaddou"), ("About an hour and a half: Toubkal, the Tizi n'Tichka pass and Aït Benhaddou.", "Kb. másfél óra: a Toubkal, a Tizi n'Tichka-hágó és Aït Benhaddou."),
      ["GMMX", ["Imlil", 31.1360, -7.9190], ["Toubkal", 31.0597, -7.9156], ["Aït Benhaddou", 31.0472, -7.1292], ["Oukaïmeden", 31.2060, -7.8640], ["Koutoubia Mosque", 31.6240, -7.9937], "GMMX"])])
add("AF", "victoria-falls", ZW, ("Victoria Falls", "Victoria-vízesés"), ("Victoria Falls", "Victoria-vízesés", -17.9243, 25.8572), ["culture", "unesco", "jungle"],
    ("The smoke that thunders: the Zambezi plunging into the Batoka Gorge on the border of Zimbabwe and Zambia.", "A mennydörgő füst: a Zambezi zuhan a Batoka-szurdokba Zimbabwe és Zambia határán."), [],
    [("loop", "loop", 100, 2500, ("Falls loop", "Vízesés-kör"), ("The Zambezi above the falls, Victoria Falls and the Batoka Gorge.", "A Zambezi a vízesés felett, a Victoria-vízesés és a Batoka-szurdok."),
      ["FVFA", ["Zambezi River Islands", -17.8700, 25.7500], ["Victoria Falls", -17.9243, 25.8572], ["Batoka Gorge", -17.9800, 25.9000], "FVFA"])])
add("AF", "luxor", EG, ("Luxor and the Nile", "Luxor és a Nílus"), ("Valley of the Kings", "Királyok völgye", 25.7402, 32.6014), ["culture", "unesco"],
    ("Ancient Thebes on the Nile: Karnak, Luxor Temple, the Colossi of Memnon and the Valley of the Kings.", "Az ókori Théba a Nílus partján: Karnak, a luxori templom, a Memnón-kolosszusok és a Királyok völgye."), [],
    [("short", "loop", 100, 3000, ("Thebes and Dendera", "Théba és Dendera"), ("About 45 minutes: Karnak, the temple of Dendera and the Valley of the Kings.", "Kb. 45 perc: Karnak, a denderai templom és a Királyok völgye."),
      ["HELX", ["Karnak Temple", 25.7188, 32.6573], ["Dendera Temple", 26.1417, 32.6700], ["Valley of the Kings", 25.7402, 32.6014], "HELX"]),
     ("dendera", "loop", 105, 3500, ("Thebes, Dendera and Abydos", "Théba, Dendera és Abüdosz"), ("About an hour and a half: the temples of Luxor, then north along the Nile to Dendera and Abydos.", "Kb. másfél óra: a luxori templomok, majd észak felé a Nílus mentén Dendera és Abüdosz."),
      ["HELX", ["Karnak Temple", 25.7188, 32.6573], ["Valley of the Kings", 25.7402, 32.6014], ["Dendera Temple", 26.1417, 32.6700], ["Abydos", 26.1850, 31.9190], ["Colossi of Memnon", 25.7207, 32.6102], "HELX"])])
add("AF", "ngorongoro", TZ, ("Ngorongoro and Lake Manyara", "Ngorongoro és a Manyara-tó"), ("Ngorongoro Crater", "Ngorongoro-kráter", -3.1694, 35.5878), ["volcano", "mountain", "unesco"],
    ("The largest intact caldera on Earth, the flamingos of Lake Manyara and the sacred volcano Ol Doinyo Lengai.", "A Föld legnagyobb ép kalderája, a Manyara-tó flamingói és a szent vulkán, az Ol Doinyo Lengai."), [],
    [("loop", "loop", 110, 9500, ("Rift Valley loop", "Hasadékvölgy-kör"), ("From Arusha: Mount Meru, Lake Manyara, Ngorongoro and Ol Doinyo Lengai.", "Arushából: a Meru-hegy, a Manyara-tó, Ngorongoro és az Ol Doinyo Lengai."),
      ["HTAR", ["Mount Meru", -3.2427, 36.7478], ["Lake Manyara", -3.5870, 35.8000], ["Ngorongoro Crater", -3.1694, 35.5878], ["Ol Doinyo Lengai", -2.7640, 35.9140], "HTAR"])])

# ---------------- Oceania ----------------
add("OC", "uluru", AU, ("Uluru and Kata Tjuta", "Uluru és Kata Tjuta"), ("Uluru", "Uluru", -25.3444, 131.0369), ["culture", "unesco"],
    ("The red heart of Australia: Uluru, the domes of Kata Tjuta and the flat-topped Mount Conner.", "Ausztrália vörös szíve: az Uluru, a Kata Tjuta kupolái és a lapos tetejű Conner-hegy."), [],
    [("short", "loop", 100, 3500, ("Uluru short", "Uluru rövid"), ("Short loop: Uluru and the domes of Kata Tjuta.", "Rövid kör: az Uluru és a Kata Tjuta kupolái."),
      ["YAYE", ["Uluru", -25.3444, 131.0369], ["Kata Tjuta", -25.3047, 130.7233], ["Mount Olga Lookout", -25.3400, 130.8300], "YAYE"]),
     ("full", "loop", 110, 4000, ("Red Centre loop", "Vörös Központ-kör"), ("About an hour and a half: Kata Tjuta, Uluru, Mount Conner and Kings Canyon.", "Kb. másfél óra: Kata Tjuta, Uluru, a Conner-hegy és a Kings Canyon."),
      ["YAYE", ["Kata Tjuta", -25.3047, 130.7233], ["Kings Canyon", -24.2594, 131.5547], ["Mount Conner", -25.4380, 131.7700], ["Uluru", -25.3444, 131.0369], "YAYE"])])
add("OC", "great-ocean-road", AU, ("Great Ocean Road", "Great Ocean Road"), ("Twelve Apostles", "Tizenkét Apostol", -38.6624, 143.1049), ["coast"],
    ("Limestone stacks rising from the Southern Ocean: the Twelve Apostles, Loch Ard Gorge and Cape Otway.", "A Déli-óceánból kiemelkedő mészkőtornyok: a Tizenkét Apostol, a Loch Ard-szurdok és a Cape Otway."), [],
    [("loop", "loop", 100, 2000, ("Ocean Road loop", "Ocean Road-kör"), ("From Avalon: Bells Beach, Cape Otway lighthouse and the Twelve Apostles.", "Avalonból: Bells Beach, a Cape Otway világítótornya és a Tizenkét Apostol."),
      ["YMAV", ["Bells Beach", -38.3700, 144.2800], ["Cape Otway Lighthouse", -38.8550, 143.5120], ["Twelve Apostles", -38.6624, 143.1049], ["Loch Ard Gorge", -38.6500, 143.0670], ["Port Campbell", -38.6177, 143.0098], ["~", -38.4000, 143.3500], "YMAV"])])
add("OC", "aoraki", NZ, ("Aoraki / Mount Cook", "Aoraki / Mount Cook"), ("Aoraki / Mount Cook", "Aoraki / Mount Cook", -43.5950, 170.1418), ["mountain", "unesco"],
    ("New Zealand's highest peak, the Tasman Glacier and the milky blue Lake Pukaki.", "Új-Zéland legmagasabb csúcsa, a Tasman-gleccser és a tejkék Pukaki-tó."), [],
    [("loop", "loop", 100, 10500, ("Aoraki loop", "Aoraki-kör"), ("From Mount Cook: Aoraki, the Tasman Glacier and Lake Pukaki.", "Mount Cookból: az Aoraki, a Tasman-gleccser és a Pukaki-tó."),
      ["NZGT", ["Aoraki / Mount Cook", -43.5950, 170.1418], ["Tasman Glacier", -43.6500, 170.2000], ["Lake Pukaki", -44.1000, 170.1500], ["Hooker Glacier", -43.6600, 170.0300], "NZGT"])])
add("OC", "bora-bora", PF, ("Bora Bora and the Leeward Islands", "Bora Bora és a Szél felőli-szigetek"), ("Mount Otemanu", "Otemanu-hegy", -16.5000, -151.7480), ["island", "coast", "volcano"],
    ("A volcanic peak inside a turquoise lagoon: Bora Bora, Maupiti and the sacred marae of Raiatea.", "Vulkáni csúcs egy türkiz lagúnában: Bora Bora, Maupiti és Raiatea szent marae-ja."), [],
    [("loop", "loop", 100, 2500, ("Bora Bora loop", "Bora Bora-kör"), ("Mount Otemanu, Matira Point, Maupiti and Raiatea.", "Az Otemanu-hegy, Matira Point, Maupiti és Raiatea."),
      ["NTTB", ["Mount Otemanu", -16.5000, -151.7480], ["Matira Point", -16.5320, -151.7470], ["Maupiti", -16.4400, -152.2500], ["Taputapuatea Marae", -16.8330, -151.3470], "NTTB"])])

# ---------------- Azsia ----------------
add("AS", "bali", ID, ("Bali", "Bali"), ("Mount Batur", "Batur-hegy", -8.2420, 115.3750), ["island", "culture", "volcano", "coast"],
    ("Volcanoes, rice terraces and sea temples: Mount Batur, Tegallalang, Tanah Lot and the cliffs of Uluwatu.", "Vulkánok, rizsteraszok és tengeri templomok: a Batur, Tegallalang, Tanah Lot és az uluwatui sziklák."), [],
    [("short", "loop", 100, 2500, ("Bali south", "Dél-Bali"), ("Short loop: Tanah Lot, Uluwatu and the south coast.", "Rövid kör: Tanah Lot, Uluwatu és a déli part."),
      ["WADD", ["Tanah Lot", -8.6212, 115.0868], ["Uluwatu Temple", -8.8291, 115.0849], ["Nusa Penida", -8.7320, 115.4750], "WADD"]),
     ("full", "loop", 105, 6500, ("Bali loop", "Bali-kör"), ("About an hour: Uluwatu, Tegallalang rice terraces, Mount Batur and Mount Agung.", "Kb. egy óra: Uluwatu, Tegallalang rizsteraszai, a Batur és az Agung."),
      ["WADD", ["Uluwatu Temple", -8.8291, 115.0849], ["Mount Agung", -8.3430, 115.5080], ["Mount Batur", -8.2420, 115.3750], ["Tegallalang Rice Terraces", -8.4312, 115.2793], ["Tanah Lot", -8.6212, 115.0868], "WADD"])])
add("AS", "singapore", SG, ("Singapore", "Szingapúr"), ("Marina Bay Sands", "Marina Bay Sands", 1.2834, 103.8607), ["city", "island", "coast"],
    ("A garden city on an island: Marina Bay Sands, Sentosa and the green island of Pulau Ubin.", "Kertváros egy szigeten: a Marina Bay Sands, Sentosa és a zöld Pulau Ubin."), [],
    [("loop", "loop", 95, 1800, ("Singapore loop", "Szingapúr-kör"), ("Marina Bay Sands, Sentosa and Pulau Ubin.", "Marina Bay Sands, Sentosa és Pulau Ubin."),
      ["WSSS", ["Pulau Ubin", 1.4040, 103.9660], ["Marina Bay Sands", 1.2834, 103.8607], ["Sentosa", 1.2494, 103.8303], ["Jurong Lake Gardens", 1.3380, 103.7300], "WSSS"])])

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
open(os.path.join(os.path.dirname(P), "..", "tools", "r2_ids.txt"), "w").write(" ".join(NEW))
print(len(NEW), "uj tura")
