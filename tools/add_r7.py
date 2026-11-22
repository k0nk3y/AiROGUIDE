#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""7. kor: Afrika, Oceania, Del-Amerika, Azsia, Eszak-Amerika surusites + STOL. Sorrend: add_r7 -> tours_order <r7_ids> -> poi_registry -> tours_kw -> tours_img -> tours_check"""
from tourlib import *
import json, os
C = lambda e, h: (e, h)
KE = C("Kenya", "Kenya"); RW = C("Rwanda", "Ruanda"); TN = C("Tunisia", "Tunézia"); MG = C("Madagascar", "Madagaszkár"); ZA = C("South Africa", "Dél-Afrika"); EG = C("Egypt", "Egyiptom")
AU = C("Australia", "Ausztrália"); NZ = C("New Zealand", "Új-Zéland"); PW = C("Palau", "Palau"); CO = C("Colombia", "Kolumbia"); PE = C("Peru", "Peru"); BO = C("Bolivia", "Bolívia"); CL = C("Chile", "Chile")
IN = C("India", "India"); NP = C("Nepal", "Nepál"); JP = C("Japan", "Japán"); VN = C("Vietnam", "Vietnám"); GE = C("Georgia", "Grúzia")
PR = C("Puerto Rico", "Puerto Rico"); MX = C("Mexico", "Mexikó"); BZ = C("Belize", "Belize"); CR = C("Costa Rica", "Costa Rica"); US = C("United States", "Egyesült Államok")
PG = C("Papua New Guinea", "Pápua Új-Guinea"); UK = C("United Kingdom", "Egyesült Királyság"); CH = C("Switzerland", "Svájc"); ES = C("Spain", "Spanyolország")
CONT = {}


def add(cont, *a):
    a = list(a)
    a.insert(6, [])
    tour(*a); CONT[a[0]] = cont


def Pt(n, la, lo): return [n, la, lo]


# ---------------- Afrika
add("AF", "nairobi-rift", KE, ("Nairobi and the Great Rift Valley", "Nairobi és a Nagy-hasadékvölgy"), ("Lake Naivasha", "Naivasha-tó", -0.7667, 36.3500), ["mountain", "city"],
    ("Giraffes against a skyline in Nairobi National Park, then the Ngong Hills, the steaming Hell's Gate gorge, Lake Naivasha and the crater of Mount Longonot.", "Zsiráfok a felhőkarcolók előtt a Nairobi Nemzeti Parkban, majd a Ngong-dombok, a gőzölgő Hell's Gate-szurdok, a Naivasha-tó és a Mount Longonot krátere."),
    [("loop", "loop", 110, 9500, ("Rift Valley loop", "Hasadékvölgy-kör"), ("Ngong Hills, Hell's Gate, Lake Naivasha, Mount Longonot and Nairobi National Park.", "Ngong-dombok, Hell's Gate, Naivasha-tó, Mount Longonot és a Nairobi Nemzeti Park."),
      ["HKNW", Pt("Ngong Hills", -1.4700, 36.6500), Pt("Hell's Gate", -0.9100, 36.3200), Pt("Lake Naivasha", -0.7667, 36.3500), Pt("Mount Longonot", -0.9170, 36.4480), Pt("Nairobi National Park", -1.3733, 36.8586), "HKNW"])])
add("AF", "kigali-volcanoes", RW, ("Kigali and the Virunga Volcanoes", "Kigali és a Virunga-vulkánok"), ("Karisimbi", "Karisimbi", -1.5030, 29.4450), ["volcano", "mountain", "city"],
    ("The land of a thousand hills, the home of the mountain gorillas on the slopes of Bisoke and Karisimbi and the lava lake of Nyiragongo above Lake Kivu.", "Az ezer domb országa, a hegyi gorillák otthona a Bisoke és a Karisimbi lejtőin, és a Nyiragongo lávatava a Kivu-tó felett."),
    [("long", "loop", 120, 12000, ("Volcano chain", "Vulkánsor"), ("Kigali, Bisoke, Karisimbi, Nyiragongo and Lake Kivu.", "Kigali, a Bisoke, a Karisimbi, a Nyiragongo és a Kivu-tó."),
      ["HRYR", Pt("Mount Bisoke", -1.4750, 29.4870), Pt("Karisimbi", -1.5030, 29.4450), Pt("Nyiragongo", -1.5217, 29.2490), Pt("Lake Kivu", -1.7000, 29.2560), Pt("Kigali", -1.9441, 30.0619), "HRYR"])])
add("AF", "tunis-carthage", TN, ("Tunis, Carthage and Cap Bon", "Tunisz, Karthágó és a Bon-fok"), ("Carthage", "Karthágó", 36.8528, 10.3233), ["culture", "coast", "unesco"],
    ("Phoenician Carthage on the gulf, blue-and-white Sidi Bou Said, the Cap Bon peninsula and the Roman aqueduct of Zaghouan.", "A föníciai Karthágó az öbölnél, a kék-fehér Sidi Bou Said, a Bon-fok félsziget és a zaghuani római vízvezeték."),
    [("loop", "loop", 100, 3000, ("Carthage and Cap Bon", "Karthágó és a Bon-fok"), ("Carthage, Sidi Bou Said, Kelibia, Hammamet and Zaghouan.", "Karthágó, Sidi Bou Said, Kelibia, Hammamet és Zaghouan."),
      ["DTTA", Pt("Carthage", 36.8528, 10.3233), Pt("Sidi Bou Said", 36.8700, 10.3410), Pt("Kelibia", 36.8470, 11.0950), Pt("Hammamet", 36.4000, 10.6130), Pt("Zaghouan", 36.4000, 10.1420), "DTTA"])])
add("AF", "morondava-tsingy", MG, ("Baobabs and the Tsingy of Madagascar", "Madagaszkár baobabjai és a Tsingy"), ("Avenue of the Baobabs", "Baobabok sétánya", -20.2510, 44.4180), ["culture", "unesco", "jungle"],
    ("The famous baobab avenue, the Tsiribihina river and the razor-sharp limestone forest of the Tsingy de Bemaraha.", "A híres baobab-fasor, a Tsiribihina folyó és a Tsingy de Bemaraha borotvaéles mészkőerdeje."),
    [("loop", "loop", 100, 3500, ("Baobabs and Tsingy", "Baobabok és Tsingy"), ("Morondava, the Avenue of the Baobabs, the Tsingy de Bemaraha and the Tsiribihina.", "Morondava, a Baobabok sétánya, a Tsingy de Bemaraha és a Tsiribihina."),
      ["FMMV", Pt("Avenue of the Baobabs", -20.2510, 44.4180), Pt("Tsingy de Bemaraha", -19.1300, 44.8200), Pt("Tsiribihina River", -19.7600, 44.6000), "FMMV"])])
add("AF", "kruger-blyde", ZA, ("Kruger and the Blyde River Canyon", "Kruger és a Blyde River-kanyon"), ("Three Rondavels", "Three Rondavels", -24.5750, 30.8130), ["mountain", "jungle"],
    ("The third-largest canyon on earth along the Drakensberg escarpment, God's Window, the Bourke's Luck potholes and the savannah of Kruger National Park.", "A Föld harmadik legnagyobb kanyonja a Drakensberg peremén, God's Window, Bourke's Luck lyukak és a Kruger Nemzeti Park szavannája."),
    [("long", "loop", 110, 7000, ("Escarpment and savannah", "Hegyperem és szavanna"), ("Pilgrim's Rest, Bourke's Luck, the Three Rondavels, God's Window and Skukuza.", "Pilgrim's Rest, Bourke's Luck, a Three Rondavels, God's Window és Skukuza."),
      ["FAKN", Pt("Pilgrim's Rest", -24.9170, 30.7600), Pt("Bourke's Luck Potholes", -24.6700, 30.8000), Pt("Three Rondavels", -24.5750, 30.8130), Pt("Skukuza", -24.9930, 31.5920), "FAKN"])])
add("AF", "aswan-abu-simbel", EG, ("Aswan to Abu Simbel", "Asszuántól Abu Szimbelig"), ("Abu Simbel", "Abu Szimbel", 22.3369, 31.6258), ["culture", "unesco"],
    ("From the Nile cataracts of Aswan along Lake Nasser to the colossal temples of Ramesses II that were moved stone by stone.", "Asszuán nílusi zuhatagaitól a Nasszer-tó mentén II. Ramszesz kolosszális, kőről kőre áthelyezett templomaiig."),
    [("ab", "ab", 110, 4000, ("Along Lake Nasser", "A Nasszer-tó mentén"), ("Philae, the Aswan High Dam, Qasr Ibrim and the temples of Abu Simbel.", "Philae, az asszuáni nagy gát, Qasr Ibrim és Abu Szimbel templomai."),
      ["HESN", Pt("Philae", 24.0250, 32.8840), Pt("Aswan High Dam", 23.9700, 32.8770), Pt("Qasr Ibrim", 22.6500, 32.0000), "HEBL"])])
# ---------------- Oceania
add("OC", "perth-rottnest", AU, ("Perth and Rottnest Island", "Perth és Rottnest-sziget"), ("Rottnest Island", "Rottnest-sziget", -32.0000, 115.5200), ["city", "coast", "island"],
    ("The sunniest capital city with the Swan River, Fremantle's harbour and Rottnest Island, home of the smiling quokkas.", "A legnaposabb főváros a Swan folyóval, Fremantle kikötőjével és a mosolygó quokkák otthonával, a Rottnest-szigettel."),
    [("loop", "loop", 100, 3000, ("Perth and Rottnest", "Perth és Rottnest"), ("Garden Island, Rottnest, Scarborough Beach and the Perth skyline.", "Garden Island, Rottnest, Scarborough Beach és Perth látképe."),
      ["YPJT", Pt("Garden Island", -32.2200, 115.6800), Pt("Rottnest Island", -32.0000, 115.5200), Pt("Scarborough Beach", -31.8940, 115.7570), Pt("Perth CBD", -31.9505, 115.8605), "YPJT"])])
add("OC", "gold-coast", AU, ("Gold Coast and Byron Bay", "Gold Coast és Byron Bay"), ("Surfers Paradise", "Surfers Paradise", -28.0023, 153.4310), ["coast", "city", "mountain"],
    ("Skyscrapers on a surf beach, the rainforest of Springbrook, the extinct volcano of Mount Warning and Australia's easternmost point at Byron Bay.", "Felhőkarcolók a szörfstrandon, Springbrook esőerdeje, a kialudt Mount Warning vulkán és Ausztrália legkeletibb pontja Byron Baynél."),
    [("loop", "loop", 100, 3500, ("Surf and volcano", "Szörf és vulkán"), ("Byron Bay, Mount Warning, Springbrook and Surfers Paradise.", "Byron Bay, a Mount Warning, Springbrook és Surfers Paradise."),
      ["YBCG", Pt("Cape Byron", -28.6385, 153.6370), Pt("Mount Warning", -28.4014, 153.2720), Pt("Springbrook", -28.2400, 153.2760), Pt("Surfers Paradise", -28.0023, 153.4310), "YBCG"])])
add("OC", "melbourne-phillip", AU, ("Melbourne and Phillip Island", "Melbourne és Phillip-sziget"), ("Phillip Island", "Phillip-sziget", -38.4880, 145.2370), ["city", "coast", "island"],
    ("Melbourne's skyline and the Yarra, the Mornington Peninsula's tip and the Nobbies of Phillip Island, famous for its little penguins.", "Melbourne látképe és a Yarra, a Mornington-félsziget csúcsa és a Phillip-sziget Nobbies sziklái a kis pingvinekkel."),
    [("loop", "loop", 100, 3000, ("Port Phillip loop", "Port Phillip-kör"), ("Cape Woolamai, the Nobbies, Cape Schanck, Portsea and the city.", "Cape Woolamai, a Nobbies, Cape Schanck, Portsea és a belváros."),
      ["YMMB", Pt("Cape Woolamai", -38.5500, 145.3500), Pt("The Nobbies", -38.5120, 145.1500), Pt("Cape Schanck", -38.4980, 144.8900), Pt("Portsea", -38.3280, 144.7160), Pt("Melbourne CBD", -37.8136, 144.9631), "YMMB"])])
add("OC", "bay-of-islands", NZ, ("Bay of Islands", "Bay of Islands"), ("Hole in the Rock", "Hole in the Rock", -35.1700, 174.3240), ["coast", "island", "culture"],
    ("144 islands in a subtropical bay, the Hole in the Rock at Cape Brett, the Waitangi Treaty Grounds and Russell, New Zealand's first capital.", "144 sziget egy szubtrópusi öbölben, a Hole in the Rock a Cape Brettnél, a Waitangi-egyezmény helyszíne és Russell, Új-Zéland első fővárosa."),
    [("loop", "loop", 100, 3000, ("Cape Brett loop", "Cape Brett-kör"), ("Waitangi, Russell, Cape Brett and Whangaroa Harbour.", "Waitangi, Russell, Cape Brett és a Whangaroa-kikötő."),
      ["NZKK", Pt("Waitangi", -35.2690, 174.0790), Pt("Russell", -35.2630, 174.1230), Pt("Cape Brett", -35.1700, 174.3240), Pt("Whangaroa Harbour", -35.0600, 173.7500), "NZKK"])])
add("OC", "rotorua-tongariro", NZ, ("Rotorua and Tongariro", "Rotorua és Tongariro"), ("Mount Ngauruhoe", "Mount Ngauruhoe", -39.1560, 175.6320), ["volcano", "unesco", "mountain"],
    ("The geothermal wonderland of Rotorua and Wai-O-Tapu, the cleft of Mount Tarawera, Lake Taupō and the volcanoes of Tongariro, Ngauruhoe and Ruapehu.", "Rotorua és Wai-O-Tapu geotermikus csodavilága, a Tarawera hasadéka, a Taupō-tó és a Tongariro, a Ngauruhoe és a Ruapehu vulkánjai."),
    [("long", "loop", 110, 8000, ("Volcanic plateau", "Vulkáni fennsík"), ("Mount Tarawera, Wai-O-Tapu, Lake Taupō, Ruapehu and Ngauruhoe.", "A Mount Tarawera, Wai-O-Tapu, a Taupō-tó, a Ruapehu és a Ngauruhoe."),
      ["NZRO", Pt("Mount Tarawera", -38.2290, 176.5030), Pt("Wai-O-Tapu", -38.3590, 176.3660), Pt("Lake Taupo", -38.6857, 176.0702), Pt("Mount Ruapehu", -39.2840, 175.5640), Pt("Mount Ngauruhoe", -39.1560, 175.6320), "NZRO"])])
add("OC", "palau", PW, ("Palau Rock Islands", "Palau Rock-szigetek"), ("Rock Islands", "Rock-szigetek", 7.2000, 134.3700), ["island", "coast", "unesco"],
    ("Hundreds of mushroom-shaped limestone islands in turquoise water, the Jellyfish Lake and the old WWII battlefield of Peleliu.", "Több száz gomba alakú mészkőszigetet turkiz vízben, a Medúza-tó és Peleliu régi második világháborús csatatere."),
    [("loop", "loop", 100, 2500, ("Rock Islands loop", "Rock-szigetek köre"), ("Koror, the Rock Islands, Jellyfish Lake and Peleliu.", "Koror, a Rock-szigetek, a Medúza-tó és Peleliu."),
      ["PTRO", Pt("Koror", 7.3400, 134.4780), Pt("Jellyfish Lake", 7.1610, 134.3770), Pt("Peleliu", 6.9900, 134.2500), Pt("Ngeremlengui Bay", 7.4150, 134.4300), "PTRO"])])
# ---------------- Del-Amerika
add("SA", "cartagena-rosario", CO, ("Cartagena and the Rosario Islands", "Cartagena és a Rosario-szigetek"), ("Cartagena Old Town", "Cartagena óvárosa", 10.4236, -75.5503), ["culture", "coast", "unesco", "island"],
    ("The walled colonial city on the Caribbean, the coral islands of Rosario and Barú and the mud volcano of El Totumo.", "A karibi tengerparti, várfallal körülvett gyarmati város, a Rosario- és Barú-korallszigetek és az El Totumo iszapvulkánja."),
    [("loop", "loop", 100, 2500, ("Caribbean loop", "Karibi kör"), ("Old Town, the Rosario Islands, Barú and the Totumo volcano.", "Az óváros, a Rosario-szigetek, Barú és a Totumo vulkán."),
      ["SKCG", Pt("Cartagena Old Town", 10.4236, -75.5503), Pt("Rosario Islands", 10.1700, -75.7400), Pt("Isla Barú", 10.2300, -75.6200), Pt("Totumo Volcano", 10.5190, -75.2850), "SKCG"])])
add("SA", "medellin-guatape", CO, ("Medellín and Guatapé", "Medellín és Guatapé"), ("El Peñol", "El Peñol", 6.2330, -75.1810), ["city", "mountain", "culture"],
    ("The city of eternal spring in the Aburrá valley and the great granite rock of El Peñol above the reservoir of Guatapé.", "Az örök tavasz városa az Aburrá-völgyben és a guatapéi víztározó felett álló hatalmas gránitszikla, az El Peñol."),
    [("loop", "loop", 100, 9000, ("Valley and reservoir", "Völgy és víztározó"), ("Guatapé, El Peñol, Medellín and Parque Arví.", "Guatapé, El Peñol, Medellín és a Parque Arví."),
      ["SKRG", Pt("Guatapé", 6.2330, -75.1810), Pt("Medellín", 6.2442, -75.5812), Pt("Parque Arví", 6.2800, -75.4930), "SKRG"])])
add("SA", "lima", PE, ("Lima and the Pacific Coast", "Lima és a csendes-óceáni part"), ("Miraflores", "Miraflores", -12.1219, -77.0297), ["city", "coast", "culture"],
    ("A desert capital on the cliffs of the Pacific: Miraflores, the port of Callao, San Lorenzo island and the temple city of Pachacamac.", "Sivatagi főváros a Csendes-óceán sziklái felett: Miraflores, Callao kikötője, a San Lorenzo-sziget és Pachacamac templomvárosa."),
    [("loop", "loop", 100, 2500, ("Lima coast", "Lima partja"), ("Miraflores, San Lorenzo, Callao and Pachacamac.", "Miraflores, San Lorenzo, Callao és Pachacamac."),
      ["SPIM", Pt("San Lorenzo Island", -12.0770, -77.2200), Pt("Callao", -12.0560, -77.1180), Pt("Miraflores", -12.1219, -77.0297), Pt("Pachacamac", -12.2540, -76.9030), "SPIM"])])
add("SA", "la-paz-titicaca", BO, ("La Paz and Lake Titicaca", "La Paz és a Titicaca-tó"), ("Lake Titicaca", "Titicaca-tó", -16.1660, -69.0870), ["mountain", "city", "culture"],
    ("The highest capital in the world below the glaciers of Illimani, the ruins of Tiwanaku and the sacred Isla del Sol on Lake Titicaca.", "A világ legmagasabban fekvő fővárosa az Illimani gleccserei alatt, Tiwanaku romjai és a szent Isla del Sol a Titicaca-tavon."),
    [("long", "loop", 110, 17000, ("Altiplano loop", "Altiplano-kör"), ("Huayna Potosí, Lake Titicaca, Isla del Sol, Tiwanaku and Illimani.", "Huayna Potosí, a Titicaca-tó, az Isla del Sol, Tiwanaku és az Illimani."),
      ["SLLP", Pt("Huayna Potosí", -16.2620, -68.1500), Pt("Copacabana", -16.1660, -69.0870), Pt("Isla del Sol", -16.0170, -69.1790), Pt("Tiwanaku", -16.5546, -68.6735), Pt("Illimani", -16.6310, -67.7870), "SLLP"])])
add("SA", "pucon-volcanoes", CL, ("Pucón and the Chilean Volcanoes", "Pucón és a chilei vulkánok"), ("Villarrica Volcano", "Villarrica vulkán", -39.4200, -71.9390), ["volcano", "mountain"],
    ("The smoking cone of Villarrica above its lake, the snow-capped Llaima and Lanín on the border with Argentina.", "A füstölgő Villarrica kúpja a tava felett, a havas Llaima és a Lanín az argentin határon."),
    [("loop", "loop", 100, 12000, ("Lake District volcanoes", "A tóvidék vulkánjai"), ("Llaima, Pucón, Villarrica, Lanín and Lake Calafquén.", "A Llaima, Pucón, a Villarrica, a Lanín és a Calafquén-tó."),
      ["SCTC", Pt("Llaima", -38.7080, -71.7340), Pt("Pucón", -39.2820, -71.9540), Pt("Villarrica Volcano", -39.4200, -71.9390), Pt("Lanín", -39.6280, -71.5000), Pt("Lake Calafquén", -39.5500, -72.1000), "SCTC"])])
# ---------------- Azsia
add("AS", "ladakh", IN, ("Ladakh and the Indus Valley", "Ladakh és az Indus-völgy"), ("Thiksey Monastery", "Thiksey-kolostor", 34.0485, 77.6670), ["mountain", "culture"],
    ("Monasteries on hilltops at 3,500 metres, the Stok Kangri massif and the Khardung La pass in the high desert of the Himalaya.", "Kolostorok a 3500 méteres dombtetőkön, a Stok Kangri-hegység és a Khardung La-hágó a Himalája magas sivatagában."),
    [("long", "loop", 110, 19000, ("Little Tibet", "Kis-Tibet"), ("Stok Kangri, Hemis, Thiksey, the Khardung La and Alchi.", "Stok Kangri, Hemis, Thiksey, a Khardung La és Alchi."),
      ["VILH", Pt("Stok Kangri", 33.9730, 77.4720), Pt("Hemis Monastery", 33.9130, 77.7020), Pt("Thiksey Monastery", 34.0485, 77.6670), Pt("Khardung La", 34.2780, 77.6040), Pt("Alchi", 34.2170, 77.1700), "VILH"])])
add("AS", "pokhara-annapurna", NP, ("Pokhara and the Annapurna Range", "Pokhara és az Annapurna-hegység"), ("Machapuchare", "Machapuchare", 28.4950, 83.9490), ["mountain"],
    ("Eight-thousanders only 30 km from a lakeside town: Dhaulagiri, Annapurna and the Fishtail peak of Machapuchare.", "Nyolcezresek mindössze 30 km-re egy tóparti várostól: a Dhaulagiri, az Annapurna és a Machapuchare, a Halfarok-csúcs."),
    [("loop", "loop", 100, 17000, ("Annapurna loop", "Annapurna-kör"), ("Poon Hill, Dhaulagiri, Annapurna, Machapuchare and Phewa Lake.", "Poon Hill, a Dhaulagiri, az Annapurna, a Machapuchare és a Phewa-tó."),
      ["VNPK", Pt("Poon Hill", 28.4000, 83.6870), Pt("Dhaulagiri", 28.6980, 83.4870), Pt("Annapurna I", 28.5960, 83.8203), Pt("Machapuchare", 28.4950, 83.9490), Pt("Phewa Lake", 28.2100, 83.9450), "VNPK"])], )
add("AS", "hiroshima-miyajima", JP, ("Hiroshima and Miyajima", "Hirosima és Mijadzsima"), ("Itsukushima Shrine", "Icukusima-szentély", 34.2958, 132.3198), ["culture", "unesco", "island", "coast"],
    ("The Peace Memorial, the floating torii of Itsukushima, the wooden Kintai Bridge of Iwakuni and the naval port of Kure on the Seto Inland Sea.", "A Béke-emlékmű, az Icukusima úszó toriija, Ivakuni fából épült Kintai-hídja és Kure haditengerészeti kikötője a Seto-belső-tengeren."),
    [("loop", "loop", 100, 3000, ("Inland Sea loop", "Belső-tengeri kör"), ("Hiroshima, Miyajima, Iwakuni and Kure.", "Hirosima, Mijadzsima, Ivakuni és Kure."),
      ["RJOA", Pt("Peace Memorial", 34.3955, 132.4536), Pt("Itsukushima Shrine", 34.2958, 132.3198), Pt("Kintai Bridge", 34.1670, 132.1790), Pt("Kure", 34.2480, 132.5650), "RJOA"])])
add("AS", "okinawa", JP, ("Okinawa", "Okinava"), ("Churaumi Aquarium", "Csurauminál akvárium", 26.6940, 127.8780), ["island", "coast", "culture", "unesco"],
    ("Turquoise reefs, the Kerama islands, Shuri Castle and the northern bridges of the Ryukyu islands.", "Türkizkék zátonyok, a Kerama-szigetek, a Suri-kastély és a Rjúkjú-szigetek északi hídjai."),
    [("loop", "loop", 100, 3000, ("Okinawa loop", "Okinava-kör"), ("The Kerama islands, Cape Zanpa, Churaumi, Kouri Bridge and Nakagusuku Castle.", "A Kerama-szigetek, Zanpa-fok, Csurauminál, a Kouri-híd és a Nakagusuku-vár."),
      ["ROAH", Pt("Kerama Islands", 26.2000, 127.3000), Pt("Cape Zanpa", 26.4380, 127.7120), Pt("Churaumi Aquarium", 26.6940, 127.8780), Pt("Kouri Bridge", 26.6870, 128.0230), Pt("Nakagusuku Castle", 26.2780, 127.7960), "ROAH"])])
add("AS", "danang-hoian", VN, ("Da Nang and Hoi An", "Da Nang és Hoi An"), ("Hai Van Pass", "Hai Van-hágó", 16.1980, 108.1190), ["coast", "culture", "unesco", "mountain"],
    ("The Hai Van Pass between sea and mountains, the Marble Mountains, the lantern town of Hoi An and the Cham temples of Mỹ Sơn.", "A tenger és a hegyek között kanyargó Hai Van-hágó, a Márvány-hegyek, a lampionos Hoi An és a Mỹ Sơn cham templomai."),
    [("loop", "loop", 100, 3000, ("Central Vietnam", "Közép-Vietnám"), ("Hai Van Pass, Ba Na Hills, My Son, Hoi An and the Cham Islands.", "Hai Van-hágó, Ba Na-hegység, Mỹ Sơn, Hoi An és a Cham-szigetek."),
      ["VVDN", Pt("Hai Van Pass", 16.1980, 108.1190), Pt("Ba Na Hills", 15.9950, 107.9960), Pt("My Son", 15.7640, 108.1250), Pt("Hoi An", 15.8801, 108.3380), Pt("Cham Islands", 15.9500, 108.5200), Pt("Marble Mountains", 16.0033, 108.2640), "VVDN"])])
add("AS", "georgia-caucasus", GE, ("Tbilisi and the Caucasus", "Tbiliszi és a Kaukázus"), ("Mount Kazbek", "Kazbek", 42.6970, 44.5190), ["mountain", "culture", "unesco"],
    ("The old town of Tbilisi, the monastery of Jvari, the Georgian Military Road and the Gergeti Trinity Church under the glaciers of Mount Kazbek.", "Tbiliszi óvárosa, a Dzsvari-kolostor, a Grúz Katonai Út és a Gergeti Szentháromság-templom a Kazbek gleccserei alatt."),
    [("long", "loop", 110, 14000, ("Military Road", "Katonai Út"), ("Mtskheta, Ananuri, Gudauri, Mount Kazbek and the Alazani valley.", "Mtshéta, Ananuri, Gudauri, a Kazbek és az Alazani-völgy."),
      ["UGTB", Pt("Jvari Monastery", 41.8386, 44.7340), Pt("Ananuri", 42.1630, 44.7030), Pt("Gudauri", 42.4800, 44.4800), Pt("Gergeti Trinity Church", 42.6620, 44.6200), Pt("Mount Kazbek", 42.6970, 44.5190), Pt("Telavi", 41.9200, 45.4730), "UGTB"])])
# ---------------- Eszak-Amerika
add("NA", "puerto-rico", PR, ("Puerto Rico", "Puerto Rico"), ("El Yunque", "El Yunque", 18.2950, -65.7870), ["island", "coast", "jungle", "culture"],
    ("Old San Juan's fortress, the only tropical rainforest in the US National Forest system and the white sand of Culebra.", "A régi San Juan erődje, az amerikai erdőrendszer egyetlen trópusi esőerdeje és Culebra fehér homokja."),
    [("loop", "loop", 100, 3000, ("San Juan and Culebra", "San Juan és Culebra"), ("El Morro, El Yunque, Fajardo and Flamenco Beach.", "El Morro, El Yunque, Fajardo és a Flamenco-strand."),
      ["TJSJ", Pt("El Morro", 18.4710, -66.1240), Pt("El Yunque", 18.2950, -65.7870), Pt("Fajardo", 18.3300, -65.6500), Pt("Flamenco Beach", 18.3300, -65.3170), "TJSJ"])])
add("NA", "cabo", MX, ("Los Cabos and Baja", "Los Cabos és Baja"), ("El Arco", "El Arco", 22.8750, -109.8940), ["coast", "mountain"],
    ("Where the Pacific meets the Sea of Cortez at the rock arch of Cabo San Lucas, Todos Santos, the Sierra de la Laguna and the reef of Cabo Pulmo.", "Ahol a Csendes-óceán a Cortés-tengerrel találkozik: Cabo San Lucas sziklaíve, Todos Santos, a Sierra de la Laguna és a Cabo Pulmo zátonya."),
    [("loop", "loop", 100, 4000, ("Land's End", "Land's End"), ("Cabo San Lucas, Todos Santos, the Sierra de la Laguna and Cabo Pulmo.", "Cabo San Lucas, Todos Santos, a Sierra de la Laguna és Cabo Pulmo."),
      ["MMSD", Pt("El Arco", 22.8750, -109.8940), Pt("Todos Santos", 23.4500, -110.2250), Pt("Sierra de la Laguna", 23.5200, -109.9800), Pt("Cabo Pulmo", 23.4380, -109.4290), "MMSD"])])
add("NA", "belize-blue-hole", BZ, ("Belize and the Great Blue Hole", "Belize és a Nagy Kék Lyuk"), ("Great Blue Hole", "Nagy Kék Lyuk", 17.3157, -87.5347), ["coast", "island", "unesco"],
    ("A perfect circle of deep blue 300 m wide in the Lighthouse Reef, the Turneffe atoll and the barrier reef off Caye Caulker.", "Egy 300 méteres, tökéletesen kerek mélykék lyuk a Lighthouse-zátonyon, a Turneffe-atoll és a Caye Caulker előtti gátzátony."),
    [("loop", "loop", 110, 3000, ("Reef loop", "Zátony-kör"), ("Caye Caulker, the Great Blue Hole, Half Moon Caye and Turneffe.", "Caye Caulker, a Nagy Kék Lyuk, Half Moon Caye és Turneffe."),
      ["MZBZ", Pt("Caye Caulker", 17.7430, -88.0240), Pt("Great Blue Hole", 17.3157, -87.5347), Pt("Half Moon Caye", 17.2000, -87.5330), Pt("Turneffe Atoll", 17.3500, -87.9500), "MZBZ"])])
add("NA", "costa-rica", CR, ("Costa Rica Volcanoes", "Costa Rica vulkánjai"), ("Arenal", "Arenal", 10.4630, -84.7030), ["volcano", "jungle", "mountain"],
    ("A chain of volcanoes from the crater lake of Poás to the perfect cone of Arenal and the cloud forest of Monteverde.", "Vulkánok sora a Poás kráteres tavától az Arenal tökéletes kúpjáig és Monteverde ködös esőerdejéig."),
    [("loop", "loop", 100, 9000, ("Volcano loop", "Vulkán-kör"), ("Irazú, Turrialba, Poás, Arenal and Monteverde.", "Irazú, Turrialba, Poás, Arenal és Monteverde."),
      ["MROC", Pt("Irazú", 9.9790, -83.8520), Pt("Turrialba Volcano", 10.0250, -83.7670), Pt("Poás", 10.2000, -84.2330), Pt("Arenal", 10.4630, -84.7030), Pt("Monteverde", 10.3000, -84.8270), "MROC"])])
# ---------------- STOL
add("AS", "jomsom-mustang", NP, ("Jomsom and Mustang", "Jomsom és Mustang"), ("Muktinath", "Muktinath", 28.8170, 83.8710), ["mountain", "culture", "stol"],
    ("One of the most dramatic airports on earth in the deepest gorge on the planet: Dhaulagiri and Nilgiri tower above, the walled kingdom of Lo Manthang is a hop to the north.", "A Föld egyik legdrámaibb repülőtere a bolygó legmélyebb szurdokában: fölötte a Dhaulagiri és a Nilgiri, északra pedig Lo Manthang fallal körülvett királysága."),
    [("loop", "loop", 100, 16000, ("Kali Gandaki gorge", "Kali Gandaki-szurdok"), ("Muktinath, Lo Manthang, Kagbeni, Nilgiri and Dhaulagiri.", "Muktinath, Lo Manthang, Kagbeni, a Nilgiri és a Dhaulagiri."),
      ["VNJS", Pt("Muktinath", 28.8170, 83.8710), Pt("Lo Manthang", 29.1830, 83.9500), Pt("Kagbeni", 28.8350, 83.7790), Pt("Nilgiri", 28.6300, 83.7930), Pt("Dhaulagiri", 28.6980, 83.4870), "VNJS"])])
add("NA", "idaho-backcountry", US, ("Idaho Backcountry", "Idaho vadonja"), ("Big Creek", "Big Creek", 45.1332, -115.3220), ["mountain", "jungle", "stol"],
    ("The home of backcountry flying: grass and gravel strips on the Salmon River in the largest roadless wilderness of the lower 48.", "A vadonrepülés hazája: fű- és kavicspályák a Salmon folyó mentén az alsó 48 állam legnagyobb út nélküli vadonjában."),
    [("loop", "loop", 100, 8500, ("Frank Church loop", "Frank Church-kör"), ("Johnson Creek, Stibnite, Big Creek, Mackay Bar, Cabin Creek and Indian Creek.", "Johnson Creek, Stibnite, Big Creek, Mackay Bar, Cabin Creek és Indian Creek."),
      ["3U2", "ID41", "U60", "ID28", "I08", "S81", "3U2"])])
add("OC", "kokoda", PG, ("Kokoda Track", "Kokoda Track"), ("Kokoda", "Kokoda", -8.8847, 147.7310), ["mountain", "jungle", "stol"],
    ("From Port Moresby over the Owen Stanley Range to the sloping airstrip of Kokoda, along the jungle track of the famous WWII campaign.", "Port Moresbytől az Owen Stanley-hegységen át Kokoda lejtős leszállópályájáig, a híres második világháborús hadjárat dzsungelösvénye mentén."),
    [("ab", "ab", 100, 9000, ("Over the Owen Stanleys", "Az Owen Stanley felett"), ("Port Moresby, the Kokoda Track and the airstrip of Kokoda.", "Port Moresby, a Kokoda Track és Kokoda leszállópályája."),
      ["AYPY", Pt("Kokoda Track", -9.1600, 147.4800), "AYKO"])])
add("EU", "tiree-hebrides", UK, ("Inner Hebrides from Tiree", "A Belső-Hebridák Tireeből"), ("Fingal's Cave", "Fingal-barlang", 56.4330, -6.3400), ["island", "coast", "stol"],
    ("The sunniest island in Scotland, Iona's abbey, the basalt columns of Staffa and the peaks of Mull.", "Skócia legnaposabb szigete, Iona apátsága, a Staffa bazaltoszlopai és Mull csúcsai."),
    [("loop", "loop", 100, 2500, ("Iona, Staffa and Mull", "Iona, Staffa és Mull"), ("Iona, Staffa, Ben More and Coll.", "Iona, Staffa, a Ben More és Coll."),
      ["EGPU", Pt("Iona", 56.3310, -6.3930), Pt("Staffa", 56.4330, -6.3400), Pt("Ben More", 56.4270, -6.0380), Pt("Coll", 56.6250, -6.5200), "EGPU"])])
add("EU", "samedan-bernina", CH, ("Engadin and the Bernina", "Engadin és a Bernina"), ("Piz Bernina", "Piz Bernina", 46.3820, 9.9070), ["mountain", "stol"],
    ("The highest airport in Europe at 5,600 ft, among the lakes of the Upper Engadine and the only four-thousander of the Eastern Alps.", "Európa legmagasabban fekvő repülőtere, 1700 méteren, az Felső-Engadin tavai között és a Keleti-Alpok egyetlen négyezresével."),
    [("loop", "loop", 100, 13000, ("Bernina loop", "Bernina-kör"), ("St. Moritz, Lake Sils, Piz Bernina, Piz Palü and the Bernina Pass.", "St. Moritz, a Sils-tó, a Piz Bernina, a Piz Palü és a Bernina-hágó."),
      ["LSZS", Pt("St. Moritz", 46.4980, 9.8350), Pt("Lake Sils", 46.4200, 9.7600), Pt("Piz Bernina", 46.3820, 9.9070), Pt("Piz Palü", 46.3680, 9.9570), Pt("Bernina Pass", 46.4090, 10.0210), "LSZS"])])
add("EU", "pyrenees", ES, ("The Pyrenees from La Seu d'Urgell", "A Pireneusok La Seu d'Urgellből"), ("Aneto", "Aneto", 42.6310, 0.6560), ["mountain"],
    ("From a mountain airfield in the Catalan Pyrenees over Andorra, Pica d'Estats, Aneto and the walls of Monte Perdido.", "Egy katalán-pireneusi hegyi repülőtérről Andorra, a Pica d'Estats, az Aneto és a Monte Perdido falai felett."),
    [("long", "loop", 110, 11000, ("High Pyrenees", "Magas-Pireneusok"), ("Andorra, Pica d'Estats, Aneto, Monte Perdido and Ainsa.", "Andorra, a Pica d'Estats, az Aneto, a Monte Perdido és Ainsa."),
      ["LESU", Pt("Andorra la Vella", 42.5063, 1.5218), Pt("Pica d'Estats", 42.6670, 1.3980), Pt("Aneto", 42.6310, 0.6560), Pt("Monte Perdido", 42.6720, 0.0360), Pt("Ainsa", 42.4160, 0.1400), "LESU"])])

for t in T:
    t["continent"] = CONT[t["id"]]
    if "stol" in t["tags"]:
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
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "r7_ids.txt"), "w").write(" ".join(NEW))
