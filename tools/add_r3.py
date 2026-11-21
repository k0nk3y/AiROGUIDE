#!/usr/bin/env python3
"""3. kor: 23 uj tura minden kontinensen. Sorrend: add_r3 -> tours_order <r3_ids> -> poi_registry -> tours_kw -> tours_img -> tours_check"""
from tourlib import *
import json, os
C = lambda e, h: (e, h)
BW = C("Botswana", "Botswana"); NA_ = C("Namibia", "Namíbia"); SC = C("Seychelles", "Seychelle-szigetek"); ZA = C("South Africa", "Dél-Afrika"); JO = C("Jordan", "Jordánia"); MV = C("Maldives", "Maldív-szigetek")
VN = C("Vietnam", "Vietnám"); JP = C("Japan", "Japán"); CN = C("China", "Kína"); TH = C("Thailand", "Thaiföld"); US = C("United States", "Egyesült Államok"); CA = C("Canada", "Kanada")
CL = C("Chile", "Chile"); AU = C("Australia", "Ausztrália"); FJ = C("Fiji", "Fidzsi"); PT = C("Portugal", "Portugália"); ES = C("Spain", "Spanyolország"); FR = C("France", "Franciaország")
CONT = {}

def add(cont, *a, **k):
    tour(*a, **k); CONT[a[0]] = cont

def Pt(n, la, lo): return [n, la, lo]

# ---------------- Afrika ----------------
add("AF", "okavango", BW, ("Okavango Delta", "Okavango-delta"), ("Okavango Delta", "Okavango-delta", -19.3000, 22.9000), ["jungle", "unesco"],
    ("The world's largest inland delta: a maze of lagoons, islands and channels full of elephants and hippos.", "A világ legnagyobb belső deltája: lagúnák, szigetek és csatornák útvesztője, tele elefántokkal és vízilovakkal."), [],
    [("short", "loop", 100, 3000, ("Delta short", "Delta rövid"), ("From Maun over Chief's Island and the Moremi Game Reserve.", "Maunból a Chief-sziget és a Moremi vadrezervátum felett."),
      ["FBMN", Pt("Chief's Island", -19.4000, 23.0500), Pt("Moremi Game Reserve", -19.2000, 23.4500), "FBMN"]),
     ("long", "loop", 105, 3500, ("Delta and Lake Ngami", "Delta és a Ngami-tó"), ("About two hours: Lake Ngami, the delta's islands, Moremi and the Khwai River.", "Kb. két óra: a Ngami-tó, a delta szigetei, Moremi és a Khwai-folyó."),
      ["FBMN", Pt("Lake Ngami", -20.5000, 22.7500), Pt("Chief's Island", -19.4000, 23.0500), Pt("Moremi Game Reserve", -19.2000, 23.4500), Pt("Khwai River", -19.1500, 23.7800), "FBMN"])])
add("AF", "sossusvlei", NA_, ("Sossusvlei and the Namib dunes", "Sossusvlei és a Namib dűnéi"), ("Sossusvlei", "Sossusvlei", -24.7275, 15.3405), ["culture", "unesco"],
    ("The tallest dunes on Earth: the red sea of sand around Sossusvlei and the dead trees of Deadvlei.", "A Föld legmagasabb dűnéi: a vörös homoktenger Sossusvlei körül és a Deadvlei kiszáradt fái."), [],
    [("short", "loop", 95, 3500, ("Dunes short", "Dűnék rövid"), ("From Sesriem: Dune 45, Sossusvlei and Deadvlei.", "Sesriemből: a Dune 45, Sossusvlei és Deadvlei."),
      ["FYSS", Pt("Dune 45", -24.7255, 15.4730), Pt("Sossusvlei", -24.7275, 15.3405), Pt("Deadvlei", -24.7597, 15.2942), "FYSS"]),
     ("long", "loop", 100, 4500, ("Namib-Naukluft loop", "Namib-Naukluft-kör"), ("About an hour: the dunes, the Tsauchab valley and the Naukluft Mountains.", "Kb. egy óra: a dűnék, a Tsauchab völgye és a Naukluft-hegység."),
      ["FYSS", Pt("Naukluft Mountains", -24.2500, 16.1500), Pt("Dune 45", -24.7255, 15.4730), Pt("Sossusvlei", -24.7275, 15.3405), Pt("Big Daddy Dune", -24.7410, 15.2850), "FYSS"])])
add("AF", "seychelles", SC, ("Seychelles", "Seychelle-szigetek"), ("Anse Source d'Argent", "Anse Source d'Argent", -4.3680, 55.8280), ["island", "coast", "unesco"],
    ("Granite boulders and powder-white beaches: Mahé, Praslin and La Digue in the Indian Ocean.", "Gránitsziklák és hófehér strandok: Mahé, Praslin és La Digue az Indiai-óceánon."), [],
    [("mahe", "loop", 90, 2500, ("Mahé loop", "Mahé-kör"), ("Mahé and its neighbours: Victoria, Morne Seychellois, Silhouette Island and Sainte Anne Marine Park.", "Mahé és szomszédai: Victoria, Morne Seychellois, a Silhouette-sziget és a Sainte Anne tengeri park."),
      ["FSIA", Pt("Victoria (Seychelles)", -4.6200, 55.4540), Pt("Beau Vallon", -4.6090, 55.4290), Pt("Morne Seychellois", -4.6570, 55.4410), Pt("Silhouette Island", -4.4850, 55.2430), Pt("Sainte Anne Marine Park", -4.6100, 55.5000), "FSIA"]),
     ("islands", "loop", 95, 2500, ("Praslin and La Digue", "Praslin és La Digue"), ("Over the Vallée de Mai, Curieuse Island and the beaches of Praslin and La Digue.", "A Vallée de Mai, a Curieuse-sziget, Praslin és La Digue strandjai felett."),
      ["FSIA", Pt("Vallée de Mai", -4.3290, 55.7400), Pt("Anse Lazio", -4.2900, 55.7150), Pt("Curieuse Island", -4.2870, 55.7260), Pt("Anse Source d'Argent", -4.3680, 55.8280), "FSIA"])])
add("AF", "garden-route", ZA, ("Garden Route", "Garden Route"), ("Knysna Heads", "Knysna Heads", -34.0810, 23.0670), ["coast"],
    ("South Africa's green coast: the lagoon of Knysna, Plettenberg Bay, the Bloukrans bridge and the Tsitsikamma forest.", "Dél-Afrika zöld partvidéke: Knysna lagúnája, Plettenberg Bay, a Bloukrans-híd és a Tsitsikamma-erdő."), [],
    [("short", "loop", 100, 2500, ("Knysna short", "Knysna rövid"), ("Short loop from George: Wilderness, Knysna Heads and Plettenberg Bay.", "Rövid kör Georgeból: Wilderness, Knysna Heads és Plettenberg Bay."),
      ["FAGG", Pt("Wilderness", -33.9930, 22.5750), Pt("Knysna Heads", -34.0810, 23.0670), Pt("Plettenberg Bay", -34.0527, 23.3716), "FAGG"]),
     ("coast", "loop", 105, 3000, ("Tsitsikamma coast", "Tsitsikamma-part"), ("About an hour and a half: Knysna, the Robberg peninsula, the Bloukrans bridge and Storms River Mouth.", "Kb. másfél óra: Knysna, a Robberg-félsziget, a Bloukrans-híd és a Storms River Mouth."),
      ["FAGG", Pt("Knysna Heads", -34.0810, 23.0670), Pt("Robberg Peninsula", -34.1100, 23.4000), Pt("Bloukrans Bridge", -33.9940, 23.6590), Pt("Storms River Mouth", -34.0210, 23.8880), "FAGG"])])

# ---------------- Azsia ----------------
add("AS", "petra-wadi-rum", JO, ("Petra and Wadi Rum", "Petra és Wadi Rum"), ("Petra", "Petra", 30.3285, 35.4444), ["culture", "unesco", "mountain"],
    ("The rose-red city of the Nabataeans and the red desert of Lawrence of Arabia, from the Red Sea at Aqaba.", "A nabateusok rózsaszín városa és Lawrence of Arabia vörös sivataga, az akabai Vörös-tenger partjáról."), [],
    [("rum", "loop", 100, 4500, ("Wadi Rum loop", "Wadi Rum-kör"), ("From Aqaba: the Red Sea coast and the sandstone towers of Wadi Rum.", "Akabából: a Vörös-tenger partja és Wadi Rum homokkőtornyai."),
      ["OJAQ", Pt("Aqaba Fort", 29.5210, 35.0050), Pt("Wadi Rum", 29.5750, 35.4200), Pt("Jebel Burdah", 29.6000, 35.4900), "OJAQ"]),
     ("petra", "loop", 105, 6500, ("Petra and Wadi Rum", "Petra és Wadi Rum"), ("About an hour and a quarter: Wadi Rum, Petra and Little Petra, back along Wadi Araba.", "Kb. 75 perc: Wadi Rum, Petra és Kis-Petra, vissza a Wadi Araba mentén."),
      ["OJAQ", Pt("Wadi Rum", 29.5750, 35.4200), Pt("Petra", 30.3285, 35.4444), Pt("Little Petra", 30.4200, 35.4700), Pt("Aqaba Fort", 29.5210, 35.0050), "OJAQ"])])
add("AS", "maldives", MV, ("Maldives atolls", "Maldív-szigetek atolljai"), ("Ari Atoll", "Ari-atoll", 3.8500, 72.8500), ["island", "coast"],
    ("Coral rings in the Indian Ocean: the capital Malé, the reefs of the atolls and turquoise lagoons.", "Korallgyűrűk az Indiai-óceánon: a főváros Malé, az atollok zátonyai és a türkiz lagúnák."), [],
    [("male", "loop", 100, 2000, ("Malé atoll", "Malé-atoll"), ("Short loop: Malé, Banana Reef and Maafushi.", "Rövid kör: Malé, Banana Reef és Maafushi."),
      ["VRMM", Pt("Malé", 4.1755, 73.5093), Pt("Maafushi", 3.9420, 73.4900), Pt("Banana Reef", 4.2610, 73.5410), "VRMM"]),
     ("ari", "loop", 105, 2000, ("Ari Atoll", "Ari-atoll"), ("About an hour: Rasdhoo and Ari Atoll, then back over Maafushi and Malé.", "Kb. egy óra: Rasdhoo és az Ari-atoll, majd vissza Maafushi és Malé felett."),
      ["VRMM", Pt("Rasdhoo Atoll", 4.2640, 72.9930), Pt("Ari Atoll", 3.8500, 72.8500), Pt("Maafushi", 3.9420, 73.4900), Pt("Malé", 4.1755, 73.5093), "VRMM"])])
add("AS", "halong", VN, ("Hanoi and Ha Long Bay", "Hanoi és a Ha Long-öböl"), ("Ha Long Bay", "Ha Long-öböl", 20.9100, 107.1830), ["coast", "culture", "unesco"],
    ("Thousands of limestone islands rising from the emerald sea, and the countryside around Hanoi.", "Több ezer mészkősziget az smaragdzöld tengerből, és Hanoi vidéke."), [],
    [("ninh", "loop", 100, 3000, ("Hanoi and Ninh Binh", "Hanoi és Ninh Binh"), ("The old centre of Hanoi, the karst and rice fields of Tam Coc and Tam Dao.", "Hanoi belvárosa, Tam Coc karsztjai és rizsföldjei, valamint Tam Dao."),
      ["VVNB", Pt("Hoan Kiem Lake", 21.0287, 105.8523), Pt("Tam Coc", 20.2150, 105.9390), Pt("Tam Dao", 21.4540, 105.6490), "VVNB"]),
     ("bay", "loop", 105, 3000, ("Ha Long Bay", "Ha Long-öböl"), ("Almost two hours: Ha Long Bay, Bai Tu Long Bay and Cat Ba Island.", "Közel két óra: a Ha Long-öböl, a Bai Tu Long-öböl és a Cat Ba-sziget."),
      ["VVNB", Pt("Bai Chay Bridge", 20.9590, 107.0650), Pt("Ha Long Bay", 20.9100, 107.1830), Pt("Bai Tu Long Bay", 21.0500, 107.4500), Pt("Cat Ba Island", 20.7970, 107.0000), "VVNB"])])
add("AS", "kyoto-osaka", JP, ("Kyoto, Osaka and Nara", "Kiotó, Oszaka és Nara"), ("Fushimi Inari Shrine", "Fushimi Inari szentély", 34.9671, 135.7727), ["culture", "city", "unesco"],
    ("Japan's ancient heart: thousands of red torii in Kyoto, Osaka Castle and the great Buddha of Nara.", "Japán ősi szíve: ezernyi vörös torii Kiotóban, az oszakai kastély és a nárai nagy Buddha."), [],
    [("osaka", "loop", 100, 3000, ("Osaka and Nara", "Oszaka és Nara"), ("From Kansai: the Akashi Kaikyō Bridge, Osaka Castle and Tōdai-ji in Nara.", "Kansaiból: az Akasi-Kaikjó híd, az oszakai kastély és a nárai Tódaidzsi."),
      ["RJBB", Pt("Akashi Kaikyō Bridge", 34.6170, 135.0220), Pt("Osaka Castle", 34.6873, 135.5262), Pt("Tōdai-ji", 34.6890, 135.8398), "RJBB"]),
     ("kyoto", "loop", 105, 3500, ("Kyoto circuit", "Kiotói kör"), ("About an hour: Osaka Castle, the golden Kinkaku-ji, Fushimi Inari and Nara.", "Kb. egy óra: az oszakai kastély, az aranyozott Kinkakudzsi, Fushimi Inari és Nara."),
      ["RJBB", Pt("Osaka Castle", 34.6873, 135.5262), Pt("Kinkaku-ji", 35.0394, 135.7292), Pt("Fushimi Inari Shrine", 34.9671, 135.7727), Pt("Tōdai-ji", 34.6890, 135.8398), "RJBB"])])
add("AS", "beijing", CN, ("Beijing and the Great Wall", "Peking és a Nagy Fal"), ("Forbidden City", "Tiltott Város", 39.9163, 116.3972), ["culture", "city", "unesco"],
    ("The imperial capital and its wall: the Forbidden City, the Summer Palace and the Great Wall in the mountains.", "A császári főváros és fala: a Tiltott Város, a Nyári Palota és a hegyekben kígyózó Nagy Fal."), [Pt("Temple of Heaven", 39.8822, 116.4066), Pt("Bird's Nest", 39.9928, 116.3965)],
    [("short", "loop", 100, 3500, ("Beijing short", "Peking rövid"), ("Short loop: the Great Wall at Mutianyu, the Bird's Nest and the Forbidden City.", "Rövid kör: a Nagy Fal Mutianyunál, a Madárfészek és a Tiltott Város."),
      ["ZBAA", Pt("Mutianyu Great Wall", 40.4319, 116.5704), Pt("Bird's Nest", 39.9928, 116.3965), Pt("Forbidden City", 39.9163, 116.3972), "ZBAA"]),
     ("long", "loop", 105, 4500, ("Palaces and the wall", "Paloták és a fal"), ("About an hour: Badaling, the Ming Tombs, the Summer Palace, the Forbidden City and the Temple of Heaven.", "Kb. egy óra: Badaling, a Ming-sírok, a Nyári Palota, a Tiltott Város és az Éghez Szentelt Templom."),
      ["ZBAA", Pt("Ming Tombs", 40.2540, 116.2340), Pt("Badaling Great Wall", 40.3540, 116.0160), Pt("Summer Palace", 39.9999, 116.2755), Pt("Forbidden City", 39.9163, 116.3972), "ZBAA"])])
add("AS", "phuket", TH, ("Phuket and Phang Nga Bay", "Phuket és a Phang Nga-öböl"), ("Phi Phi Islands", "Phi Phi-szigetek", 7.7407, 98.7784), ["island", "coast"],
    ("Limestone islets in the Andaman Sea: Phang Nga Bay, the Phi Phi Islands and Railay's cliffs.", "Mészkősziklák az Andamán-tengerben: a Phang Nga-öböl, a Phi Phi-szigetek és Railay sziklái."), [],
    [("south", "loop", 95, 2500, ("Phuket south", "Phuket déli rész"), ("Short loop: Patong Beach, Promthep Cape and the Big Buddha.", "Rövid kör: Patong Beach, Promthep-fok és a Nagy Buddha."),
      ["VTSP", Pt("Patong Beach", 7.8960, 98.2960), Pt("Promthep Cape", 7.7627, 98.3050), Pt("Big Buddha (Phuket)", 7.8277, 98.3126), "VTSP"]),
     ("bays", "loop", 105, 3500, ("Andaman bays", "Andamán-öblök"), ("About an hour: Phang Nga Bay, Railay, the Phi Phi Islands and Promthep Cape.", "Kb. egy óra: a Phang Nga-öböl, Railay, a Phi Phi-szigetek és a Promthep-fok."),
      ["VTSP", Pt("Phang Nga Bay", 8.2900, 98.5300), Pt("Railay Beach", 8.0110, 98.8370), Pt("Phi Phi Islands", 7.7407, 98.7784), Pt("Promthep Cape", 7.7627, 98.3050), "VTSP"])])

# ---------------- Eszak-Amerika ----------------
add("NA", "denali", US, ("Denali", "Denali"), ("Denali", "Denali", 63.0692, -151.0070), ["mountain", "unesco"],
    ("North America's highest peak: Denali, Mount Foraker and the glaciers of the Alaska Range from Talkeetna.", "Észak-Amerika legmagasabb csúcsa: a Denali, a Mount Foraker és az Alaszkai-hegység gleccserei Talkeetnából."), [],
    [("short", "loop", 105, 13000, ("Denali short", "Denali rövid"), ("From Talkeetna over the Ruth Glacier and around Denali.", "Talkeetnából a Ruth-gleccser felett a Denali körül."),
      ["PATK", Pt("Ruth Glacier", 62.9450, -150.6000), Pt("Denali", 63.0692, -151.0070), Pt("Kahiltna Glacier", 62.8800, -151.1800), "PATK"]),
     ("foraker", "loop", 110, 13500, ("Foraker and Denali", "Foraker és Denali"), ("About an hour: Mount Foraker, Denali and the Ruth Glacier.", "Kb. egy óra: a Mount Foraker, a Denali és a Ruth-gleccser."),
      ["PATK", Pt("Mount Foraker", 62.9600, -151.3990), Pt("Denali", 63.0692, -151.0070), Pt("Ruth Glacier", 62.9450, -150.6000), Pt("Kahiltna Glacier", 62.8800, -151.1800), "PATK"])])
add("NA", "monument-valley", US, ("Monument Valley and Lake Powell", "Monument Valley és a Powell-tó"), ("Monument Valley", "Monument Valley", 36.9980, -110.0985), ["culture", "mountain"],
    ("Red buttes in the Arizona desert: Horseshoe Bend, Antelope Canyon, Rainbow Bridge and Monument Valley.", "Vörös tanúhegyek az arizonai sivatagban: Horseshoe Bend, Antelope-kanyon, Rainbow Bridge és Monument Valley."), [],
    [("short", "loop", 100, 6500, ("Page short", "Page rövid"), ("Loop from Page: Antelope Canyon, Horseshoe Bend, the Glen Canyon Dam and Lone Rock.", "Kör Page-ből: az Antelope-kanyon, Horseshoe Bend, a Glen Canyon-gát és a Lone Rock."),
      ["KPGA", Pt("Antelope Canyon", 36.8619, -111.3743), Pt("Horseshoe Bend", 36.8791, -111.5103), Pt("Glen Canyon Dam", 36.9370, -111.4840), Pt("Lone Rock Beach", 37.0300, -111.4900), "KPGA"]),
     ("long", "loop", 110, 8500, ("Monument Valley loop", "Monument Valley-kör"), ("About an hour and a half: Horseshoe Bend, Rainbow Bridge, Monument Valley and Antelope Canyon.", "Kb. másfél óra: Horseshoe Bend, Rainbow Bridge, Monument Valley és az Antelope-kanyon."),
      ["KPGA", Pt("Horseshoe Bend", 36.8791, -111.5103), Pt("Rainbow Bridge", 37.0778, -110.9640), Pt("Monument Valley", 36.9980, -110.0985), Pt("Antelope Canyon", 36.8619, -111.3743), "KPGA"])])
add("NA", "toronto-niagara", CA, ("Toronto and Niagara Falls", "Toronto és a Niagara-vízesés"), ("Niagara Falls", "Niagara-vízesés", 43.0896, -79.0849), ["city", "coast"],
    ("A skyline on Lake Ontario and the thundering falls: Toronto, the Scarborough Bluffs and Niagara.", "Látkép az Ontario-tavon és a mennydörgő vízesés: Toronto, a Scarborough Bluffs és a Niagara."), [],
    [("city", "loop", 95, 2500, ("Toronto loop", "Toronto-kör"), ("Loop over the skyline: the CN Tower, Casa Loma, the Scarborough Bluffs and Mississauga.", "Kör a látkép felett: a CN Tower, a Casa Loma, a Scarborough Bluffs és Mississauga."),
      ["CYTZ", Pt("CN Tower", 43.6426, -79.3871), Pt("Casa Loma", 43.6780, -79.4094), Pt("Scarborough Bluffs", 43.7050, -79.2300), Pt("Mississauga Skyline", 43.5930, -79.6430), "CYTZ"]),
     ("niagara", "loop", 105, 3500, ("Niagara loop", "Niagara-kör"), ("About an hour: Toronto's skyline, Hamilton and Niagara Falls over Lake Ontario.", "Kb. egy óra: Toronto látképe, Hamilton és a Niagara-vízesés az Ontario-tó felett."),
      ["CYTZ", Pt("CN Tower", 43.6426, -79.3871), Pt("Hamilton Skyway", 43.2790, -79.8000), Pt("Niagara Falls", 43.0896, -79.0849), Pt("Scarborough Bluffs", 43.7050, -79.2300), "CYTZ"])])
add("NA", "big-island", US, ("Hawaii Big Island", "Hawaii Nagy-sziget"), ("Kīlauea", "Kīlauea", 19.4069, -155.2834), ["island", "volcano", "mountain"],
    ("Fire and ice on one island: the lava of Kīlauea, the snowy summit of Mauna Kea and the black sand of the south.", "Tűz és jég egy szigeten: a Kīlauea lávája, a Mauna Kea havas csúcsa és a déli fekete homok."), [],
    [("volcano", "loop", 100, 9000, ("Volcano loop", "Vulkán-kör"), ("From Hilo: Akaka Falls, Mauna Kea, Mauna Loa and Kīlauea.", "Hilóból: Akaka-vízesés, Mauna Kea, Mauna Loa és Kīlauea."),
      ["PHTO", Pt("Akaka Falls", 19.8540, -155.1520), Pt("Mauna Kea", 19.8207, -155.4681), Pt("Mauna Loa", 19.4750, -155.6080), Pt("Kīlauea", 19.4069, -155.2834), "PHTO"]),
     ("grand", "loop", 110, 8000, ("Around the island", "Körbe a szigeten"), ("About two hours: the Waipiʻo and Pololu valleys, Mauna Kea, South Point, Punaluʻu and Kīlauea.", "Kb. két óra: a Waipiʻo- és Pololu-völgy, a Mauna Kea, a South Point, Punaluʻu és a Kīlauea."),
      ["PHTO", Pt("Waipiʻo Valley", 20.1100, -155.5900), Pt("Pololu Valley", 20.2070, -155.7300), Pt("Mauna Kea", 19.8207, -155.4681), Pt("South Point", 18.9110, -155.6810), Pt("Punaluʻu Black Sand Beach", 19.1360, -155.5050), Pt("Kīlauea", 19.4069, -155.2834), "PHTO"])])
add("NA", "florida-keys", US, ("Florida Keys", "Florida Keys"), ("Seven Mile Bridge", "Seven Mile Bridge", 24.7050, -81.1500), ["coast", "island"],
    ("A chain of islands strung on a road over the sea: Key Biscayne, Key Largo, the Seven Mile Bridge and Key West.", "Szigetlánc egy tenger feletti úton: Key Biscayne, Key Largo, a Seven Mile Bridge és Key West."), [],
    [("run", "ab", 110, 1500, ("Miami to Key West", "Miamitól Key Westig"), ("A one-way run along the Keys, from Miami over Key Largo and the Seven Mile Bridge to Key West.", "Egyirányú repülés a Keys mentén Miamitól Key Largón és a Seven Mile Bridge-en át Key Westig."),
      ["KMIA", Pt("Key Biscayne Lighthouse", 25.6667, -80.1560), Pt("Key Largo", 25.0864, -80.4473), Pt("Seven Mile Bridge", 24.7050, -81.1500), "KEYW"]),
     ("tortugas", "loop", 110, 1500, ("Dry Tortugas", "Dry Tortugas"), ("From Key West over Old Town to Fort Jefferson on the Dry Tortugas.", "Key Westből az Old Town felett a Dry Tortugas-i Fort Jeffersonhoz."),
      ["KEYW", Pt("Key West Old Town", 24.5510, -81.8010), Pt("Fort Jefferson", 24.6280, -82.8730), Pt("Marquesas Keys", 24.5500, -82.1300), "KEYW"])])

# ---------------- Del-Amerika ----------------
add("SA", "easter-island", CL, ("Easter Island", "Húsvét-sziget"), ("Ahu Tongariki", "Ahu Tongariki", -27.1257, -109.2770), ["island", "culture", "unesco"],
    ("The most remote inhabited island: the moai statues of Rapa Nui, the crater of Rano Kau and Anakena beach.", "A legtávolabbi lakott sziget: Rapa Nui moai-szobrai, a Rano Kau krátere és az Anakena strand."), [],
    [("loop", "loop", 90, 2500, ("Rapa Nui loop", "Rapa Nui-kör"), ("Around the island: Rano Kau, Rano Raraku, Ahu Tongariki and Anakena.", "A sziget körül: Rano Kau, Rano Raraku, Ahu Tongariki és Anakena."),
      ["SCIP", Pt("Rano Kau", -27.1900, -109.4410), Pt("Rano Raraku", -27.1240, -109.2890), Pt("Ahu Tongariki", -27.1257, -109.2770), Pt("Anakena Beach", -27.0730, -109.3230), "SCIP"])])
add("SA", "atacama", CL, ("Atacama Desert", "Atacama-sivatag"), ("Valle de la Luna", "Holdvölgy", -22.9230, -68.2750), ["mountain", "volcano"],
    ("The driest desert on Earth: salt flats, steaming geysers and the cone of Licancabur.", "A Föld legszárazabb sivataga: sósíkságok, gőzölgő gejzírek és a Licancabur kúpja."), [],
    [("short", "loop", 105, 12500, ("Geysers and copper", "Gejzírek és réz"), ("From Calama: the Chuquicamata mine, the El Tatio geysers and Licancabur.", "Calamából: a Chuquicamata bánya, az El Tatio gejzírek és a Licancabur."),
      ["SCCF", Pt("Chuquicamata", -22.2970, -68.9010), Pt("El Tatio Geysers", -22.3300, -68.0100), Pt("Licancabur", -22.8350, -67.8830), "SCCF"]),
     ("long", "loop", 110, 13500, ("Salt flats and lagoons", "Sólapok és lagúnák"), ("About two hours: the Valley of the Moon, the Salar de Atacama and Laguna Miscanti.", "Kb. két óra: a Holdvölgy, a Salar de Atacama és a Miscanti-lagúna."),
      ["SCCF", Pt("Valle de la Luna", -22.9230, -68.2750), Pt("Salar de Atacama", -23.5000, -68.3000), Pt("Laguna Miscanti", -23.7400, -67.7700), Pt("Licancabur", -22.8350, -67.8830), "SCCF"])])

# ---------------- Oceania ----------------
add("OC", "tasmania", AU, ("Tasmania", "Tasmánia"), ("Wineglass Bay", "Wineglass Bay", -42.1590, 148.3010), ["coast", "mountain", "unesco"],
    ("Wild island at the bottom of Australia: Wineglass Bay, the cliffs of Port Arthur and kunanyi/Mount Wellington.", "Vad sziget Ausztrália alján: a Wineglass Bay, Port Arthur sziklái és a kunanyi/Wellington-hegy."), [],
    [("short", "loop", 100, 3500, ("Hobart short", "Hobart rövid"), ("Short loop from Hobart: Mount Wellington, Bruny Island and Port Arthur.", "Rövid kör Hobartból: a Wellington-hegy, a Bruny-sziget és Port Arthur."),
      ["YMHB", Pt("Mount Wellington", -42.8960, 147.2360), Pt("Bruny Island", -43.3500, 147.3000), Pt("Port Arthur", -43.1470, 147.8500), "YMHB"]),
     ("east", "loop", 110, 4500, ("East coast loop", "Keleti part"), ("About an hour and a half: Port Arthur, Wineglass Bay in Freycinet and Mount Wellington.", "Kb. másfél óra: Port Arthur, a freycineti Wineglass Bay és a Wellington-hegy."),
      ["YMHB", Pt("Port Arthur", -43.1470, 147.8500), Pt("Wineglass Bay", -42.1590, 148.3010), Pt("Mount Wellington", -42.8960, 147.2360), "YMHB"])])
add("OC", "cairns", AU, ("Cairns and the Great Barrier Reef", "Cairns és a Nagy-korallzátony"), ("Great Barrier Reef", "Nagy-korallzátony", -16.6070, 145.9760), ["coast", "jungle", "unesco"],
    ("Where the rainforest meets the reef: Green Island, Michaelmas Cay and the Daintree.", "Ahol az esőerdő találkozik a zátonnyal: a Green Island, a Michaelmas Cay és a Daintree."), [],
    [("reef", "loop", 100, 2500, ("Reef short", "Zátony rövid"), ("Short loop: Green Island, Michaelmas Cay and Kuranda.", "Rövid kör: a Green Island, a Michaelmas Cay és Kuranda."),
      ["YBCS", Pt("Green Island", -16.7580, 145.9740), Pt("Michaelmas Cay", -16.6070, 145.9760), Pt("Kuranda", -16.8190, 145.6370), "YBCS"]),
     ("daintree", "loop", 105, 3000, ("Daintree and Low Isles", "Daintree és Low Isles"), ("About an hour and a half: Low Isles, Cape Tribulation, the Daintree and the Atherton Tablelands.", "Kb. másfél óra: Low Isles, Cape Tribulation, a Daintree és az Atherton-fennsík."),
      ["YBCS", Pt("Low Isles", -16.3870, 145.5600), Pt("Cape Tribulation", -16.0780, 145.4640), Pt("Daintree Rainforest", -16.2500, 145.4170), Pt("Lake Eacham", -17.2830, 145.6330), "YBCS"])])
add("OC", "fiji", FJ, ("Fiji islands", "Fidzsi-szigetek"), ("Mamanuca Islands", "Mamanuca-szigetek", -17.6500, 177.1500), ["island", "coast"],
    ("Coral islands off Nadi: the Mamanucas, the Yasawas and the reef passes of Cloudbreak.", "Korallszigetek Nadi előtt: a Mamanuca- és Yasawa-szigetek és a Cloudbreak zátonya."), [],
    [("short", "loop", 95, 2000, ("Mamanuca loop", "Mamanuca-kör"), ("Short loop: Monuriki, the Mamanucas and Cloudbreak.", "Rövid kör: Monuriki, a Mamanucák és a Cloudbreak."),
      ["NFFN", Pt("Monuriki", -17.7000, 177.0300), Pt("Mamanuca Islands", -17.6500, 177.1500), Pt("Cloudbreak", -17.8780, 177.1900), "NFFN"]),
     ("yasawa", "loop", 100, 2000, ("Yasawa loop", "Yasawa-kör"), ("About an hour: the Mamanucas, the Yasawa chain and the Blue Lagoon.", "Kb. egy óra: a Mamanucák, a Yasawa-lánc és a Kék-lagúna."),
      ["NFFN", Pt("Mamanuca Islands", -17.6500, 177.1500), Pt("Yasawa Islands", -16.9000, 177.3500), Pt("Blue Lagoon (Yasawa)", -16.9500, 177.3000), "NFFN"])])

# ---------------- Europa ----------------
add("EU", "madeira", PT, ("Madeira", "Madeira"), ("Cabo Girão", "Cabo Girão", 32.6540, -17.0000), ["island", "coast", "mountain", "unesco"],
    ("The floating garden of the Atlantic: Funchal, the cliffs of Cabo Girão, Pico Ruivo and the lava pools of Porto Moniz.", "Az Atlanti-óceán lebegő kertje: Funchal, a Cabo Girão sziklái, a Pico Ruivo és Porto Moniz lávamedencéi."), [],
    [("short", "loop", 95, 3500, ("Madeira short", "Madeira rövid"), ("Short loop: Funchal, Cabo Girão, Pico Ruivo and São Lourenço.", "Rövid kör: Funchal, Cabo Girão, a Pico Ruivo és São Lourenço."),
      ["LPMA", Pt("Funchal", 32.6500, -16.9080), Pt("Cabo Girão", 32.6540, -17.0000), Pt("Pico Ruivo", 32.7590, -16.9420), Pt("Ponta de São Lourenço", 32.7440, -16.6930), "LPMA"]),
     ("grand", "loop", 105, 4000, ("Island loop", "Szigetkör"), ("About an hour: São Lourenço, Porto Santo, Pico Ruivo, Porto Moniz and Cabo Girão.", "Kb. egy óra: São Lourenço, Porto Santo, a Pico Ruivo, Porto Moniz és Cabo Girão."),
      ["LPMA", Pt("Ponta de São Lourenço", 32.7440, -16.6930), Pt("Porto Santo", 33.0700, -16.3400), Pt("Pico Ruivo", 32.7590, -16.9420), Pt("Porto Moniz", 32.8680, -17.1700), Pt("Cabo Girão", 32.6540, -17.0000), "LPMA"])])
add("EU", "tenerife", ES, ("Tenerife and La Gomera", "Tenerife és La Gomera"), ("Teide", "Teide", 28.2724, -16.6425), ["island", "volcano", "mountain", "unesco"],
    ("Spain's highest volcano rising from the Atlantic: Teide, the cliffs of Los Gigantes and the laurel forest of La Gomera.", "Spanyolország legmagasabb vulkánja az Atlanti-óceánból: a Teide, Los Gigantes sziklái és La Gomera babérerdeje."), [],
    [("short", "loop", 95, 9000, ("Teide short", "Teide rövid"), ("Short loop: Los Gigantes, Masca, Teide and Playa de las Américas.", "Rövid kör: Los Gigantes, Masca, a Teide és Playa de las Américas."),
      ["GCTS", Pt("Los Gigantes Cliffs", 28.2440, -16.8400), Pt("Masca Gorge", 28.3070, -16.8400), Pt("Teide", 28.2724, -16.6425), Pt("Playa de las Américas", 28.0620, -16.7290), "GCTS"]),
     ("grand", "loop", 105, 8000, ("Tenerife and La Gomera", "Tenerife és La Gomera"), ("About an hour and a half: La Gomera, Los Gigantes, Teide, the Anaga Mountains and Santa Cruz.", "Kb. másfél óra: La Gomera, Los Gigantes, a Teide, az Anaga-hegység és Santa Cruz."),
      ["GCTS", Pt("Garajonay", 28.1190, -17.2370), Pt("Los Gigantes Cliffs", 28.2440, -16.8400), Pt("Teide", 28.2724, -16.6425), Pt("Anaga Mountains", 28.5640, -16.2500), Pt("Santa Cruz de Tenerife", 28.4690, -16.2540), "GCTS"])])
add("EU", "paris", FR, ("Paris", "Párizs"), ("Eiffel Tower", "Eiffel-torony", 48.8584, 2.2945), ["city", "culture", "unesco"],
    ("The City of Light from above: the Eiffel Tower, Notre-Dame, the Louvre, Sacré-Cœur and Versailles.", "A fények városa fentről: az Eiffel-torony, a Notre-Dame, a Louvre, a Sacré-Cœur és Versailles."), [Pt("Arc de Triomphe", 48.8738, 2.2950), Pt("Stade de France", 48.9245, 2.3601)],
    [("city", "loop", 95, 2500, ("Paris landmarks", "Párizs nevezetességei"), ("Loop from Le Bourget: Sacré-Cœur, La Défense, the Eiffel Tower, Notre-Dame and Vincennes.", "Kör Le Bourget-ból: Sacré-Cœur, La Défense, az Eiffel-torony, a Notre-Dame és Vincennes."),
      ["LFPB", Pt("Sacré-Cœur", 48.8867, 2.3431), Pt("La Défense", 48.8920, 2.2360), Pt("Eiffel Tower", 48.8584, 2.2945), Pt("Notre-Dame de Paris", 48.8530, 2.3499), Pt("Château de Vincennes", 48.8427, 2.4354), "LFPB"]),
     ("versailles", "loop", 105, 3000, ("Paris and Versailles", "Párizs és Versailles"), ("About 40 minutes: the Louvre, the Eiffel Tower, the palace of Versailles and Disneyland Paris.", "Kb. 40 perc: a Louvre, az Eiffel-torony, a versailles-i kastély és a Disneyland Paris."),
      ["LFPB", Pt("Louvre", 48.8606, 2.3376), Pt("Eiffel Tower", 48.8584, 2.2945), Pt("Versailles", 48.8049, 2.1204), Pt("La Défense", 48.8920, 2.2360), Pt("Disneyland Paris", 48.8722, 2.7758), "LFPB"])])

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
open(os.path.join(os.path.dirname(P), "..", "tools", "r3_ids.txt"), "w").write(" ".join(NEW))
print(len(NEW), "uj tura")
