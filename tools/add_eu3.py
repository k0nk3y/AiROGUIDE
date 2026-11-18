#!/usr/bin/env python3
"""Europa 3. csomag: Skandinavia, Benelux, Lengyelorszag, Balkan, Kelet-Europa, Malta, Ciprus, Irorszag (rovid + hosszabb korok).
Sorrend: add_eu1 -> add_eu2 -> add_var_eu -> add_eu3 -> tours_order -> tours_check"""
from tourlib import *

PL = ("Poland", "Lengyelország"); SE = ("Sweden", "Svédország"); DK = ("Denmark", "Dánia"); FI = ("Finland", "Finnország"); NO = ("Norway", "Norvégia")
SI = ("Slovenia", "Szlovénia"); MT = ("Malta", "Málta"); RO = ("Romania", "Románia"); ME = ("Montenegro", "Montenegró"); NL = ("Netherlands", "Hollandia")
BE = ("Belgium", "Belgium"); SK = ("Slovakia", "Szlovákia"); BG = ("Bulgaria", "Bulgária"); HR = ("Croatia", "Horvátország"); IE = ("Ireland", "Írország"); CY = ("Cyprus", "Ciprus")

tour("krakow-tatras", PL, ("Kraków and the Tatras", "Krakkó és a Tátra"), ("Wawel Castle", "Wawel", 50.0541, 19.9354), ["city", "culture", "mountain", "unesco"],
     ("Royal Kraków, the salt cathedral of Wieliczka and Poland's highest mountains, the Tatras above Zakopane.", "A királyi Krakkó, a wieliczkai sóbánya és Lengyelország legmagasabb hegyei, a Tátra Zakopane felett."),
     [["Wieliczka Salt Mine", 49.9833, 20.0550]],
     [("short", "loop", 100, 3000, ("Kraków short", "Krakkó rövid"), ("Short loop over the Wawel and the Wieliczka salt mine.", "Rövid kör a Wawel és a wieliczkai sóbánya felett."),
       ["EPKK", ["Wawel Castle", 50.0541, 19.9354], ["Wieliczka Salt Mine", 49.9833, 20.0550], ["Niepołomice Castle", 50.0350, 20.2200], "EPKK"]),
      ("tatras", "loop", 110, 10500, ("Kraków and the Tatras", "Krakkó és a Tátra"), ("About an hour: Wieliczka, Zakopane and Giewont, back over the Wawel.", "Kb. egy óra: Wieliczka, Zakopane és Giewont, vissza a Wawel felett."),
       ["EPKK", ["Wieliczka Salt Mine", 49.9833, 20.0550], ["Zakopane", 49.2992, 19.9496], ["Giewont", 49.2511, 19.9339], ["Wawel Castle", 50.0541, 19.9354], "EPKK"])])
tour("stockholm", SE, ("Stockholm archipelago", "Stockholmi szigetvilág"), ("Gamla Stan", "Gamla Stan", 59.3252, 18.0711), ["city", "culture", "island", "coast"],
     ("The royal capital on its islands: the Old Town, the Vasa Museum, Drottningholm and the skerries out to Sandhamn.", "A királyi főváros szigetein: az Óváros, a Vasa Múzeum, Drottningholm és a szigetvilág Sandhamnig."),
     [["Drottningholm Palace", 59.3215, 17.8860]],
     [("archipelago", "loop", 105, 2500, ("Out to the skerries", "A szigetvilágba"), ("The city and then the archipelago out to Sandhamn.", "A város, majd a szigetvilág Sandhamnig."),
       ["ESSA", ["Gamla Stan", 59.3252, 18.0711], ["Vasa Museum", 59.3280, 18.0914], ["Sandhamn", 59.2880, 18.9170], ["Vaxholm Fortress", 59.4020, 18.3550], "ESSA"])])
tour("copenhagen", DK, ("Copenhagen and Zealand", "Koppenhága és Zéland"), ("The Little Mermaid", "A kis hableány", 55.6929, 12.5993), ["city", "culture", "coast"],
     ("Copenhagen's harbour, Hamlet's Kronborg, the Øresund Bridge, Roskilde and the white chalk cliffs of Møn.", "Koppenhága kikötője, Hamlet Kronborg-ja, az Øresund-híd, Roskilde és Møn fehér krétasziklái."),
     [["Nyhavn", 55.6798, 12.5911]],
     [("short", "loop", 100, 2500, ("Copenhagen short", "Koppenhága rövid"), ("Short loop: the Øresund Bridge, the Little Mermaid and Kronborg.", "Rövid kör: Øresund-híd, A kis hableány és Kronborg."),
       ["EKCH", ["Øresund Bridge", 55.5700, 12.8300], ["The Little Mermaid", 55.6929, 12.5993], ["Kronborg Castle", 56.0390, 12.6210], "EKCH"]),
      ("zealand", "loop", 110, 2500, ("Zealand loop", "Zéland-kör"), ("About an hour: Roskilde Cathedral, Møns Klint, the Øresund Bridge and the Little Mermaid.", "Kb. egy óra: roskildei székesegyház, Møns Klint, Øresund-híd és A kis hableány."),
       ["EKCH", ["Roskilde Cathedral", 55.6430, 12.0804], ["Møns Klint", 54.9733, 12.5483], ["Øresund Bridge", 55.5700, 12.8300], ["The Little Mermaid", 55.6929, 12.5993], "EKCH"])])
tour("helsinki", FI, ("Helsinki and the Finnish coast", "Helsinki és a finn tengerpart"), ("Helsinki Cathedral", "Helsinki székesegyház", 60.1700, 24.9522), ["city", "culture", "coast", "island"],
     ("Helsinki's white cathedral, the sea fortress of Suomenlinna and the old wooden town of Porvoo.", "Helsinki fehér székesegyháza, a Suomenlinna tengeri erőd és Porvoo régi fa óvárosa."),
     [["Temppeliaukio Church", 60.1731, 24.9255]],
     [("loop", "loop", 100, 2500, ("Helsinki loop", "Helsinki-kör"), ("Helsinki Cathedral, Suomenlinna and Porvoo.", "Helsinki székesegyház, Suomenlinna és Porvoo."),
       ["EFHK", ["Helsinki Cathedral", 60.1700, 24.9522], ["Suomenlinna", 60.1451, 24.9880], ["Porvoo Old Town", 60.3933, 25.6650], "EFHK"])])
tour("lofoten", NO, ("Lofoten islands", "Lofoten-szigetek"), ("Reine", "Reine", 67.9330, 13.0890), ["mountain", "coast", "island"],
     ("Sharp peaks rising straight out of the Arctic sea: Reine, Hamnøy, Henningsvær and Svolvær.", "Az északi-sarki tengerből közvetlenül kiemelkedő, éles csúcsok: Reine, Hamnøy, Henningsvær és Svolvær."),
     [["Hamnøy", 67.9460, 13.1330]],
     [("short", "loop", 100, 4500, ("Reine and Å", "Reine és Å"), ("Short loop from Leknes down the island chain.", "Rövid kör Leknesből a szigetlánc déli végéig."),
       ["ENLK", ["Reine", 67.9330, 13.0890], ["Å", 67.8800, 12.9850], ["Hamnøy", 67.9460, 13.1330], "ENLK"]),
      ("full", "loop", 105, 4500, ("Lofoten loop", "Lofoten-kör"), ("About an hour: Reine, Å, Henningsvær and Svolvær.", "Kb. egy óra: Reine, Å, Henningsvær és Svolvær."),
       ["ENLK", ["Å", 67.8800, 12.9850], ["Reine", 67.9330, 13.0890], ["Henningsvær", 68.1500, 14.2000], ["Svolvær", 68.2340, 14.5680], "ENLK"])])
tour("slovenia", SI, ("Julian Alps and Lake Bled", "Júliai-Alpok és a Bled-tó"), ("Lake Bled", "Bled-tó", 46.3625, 14.0939), ["mountain", "culture", "coast"],
     ("Ljubljana's castle, the island church on Lake Bled and Triglav, the highest peak of the Julian Alps.", "A ljubljanai vár, a Bled-tó szigeti temploma és a Triglav, a Júliai-Alpok legmagasabb csúcsa."),
     [["Ljubljana Castle", 46.0489, 14.5086]],
     [("bled", "loop", 100, 5500, ("Ljubljana and Bled", "Ljubljana és Bled"), ("Short loop: Ljubljana Castle and Lake Bled.", "Rövid kör: ljubljanai vár és a Bled-tó."),
       ["LJLJ", ["Ljubljana Castle", 46.0489, 14.5086], ["Lake Bled", 46.3625, 14.0939], ["Kranj", 46.2389, 14.3556], "LJLJ"]),
      ("triglav", "loop", 110, 11000, ("Triglav loop", "Triglav-kör"), ("About an hour: Predjama Castle, Triglav and Lake Bled.", "Kb. egy óra: Predjama vár, Triglav és a Bled-tó."),
       ["LJLJ", ["Predjama Castle", 45.8157, 14.1265], ["Triglav", 46.3786, 13.8366], ["Lake Bled", 46.3625, 14.0939], "LJLJ"])])
tour("malta", MT, ("Malta and Gozo", "Málta és Gozo"), ("Valletta", "Valletta", 35.8997, 14.5147), ["city", "culture", "island", "unesco"],
     ("Valletta's bastions, silent Mdina, the Blue Lagoon of Comino and the temples of Gozo.", "Valletta bástyái, a csendes Mdina, Comino Kék-lagúnája és Gozo templomai."),
     [["Mdina", 35.8860, 14.4025]],
     [("gozo", "loop", 105, 2000, ("Malta and Gozo", "Málta és Gozo"), ("Valletta, Gozo's Ġgantija temples, the Dwejra coast and the Dingli cliffs.", "Valletta, Gozo Ġgantija templomai, a Dwejra part és a Dingli-szirtek."),
       ["LMML", ["Valletta", 35.8997, 14.5147], ["Ġgantija Temples", 36.0463, 14.2696], ["Dwejra", 36.0526, 14.1887], ["Dingli Cliffs", 35.8590, 14.3870], "LMML"])])
tour("transylvania", RO, ("Transylvania", "Erdély"), ("Bran Castle", "Törcsvári vár", 45.5150, 25.3672), ["mountain", "culture", "city"],
     ("Sibiu's old town, the Transfăgărășan high road at Bâlea Lake and the castles of Peleș and Bran.", "Nagyszeben óvárosa, a Transzfogarasi hegyi út a Bâlea-tónál, valamint a Peleș és Törcsvári vár."),
     [["Sibiu Council Tower", 45.7983, 24.1519]],
     [("balea", "loop", 120, 9500, ("Sibiu and Bâlea Lake", "Nagyszeben és a Bâlea-tó"), ("Short loop over Sibiu and the Transfăgărășan.", "Rövid kör Nagyszeben és a Transzfogarasi felett."),
       ["LRSB", ["Sibiu Council Tower", 45.7983, 24.1519], ["Bâlea Lake", 45.6020, 24.6170], ["Cisnădie", 45.7106, 24.1519], "LRSB"]),
      ("castles", "loop", 120, 9500, ("Carpathian castles", "Kárpáti várak"), ("Bâlea Lake, Peleș, Bran and Brașov's Black Church.", "Bâlea-tó, Peleș, Törcsvár és Brassó Fekete temploma."),
       ["LRSB", ["Bâlea Lake", 45.6020, 24.6170], ["Peleș Castle", 45.3599, 25.5429], ["Bran Castle", 45.5150, 25.3672], ["Black Church, Brașov", 45.6403, 25.5886], "LRSB"])])
tour("montenegro", ME, ("Bay of Kotor and Durmitor", "Kotori-öböl és Durmitor"), ("Bay of Kotor", "Kotori-öböl", 42.4247, 18.7712), ["coast", "mountain", "unesco"],
     ("Europe's southernmost fjord-like bay, the islet of Sveti Stefan, Lake Skadar and the Tara canyon below Durmitor.", "Európa legdélibb fjordszerű öble, a Sveti Stefan szigetfalu, a Shkodrai-tó és a Tara-kanyon a Durmitor alatt."),
     [["Sveti Stefan", 42.2554, 18.8912]],
     [("coast", "loop", 110, 5500, ("Kotor and the coast", "Kotor és a tengerpart"), ("Lake Skadar, Sveti Stefan and the Bay of Kotor.", "Shkodrai-tó, Sveti Stefan és a Kotori-öböl."),
       ["LYPG", ["Skadar Lake", 42.2000, 19.2800], ["Sveti Stefan", 42.2554, 18.8912], ["Bay of Kotor", 42.4247, 18.7712], "LYPG"]),
      ("durmitor", "loop", 115, 9500, ("Coast and Durmitor", "Tenger és Durmitor"), ("Kotor, Durmitor and the Tara canyon bridge.", "Kotor, Durmitor és a Tara-híd."),
       ["LYPG", ["Bay of Kotor", 42.4247, 18.7712], ["Durmitor (Bobotov Kuk)", 43.1280, 19.0300], ["Đurđevića Tara Bridge", 43.1425, 19.2944], "LYPG"])])
tour("netherlands", NL, ("Netherlands: tulips and canals", "Hollandia: tulipánok és csatornák"), ("Keukenhof", "Keukenhof", 52.2697, 4.5460), ["city", "culture", "coast"],
     ("Amsterdam's canal ring, the Keukenhof bulb fields, Kinderdijk's windmills and the Delta Works.", "Amszterdam csatornagyűrűje, a Keukenhof hagymamezői, a Kinderdijk szélmalmai és a Delta-művek."),
     [["Amsterdam Canal Ring", 52.3700, 4.8900]],
     [("short", "loop", 100, 2000, ("Amsterdam and Keukenhof", "Amszterdam és Keukenhof"), ("Short loop: the canal ring and the bulb fields.", "Rövid kör: a csatornagyűrű és a hagymamezők."),
       ["EHAM", ["Amsterdam Canal Ring", 52.3700, 4.8900], ["Keukenhof", 52.2697, 4.5460], ["Zandvoort Beach", 52.3720, 4.5300], "EHAM"]),
      ("delta", "loop", 110, 2000, ("Windmills and Delta Works", "Szélmalmok és Delta-művek"), ("About an hour: Keukenhof, Kinderdijk and the Oosterschelde barrier.", "Kb. egy óra: Keukenhof, Kinderdijk és az Oosterschelde-gát."),
       ["EHAM", ["Keukenhof", 52.2697, 4.5460], ["Kinderdijk", 51.8830, 4.6370], ["Oosterschelde Barrier", 51.6350, 3.7000], ["Amsterdam Canal Ring", 52.3700, 4.8900], "EHAM"])])
tour("belgium", BE, ("Flanders and Brussels", "Flandria és Brüsszel"), ("Brussels Grand-Place", "Brüsszel Grand-Place", 50.8467, 4.3525), ["city", "culture", "unesco"],
     ("The Atomium and Grand-Place, Ghent's castle, medieval Bruges and the battlefield memorials of Flanders.", "Az Atomium és a Grand-Place, Gent vára, a középkori Brugge és a flandriai csatamezők emlékművei."),
     [["Atomium", 50.8947, 4.3415]],
     [("brussels", "loop", 100, 2000, ("Brussels short", "Brüsszel rövid"), ("Short loop: Atomium, Grand-Place and the Waterloo battlefield.", "Rövid kör: Atomium, Grand-Place és a waterlooi csatatér."),
       ["EBBR", ["Atomium", 50.8947, 4.3415], ["Brussels Grand-Place", 50.8467, 4.3525], ["Lion's Mound, Waterloo", 50.6788, 4.4121], "EBBR"]),
      ("flanders", "loop", 110, 2000, ("Ghent, Bruges, Ypres", "Gent, Brugge, Ypres"), ("About an hour: Ghent, Bruges and Ypres.", "Kb. egy óra: Gent, Brugge és Ypres."),
       ["EBBR", ["Gravensteen, Ghent", 51.0571, 3.7210], ["Belfry of Bruges", 51.2085, 3.2250], ["Menin Gate, Ypres", 50.8515, 2.8780], ["Brussels Grand-Place", 50.8467, 4.3525], "EBBR"])])
tour("tatras-slovakia", SK, ("High Tatras and Spiš", "Magas-Tátra és Szepes"), ("Gerlach Peak", "Gerlachfalvi-csúcs", 49.1640, 20.1328), ["mountain", "culture", "unesco"],
     ("Slovakia's alpine peaks above Štrbské Pleso and the vast ruin of Spiš Castle.", "Szlovákia alpesi csúcsai a Csorbai-tó felett és a hatalmas szepesi vár romja."),
     [["Štrbské Pleso", 49.1190, 20.0600]],
     [("peaks", "loop", 110, 10500, ("Tatra peaks", "Tátra-csúcsok"), ("Short loop: Štrbské Pleso, Gerlach and Lomnický štít.", "Rövid kör: Csorbai-tó, Gerlach és Lomnici-csúcs."),
       ["LZTT", ["Štrbské Pleso", 49.1190, 20.0600], ["Gerlach Peak", 49.1640, 20.1328], ["Lomnický štít", 49.1950, 20.2130], ["Kežmarok Castle", 49.1383, 20.4281], "LZTT"]),
      ("spis", "loop", 110, 10500, ("Tatras and Spiš Castle", "Tátra és szepesi vár"), ("About an hour: the peaks and Spiš Castle.", "Kb. egy óra: a csúcsok és a szepesi vár."),
       ["LZTT", ["Štrbské Pleso", 49.1190, 20.0600], ["Gerlach Peak", 49.1640, 20.1328], ["Lomnický štít", 49.1950, 20.2130], ["Spiš Castle", 48.9999, 20.7681], "LZTT"])])
tour("bulgaria", BG, ("Sofia, Rila and Vitosha", "Szófia, Rila és Vitosa"), ("Rila Monastery", "Rilai kolostor", 42.1334, 23.3401), ["mountain", "culture", "unesco", "city"],
     ("The golden domes of Sofia, the lonely Boyana church, Vitosha and the Rila Monastery below Musala, the highest peak of the Balkans.", "Szófia aranykupolái, a Bojanai templom, a Vitosa és a Rilai kolostor a Balkán legmagasabb csúcsa, a Musala alatt."),
     [["Alexander Nevsky Cathedral", 42.6958, 23.3328]],
     [("sofia", "loop", 100, 6500, ("Sofia and Vitosha", "Szófia és Vitosa"), ("Short loop: Boyana Church, Cherni Vrah and Alexander Nevsky.", "Rövid kör: Bojanai templom, Cserni Vrah és az Alekszandr Nyevszkij-székesegyház."),
       ["LBSF", ["Boyana Church", 42.6445, 23.2686], ["Cherni Vrah", 42.5636, 23.2784], ["Alexander Nevsky Cathedral", 42.6958, 23.3328], ["Pancharevo Lake", 42.6000, 23.4167], "LBSF"]),
      ("rila", "loop", 110, 11500, ("Rila loop", "Rila-kör"), ("About an hour: Sofia, Rila Monastery and Musala.", "Kb. egy óra: Szófia, a Rilai kolostor és a Musala."),
       ["LBSF", ["Alexander Nevsky Cathedral", 42.6958, 23.3328], ["Rila Monastery", 42.1334, 23.3401], ["Musala", 42.1800, 23.5850], "LBSF"])])
tour("istria", HR, ("Istria", "Isztria"), ("Pula Arena", "Pulai amfiteátrum", 44.8733, 13.8500), ["culture", "coast", "city"],
     ("Pula's Roman arena, the Brijuni islands, Rovinj's old town and the hill town of Motovun.", "Pula római amfiteátruma, a Brioni-szigetek, Rovinj óvárosa és a hegyi város, Motovun."),
     [["Brijuni", 44.9150, 13.7650]],
     [("full", "loop", 105, 2500, ("Istria loop", "Isztria-kör"), ("About an hour: Rovinj, Motovun, Pula Arena and Brijuni.", "Kb. egy óra: Rovinj, Motovun, Pulai amfiteátrum és Brioni."),
       ["LDPL", ["Rovinj", 45.0811, 13.6387], ["Motovun", 45.3378, 13.8283], ["Pula Arena", 44.8733, 13.8500], ["Brijuni", 44.9150, 13.7650], "LDPL"])])
tour("ireland-west", IE, ("Cliffs of Moher and the Burren", "A Moher-szirtek és a Burren"), ("Cliffs of Moher", "Moher-szirtek", 52.9715, -9.4309), ["coast", "culture", "island"],
     ("Ireland's Atlantic cliffs, the Burren's stone plateau, the Aran Islands' Dún Aonghasa and Bunratty Castle.", "Írország atlanti szirtjei, a Burren köves fennsíkja, az Aran-szigetek Dún Aonghasa erődje és a Bunratty-kastély."),
     [["Bunratty Castle", 52.7011, -8.8115]],
     [("cliffs", "loop", 105, 2500, ("Cliffs of Moher", "Moher-szirtek"), ("Short loop from Shannon: Bunratty and the cliffs.", "Rövid kör Shannonból: Bunratty és a szirtek."),
       ["EINN", ["Bunratty Castle", 52.7011, -8.8115], ["Cliffs of Moher", 52.9715, -9.4309], ["Kilrush Marina", 52.6380, -9.4830], "EINN"]),
      ("aran", "loop", 110, 2500, ("Burren and Aran Islands", "Burren és Aran-szigetek"), ("About an hour: the cliffs, Dún Aonghasa and the Burren.", "Kb. egy óra: a szirtek, Dún Aonghasa és a Burren."),
       ["EINN", ["Cliffs of Moher", 52.9715, -9.4309], ["Dún Aonghasa", 53.1225, -9.7660], ["Poulnabrone Dolmen", 53.0488, -9.1396], ["Bunratty Castle", 52.7011, -8.8115], "EINN"])])
tour("cyprus", CY, ("Cyprus: island of Aphrodite", "Ciprus: Aphrodité szigete"), ("Petra tou Romiou", "Petra tou Romiou", 34.6630, 32.6270), ["culture", "coast", "mountain"],
     ("Aphrodite's rock, the Roman theatre of Kourion, the Troodos mountains and the wild Akamas peninsula.", "Aphrodité sziklája, a kuriói római színház, a Troodos-hegység és a vad Akamas-félsziget."),
     [["Tombs of the Kings, Paphos", 34.7783, 32.4070]],
     [("short", "loop", 100, 3000, ("Paphos coast", "Páfosz partja"), ("Short loop: Tombs of the Kings, Petra tou Romiou and Kourion.", "Rövid kör: Királysírok, Petra tou Romiou és Kourion."),
       ["LCPH", ["Tombs of the Kings, Paphos", 34.7783, 32.4070], ["Petra tou Romiou", 34.6630, 32.6270], ["Kourion", 34.6640, 32.8870], "LCPH"]),
      ("troodos", "loop", 110, 7000, ("Troodos and Akamas", "Troodos és Akamas"), ("About an hour: Kourion, Mount Olympus and the Akamas peninsula.", "Kb. egy óra: Kourion, az Olümposz-hegy és az Akamas-félsziget."),
       ["LCPH", ["Kourion", 34.6640, 32.8870], ["Mount Olympus (Troodos)", 34.9370, 32.8640], ["Blue Lagoon, Akamas", 35.0830, 32.3180], "LCPH"])])
save()
