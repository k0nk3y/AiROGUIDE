#!/usr/bin/env python3
"""4. kor: 20 uj tura (Azsia, Eszak-/Del-Amerika, Afrika, Oceania). Sorrend: add_r4 -> tours_order <r4_ids> -> poi_registry -> tours_kw -> tours_img -> tours_check"""
from tourlib import *
import json, os
C = lambda e, h: (e, h)
KR = C("South Korea", "Dél-Korea"); IN = C("India", "India"); ID = C("Indonesia", "Indonézia"); BT = C("Bhutan", "Bhután"); LK = C("Sri Lanka", "Srí Lanka")
US = C("United States", "Egyesült Államok"); MX = C("Mexico", "Mexikó"); PE = C("Peru", "Peru"); BO = C("Bolivia", "Bolívia"); VE = C("Venezuela", "Venezuela"); BR = C("Brazil", "Brazília")
TZ = C("Tanzania", "Tanzánia"); MU = C("Mauritius", "Mauritius"); MA = C("Morocco", "Marokkó"); NZ = C("New Zealand", "Új-Zéland")
CONT = {}


def add(cont, *a, **k):
    tour(*a, **k); CONT[a[0]] = cont


def Pt(n, la, lo): return [n, la, lo]


# ---------------- Azsia ----------------
add("AS", "jeju", KR, ("Jeju Island", "Jeju-sziget"), ("Hallasan", "Hallasan", 33.3617, 126.5292), ["island", "volcano", "coast", "unesco"],
    ("Korea's volcanic island: the crater of Hallasan, the tuff cone of Seongsan Ilchulbong and waterfalls plunging into the sea.", "Korea vulkanikus szigete: a Hallasan krátere, a Seongsan Ilchulbong tufakúpja és a tengerbe zuhanó vízesések."), [],
    [("long", "loop", 105, 4000, ("Around Jeju", "Jeju körül"), ("About an hour: Seongsan, the Jeongbang waterfall, Yongmeori coast and Hallasan.", "Kb. egy óra: Seongsan, a Jeongbang-vízesés, a Yongmeori-part és a Hallasan."),
      ["RKPC", Pt("Seongsan Ilchulbong", 33.4590, 126.9420), Pt("Jeongbang Falls", 33.2440, 126.5710), Pt("Yongmeori Coast", 33.2310, 126.3120), Pt("Hallasan", 33.3617, 126.5292), "RKPC"])])
add("AS", "rajasthan", IN, ("Jaipur and Rajasthan", "Jaipur és Rádzsasztán"), ("Amber Fort", "Amber-erőd", 26.9855, 75.8513), ["culture", "city"],
    ("The Pink City, its hilltop forts and the palaces of Rajasthan, with the holy lake of Pushkar and the salt flats of Sambhar.", "A Rózsaszín Város, hegytetői erődjei és Rádzsasztán palotái, a szent Pushkar-tóval és a Sambhar sósivataggal."), [],
    [("short", "loop", 110, 4000, ("Jaipur and Sambhar Lake", "Jaipur és a Sambhar-tó"), ("Over the Pink City, Amber Fort, the Jal Mahal and the salt lake of Sambhar.", "A Rózsaszín Város, az Amber-erőd, a Jal Mahal és a Sambhar sóstó felett."),
      ["VIJP", Pt("Sambhar Lake", 26.9100, 75.1900), Pt("Amber Fort", 26.9855, 75.8513), Pt("Jal Mahal", 26.9535, 75.8460), Pt("Hawa Mahal", 26.9239, 75.8267), "VIJP"]),
     ("long", "loop", 115, 5000, ("Jaipur and Pushkar", "Jaipur és Pushkar"), ("About an hour and a half: Jaipur's forts, Sambhar Lake and the holy lake of Pushkar.", "Kb. másfél óra: Jaipur erődjei, a Sambhar-tó és a szent Pushkar-tó."),
      ["VIJP", Pt("Hawa Mahal", 26.9239, 75.8267), Pt("Jal Mahal", 26.9535, 75.8460), Pt("Amber Fort", 26.9855, 75.8513), Pt("Sambhar Lake", 26.9100, 75.1900), Pt("Pushkar Lake", 26.4880, 74.5510), "VIJP"])])
add("AS", "java", ID, ("Java: temples and volcanoes", "Jáva: templomok és vulkánok"), ("Borobudur", "Borobudur", -7.6079, 110.2038), ["culture", "unesco", "volcano"],
    ("The world's largest Buddhist temple, the towers of Prambanan and the smoking cone of Mount Merapi around Yogyakarta.", "A világ legnagyobb buddhista temploma, Prambanan tornyai és a füstölgő Merapi kúpja Yogyakarta körül."), [],
    [("short", "loop", 100, 4500, ("Yogyakarta temples", "Yogyakartai templomok"), ("Prambanan, Mount Merapi and Borobudur in one short loop.", "Prambanan, a Merapi és Borobudur egyetlen rövid körben."),
      ["WARJ", Pt("Prambanan", -7.7520, 110.4915), Pt("Mount Merapi", -7.5407, 110.4457), Pt("Borobudur", -7.6079, 110.2038), "WARJ"]),
     ("long", "loop", 105, 6000, ("Merapi and the Dieng Plateau", "Merapi és a Dieng-fennsík"), ("About an hour and a half: Prambanan, Merapi, the volcanic Dieng Plateau and Borobudur.", "Kb. másfél óra: Prambanan, a Merapi, a vulkanikus Dieng-fennsík és Borobudur."),
      ["WARJ", Pt("Prambanan", -7.7520, 110.4915), Pt("Mount Merapi", -7.5407, 110.4457), Pt("Dieng Plateau", -7.2000, 109.9100), Pt("Borobudur", -7.6079, 110.2038), "WARJ"])])
add("AS", "bhutan", BT, ("Bhutan: Paro and Thimphu", "Bhután: Paro és Thimphu"), ("Tiger's Nest", "Tigrisfészek-kolostor", 27.4916, 89.3636), ["culture", "mountain"],
    ("A Himalayan kingdom: the Tiger's Nest monastery clinging to a cliff, whitewashed dzongs and 7,000 m peaks.", "Himalájai királyság: a sziklafalra tapadó Tigrisfészek-kolostor, fehérre meszelt dzongok és 7000 méteres csúcsok."), [],
    [("short", "loop", 95, 12000, ("Paro and Thimphu", "Paro és Thimphu"), ("From Paro over the Tiger's Nest and the Tashichho Dzong in Thimphu.", "Paróból a Tigrisfészek-kolostor és a thimphui Tashichho-dzong felett."),
      ["VQPR", Pt("Tiger's Nest", 27.4916, 89.3636), Pt("Tashichho Dzong", 27.4929, 89.6600), "VQPR"]),
     ("long", "loop", 100, 15000, ("Jomolhari and Punakha", "Jomolhari és Punakha"), ("About an hour and a half: Jomolhari, the Punakha Dzong and the Dochula pass.", "Kb. másfél óra: a Jomolhari, a Punakha-dzong és a Dochula-hágó."),
      ["VQPR", Pt("Tiger's Nest", 27.4916, 89.3636), Pt("Jomolhari", 27.8000, 89.2700), Pt("Punakha Dzong", 27.5830, 89.8600), Pt("Dochula Pass", 27.4963, 89.7450), Pt("Tashichho Dzong", 27.4929, 89.6600), "VQPR"])])
add("AS", "sri-lanka", LK, ("Sri Lanka: Sigiriya and Kandy", "Srí Lanka: Sigiriya és Kandy"), ("Sigiriya", "Sigiriya", 7.9570, 80.7599), ["culture", "unesco", "mountain"],
    ("The Lion Rock fortress, the cave temples of Dambulla and the hill capital Kandy among tea hills and jungle.", "Az Oroszlán-szikla erődje, Dambulla barlangtemplomai és a hegyi főváros, Kandy teaültetvények és dzsungel között."), [],
    [("short", "loop", 100, 3500, ("Sigiriya, Dambulla and Kandy", "Sigiriya, Dambulla és Kandy"), ("Lion Rock, the Dambulla cave temples and Kandy's lake.", "Az Oroszlán-szikla, a dambullai barlangtemplomok és Kandy tava."),
      ["VCCS", Pt("Sigiriya", 7.9570, 80.7599), Pt("Dambulla", 7.8570, 80.6490), Pt("Kandy", 7.2936, 80.6413), "VCCS"]),
     ("long", "loop", 105, 6000, ("Sri Lanka's hill country", "Srí Lanka hegyvidéke"), ("About an hour and a half: Kandy, Adam's Peak, Horton Plains and the Knuckles Range.", "Kb. másfél óra: Kandy, az Ádám-csúcs, a Horton-fennsík és a Knuckles-hegység."),
      ["VCCS", Pt("Sigiriya", 7.9570, 80.7599), Pt("Dambulla", 7.8570, 80.6490), Pt("Kandy", 7.2936, 80.6413), Pt("Adam's Peak", 6.8094, 80.4994), Pt("Horton Plains", 6.8020, 80.8000), Pt("Knuckles Range", 7.4000, 80.8000), "VCCS"])])
# ---------------- Eszak-Amerika ----------------
add("NA", "chicago", US, ("Chicago", "Chicago"), ("Willis Tower", "Willis Tower", 41.8789, -87.6359), ["city", "culture"],
    ("The birthplace of the skyscraper on the shore of Lake Michigan: Willis Tower, Navy Pier and the Loop's canyons of glass.", "A felhőkarcoló szülőhelye a Michigan-tó partján: a Willis Tower, a Navy Pier és a Loop üvegkanyonjai."), [],
    [("short", "loop", 90, 2500, ("Skyline loop", "Látképkör"), ("Over Soldier Field, Millennium Park, Navy Pier, Wrigley Field and Willis Tower.", "A Soldier Field, a Millennium Park, a Navy Pier, a Wrigley Field és a Willis Tower felett."),
      ["KMDW", Pt("Soldier Field", 41.8623, -87.6167), Pt("Millennium Park", 41.8826, -87.6226), Pt("Navy Pier", 41.8917, -87.6019), Pt("Wrigley Field", 41.9484, -87.6553), Pt("Willis Tower", 41.8789, -87.6359), "KMDW"]),
     ("long", "loop", 100, 3000, ("Chicago and the Indiana Dunes", "Chicago és az Indiana-dűnék"), ("About an hour: the lakeshore skyline and the sand dunes of Indiana.", "Kb. egy óra: a tópart látképe és Indiana homokdűnéi."),
      ["KMDW", Pt("Indiana Dunes", 41.6530, -87.0520), Pt("Soldier Field", 41.8623, -87.6167), Pt("Millennium Park", 41.8826, -87.6226), Pt("Navy Pier", 41.8917, -87.6019), Pt("Wrigley Field", 41.9484, -87.6553), Pt("Willis Tower", 41.8789, -87.6359), "KMDW"])])
add("NA", "seattle-rainier", US, ("Seattle and Mount Rainier", "Seattle és a Mount Rainier"), ("Mount Rainier", "Mount Rainier", 46.8523, -121.7603), ["city", "mountain", "volcano"],
    ("The Space Needle, Puget Sound and the glaciated volcano Mount Rainier towering over the Pacific Northwest.", "A Space Needle, a Puget-öböl és a gleccserekkel borított Mount Rainier vulkán a Csendes-óceán északnyugati partvidéke felett."), [],
    [("short", "loop", 100, 3500, ("Seattle and Snoqualmie", "Seattle és Snoqualmie"), ("Over the Space Needle, Lake Washington and Snoqualmie Falls.", "A Space Needle, a Washington-tó és a Snoqualmie-vízesés felett."),
      ["KBFI", Pt("Space Needle", 47.6205, -122.3493), Pt("Bellevue", 47.6101, -122.2015), Pt("Snoqualmie Falls", 47.5414, -121.8375), "KBFI"]),
     ("long", "loop", 110, 9500, ("Rainier and Mount St. Helens", "Rainier és a Mount St. Helens"), ("About an hour and three quarters: Seattle, Mount Rainier and the crater of Mount St. Helens.", "Kb. másfél-két óra: Seattle, a Mount Rainier és a Mount St. Helens krátere."),
      ["KBFI", Pt("Space Needle", 47.6205, -122.3493), Pt("Snoqualmie Falls", 47.5414, -121.8375), Pt("Mount Rainier", 46.8523, -121.7603), Pt("Mount St. Helens", 46.1912, -122.1944), "KBFI"])])
add("NA", "zion-bryce", US, ("Zion and Bryce Canyon", "Zion és Bryce Canyon"), ("Bryce Canyon", "Bryce Canyon", 37.5930, -112.1871), ["mountain", "culture"],
    ("Red rock country: the sheer walls of Zion Canyon, the hoodoos of Bryce Canyon and the alpine rim of Cedar Breaks.", "A vörös sziklák földje: a Zion-kanyon függőleges falai, a Bryce Canyon kőtornyai és a Cedar Breaks alpesi pereme."), [],
    [("short", "loop", 110, 9500, ("Zion and Kolob", "Zion és Kolob"), ("From St. George over Kolob Canyons and Angels Landing in Zion.", "St. Georgeból a Kolob-kanyonok és a Zion Angels Landing felett."),
      ["KSGU", Pt("Kolob Canyons", 37.4600, -113.2200), Pt("Angels Landing", 37.2690, -112.9470), "KSGU"]),
     ("long", "loop", 115, 11500, ("Zion, Bryce and Cedar Breaks", "Zion, Bryce és Cedar Breaks"), ("About an hour and a half: Zion, the Bryce Canyon amphitheatre and Cedar Breaks.", "Kb. másfél óra: a Zion, a Bryce Canyon amfiteátruma és a Cedar Breaks."),
      ["KSGU", Pt("Angels Landing", 37.2690, -112.9470), Pt("Bryce Canyon", 37.5930, -112.1871), Pt("Cedar Breaks", 37.6410, -112.8400), Pt("Kolob Canyons", 37.4600, -113.2200), "KSGU"])])
add("NA", "mexico-city", MX, ("Mexico City and Teotihuacan", "Mexikóváros és Teotihuacán"), ("Pyramid of the Sun", "Nap-piramis", 19.6925, -98.8438), ["city", "culture", "unesco", "volcano"],
    ("The sprawling capital on a drained lake, the pyramids of Teotihuacan and the snow-capped cone of Popocatépetl.", "A leszárított tó helyén fekvő hatalmas főváros, Teotihuacán piramisai és a Popocatépetl hósipkás kúpja."), [],
    [("short", "loop", 90, 10000, ("City centre", "Belváros"), ("The Zócalo, Chapultepec Castle, Estadio Azteca and the canals of Xochimilco.", "A Zócalo, a Chapultepec-kastély, az Estadio Azteca és Xochimilco csatornái."),
      ["MMMX", Pt("Zócalo", 19.4326, -99.1332), Pt("Chapultepec Castle", 19.4204, -99.1819), Pt("Estadio Azteca", 19.3029, -99.1505), Pt("Xochimilco", 19.2600, -99.1030), "MMMX"]),
     ("long", "loop", 100, 12500, ("Teotihuacan and Popocatépetl", "Teotihuacán és a Popocatépetl"), ("About an hour and a half: Teotihuacan, the capital and the volcano Popocatépetl.", "Kb. másfél óra: Teotihuacán, a főváros és a Popocatépetl vulkán."),
      ["MMMX", Pt("Pyramid of the Sun", 19.6925, -98.8438), Pt("Zócalo", 19.4326, -99.1332), Pt("Chapultepec Castle", 19.4204, -99.1819), Pt("Estadio Azteca", 19.3029, -99.1505), Pt("Xochimilco", 19.2600, -99.1030), Pt("Popocatépetl", 19.0225, -98.6278), "MMMX"])])
# ---------------- Del-Amerika ----------------
add("SA", "nazca", PE, ("Nazca Lines", "Nazca-vonalak"), ("Hummingbird geoglyph", "Kolibri-geoglifa", -14.6917, -75.1458), ["culture", "unesco"],
    ("Giant figures scratched into the desert 2,000 years ago: the hummingbird, the monkey and the spider, best seen from the air.", "2000 éve a sivatagba karcolt óriási alakzatok: a kolibri, a majom és a pók, legjobban a levegőből látszanak."), [],
    [("long", "loop", 95, 2000, ("Nazca and Palpa", "Nazca és Palpa"), ("About an hour: Chauchilla cemetery, Cahuachi, the Nazca lines and the Palpa geoglyphs.", "Kb. egy óra: a Chauchilla-temető, Cahuachi, a Nazca-vonalak és a palpai geoglifák."),
      ["SPZA", Pt("Chauchilla Cemetery", -14.9750, -75.0980), Pt("Cahuachi", -14.8183, -75.1156), Pt("Hummingbird geoglyph", -14.6917, -75.1458), Pt("Palpa geoglyphs", -14.5500, -75.1830), "SPZA"])])
add("SA", "uyuni", BO, ("Salar de Uyuni", "Uyuni sósivatag"), ("Salar de Uyuni", "Uyuni sósivatag", -20.1338, -67.4891), ["culture", "volcano"],
    ("The world's largest salt flat: a mirror of white crust stretching to the horizon, with cactus islands and volcanoes.", "A világ legnagyobb sósivataga: a horizontig nyúló fehér tükör kaktuszszigetekkel és vulkánokkal."), [],
    [("short", "loop", 110, 14000, ("Salt flat loop", "Sósivatag-kör"), ("The train cemetery, Incahuasi Island, the salt flat and the Tunupa volcano.", "A vonattemető, az Incahuasi-sziget, a sósivatag és a Tunupa vulkán."),
      ["SLUY", Pt("Train Cemetery", -20.4753, -66.8225), Pt("Isla Incahuasi", -20.2410, -67.6250), Pt("Salar de Uyuni", -20.1338, -67.4891), Pt("Tunupa Volcano", -19.8333, -67.6167), "SLUY"]),
     ("long", "loop", 120, 16000, ("Salar and Laguna Colorada", "Sósivatag és a Laguna Colorada"), ("A long flight south: Incahuasi, Ollagüe volcano and the red lagoon of Laguna Colorada.", "Hosszú repülés délre: Incahuasi, az Ollagüe vulkán és a vörös Laguna Colorada."),
      ["SLUY", Pt("Isla Incahuasi", -20.2410, -67.6250), Pt("Ollagüe Volcano", -21.3000, -68.1800), Pt("Laguna Colorada", -22.2000, -67.7800), "SLUY"])])
add("SA", "angel-falls", VE, ("Angel Falls", "Angel-vízesés"), ("Angel Falls", "Angel-vízesés", 5.9701, -62.5362), ["culture", "unesco", "jungle"],
    ("The tallest waterfall on Earth, 979 m, plunging off the flat-topped Auyán-tepui in the Venezuelan jungle.", "A Föld legmagasabb vízesése, 979 méter, a venezuelai dzsungel lapostetejű Auyán-tepuijáról zuhan alá."), [],
    [("loop", "loop", 100, 7000, ("Canaima and Angel Falls", "Canaima és az Angel-vízesés"), ("From Canaima Lagoon to Angel Falls and around the Auyán-tepui.", "A Canaima-lagúnától az Angel-vízeséshez és az Auyán-tepui körül."),
      ["SVCN", Pt("Angel Falls", 5.9701, -62.5362), Pt("Auyán-tepui", 5.7800, -62.5400), "SVCN"])])
add("SA", "manaus", BR, ("Manaus and the Amazon", "Manaus és az Amazonas"), ("Meeting of Waters", "Vizek találkozása", -3.1380, -59.9040), ["city", "jungle"],
    ("The Amazon's jungle capital: the opera house in the rainforest, the Rio Negro bridge and the dark and sandy rivers that refuse to mix.", "Az Amazonas dzsungelfővárosa: operaház az esőerdőben, a Rio Negro-híd és a két folyó, amely nem akar összekeveredni."), [],
    [("short", "loop", 85, 2500, ("Meeting of Waters", "A vizek találkozása"), ("Over the Teatro Amazonas, the Meeting of Waters and the Rio Negro bridge.", "Az Amazonas-színház, a vizek találkozása és a Rio Negro-híd felett."),
      ["SBEG", Pt("Teatro Amazonas", -3.1303, -60.0233), Pt("Meeting of Waters", -3.1380, -59.9040), Pt("Rio Negro Bridge", -3.0880, -60.0180), "SBEG"]),
     ("long", "loop", 100, 3000, ("Anavilhanas and Presidente Figueiredo", "Anavilhanas és Presidente Figueiredo"), ("About an hour: Manaus, the river islands of Anavilhanas and the waterfalls of Presidente Figueiredo.", "Kb. egy óra: Manaus, az Anavilhanas folyami szigetei és Presidente Figueiredo vízesései."),
      ["SBEG", Pt("Teatro Amazonas", -3.1303, -60.0233), Pt("Meeting of Waters", -3.1380, -59.9040), Pt("Rio Negro Bridge", -3.0880, -60.0180), Pt("Anavilhanas", -2.7000, -60.7500), Pt("Presidente Figueiredo", -2.0300, -60.0250), "SBEG"])])
# ---------------- Afrika ----------------
add("AF", "serengeti-mara", TZ, ("Serengeti and the Mara", "Serengeti és a Mara"), ("Serengeti", "Serengeti", -2.4580, 34.8225), ["culture", "unesco"],
    ("Endless savanna and the Great Migration: wildebeest, zebras and lions on the plains of the Serengeti.", "Végtelen szavanna és a Nagy Vándorlás: gnúk, zebrák és oroszlánok a Serengeti síkságain."), [],
    [("short", "loop", 100, 2500, ("Serengeti kopjes", "Serengeti sziklaszigetei"), ("From Seronera over the Moru and Gol kopjes.", "Seroneráról a Moru- és Gol-sziklaszigetek felett."),
      ["HTSN", Pt("Moru Kopjes", -2.7000, 34.7500), Pt("Gol Kopjes", -2.6500, 35.2000), "HTSN"]),
     ("long", "loop", 105, 3000, ("Mara River and Grumeti", "Mara-folyó és Grumeti"), ("About an hour and a half: the Lobo Valley, the Mara River crossings and the Grumeti River.", "Kb. másfél óra: a Lobo-völgy, a Mara-folyó átkelői és a Grumeti-folyó."),
      ["HTSN", Pt("Lobo Valley", -1.8500, 35.0000), Pt("Mara River crossing", -1.6500, 34.9500), Pt("Grumeti River", -2.1500, 34.2500), "HTSN"])])
add("AF", "mauritius", MU, ("Mauritius", "Mauritius"), ("Le Morne Brabant", "Le Morne Brabant", -20.4520, 57.3130), ["island", "coast", "unesco", "volcano"],
    ("Turquoise lagoons, the UNESCO rock of Le Morne and the coloured earths of Chamarel on a volcanic island.", "Türkizkék lagúnák, a világörökségi Le Morne-szikla és Chamarel színes földjei egy vulkanikus szigeten."), [],
    [("long", "loop", 105, 3000, ("Mauritius from coast to coast", "Mauritius partról partra"), ("About an hour: the lagoons, Port Louis, Chamarel and the Le Morne peninsula.", "Kb. egy óra: a lagúnák, Port Louis, Chamarel és a Le Morne-félsziget."),
      ["FIMP", Pt("Île aux Cerfs", -20.2700, 57.8060), Pt("Pieter Both", -20.1750, 57.5900), Pt("Port Louis", -20.1609, 57.5012), Pt("Chamarel", -20.4400, 57.3800), Pt("Le Morne Brabant", -20.4520, 57.3130), Pt("Blue Bay Marine Park", -20.4440, 57.7120), "FIMP"])])
add("AF", "zanzibar", TZ, ("Zanzibar", "Zanzibár"), ("Stone Town", "Stone Town", -6.1630, 39.1900), ["island", "coast", "unesco"],
    ("Spice island of the Indian Ocean: the winding alleys of Stone Town, white beaches and the Mnemba coral atoll.", "Az Indiai-óceán fűszerszigete: Stone Town szűk sikátorai, fehér strandok és a Mnemba korallatoll."), [],
    [("short", "loop", 95, 2000, ("Stone Town and Jozani", "Stone Town és Jozani"), ("Prison Island, Stone Town, Chumbe Island and Jozani Forest.", "A Prison Island, Stone Town, a Chumbe-sziget és a Jozani-erdő."),
      ["HTZA", Pt("Prison Island", -6.1250, 39.1700), Pt("Stone Town", -6.1630, 39.1900), Pt("Chumbe Island", -6.2800, 39.1650), Pt("Jozani Forest", -6.2500, 39.4200), "HTZA"]),
     ("long", "loop", 100, 2500, ("Zanzibar from north to south", "Zanzibár északtól délig"), ("About an hour: Stone Town, Nungwi, Mnemba Atoll and the Paje coast.", "Kb. egy óra: Stone Town, Nungwi, a Mnemba-atoll és a Paje-part."),
      ["HTZA", Pt("Stone Town", -6.1630, 39.1900), Pt("Nungwi", -5.7260, 39.2970), Pt("Mnemba Atoll", -5.8200, 39.3800), Pt("Paje Beach", -6.2700, 39.5300), "HTZA"])])
add("AF", "sahara-merzouga", MA, ("Sahara: Erg Chebbi", "Szahara: Erg Chebbi"), ("Erg Chebbi", "Erg Chebbi", 31.1500, -3.9700), ["culture"],
    ("Orange dunes up to 150 m high at the edge of the Sahara, with the palm oases and kasbahs of southern Morocco.", "Akár 150 méter magas narancsszínű dűnék a Szahara szélén, pálmaligetekkel és kasbákkal Dél-Marokkóban."), [],
    [("loop", "loop", 125, 7000, ("Dunes and gorges", "Dűnék és szurdokok"), ("From Errachidia over the Erg Chebbi dunes and the Todra Gorge.", "Errachidiából az Erg Chebbi dűnéi és a Todra-szurdok felett."),
      ["GMFK", Pt("Erg Chebbi", 31.1500, -3.9700), Pt("Todra Gorge", 31.5800, -5.5700), "GMFK"])])
# ---------------- Oceania ----------------
add("OC", "auckland", NZ, ("Auckland and the Hauraki Gulf", "Auckland és a Hauraki-öböl"), ("Sky Tower", "Sky Tower", -36.8485, 174.7633), ["city", "island", "coast", "volcano"],
    ("The City of Sails: the Sky Tower, the volcanic cone of Rangitoto and the islands of the Hauraki Gulf.", "A Vitorlások Városa: a Sky Tower, a Rangitoto vulkáni kúpja és a Hauraki-öböl szigetei."), [],
    [("short", "loop", 100, 2500, ("Auckland and Waiheke", "Auckland és Waiheke"), ("Over the Sky Tower, Rangitoto Island and Waiheke Island.", "A Sky Tower, a Rangitoto-sziget és a Waiheke-sziget felett."),
      ["NZAA", Pt("Sky Tower", -36.8485, 174.7633), Pt("Rangitoto Island", -36.7900, 174.8600), Pt("Waiheke Island", -36.8000, 175.1000), "NZAA"]),
     ("long", "loop", 105, 3000, ("Auckland and Hobbiton", "Auckland és Hobbiton"), ("About an hour and a half: Piha beach, the city, the gulf islands and the Hobbiton movie set.", "Kb. másfél óra: a Piha-part, a város, az öböl szigetei és a Hobbiton filmes díszlet."),
      ["NZAA", Pt("Piha Beach", -36.9540, 174.4690), Pt("Sky Tower", -36.8485, 174.7633), Pt("Rangitoto Island", -36.7900, 174.8600), Pt("Waiheke Island", -36.8000, 175.1000), Pt("Hobbiton", -37.8722, 175.6830), "NZAA"])])
add("OC", "queenstown", NZ, ("Queenstown, Wanaka and the glaciers", "Queenstown, Wanaka és a gleccserek"), ("Mount Aspiring", "Mount Aspiring", -44.3850, 168.7280), ["mountain", "coast"],
    ("Alpine lakes, the pyramid of Mount Aspiring and glaciers flowing almost to the rainforest of the West Coast.", "Alpesi tavak, a Mount Aspiring piramisa és az esőerdőig leereszkedő nyugati-parti gleccserek."), [],
    [("short", "loop", 100, 8000, ("Wanaka and Mount Aspiring", "Wanaka és a Mount Aspiring"), ("From Queenstown over Lake Wanaka and Mount Aspiring.", "Queenstownból a Wanaka-tó és a Mount Aspiring felett."),
      ["NZQN", Pt("Lake Wanaka", -44.5500, 169.1000), Pt("Mount Aspiring", -44.3850, 168.7280), "NZQN"]),
     ("long", "loop", 110, 11000, ("Franz Josef and Fox Glacier", "Franz Josef- és Fox-gleccser"), ("About two hours: Wanaka, Mount Aspiring and the Fox and Franz Josef glaciers.", "Kb. két óra: Wanaka, a Mount Aspiring, valamint a Fox- és a Franz Josef-gleccser."),
      ["NZQN", Pt("Lake Wanaka", -44.5500, 169.1000), Pt("Mount Aspiring", -44.3850, 168.7280), Pt("Fox Glacier", -43.5000, 170.0200), Pt("Franz Josef Glacier", -43.4670, 170.1850), "NZQN"])])

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
open(os.path.join(os.path.dirname(P), "..", "tools", "r4_ids.txt"), "w").write(" ".join(NEW))
print(len(NEW), "uj tura")
