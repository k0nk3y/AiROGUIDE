#!/usr/bin/env python3
"""1. kor: europai feher foltok + tura minden mas kontinensen (rovid ~20-30 perces es ~1 oras korok). Futtatas: add_r1.py -> tours_check.py"""
from tourlib import *
import json, os

PT = ("Portugal", "Portugália"); TR = ("Turkey", "Törökország"); ES = ("Spain", "Spanyolország"); GR = ("Greece", "Görögország"); DE = ("Germany", "Németország")
FO = ("Faroe Islands", "Feröer-szigetek"); FR = ("France", "Franciaország"); US = ("United States", "Egyesült Államok"); PE = ("Peru", "Peru"); BR = ("Brazil", "Brazília")
ZA = ("South Africa", "Dél-Afrika"); EG = ("Egypt", "Egyiptom"); TZ = ("Tanzania", "Tanzánia"); AU = ("Australia", "Ausztrália"); NZ = ("New Zealand", "Új-Zéland")
JP = ("Japan", "Japán"); AE = ("United Arab Emirates", "Egyesült Arab Emírségek"); HK = ("Hong Kong", "Hongkong")

# ---------------- Europa ----------------
tour("lisbon-sintra", PT, ("Lisbon and Sintra", "Lisszabon és Sintra"), ("Belém Tower", "Belémi torony", 38.6916, -9.2160), ["city", "culture", "coast", "unesco"],
     ("Lisbon on its seven hills, the Tagus and the fairytale palaces of Sintra, out to the Atlantic cliffs of Cabo da Roca.", "Lisszabon hét dombja, a Tejo és Sintra mesebeli palotái, egészen a Cabo da Roca atlanti szikláiig."), [],
     [("short", "loop", 100, 2000, ("Lisbon short", "Lisszabon rövid"), ("Short loop over the Tagus: the 25 de Abril Bridge, Belém and the Jerónimos Monastery.", "Rövid kör a Tejo felett: 25 de Abril híd, Belém és a Jerónimos-kolostor."),
       ["LPPT", ["Vasco da Gama Bridge", 38.7650, -9.0950], ["Cascais", 38.6970, -9.4215], ["Cristo Rei", 38.6779, -9.1712], ["25 de Abril Bridge", 38.6916, -9.1771], ["Belém Tower", 38.6916, -9.2160], ["Jerónimos Monastery", 38.6979, -9.2068], ["Praça do Comércio", 38.7075, -9.1364], "LPPT"]),
      ("sintra", "loop", 110, 2500, ("Lisbon, Sintra and Cabo da Roca", "Lisszabon, Sintra és Cabo da Roca"), ("About an hour: Belém, Cascais, Cabo da Roca and the palaces of Sintra.", "Kb. egy óra: Belém, Cascais, Cabo da Roca és a sintrai paloták."),
       ["LPPT", ["Belém Tower", 38.6916, -9.2160], ["Cascais", 38.6970, -9.4215], ["Cabo da Roca", 38.7804, -9.4986], ["Pena Palace", 38.7876, -9.3906], ["Sintra National Palace", 38.7970, -9.3900], "LPPT"])])
tour("algarve", PT, ("Algarve coast", "Algarve-part"), ("Benagil Cave", "Benagili barlang", 37.0870, -8.4210), ["coast", "culture"],
     ("Golden cliffs, sea caves and hidden beaches: Benagil, Lagos, Sagres and the Cape St Vincent lighthouse.", "Aranyló sziklák, tengeri barlangok és rejtett strandok: Benagil, Lagos, Sagres és a Szent Vince-fok világítótornya."), [],
     [("short", "loop", 100, 2000, ("Algarve short", "Algarve rövid"), ("Short loop along the golden cliffs: Albufeira, Benagil and Carvoeiro.", "Rövid kör az aranyló sziklák mentén: Albufeira, Benagil és Carvoeiro."),
       ["LPFR", ["Albufeira", 37.0860, -8.2500], ["Benagil Cave", 37.0870, -8.4210], ["Ponta da Piedade", 37.0790, -8.6700], ["Praia da Marinha", 37.0900, -8.4130], "LPFR"]),
      ("sagres", "loop", 110, 2000, ("Algarve to Sagres", "Algarve Sagresig"), ("About an hour: Faro lagoon, Benagil, Lagos and the Cape St Vincent lighthouse.", "Kb. egy óra: Faro lagúna, Benagil, Lagos és a Szent Vince-fok világítótornya."),
       ["LPFR", ["Ria Formosa", 37.0020, -7.8000], ["Benagil Cave", 37.0870, -8.4210], ["Lagos", 37.1028, -8.6730], ["Cape St Vincent Lighthouse", 37.0230, -8.9967], ["Ponta da Piedade", 37.0790, -8.6700], "LPFR"])])
tour("istanbul", TR, ("Istanbul and the Bosphorus", "Isztambul és a Boszporusz"), ("Hagia Sophia", "Hagia Sophia", 41.0086, 28.9802), ["city", "culture", "unesco", "coast"],
     ("Two continents in one flight: Hagia Sophia, the Blue Mosque, the Bosphorus bridges and the Golden Horn.", "Két kontinens egyetlen repülésben: Hagia Sophia, Kék mecset, a Boszporusz hídjai és az Aranyszarv-öböl."), [],
     [("short", "loop", 100, 2500, ("Istanbul short", "Isztambul rövid"), ("Short loop: the Princes' Islands, the Bosphorus Bridge, Dolmabahçe, the Galata Tower and Hagia Sophia.", "Rövid kör: a Hercegek-szigetei, a Boszporusz-híd, Dolmabahçe, a Galata-torony és a Hagia Sophia."),
       ["LTBA", ["Büyükada", 40.8587, 29.1253], ["Bosphorus Bridge", 41.0452, 29.0340], ["Dolmabahçe Palace", 41.0392, 29.0005], ["Galata Tower", 41.0256, 28.9744], ["Hagia Sophia", 41.0086, 28.9802], "LTBA"]),
      ("bosphorus", "loop", 105, 2500, ("Old city and the Bosphorus", "Óváros és a Boszporusz"), ("About an hour: the old city, the Galata Tower, Dolmabahçe and the three Bosphorus bridges.", "Kb. egy óra: az óváros, a Galata-torony, Dolmabahçe és a Boszporusz három hídja."),
       ["LTBA", ["Hagia Sophia", 41.0086, 28.9802], ["Galata Tower", 41.0256, 28.9744], ["Dolmabahçe Palace", 41.0392, 29.0005], ["Bosphorus Bridge", 41.0452, 29.0340], ["Fatih Sultan Mehmet Bridge", 41.0911, 29.0620], "LTBA"])])
tour("cappadocia", TR, ("Cappadocia", "Kappadókia"), ("Göreme", "Göreme", 38.6431, 34.8287), ["culture", "unesco", "mountain"],
     ("Fairy chimneys, cave dwellings and the morning balloons over the valleys of Göreme.", "Tündérkémények, barlanglakások és a reggeli hőlégballonok Göreme völgyei felett."), [],
     [("short", "loop", 100, 6000, ("Cappadocia short", "Kappadókia rövid"), ("Short loop over Göreme, Uçhisar and the Love Valley.", "Rövid kör Göreme, Uçhisar és a Szerelem-völgy felett."),
       ["LTAZ", ["Uçhisar Castle", 38.6285, 34.8040], ["Göreme", 38.6431, 34.8287], ["Love Valley", 38.6560, 34.8310], ["Ürgüp", 38.6310, 34.9120], "LTAZ"]),
      ("full", "loop", 105, 7000, ("Cappadocia loop", "Kappadókia-kör"), ("About an hour: Avanos, Göreme, Derinkuyu and Mount Erciyes.", "Kb. egy óra: Avanos, Göreme, Derinkuyu és az Erciyes-hegy."),
       ["LTAZ", ["Avanos", 38.7150, 34.8450], ["Göreme", 38.6431, 34.8287], ["Ürgüp", 38.6310, 34.9120], ["Mount Erciyes", 38.5300, 35.4480], ["Derinkuyu Underground City", 38.3730, 34.7340], "LTAZ"])])
tour("mallorca", ES, ("Mallorca", "Mallorca"), ("Cap de Formentor", "Cap de Formentor", 39.9606, 3.2147), ["island", "coast", "culture"],
     ("Palma's cathedral, the Serra de Tramuntana, the coast road of Sa Calobra and the cliffs of Formentor.", "Palma katedrálisa, a Serra de Tramuntana, Sa Calobra kanyargós útja és a Formentor-fok sziklái."), [],
     [("short", "loop", 100, 3000, ("Mallorca short", "Mallorca rövid"), ("Short loop: Palma Cathedral, Valldemossa and the Tramuntana coast.", "Rövid kör: Palma katedrális, Valldemossa és a Tramuntana-part."),
       ["LEPA", ["Palma Cathedral", 39.5676, 2.6483], ["Valldemossa", 39.7110, 2.6240], ["Sa Calobra", 39.8500, 2.8000], ["Sóller", 39.7660, 2.7150], "LEPA"]),
      ("north", "loop", 110, 3500, ("Tramuntana and Formentor", "Tramuntana és Formentor"), ("About an hour: Valldemossa, Sa Calobra, Pollença and Cap de Formentor.", "Kb. egy óra: Valldemossa, Sa Calobra, Pollença és a Cap de Formentor."),
       ["LEPA", ["Valldemossa", 39.7110, 2.6240], ["Sa Calobra", 39.8500, 2.8000], ["Pollença", 39.8760, 3.0150], ["Cap de Formentor", 39.9606, 3.2147], ["Alcúdia", 39.8530, 3.1210], "LEPA"])])
tour("crete", GR, ("Crete", "Kréta"), ("Knossos Palace", "Knósszoszi palota", 35.2980, 25.1630), ["island", "culture", "coast", "mountain"],
     ("The Minoan palace of Knossos, the White Mountains with the Samaria Gorge and the lagoon of Balos.", "A minószi Knósszosz, a Lefka Ori a Szamaria-szurdokkal és a Balosz-lagúna."), [],
     [("short", "loop", 100, 3000, ("Crete short", "Kréta rövid"), ("Short loop from Heraklion: Knossos, Mount Ida and the south coast at Matala.", "Rövid kör Iráklióból: Knósszosz, az Ida-hegy és a déli part Matalánál."),
       ["LGIR", ["Knossos Palace", 35.2980, 25.1630], ["Mount Ida", 35.2280, 24.7740], ["Matala", 34.9940, 24.7490], ["Phaistos", 35.0510, 24.8140], "LGIR"]),
      ("west", "loop", 115, 5000, ("Western Crete", "Nyugat-Kréta"), ("About an hour from Chania: Samaria Gorge, Elafonisi and Balos lagoon.", "Kb. egy óra Haniából: Szamaria-szurdok, Elafonisi és a Balosz-lagúna."),
       ["LGSA", ["Balos Lagoon", 35.5880, 23.5880], ["Elafonisi Beach", 35.2740, 23.5420], ["Samaria Gorge", 35.2780, 23.9560], ["Chania Old Port", 35.5176, 24.0180], "LGSA"]),
      ("grand", "loop", 115, 4000, ("Crete grand loop", "Kréta nagy kör"), ("The east and south of the island: Spinalonga, Vai palm beach, Zakros, Chrissi island, Matala and Mount Ida.", "A sziget keleti és déli fele: Spinalonga, a Vai pálmaliget, Zakrosz, Chrissi-sziget, Matala és az Ida-hegy."),
       ["LGIR", ["Spinalonga", 35.2989, 25.7390], ["Vai Palm Beach", 35.2520, 26.2610], ["Zakros", 35.0980, 26.2610], ["Chrissi Island", 34.8830, 25.7050], ["Matala", 34.9940, 24.7490], ["Mount Ida", 35.2280, 24.7740], ["Knossos Palace", 35.2980, 25.1630], "LGIR"])])
tour("berlin", DE, ("Berlin and Potsdam", "Berlin és Potsdam"), ("Brandenburg Gate", "Brandenburgi kapu", 52.5163, 13.3777), ["city", "culture", "unesco"],
     ("The Reichstag, the Brandenburg Gate, the TV Tower and Sanssouci, the Prussian kings' summer palace in Potsdam.", "A Reichstag, a Brandenburgi kapu, a tévétorony és a potsdami Sanssouci, a porosz királyok nyári palotája."), [],
     [("short", "loop", 90, 2500, ("Berlin short", "Berlin rövid"), ("Short loop over the centre: TV Tower, Reichstag and the Brandenburg Gate.", "Rövid kör a belváros felett: tévétorony, Reichstag és Brandenburgi kapu."),
       ["EDDB", ["Tempelhof Field", 52.4733, 13.4019], ["Berlin Victory Column", 52.5145, 13.3501], ["Brandenburg Gate", 52.5163, 13.3777], ["Berlin TV Tower", 52.5208, 13.4094], ["East Side Gallery", 52.5050, 13.4396], "EDDB"]),
      ("potsdam", "loop", 105, 2500, ("Berlin and Potsdam", "Berlin és Potsdam"), ("About an hour: the centre, Charlottenburg Palace, Sanssouci and Müggelsee.", "Kb. egy óra: a belváros, a Charlottenburg-palota, Sanssouci és a Müggel-tó."),
       ["EDDB", ["Berlin TV Tower", 52.5208, 13.4094], ["Brandenburg Gate", 52.5163, 13.3777], ["Charlottenburg Palace", 52.5206, 13.2960], ["Sanssouci Palace", 52.4040, 13.0380], ["Müggelsee", 52.4350, 13.6450], "EDDB"])])
tour("faroe", FO, ("Faroe Islands", "Feröer-szigetek"), ("Múlafossur Waterfall", "Múlafossur-vízesés", 62.1330, -7.4460), ["island", "coast", "mountain"],
     ("Green cliffs dropping into the North Atlantic: Gásadalur, Saksun and the Kallur lighthouse on the island of Kalsoy.", "Zöld sziklafalak az Atlanti-óceánba: Gásadalur, Saksun és a Kallur világítótorony Kalsoy szigetén."), [],
     [("short", "loop", 100, 3000, ("Faroe short", "Feröer rövid"), ("Short loop over Vágar and Streymoy: Gásadalur, Saksun and Tórshavn.", "Rövid kör Vágar és Streymoy felett: Gásadalur, Saksun és Tórshavn."),
       ["EKVG", ["Múlafossur Waterfall", 62.1330, -7.4460], ["Saksun", 62.2490, -7.1670], ["Tórshavn", 62.0110, -6.7710], "EKVG"]),
      ("north", "loop", 105, 3500, ("Faroe north isles", "Feröer északi szigetek"), ("About an hour: Gásadalur, Saksun, Kalsoy and the cliffs of Vestmanna.", "Kb. egy óra: Gásadalur, Saksun, Kalsoy és a vestmannai sziklák."),
       ["EKVG", ["Múlafossur Waterfall", 62.1330, -7.4460], ["Vestmanna Bird Cliffs", 62.1560, -7.1760], ["Saksun", 62.2490, -7.1670], ["Kallur Lighthouse", 62.3680, -6.6760], ["Tórshavn", 62.0110, -6.7710], "EKVG"])])
tour("brittany", FR, ("Brittany coast", "Bretagne partvidéke"), ("Cap Fréhel", "Cap Fréhel", 48.6830, -2.3170), ["coast", "culture", "island"],
     ("Saint-Malo's walled harbour, the cliffs of Cap Fréhel and the pink granite coast of Perros-Guirec.", "Saint-Malo falakkal körülvett kikötője, a Cap Fréhel sziklái és Perros-Guirec rózsaszín gránitpartja."), [],
     [("short", "loop", 100, 2000, ("Emerald Coast", "Smaragd-part"), ("Short loop from Dinard: Saint-Malo, Cap Fréhel and Fort La Latte.", "Rövid kör Dinardból: Saint-Malo, Cap Fréhel és a La Latte-erőd."),
       ["LFRD", ["Saint-Malo", 48.6490, -2.0260], ["Fort La Latte", 48.6740, -2.2860], ["Cap Fréhel", 48.6830, -2.3170], ["Dinan", 48.4550, -2.0500], "LFRD"]),
      ("pink", "loop", 110, 2000, ("Pink granite coast", "Rózsaszín gránitpart"), ("About an hour: Saint-Malo, Cap Fréhel, Perros-Guirec and Mont-Dol.", "Kb. egy óra: Saint-Malo, Cap Fréhel, Perros-Guirec és a Mont-Dol."),
       ["LFRD", ["Saint-Malo", 48.6490, -2.0260], ["Cap Fréhel", 48.6830, -2.3170], ["Perros-Guirec", 48.8250, -3.4400], ["Brehat Island", 48.8500, -3.0050], ["Mont-Dol", 48.5420, -1.7230], "LFRD"])])

# ---------------- Eszak-Amerika ----------------
tour("new-york", US, ("New York City", "New York"), ("Statue of Liberty", "Szabadság-szobor", 40.6892, -74.0445), ["city", "culture", "coast"],
     ("Manhattan's skyline from the Hudson: the Statue of Liberty, Empire State Building, Central Park and the Brooklyn Bridge.", "Manhattan látképe a Hudson felől: Szabadság-szobor, Empire State Building, Central Park és a Brooklyn-híd."), [],
     [("loop", "loop", 100, 1500, ("Manhattan loop", "Manhattan-kör"), ("Central Park, Empire State Building, the Statue of Liberty and the Brooklyn Bridge.", "Central Park, Empire State Building, Szabadság-szobor és a Brooklyn-híd."),
       ["KLGA", ["Central Park", 40.7829, -73.9654], ["Empire State Building", 40.7484, -73.9857], ["Statue of Liberty", 40.6892, -74.0445], ["Brooklyn Bridge", 40.7061, -73.9969], ["One World Trade Center", 40.7127, -74.0134], ["Yankee Stadium", 40.8296, -73.9262], "KLGA"])])
tour("grand-canyon", US, ("Grand Canyon", "Grand Canyon"), ("Grand Canyon South Rim", "Grand Canyon déli pereme", 36.0544, -112.1401), ["mountain", "culture", "coast"],
     ("A mile deep and 277 miles long: the South Rim, Desert View and the North Rim from above.", "Másfél kilométer mély és 446 kilométer hosszú: a déli perem, a Desert View és az északi perem felülről."), [],
     [("loop", "loop", 110, 9500, ("Canyon rim loop", "Kanyon-perem kör"), ("From the South Rim over Desert View to the North Rim and back across the canyon.", "A déli peremről a Desert View felett az északi peremre, majd vissza a kanyon felett."),
       ["KGCN", ["Desert View Watchtower", 36.0436, -111.8260], ["Bright Angel Point", 36.1900, -112.0536], ["Grand Canyon Village", 36.0544, -112.1401], "KGCN"])])
tour("sf-bay", US, ("San Francisco Bay", "San Francisco-öböl"), ("Golden Gate Bridge", "Golden Gate híd", 37.8199, -122.4783), ["city", "culture", "coast"],
     ("The Golden Gate, Alcatraz and the Bay Bridge, with the fog rolling in from the Pacific.", "A Golden Gate, Alcatraz és a Bay Bridge, miközben a köd gördül be a Csendes-óceán felől."), [],
     [("loop", "loop", 95, 1800, ("Bay loop", "Öböl-kör"), ("Ocean Beach, the Golden Gate Bridge, Alcatraz and the Bay Bridge.", "Ocean Beach, Golden Gate híd, Alcatraz és a Bay Bridge."),
       ["KSFO", ["Ocean Beach", 37.7600, -122.5100], ["Golden Gate Bridge", 37.8199, -122.4783], ["Alcatraz Island", 37.8267, -122.4230], ["Bay Bridge", 37.7983, -122.3778], "KSFO"])])
tour("oahu", US, ("Hawaiian Islands", "Hawaii szigetei"), ("Diamond Head", "Diamond Head", 21.2619, -157.8058), ["island", "coast", "volcano"],
     ("Oahu's Diamond Head and Pearl Harbor, the Na Pali cliffs of Kauai, Maui's Haleakala crater and the volcanoes of the Big Island.", "Oahu Diamond Head-je és Pearl Harbor, Kauai Na Pali-sziklái, Maui Haleakala-kráterje és a Nagy-sziget vulkánjai."), [],
     [("loop", "loop", 100, 2000, ("Oahu loop", "Oahu-kör"), ("Diamond Head, Hanauma Bay, Kualoa and Pearl Harbor.", "Diamond Head, Hanauma-öböl, Kualoa és Pearl Harbor."),
       ["PHNL", ["Diamond Head", 21.2619, -157.8058], ["Hanauma Bay", 21.2690, -157.6940], ["Makapuu Point Lighthouse", 21.3103, -157.6490], ["Kualoa Ranch", 21.5222, -157.8369], ["Pearl Harbor", 21.3649, -157.9500], "PHNL"]),
      ("kauai", "loop", 100, 4500, ("Kauai: Na Pali and Waimea", "Kauai: Na Pali és Waimea"), ("From Lihue: Wailua Falls, Waimea Canyon, the Na Pali coast and Hanalei Bay.", "Lihue felől: Wailua-vízesés, Waimea-kanyon, a Na Pali-part és a Hanalei-öböl."),
       ["PHLI", ["Wailua Falls", 22.0467, -159.3786], ["Waimea Canyon", 22.0714, -159.6638], ["Kalalau Valley", 22.1700, -159.6400], ["Hanalei Bay", 22.2035, -159.5013], "PHLI"]),
      ("maui", "loop", 105, 11000, ("Maui: Haleakala and Hana", "Maui: Haleakala és Hana"), ("From Kahului: Iao Valley, Lahaina, Molokini and the Haleakala crater, back over the Hana coast.", "Kahuluiból: Iao-völgy, Lahaina, Molokini és a Haleakala-kráter, vissza a Hana-part felett."),
       ["PHOG", ["Iao Valley", 20.8830, -156.5460], ["Lahaina", 20.8783, -156.6825], ["Molokini Crater", 20.6300, -156.4960], ["Haleakala Crater", 20.7097, -156.2533], ["Hana", 20.7580, -155.9890], "PHOG"]),
      ("bigisland", "loop", 110, 14500, ("Big Island volcanoes", "A Nagy-sziget vulkánjai"), ("From Hilo: Akaka Falls, Mauna Kea and the Kilauea crater.", "Hilóból: Akaka-vízesés, Mauna Kea és a Kilauea-kráter."),
       ["PHTO", ["Akaka Falls", 19.8550, -155.1530], ["Mauna Kea", 19.8206, -155.4681], ["Kilauea Crater", 19.4069, -155.2834], ["Rainbow Falls", 19.7220, -155.1100], "PHTO"]),
      ("hop", "ab", 110, 5500, ("Island hop: Oahu to Maui", "Szigetugrás: Oahutól Mauiig"), ("A one-way hop over the channel islands: Diamond Head, Molokai's sea cliffs, Lanai and Molokini.", "Egyirányú szigetugrás: Diamond Head, Molokai tengeri sziklái, Lanai és Molokini."),
       ["PHNL", ["Diamond Head", 21.2619, -157.8058], ["Kalaupapa", 21.1888, -156.9830], ["Lanai City", 20.8270, -156.9200], ["Molokini Crater", 20.6300, -156.4960], "PHOG"]),
      ("all", "ab", 120, 8500, ("All islands: Kauai to the Big Island", "Összes sziget: Kauaitól a Nagy-szigetig"), ("A one-way flight along the whole chain: Kauai's Na Pali coast, Pearl Harbor, Molokai's sea cliffs, Haleakala on Maui, then Mauna Kea and Kilauea on the Big Island.", "Egyirányú repülés az egész szigetláncon: Kauai Na Pali-partja, Pearl Harbor, Molokai tengeri sziklái, Maui Haleakalája, majd a Nagy-sziget Mauna Keája és Kilaueája."),
       ["PHLI", ["Hanalei Bay", 22.2035, -159.5013], ["Kalalau Valley", 22.1700, -159.6400], ["Waimea Canyon", 22.0714, -159.6638], ["Pearl Harbor", 21.3649, -157.9500], ["Diamond Head", 21.2619, -157.8058],
        ["Kalaupapa", 21.1888, -156.9830], ["Haleakala Crater", 20.7097, -156.2533], ["Mauna Kea", 19.8206, -155.4681], ["Kilauea Crater", 19.4069, -155.2834], "PHTO"])])

# ---------------- Del-Amerika ----------------
tour("machu-picchu", PE, ("Machu Picchu and the Sacred Valley", "Machu Picchu és a Szent-völgy"), ("Machu Picchu", "Machu Picchu", -13.1631, -72.5450), ["mountain", "culture", "unesco"],
     ("The Inca citadel in the clouds, the terraces of Moray and the fortress of Ollantaytambo above the Urubamba river.", "Az inka fellegvár a felhők között, Moray teraszai és Ollantaytambo erődje az Urubamba folyó felett."), [],
     [("short", "loop", 100, 15000, ("Cusco short", "Cusco rövid"), ("Short loop from Cusco: Sacsayhuamán, Pisac and Moray.", "Rövid kör Cuscóból: Sacsayhuamán, Pisac és Moray."),
       ["SPZO", ["Sacsayhuamán", -13.5093, -71.9817], ["Pisac", -13.4167, -71.8475], ["Moray", -13.3293, -72.1962], "SPZO"]),
      ("full", "loop", 110, 15000, ("Machu Picchu loop", "Machu Picchu-kör"), ("About an hour: Pisac, Ollantaytambo and Machu Picchu, back over Moray.", "Kb. egy óra: Pisac, Ollantaytambo és Machu Picchu, vissza Moray felett."),
       ["SPZO", ["Pisac", -13.4167, -71.8475], ["Ollantaytambo", -13.2584, -72.2631], ["Machu Picchu", -13.1631, -72.5450], ["Moray", -13.3293, -72.1962], ["Sacsayhuamán", -13.5093, -71.9817], "SPZO"])])
tour("rio", BR, ("Rio de Janeiro", "Rio de Janeiro"), ("Christ the Redeemer", "Megváltó Krisztus-szobor", -22.9519, -43.2105), ["city", "culture", "coast", "mountain"],
     ("Christ the Redeemer, Sugarloaf Mountain and Copacabana: Rio between the granite peaks and the sea.", "A Megváltó Krisztus-szobor, a Cukorsüvegcsúcs és Copacabana: Rio a gránitcsúcsok és a tenger között."), [],
     [("loop", "loop", 95, 2500, ("Rio loop", "Rio-kör"), ("Sugarloaf, Copacabana, Christ the Redeemer and the Maracanã stadium.", "Cukorsüvegcsúcs, Copacabana, a Megváltó Krisztus-szobor és a Maracanã stadion."),
       ["SBGL", ["Rio-Niterói Bridge", -22.8780, -43.1630], ["Sugarloaf Mountain", -22.9486, -43.1566], ["Copacabana", -22.9711, -43.1822], ["Christ the Redeemer", -22.9519, -43.2105], ["Maracanã Stadium", -22.9122, -43.2302], ["Pedra da Gávea", -22.9980, -43.2850], "SBGL"])])
tour("iguazu", BR, ("Iguazu Falls", "Iguazú-vízesés"), ("Devil's Throat", "Az Ördög torka", -25.6953, -54.4367), ["culture", "unesco", "jungle"],
     ("275 waterfalls in the rainforest on the border of Brazil and Argentina, and the vast Itaipu Dam.", "275 vízesés az esőerdőben Brazília és Argentína határán, valamint a hatalmas Itaipu-gát."), [],
     [("loop", "loop", 100, 3000, ("Falls and Itaipu", "A vízesés és az Itaipu"), ("The Iguazu Falls and the Itaipu Dam on the Paraná river.", "Az Iguazú-vízesés és az Itaipu-gát a Paraná folyón."),
       ["SBFI", ["Iguazu Falls", -25.6953, -54.4367], ["Triple Frontier", -25.5990, -54.5780], ["Itaipu Dam", -25.4079, -54.5886], "SBFI"])])

# ---------------- Afrika ----------------
tour("cape-town", ZA, ("Cape Town and the Cape Peninsula", "Fokváros és a Fok-félsziget"), ("Table Mountain", "Table Mountain", -33.9628, 18.4098), ["city", "coast", "mountain"],
     ("Table Mountain, Robben Island, the road along Chapman's Peak and the penguins of Boulders Beach.", "A Table Mountain, a Robben-sziget, a Chapman's Peak útja és a Boulders Beach pingvinjei."), [],
     [("short", "loop", 100, 3500, ("Cape Town short", "Fokváros rövid"), ("Short loop: Robben Island, Table Mountain and Camps Bay.", "Rövid kör: Robben-sziget, Table Mountain és Camps Bay."),
       ["FACT", ["Robben Island", -33.8070, 18.3710], ["Table Mountain", -33.9628, 18.4098], ["Camps Bay", -33.9500, 18.3780], ["Cape Town Stadium", -33.9035, 18.4110], "FACT"]),
      ("peninsula", "loop", 105, 3500, ("The Cape Peninsula", "A Fok-félsziget"), ("About an hour: Table Mountain, Chapman's Peak, Cape Point and Boulders Beach.", "Kb. egy óra: Table Mountain, Chapman's Peak, Cape Point és Boulders Beach."),
       ["FACT", ["Table Mountain", -33.9628, 18.4098], ["Chapman's Peak", -34.0830, 18.3670], ["Cape Point", -34.3568, 18.4971], ["Boulders Beach", -34.1976, 18.4511], "FACT"])])
tour("giza", EG, ("Cairo and the Pyramids", "Kairó és a piramisok"), ("Pyramids of Giza", "Gízai piramisok", 29.9792, 31.1342), ["culture", "unesco", "city"],
     ("The Pyramids of Giza, the step pyramid of Saqqara and the Nile cutting through Cairo.", "A gízai piramisok, a szakkarai lépcsős piramis és a Kairón átfolyó Nílus."), [],
     [("loop", "loop", 100, 3500, ("Pyramids loop", "Piramis-kör"), ("The Cairo Citadel, the Pyramids of Giza, Saqqara and Dahshur.", "A kairói fellegvár, a gízai piramisok, Szakkara és Dahsúr."),
       ["HECA", ["Cairo Citadel", 30.0287, 31.2612], ["Pyramids of Giza", 29.9792, 31.1342], ["Step Pyramid of Djoser", 29.8713, 31.2165], ["Red Pyramid", 29.8089, 31.2062], "HECA"]),
      ("fayum", "loop", 110, 4000, ("Pyramids and the Fayum", "Piramisok és a Fajjúm"), ("About an hour and a half: Giza, Saqqara, Dahshur, the Meidum pyramid and Lake Qarun in the Fayum oasis.", "Kb. másfél óra: Gíza, Szakkara, Dahsúr, a meidumi piramis és a Qarún-tó a Fajjúm-oázisban."),
       ["HECA", ["Cairo Citadel", 30.0287, 31.2612], ["Pyramids of Giza", 29.9792, 31.1342], ["Step Pyramid of Djoser", 29.8713, 31.2165], ["Red Pyramid", 29.8089, 31.2062], ["Meidum Pyramid", 29.3881, 31.1572], ["Lake Qarun", 29.4700, 30.6700], "HECA"])])
tour("kilimanjaro", TZ, ("Kilimanjaro and Amboseli", "Kilimandzsáró és Amboseli"), ("Mount Kilimanjaro", "Kilimandzsáró", -3.0674, 37.3556), ["mountain", "volcano"],
     ("Africa's highest peak above the savanna: Kilimanjaro, Mount Meru and the elephants of Amboseli.", "Afrika legmagasabb csúcsa a szavanna felett: a Kilimandzsáró, a Meru-hegy és Amboseli elefántjai."), [],
     [("loop", "loop", 110, 10500, ("Kilimanjaro loop", "Kilimandzsáró-kör"), ("Mount Meru, Amboseli and the summit of Kilimanjaro.", "A Meru-hegy, Amboseli és a Kilimandzsáró csúcsa."),
       ["HTKJ", ["Mount Meru", -3.2427, 36.7478], ["Amboseli National Park", -2.6527, 37.2606], ["Mount Kilimanjaro", -3.0674, 37.3556], "HTKJ"])])

# ---------------- Oceania ----------------
tour("sydney", AU, ("Sydney Harbour", "Sydney kikötő"), ("Sydney Opera House", "Sydney-i Operaház", -33.8568, 151.2153), ["city", "culture", "coast"],
     ("The Opera House, the Harbour Bridge, Bondi Beach and the sandstone cliffs of the Heads.", "Az Operaház, a Harbour Bridge, a Bondi-part és a homokkő sziklák a Heads-nél."), [],
     [("loop", "loop", 95, 1800, ("Harbour loop", "Kikötő-kör"), ("Bondi Beach, the Heads, the Opera House and the Harbour Bridge.", "Bondi-part, a Heads, az Operaház és a Harbour Bridge."),
       ["YSSY", ["Bondi Beach", -33.8915, 151.2767], ["Sydney Heads", -33.8310, 151.2860], ["Sydney Opera House", -33.8568, 151.2153], ["Sydney Harbour Bridge", -33.8523, 151.2108], ["Manly Beach", -33.7970, 151.2880], ["Sydney Tower", -33.8704, 151.2089], "YSSY"])])
tour("whitsundays", AU, ("Whitsunday Islands", "Whitsunday-szigetek"), ("Whitehaven Beach", "Whitehaven-part", -20.2818, 149.0415), ["island", "coast"],
     ("Silica-white sand and turquoise water: Whitehaven Beach, Hill Inlet and the Great Barrier Reef.", "Hófehér kvarchomok és türkiz víz: a Whitehaven-part, a Hill Inlet és a Nagy-korallzátony."), [],
     [("loop", "loop", 100, 1500, ("Whitsunday loop", "Whitsunday-kör"), ("Whitehaven Beach, with Hill Inlet at its north end, and the Heart Reef.", "A Whitehaven-part (északi végén a Hill Inlettel) és a Szív-zátony."),
       ["YBHM", ["Whitehaven Beach", -20.2818, 149.0415], ["Heart Reef", -19.7800, 149.2300], "YBHM"])])
tour("milford-sound", NZ, ("Milford Sound", "Milford Sound"), ("Mitre Peak", "Mitre Peak", -44.6190, 167.8070), ["mountain", "coast", "unesco"],
     ("From Queenstown over the Southern Alps into Fiordland: the Remarkables, Lake Wakatipu and Milford Sound.", "Queenstownból a Déli-Alpok felett Fiordlandbe: a Remarkables, a Wakatipu-tó és a Milford Sound."), [],
     [("ab", "ab", 110, 8500, ("Queenstown to Milford Sound", "Queenstowntól Milford Soundig"), ("A one-way flight over the Southern Alps; keep terrain clearance in mind.", "Egyirányú repülés a Déli-Alpok felett; figyelj a terep feletti magasságra."),
       ["NZQN", ["The Remarkables", -45.0500, 168.8000], ["Lake Wakatipu", -45.1000, 168.4000], ["Mitre Peak", -44.6190, 167.8070], "NZMF"])])

# ---------------- Azsia ----------------
tour("tokyo-fuji", JP, ("Tokyo and Mount Fuji", "Tokió és a Fudzsi"), ("Mount Fuji", "Fudzsi", 35.3606, 138.7274), ["city", "culture", "mountain", "volcano"],
     ("Tokyo Skytree and Tokyo Tower, then west to the perfect cone of Mount Fuji.", "A Tokyo Skytree és a Tokyo Tower, majd nyugatra a Fudzsi tökéletes kúpja."), [],
     [("short", "loop", 100, 2500, ("Tokyo short", "Tokió rövid"), ("Short loop over the bay: Tokyo Skytree, Tokyo Tower and the Rainbow Bridge.", "Rövid kör az öböl felett: Tokyo Skytree, Tokyo Tower és a Rainbow Bridge."),
       ["RJTT", ["Rainbow Bridge", 35.6364, 139.7630], ["Tokyo Tower", 35.6586, 139.7454], ["Tokyo Skytree", 35.7101, 139.8107], ["Senso-ji Temple", 35.7148, 139.7967], ["Tokyo Disneyland", 35.6329, 139.8804], ["Meiji Shrine", 35.6764, 139.6993], "RJTT"]),
      ("fuji", "loop", 110, 10500, ("Tokyo and Fuji", "Tokió és a Fudzsi"), ("About an hour: Tokyo Tower, Hakone and Mount Fuji, back over Yokohama.", "Kb. egy óra: Tokyo Tower, Hakone és a Fudzsi, vissza Jokohama felett."),
       ["RJTT", ["Tokyo Tower", 35.6586, 139.7454], ["Lake Ashi", 35.2000, 139.0250], ["Mount Fuji", 35.3606, 138.7274], ["Lake Kawaguchi", 35.5120, 138.7600], ["Yokohama Landmark Tower", 35.4545, 139.6318], "RJTT"])])
tour("dubai", AE, ("Dubai", "Dubaj"), ("Burj Khalifa", "Burdzs Kalifa", 25.1972, 55.2744), ["city", "coast", "island"],
     ("The Burj Khalifa, Palm Jumeirah and the Burj Al Arab: a desert city built on the Gulf.", "A Burdzs Kalifa, a Palm Jumeirah és a Burdzs al-Arab: sivatagi város a Perzsa-öböl partján."), [],
     [("loop", "loop", 105, 2500, ("Dubai loop", "Dubaj-kör"), ("The Burj Khalifa, Palm Jumeirah and the Burj Al Arab.", "A Burdzs Kalifa, a Palm Jumeirah és a Burdzs al-Arab."),
       ["OMDB", ["Burj Khalifa", 25.1972, 55.2744], ["Burj Al Arab", 25.1412, 55.1853], ["Palm Jumeirah", 25.1124, 55.1390], ["Dubai Marina", 25.0800, 55.1400], ["Palm Jebel Ali", 25.0020, 54.9790], "OMDB"])])
tour("hong-kong", HK, ("Hong Kong", "Hongkong"), ("Victoria Peak", "Victoria-csúcs", 22.2759, 114.1455), ["city", "coast", "mountain"],
     ("Skyscrapers against green peaks: Victoria Harbour, Victoria Peak and the Tian Tan Buddha on Lantau.", "Felhőkarcolók zöld csúcsok előtt: a Victoria-kikötő, a Victoria-csúcs és a Tian Tan Buddha Lantau szigetén."), [],
     [("loop", "loop", 110, 2500, ("Harbour loop", "Kikötő-kör"), ("The Tsing Ma Bridge, Victoria Harbour, Victoria Peak and the Tian Tan Buddha.", "A Tsing Ma híd, a Victoria-kikötő, a Victoria-csúcs és a Tian Tan Buddha."),
       ["VHHH", ["Tsing Ma Bridge", 22.3500, 114.0430], ["Victoria Harbour", 22.2900, 114.1700], ["Victoria Peak", 22.2759, 114.1455], ["Tian Tan Buddha", 22.2540, 113.9047], ["~", 22.2900, 113.8700], "VHHH"])])

CONT = {"new-york": "NA", "grand-canyon": "NA", "sf-bay": "NA", "oahu": "NA", "machu-picchu": "SA", "rio": "SA", "iguazu": "SA",
        "cape-town": "AF", "giza": "AF", "kilimanjaro": "AF", "sydney": "OC", "whitsundays": "OC", "milford-sound": "OC",
        "tokyo-fuji": "AS", "dubai": "AS", "hong-kong": "AS"}
for t in T:
    t["continent"] = CONT.get(t["id"], "EU")
NEW = [t["id"] for t in T]
save()
REV = set(open(os.path.join(os.path.dirname(P), "..", "tools", "reviewed.txt"), encoding="utf-8").read().split())
d = json.load(open(P, encoding="utf-8"))
for t in d["tours"]:
    if t["id"] in NEW and t["id"] not in REV:
        t["new"] = True
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(NEW), "uj tura")
open(os.path.join(os.path.dirname(P), "..", "tools", "r1_ids.txt"), "w").write(" ".join(NEW))
