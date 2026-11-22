#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""6. kor: surusites (Europa + minden foldresz). Sorrend: add_r6 -> tours_order <r6_ids> -> poi_registry -> tours_kw -> tours_img -> tours_check"""
from tourlib import *
import json, os
C = lambda e, h: (e, h)
CH = C("Switzerland", "Svájc"); IS = C("Iceland", "Izland"); NO = C("Norway", "Norvégia"); GR = C("Greece", "Görögország"); IT = C("Italy", "Olaszország")
ES = C("Spain", "Spanyolország"); AT = C("Austria", "Ausztria"); IE = C("Ireland", "Írország"); UK = C("United Kingdom", "Egyesült Királyság"); HU = C("Hungary", "Magyarország")
JP = C("Japan", "Japán"); TW = C("Taiwan", "Tajvan"); US = C("United States", "Egyesült Államok"); CA = C("Canada", "Kanada"); CL = C("Chile", "Chile"); AR = C("Argentina", "Argentína")
PF = C("French Polynesia", "Francia Polinézia")
CONT = {}


def add(cont, *a, **k):
    a = list(a)
    a.insert(6, [])
    tour(*a); CONT[a[0]] = cont


def Pt(n, la, lo): return [n, la, lo]


add("EU", "jungfrau", CH, ("Jungfrau and the Bernese Oberland", "A Jungfrau és a Berni-Alpok"), ("Jungfraujoch", "Jungfraujoch", 46.5472, 7.9853), ["mountain", "unesco"],
    ("Eiger, Mönch and Jungfrau above Interlaken, the longest glacier of the Alps and the turquoise lakes of Thun and Brienz.", "Az Eiger, a Mönch és a Jungfrau Interlaken felett, az Alpok leghosszabb gleccsere és a Thuni- és Brienzi-tó türkiz vize."),
    [("loop", "loop", 110, 11000, ("Eiger, Mönch, Jungfrau", "Eiger, Mönch, Jungfrau"), ("From Bern over Thun and Interlaken to the Jungfrau and the Aletsch glacier.", "Bernből Thun és Interlaken felett a Jungfrauhoz és az Aletsch-gleccserhez."),
      ["LSZB", Pt("Thun", 46.7580, 7.6280), Pt("Interlaken", 46.6863, 7.8632), Pt("Eiger", 46.5775, 8.0053), Pt("Jungfraujoch", 46.5472, 7.9853), Pt("Konkordiaplatz", 46.4980, 8.0640), Pt("Grindelwald", 46.6240, 8.0410), "LSZB"])])
add("EU", "iceland-south", IS, ("South Iceland: Hekla and the Waterfalls", "Dél-Izland: Hekla és a vízesések"), ("Skógafoss", "Skógafoss", 63.5321, -19.5115), ["volcano", "coast", "island"],
    ("Seljalandsfoss and Skógafoss, the black beach of Vík, the Westman Islands and the Hekla volcano, all within an hour of Reykjavik.", "Seljalandsfoss és Skógafoss, Vík fekete partja, a Vestmann-szigetek és a Hekla vulkán, egy órán belül Reykjavíkból."),
    [("loop", "loop", 120, 5000, ("Fire and Water", "Tűz és víz"), ("Hekla, Eyjafjallajökull, the waterfalls, Vík and the Westman Islands.", "Hekla, Eyjafjallajökull, a vízesések, Vík és a Vestmann-szigetek."),
      ["BIRK", Pt("Hekla", 63.9920, -19.6660), Pt("Eyjafjallajökull", 63.6314, -19.6083), Pt("Seljalandsfoss", 63.6156, -19.9886), Pt("Skógafoss", 63.5321, -19.5115), Pt("Vík í Mýrdal", 63.4190, -19.0060), Pt("Vestmannaeyjar", 63.4427, -20.2730), "BIRK"])])
add("EU", "tromso", NO, ("Tromsø and the Lyngen Alps", "Tromsø és a Lyngen-Alpok"), ("Tromsø", "Tromsø", 69.6489, 18.9553), ["mountain", "coast", "city"],
    ("The capital of the Arctic with sharp alpine peaks rising straight out of the fjords, and the island of Kvaløya.", "Az Északi-sark fővárosa, a fjordokból egyenesen kiemelkedő éles alpesi csúcsokkal és Kvaløya szigetével."),
    [("loop", "loop", 110, 6000, ("Arctic Alps", "Sarkvidéki Alpok"), ("Tromsø, the Lyngen Alps and Kvaløya.", "Tromsø, a Lyngen-Alpok és Kvaløya."),
      ["ENTC", Pt("Tromsø", 69.6489, 18.9553), Pt("Jiehkkevárri", 69.6003, 20.0636), Pt("Lyngenfjord", 69.7000, 20.2500), Pt("Kvaløya", 69.7000, 18.5500), "ENTC"])])
add("EU", "meteora", GR, ("Meteora and Mount Olympus", "Meteora és az Olümposz"), ("Meteora monasteries", "Meteora kolostorai", 39.7217, 21.6306), ["culture", "unesco", "mountain"],
    ("Monasteries on sandstone pillars and the mythical home of the Greek gods, with the Thermaic Gulf on the way.", "Kolostorok homokkő-oszlopokon és a görög istenek mondabeli otthona, útközben a Thermaikosz-öböllel."),
    [("long", "loop", 120, 7000, ("Gods and Monks", "Istenek és szerzetesek"), ("Thessaloniki, Mount Olympus and the Meteora monasteries and back.", "Thesszaloniki, az Olümposz és a Meteora kolostorai, majd vissza."),
      ["LGTS", Pt("Mount Olympus", 40.0850, 22.3580), Pt("Meteora", 39.7217, 21.6306), Pt("Kozani", 40.3000, 21.7900), Pt("Veria", 40.5240, 22.2020), "LGTS"])])
add("EU", "corfu", GR, ("Corfu and Paxos", "Korfu és Paxosz"), ("Corfu Old Town", "Korfu óvárosa", 39.6243, 19.9217), ["island", "coast", "unesco"],
    ("Venetian old town, the Canal d'Amour rock formations, tiny Paxos and the Albanian ruins of Butrint just across the strait.", "Velencei óváros, a Canal d'Amour sziklái, a pici Paxosz és a szoros túloldalán Butrint albán romjai."),
    [("loop", "loop", 100, 3000, ("Ionian loop", "Jón-tengeri kör"), ("Corfu Town, Sidari, Butrint, Paxos and back along the coast.", "Korfu városa, Sidari, Butrint, Paxosz, majd vissza a part mentén."),
      ["LGKR", Pt("Corfu Old Town", 39.6243, 19.9217), Pt("Sidari", 39.7900, 19.7000), Pt("Butrint", 39.7460, 20.0210), Pt("Paxos", 39.2000, 20.1800), Pt("Kavos", 39.3900, 20.0300), "LGKR"])])
add("EU", "rhodes", GR, ("Rhodes and Symi", "Rodosz és Szümi"), ("Rhodes Old Town", "Rodosz óvárosa", 36.4450, 28.2270), ["island", "culture", "unesco"],
    ("The medieval city of the Knights, white Lindos on its cliff and the pastel harbour of Symi.", "A lovagok középkori városa, a sziklán álló fehér Lindosz és Szümi pasztellszínű kikötője."),
    [("loop", "loop", 100, 3000, ("Knights' Island", "A lovagok szigete"), ("Rhodes Old Town, Lindos, Symi and the west coast.", "Rodosz óvárosa, Lindosz, Szümi és a nyugati part."),
      ["LGRP", Pt("Rhodes Old Town", 36.4450, 28.2270), Pt("Lindos", 36.0920, 28.0850), Pt("Symi", 36.6000, 27.8400), Pt("Monolithos", 36.1200, 27.7500), "LGRP"])])
add("EU", "sardinia", IT, ("Sardinia: Costa Smeralda", "Szardínia: Costa Smeralda"), ("Porto Cervo", "Porto Cervo", 41.1370, 9.5380), ["island", "coast"],
    ("Emerald water, granite coves, the La Maddalena archipelago and Bonifacio's cliffs just across the strait in Corsica.", "Smaragdzöld víz, gránitöblök, a La Maddalena-szigetcsoport és Bonifacio sziklái a szoros túloldalán, Korzikán."),
    [("loop", "loop", 100, 3000, ("Emerald Coast", "Smaragd-part"), ("Porto Cervo, La Maddalena, Bonifacio and Capo Testa.", "Porto Cervo, La Maddalena, Bonifacio és Capo Testa."),
      ["LIEO", Pt("Porto Cervo", 41.1370, 9.5380), Pt("La Maddalena", 41.2150, 9.4080), Pt("Bonifacio", 41.3870, 9.1590), Pt("Capo Testa", 41.2420, 9.1450), "LIEO"])])
add("EU", "puglia", IT, ("Puglia: Trulli and Baroque", "Puglia: trullók és barokk"), ("Alberobello", "Alberobello", 40.7860, 17.2400), ["culture", "coast", "unesco"],
    ("The heel of Italy: the conical trulli of Alberobello, cliffside Polignano a Mare, baroque Lecce and Otranto on the Adriatic.", "Olaszország sarka: Alberobello kúpos trullói, a sziklaperemi Polignano a Mare, a barokk Lecce és Otranto az Adrián."),
    [("ab", "ab", 110, 3000, ("Bari to Brindisi", "Bari és Brindisi között"), ("Polignano a Mare, the trulli of Alberobello and white Ostuni.", "Polignano a Mare, Alberobello trullói és a fehér Ostuni."),
      ["LIBD", Pt("Polignano a Mare", 40.9970, 17.2190), Pt("Alberobello", 40.7860, 17.2400), Pt("Ostuni", 40.7290, 17.5780), "LIBR"])])
add("EU", "lanzarote", ES, ("Lanzarote: Land of Fire", "Lanzarote: a tűz országa"), ("Timanfaya", "Timanfaya", 29.0300, -13.7270), ["volcano", "island", "unesco"],
    ("A black volcanic landscape of Timanfaya, César Manrique's lava caves and the white beaches of Papagayo.", "Timanfaya fekete vulkáni tája, César Manrique lávabarlangjai és a Papagayo fehér strandjai."),
    [("loop", "loop", 100, 3000, ("Timanfaya loop", "Timanfaya-kör"), ("Timanfaya, Jameos del Agua, La Graciosa and Papagayo.", "Timanfaya, Jameos del Agua, La Graciosa és Papagayo."),
      ["GCRR", Pt("Timanfaya", 29.0300, -13.7270), Pt("Jameos del Agua", 29.1570, -13.4310), Pt("La Graciosa", 29.2330, -13.5030), Pt("Playa Papagayo", 28.8590, -13.7900), "GCRR"])])
add("EU", "tyrol", AT, ("Tyrol: Innsbruck and the Zugspitze", "Tirol: Innsbruck és a Zugspitze"), ("Zugspitze", "Zugspitze", 47.4210, 10.9850), ["mountain", "city"],
    ("Innsbruck below the Nordkette, Germany's highest peak, the Wilder Kaiser and Austria's highest mountain, the Grossglockner.", "Innsbruck az Északi-lánc alatt, Németország legmagasabb csúcsa, a Wilder Kaiser és Ausztria legmagasabb hegye, a Grossglockner."),
    [("long", "loop", 110, 11000, ("Alpine Giants", "Alpesi óriások"), ("Innsbruck, the Zugspitze, Wilder Kaiser, Kitzbühel and the Grossglockner.", "Innsbruck, a Zugspitze, a Wilder Kaiser, Kitzbühel és a Grossglockner."),
      ["LOWI", Pt("Zugspitze", 47.4210, 10.9850), Pt("Wilder Kaiser", 47.5600, 12.2800), Pt("Kitzbühel", 47.4460, 12.3920), Pt("Grossglockner", 47.0740, 12.6940), Pt("Zillertal Alps", 47.0500, 11.7000), "LOWI"])])
add("EU", "lake-geneva", CH, ("Lake Geneva and Lavaux", "A Genfi-tó és Lavaux"), ("Chillon Castle", "Chillon vára", 46.4146, 6.9276), ["culture", "unesco", "mountain"],
    ("The Jet d'Eau, the terraced vineyards of Lavaux, Chillon Castle and Mont Blanc towering behind the Savoy Alps.", "A Jet d'Eau, Lavaux teraszos szőlői, a Chillon-vár és a Savoyai-Alpok mögül kiemelkedő Mont Blanc."),
    [("loop", "loop", 110, 7000, ("Lake Geneva loop", "Genfi-tó kör"), ("Geneva, Lausanne, Lavaux, Chillon and the Mont Blanc massif.", "Genf, Lausanne, Lavaux, Chillon és a Mont Blanc-hegység."),
      ["LSGG", Pt("Jet d'Eau", 46.2074, 6.1558), Pt("Lausanne", 46.5197, 6.6323), Pt("Lavaux", 46.4900, 6.7300), Pt("Chillon Castle", 46.4146, 6.9276), Pt("Mont Blanc", 45.8326, 6.8652), "LSGG"])])
add("EU", "kerry", IE, ("Kerry and the Skelligs", "Kerry és a Skellig-szigetek"), ("Skellig Michael", "Skellig Michael", 51.7710, -10.5400), ["coast", "island", "unesco", "mountain"],
    ("Ireland's wildest corner: Killarney's lakes, the Dingle peninsula and the monastic rock of Skellig Michael out in the Atlantic.", "Írország legvadabb sarka: Killarney tavai, a Dingle-félsziget és az Atlanti-óceán közepén álló Skellig Michael kolostorsziklája."),
    [("loop", "loop", 100, 3000, ("Ring of Kerry and Dingle", "Kerry-gyűrű és Dingle"), ("Killarney, Skellig Michael, Slea Head and the Dingle peninsula.", "Killarney, Skellig Michael, Slea Head és a Dingle-félsziget."),
      ["EIKY", Pt("Killarney", 52.0600, -9.5200), Pt("Skellig Michael", 51.7710, -10.5400), Pt("Slea Head", 52.1000, -10.4600), Pt("Dingle", 52.1400, -10.2700), "EIKY"])])
add("EU", "snowdonia", UK, ("Snowdonia and Anglesey", "Snowdonia és Anglesey"), ("Snowdon", "Snowdon", 53.0685, -4.0763), ["mountain", "coast", "culture"],
    ("The highest mountain of Wales, the castles of Conwy and Caernarfon and the colourful village of Portmeirion.", "Wales legmagasabb hegye, Conwy és Caernarfon várai és a színes Portmeirion falu."),
    [("loop", "loop", 100, 4000, ("Castles and Peaks", "Várak és csúcsok"), ("Conwy, Snowdon, Caernarfon, Anglesey and Portmeirion.", "Conwy, a Snowdon, Caernarfon, Anglesey és Portmeirion."),
      ["EGNR", Pt("Conwy Castle", 53.2800, -3.8250), Pt("Snowdon", 53.0685, -4.0763), Pt("Portmeirion", 52.9140, -4.0980), Pt("Caernarfon Castle", 53.1390, -4.2770), Pt("South Stack", 53.3090, -4.6990), "EGNR"])])
add("EU", "lake-district", UK, ("Lake District and Hadrian's Wall", "Lake District és a Hadrianus-fal"), ("Windermere", "Windermere", 54.3700, -2.9300), ["mountain", "culture", "unesco"],
    ("England's lakeland with Scafell Pike and Windermere, then the Roman wall striding across the hills.", "Anglia tóvidéke a Scafell Pike-kal és a Windermere-rel, majd a dombokon átvonuló római fal."),
    [("loop", "loop", 100, 4000, ("Lakes and the Wall", "Tavak és a fal"), ("Keswick, Scafell Pike, Windermere and Hadrian's Wall at Housesteads.", "Keswick, a Scafell Pike, Windermere és a Hadrianus-fal Housesteadsnél."),
      ["EGNC", Pt("Keswick", 54.6000, -3.1340), Pt("Scafell Pike", 54.4542, -3.2116), Pt("Windermere", 54.3700, -2.9300), Pt("Housesteads", 55.0270, -2.3270), "EGNC"])])
add("EU", "danube-bend", HU, ("Danube Bend", "Dunakanyar"), ("Visegrád", "Visegrád", 47.7890, 18.9690), ["culture", "city"],
    ("The Danube cutting through the Visegrád hills: the Esztergom basilica, the royal castle and the artists' town of Szentendre.", "A Duna a Visegrádi-hegységen át: az esztergomi bazilika, a királyi vár és a művészváros, Szentendre."),
    [("short", "loop", 100, 3000, ("Danube Bend", "Dunakanyar"), ("Szentendre, Visegrád, Esztergom and Vác.", "Szentendre, Visegrád, Esztergom és Vác."),
      ["LHBP", Pt("Szentendre", 47.6700, 19.0750), Pt("Visegrád", 47.7890, 18.9690), Pt("Esztergom Basilica", 47.7990, 18.7390), Pt("Vác", 47.7800, 19.1330), "LHBP"])])
add("EU", "tokaj-eger", HU, ("Eger, Bükk and Tokaj", "Eger, Bükk és Tokaj"), ("Tokaj", "Tokaj", 48.1180, 21.4090), ["culture", "mountain"],
    ("Two wine regions in one flight: Eger's baroque castle town under the Bükk hills and the volcanic Tokaj hill with its vineyards.", "Két borvidék egy repülésben: Eger barokk vára a Bükk alatt és a vulkáni Tokaj-hegy szőlői."),
    [("long", "loop", 105, 4000, ("Wine route", "Borút"), ("Eger, the Bükk plateau, Tokaj and the Zemplén hills.", "Eger, a Bükk fennsík, Tokaj és a Zempléni-hegység."),
      ["LHBP", Pt("Eger", 47.9020, 20.3770), Pt("Bükk plateau", 48.0700, 20.5000), Pt("Tokaj", 48.1180, 21.4090), Pt("Zemplén Hills", 48.3500, 21.4000), "LHBP"])])
add("AS", "hokkaido", JP, ("Hokkaido: Lake Toya and Sapporo", "Hokkaidó: Tója-tó és Szapporo"), ("Lake Toya", "Tója-tó", 42.6000, 140.8500), ["volcano", "mountain", "city"],
    ("Crater lakes, the steaming valleys of Noboribetsu, perfect Mount Yotei and Sapporo.", "Kráterek tavai, Noboribetsu gőzölgő völgyei, a tökéletes Mount Yotei és Szapporo."),
    [("loop", "loop", 120, 6000, ("Crater lakes", "Kráter-tavak"), ("Sapporo, Mount Yotei, Lake Toya, Noboribetsu and Lake Shikotsu.", "Szapporo, a Mount Yotei, a Tója-tó, Noboribetsu és a Sikocu-tó."),
      ["RJCC", Pt("Mount Yotei", 42.8260, 140.8130), Pt("Lake Toya", 42.6000, 140.8500), Pt("Noboribetsu", 42.4980, 141.1450), Pt("Lake Shikotsu", 42.7600, 141.3300), "RJCC"])])
add("AS", "taiwan", TW, ("Taiwan: Taroko Gorge and Sun Moon Lake", "Tajvan: Taroko-szurdok és a Nap-Hold-tó"), ("Taroko Gorge", "Taroko-szurdok", 24.1590, 121.6220), ["mountain", "coast", "city"],
    ("Taipei 101, the marble gorge of Taroko, Yushan and Sun Moon Lake on a single sweep over the island.", "A Taipei 101, a Taroko márványszurdoka, a Jade-hegy és a Nap-Hold-tó egyetlen körrepülésben."),
    [("long", "loop", 120, 9000, ("Around Taiwan's heart", "Tajvan szíve körül"), ("Taipei, Jiufen, Taroko Gorge, Yushan and Sun Moon Lake.", "Tajpej, Csiufen, a Taroko-szurdok, a Jade-hegy és a Nap-Hold-tó."),
      ["RCSS", Pt("Taipei 101", 25.0330, 121.5654), Pt("Jiufen", 25.1090, 121.8440), Pt("Taroko Gorge", 24.1590, 121.6220), Pt("Yushan", 23.4700, 120.9570), Pt("Sun Moon Lake", 23.8570, 120.9150), "RCSS"])])
add("NA", "big-island", US, ("Big Island of Hawaii", "Hawaii Nagy-sziget"), ("Kīlauea", "Kīlauea", 19.4069, -155.2834), ["volcano", "island", "coast"],
    ("The only place on earth where you can fly past an erupting volcano, snow on Mauna Kea and the Waipi'o valley.", "Az egyetlen hely a Földön, ahol kitörő vulkán mellett repülhetsz el, a Mauna Kea havával és a Waipi'o-völggyel."),
    [("loop", "loop", 110, 9000, ("Volcanoes", "Vulkánok"), ("Hilo, Mauna Kea, Waipi'o and Kīlauea.", "Hilo, a Mauna Kea, Waipi'o és a Kīlauea."),
      ["PHTO", Pt("Akaka Falls", 19.8540, -155.1520), Pt("Waipi'o Valley", 20.1170, -155.5830), Pt("Mauna Kea", 19.8200, -155.4680), Pt("Kīlauea", 19.4069, -155.2834), "PHTO"])])
add("NA", "los-angeles", US, ("Los Angeles", "Los Angeles"), ("Hollywood Sign", "Hollywood-felirat", 34.1341, -118.3215), ["city", "coast"],
    ("The Hollywood sign, Griffith Observatory, Downtown and the Pacific coast from Santa Monica to Malibu.", "A Hollywood-felirat, a Griffith Obszervatórium, Downtown és a Csendes-óceán partja Santa Monicától Malibuig."),
    [("short", "loop", 100, 3000, ("Hollywood and the Coast", "Hollywood és a part"), ("Santa Monica, Hollywood sign, Downtown LA and Malibu.", "Santa Monica, Hollywood-felirat, Downtown LA és Malibu."),
      ["KSMO", Pt("Santa Monica Pier", 34.0092, -118.4973), Pt("Hollywood Sign", 34.1341, -118.3215), Pt("Downtown Los Angeles", 34.0522, -118.2437), Pt("Malibu Pier", 34.0360, -118.6770), "KSMO"])])
add("NA", "vancouver", CA, ("Vancouver and Whistler", "Vancouver és Whistler"), ("Stanley Park", "Stanley Park", 49.3043, -123.1443), ["city", "mountain", "coast"],
    ("A harbour city under the coastal mountains: Stanley Park, Grouse Mountain, the fjord of Howe Sound and Whistler.", "Kikötőváros a tengerparti hegyek alatt: Stanley Park, Grouse Mountain, a Howe Sound fjordja és Whistler."),
    [("loop", "loop", 110, 6000, ("Sea to Sky", "Tengertől az égig"), ("Stanley Park, Grouse Mountain, Howe Sound and Whistler.", "Stanley Park, Grouse Mountain, Howe Sound és Whistler."),
      ["CYVR", Pt("Stanley Park", 49.3043, -123.1443), Pt("Grouse Mountain", 49.3790, -123.0830), Pt("Howe Sound", 49.6500, -123.2000), Pt("Whistler", 50.1163, -122.9574), "CYVR"])])
add("SA", "santiago-andes", CL, ("Santiago and the Andes", "Santiago és az Andok"), ("Aconcagua", "Aconcagua", -32.6532, -70.0109), ["mountain", "city", "coast"],
    ("The Chilean capital under a wall of snowy Andes, the Aconcagua and Valparaíso's coloured hills on the Pacific.", "A chilei főváros a havas Andok fala alatt, az Aconcagua és Valparaíso színes dombjai a Csendes-óceánon."),
    [("long", "loop", 120, 14000, ("Andes and Pacific", "Andok és Csendes-óceán"), ("Santiago, Aconcagua and Valparaíso.", "Santiago, az Aconcagua és Valparaíso."),
      ["SCEL", Pt("Santiago", -33.4372, -70.6506), Pt("Aconcagua", -32.6532, -70.0109), Pt("Valparaíso", -33.0472, -71.6127), "SCEL"])])
add("SA", "bariloche", AR, ("Bariloche and the Lake District", "Bariloche és a tóvidék"), ("Cerro Tronador", "Cerro Tronador", -41.1670, -71.8840), ["mountain", "coast"],
    ("Patagonia's lake district: Nahuel Huapi, the glaciers of Tronador and the Circuito Chico.", "Patagónia tóvidéke: a Nahuel Huapi, a Tronador gleccserei és a Circuito Chico."),
    [("loop", "loop", 100, 8000, ("Nahuel Huapi", "Nahuel Huapi"), ("Cerro Catedral, Cerro Tronador and Lake Nahuel Huapi.", "A Cerro Catedral, a Cerro Tronador és a Nahuel Huapi-tó."),
      ["SAZS", Pt("Cerro Catedral", -41.1700, -71.4400), Pt("Cerro Tronador", -41.1670, -71.8840), Pt("Isla Victoria", -40.9100, -71.5400), "SAZS"])])
add("OC", "kauai", US, ("Kauai: Na Pali and Waimea", "Kauai: Na Pali és Waimea"), ("Na Pali Coast", "Na Pali-part", 22.1700, -159.6500), ["island", "coast", "mountain"],
    ("Emerald cliffs of the Na Pali, Waimea Canyon and Mount Waialeale, the wettest spot on earth.", "A Na Pali smaragd sziklái, a Waimea-kanyon és a Mount Waialeale, a Föld egyik legcsapadékosabb pontja."),
    [("loop", "loop", 100, 4000, ("Garden Island", "A kert-sziget"), ("Waimea Canyon, the Na Pali coast, Hanalei and Mount Waialeale.", "A Waimea-kanyon, a Na Pali-part, Hanalei és a Mount Waialeale."),
      ["PHLI", Pt("Waimea Canyon", 22.0710, -159.6620), Pt("Na Pali Coast", 22.1700, -159.6500), Pt("Hanalei Bay", 22.2100, -159.5000), Pt("Mount Waialeale", 22.0700, -159.4950), "PHLI"])])
add("OC", "tahiti-moorea", PF, ("Tahiti and Moorea", "Tahiti és Moorea"), ("Moorea", "Moorea", -17.5388, -149.8295), ["island", "coast", "volcano"],
    ("Moorea's jagged peaks above lagoons, the surf of Teahupo'o and Tahiti's green volcanic interior.", "Moorea csipkézett csúcsai a lagúnák felett, Teahupo'o hullámai és Tahiti zöld vulkáni belseje."),
    [("loop", "loop", 100, 3500, ("Tahiti and Moorea", "Tahiti és Moorea"), ("Papeete, Moorea, Teahupo'o and Tahiti's interior.", "Papeete, Moorea, Teahupo'o és Tahiti belseje."),
      ["NTAA", Pt("Moorea", -17.5388, -149.8295), Pt("Cook's Bay", -17.5000, -149.8300), Pt("Teahupo'o", -17.8500, -149.2600), Pt("Mount Orohena", -17.6300, -149.5100), "NTAA"])])

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
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "r6_ids.txt"), "w").write(" ".join(NEW))
