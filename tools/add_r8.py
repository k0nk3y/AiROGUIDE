#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""8. kor: surusites Europa/Azsia/Eszak-Amerika/Afrika/Del-Amerika/Oceania. Sorrend: add_r8 -> tours_order <r8_ids> -> poi_registry -> tours_kw -> tours_img -> tours_check"""
from tourlib import *
import json, os
C = lambda e, h: (e, h)
DE = C("Germany", "Németország"); FR = C("France", "Franciaország"); ES = C("Spain", "Spanyolország"); PT = C("Portugal", "Portugália"); PL = C("Poland", "Lengyelország"); RS = C("Serbia", "Szerbia")
KR = C("South Korea", "Dél-Korea"); PH = C("Philippines", "Fülöp-szigetek"); MY = C("Malaysia", "Malajzia"); TH = C("Thailand", "Thaiföld"); OM = C("Oman", "Omán"); TR = C("Turkey", "Törökország")
US = C("United States", "Egyesült Államok"); CA = C("Canada", "Kanada"); UG = C("Uganda", "Uganda"); NA_ = C("Namibia", "Namíbia"); MA = C("Morocco", "Marokkó"); KE = C("Kenya", "Kenya")
BR = C("Brazil", "Brazília"); EC = C("Ecuador", "Ecuador"); AR = C("Argentina", "Argentína"); NZ = C("New Zealand", "Új-Zéland"); AU = C("Australia", "Ausztrália")
CONT = {}


def add(cont, *a):
    a = list(a)
    a.insert(6, [])
    tour(*a); CONT[a[0]] = cont


def Pt(n, la, lo): return [n, la, lo]


# ---------------- Europa
add("EU", "hamburg-lubeck", DE, ("Hamburg, Lübeck and the Kiel Canal", "Hamburg, Lübeck és a Kieli-csatorna"), ("Elbphilharmonie", "Elbphilharmonie", 53.5413, 9.9841), ["city", "coast", "unesco"],
    ("Europe's third-largest port, the brick Gothic Holstentor of Lübeck, the Baltic fjord of Kiel and the High Bridge over the world's busiest artificial waterway.", "Európa harmadik legnagyobb kikötője, Lübeck téglagótikus Holstentorja, a kieli Balti-tengeri fjord és a világ legforgalmasabb mesterséges vízi útja feletti magas híd."),
    [("long", "loop", 110, 3000, ("Hanseatic loop", "Hanza-kör"), ("Lübeck, Laboe, Rendsburg, Brunsbüttel and the Hamburg harbour.", "Lübeck, Laboe, Rendsburg, Brunsbüttel és a hamburgi kikötő."),
      ["EDDH", Pt("Holstentor", 53.8667, 10.6844), Pt("Laboe Naval Memorial", 54.4040, 10.2260), Pt("Rendsburg High Bridge", 54.3000, 9.6650), Pt("Brunsbüttel Locks", 53.9120, 9.1450), Pt("Elbphilharmonie", 53.5413, 9.9841), "EDDH"])])
add("EU", "black-forest", DE, ("Black Forest and Strasbourg", "Fekete-erdő és Strasbourg"), ("Triberg Waterfalls", "Triberg-vízesés", 48.1300, 8.2300), ["mountain", "culture"],
    ("Dark fir-covered ridges, the highest waterfalls in Germany at Triberg, Lake Titisee, the Feldberg and the red Gothic cathedral of Strasbourg.", "Sötét fenyves gerincek, Németország legmagasabb vízesései Tribergben, a Titisee, a Feldberg és Strasbourg vörös gótikus katedrálisa."),
    [("long", "loop", 110, 5000, ("Schwarzwald loop", "Schwarzwald-kör"), ("Triberg, Lake Titisee, the Feldberg, Freiburg and Strasbourg.", "Triberg, a Titisee, a Feldberg, Freiburg és Strasbourg."),
      ["EDSB", Pt("Triberg Waterfalls", 48.1300, 8.2300), Pt("Lake Titisee", 47.9000, 8.1500), Pt("Feldberg", 47.8740, 8.0040), Pt("Freiburg", 47.9960, 7.8530), Pt("Strasbourg Cathedral", 48.5819, 7.7507), "EDSB"])])
add("EU", "bordeaux", FR, ("Bordeaux and the Arcachon Bay", "Bordeaux és az Arcachon-öböl"), ("Dune du Pilat", "Dune du Pilat", 44.5900, -1.2130), ["coast", "culture", "unesco"],
    ("Europe's tallest sand dune, the oyster bay of Cap Ferret, the wine villages of Saint-Émilion and the stone bridge over the Garonne.", "Európa legmagasabb homokdűnéje, Cap Ferret osztrigás öble, Saint-Émilion borfalvai és a Garonne feletti kőhíd."),
    [("loop", "loop", 100, 3000, ("Dune and vineyards", "Dűne és szőlők"), ("Cap Ferret, the Dune du Pilat, Saint-Émilion and Bordeaux.", "Cap Ferret, a Dune du Pilat, Saint-Émilion és Bordeaux."),
      ["LFBD", Pt("Cap Ferret", 44.6400, -1.2500), Pt("Dune du Pilat", 44.5900, -1.2130), Pt("Saint-Émilion", 44.8940, -0.1550), Pt("Bordeaux Pont de Pierre", 44.8370, -0.5600), "LFBD"])])
add("EU", "corsica", FR, ("Corsica", "Korzika"), ("Scandola", "Scandola", 42.3790, 8.5500), ["island", "mountain", "coast", "unesco"],
    ("The island of beauty: the finger of Cap Corse, the citadel of Calvi, the red cliffs of Scandola and the 2,700-metre peaks of Monte Cinto.", "A szépség szigete: a Cap Corse ujja, Calvi fellegvára, Scandola vörös sziklái és a Monte Cinto 2700 méteres csúcsai."),
    [("long", "loop", 110, 7000, ("Island of beauty", "A szépség szigete"), ("Cap Corse, Saint-Florent, Calvi, Scandola and Monte Cinto.", "Cap Corse, Saint-Florent, Calvi, Scandola és a Monte Cinto."),
      ["LFKB", Pt("Cap Corse", 43.0000, 9.3800), Pt("Saint-Florent", 42.6800, 9.3000), Pt("Calvi", 42.5670, 8.7570), Pt("Scandola", 42.3790, 8.5500), Pt("Monte Cinto", 42.3830, 8.9500), "LFKB"])])
add("EU", "basque-coast", ES, ("Basque Coast", "Baszk tengerpart"), ("Gaztelugatxe", "Gaztelugatxe", 43.4470, -2.7850), ["coast", "culture"],
    ("The titanium Guggenheim of Bilbao, the islet of Gaztelugatxe, the shell-shaped bay of San Sebastián and Biarritz across the border.", "Bilbao titánium Guggenheimja, a Gaztelugatxe-szigetke, San Sebastián kagyló alakú öble és a határ túloldalán Biarritz."),
    [("loop", "loop", 100, 3000, ("Bay of Biscay loop", "Vizcayai-öböl kör"), ("Gaztelugatxe, San Sebastián, Biarritz, La Rhune and Bilbao.", "Gaztelugatxe, San Sebastián, Biarritz, La Rhune és Bilbao."),
      ["LEBB", Pt("Gaztelugatxe", 43.4470, -2.7850), Pt("San Sebastián", 43.3180, -1.9860), Pt("Biarritz", 43.4920, -1.5610), Pt("La Rhune", 43.3100, -1.6370), Pt("Guggenheim Bilbao", 43.2687, -2.9340), "LEBB"])])
add("EU", "costa-brava", ES, ("Costa Brava", "Costa Brava"), ("Cap de Creus", "Cap de Creus", 42.3190, 3.3160), ["coast", "culture"],
    ("Rugged rocky coves, Dalí's Cadaqués, the Medes Islands and the walled seaside town of Tossa de Mar.", "Zord sziklás öblök, Dalí Cadaqués-e, a Medes-szigetek és a várfallal övezett Tossa de Mar."),
    [("loop", "loop", 100, 3000, ("Wild Coast", "A vad part"), ("Tossa de Mar, the Medes Islands, Cadaqués, Cap de Creus and Girona.", "Tossa de Mar, a Medes-szigetek, Cadaqués, Cap de Creus és Girona."),
      ["LEGE", Pt("Tossa de Mar", 41.7190, 2.9310), Pt("Medes Islands", 42.0490, 3.2250), Pt("Cadaqués", 42.2890, 3.2770), Pt("Cap de Creus", 42.3190, 3.3160), Pt("Girona", 41.9794, 2.8214), "LEGE"])])
add("EU", "douro", PT, ("Porto and the Douro Valley", "Porto és a Douro-völgy"), ("Pinhão", "Pinhão", 41.1900, -7.5450), ["culture", "unesco"],
    ("The terraced vineyards of the oldest demarcated wine region in the world, Guimarães, birthplace of Portugal, and Braga's pilgrim stairway.", "A világ legrégebbi védett borvidékének teraszos szőlői, Guimarães, Portugália bölcsője és Braga zarándoklépcsője."),
    [("long", "loop", 100, 4000, ("Douro loop", "Douro-kör"), ("Régua, Pinhão, Guimarães, Braga and the Porto riverfront.", "Régua, Pinhão, Guimarães, Braga és a portói folyópart."),
      ["LPPR", Pt("Régua", 41.1650, -7.7880), Pt("Pinhão", 41.1900, -7.5450), Pt("Guimarães", 41.4440, -8.2960), Pt("Bom Jesus do Monte", 41.5550, -8.3770), Pt("Ribeira Porto", 41.1405, -8.6111), "LPPR"])])
add("EU", "gdansk", PL, ("Gdańsk and the Hel Peninsula", "Gdańsk és a Hel-félsziget"), ("Gdańsk Old Town", "Gdańsk óvárosa", 54.3520, 18.6560), ["city", "coast", "culture"],
    ("The Hanseatic port with its colourful Long Market, the red brick castle of the Teutonic Knights in Malbork and a 35 km sand spit into the Baltic.", "A hanza-kikötő színes Hosszú Piaccal, a Német Lovagrend vörös téglás vára Malborkban és egy 35 km-es homokzátony a Balti-tengerbe."),
    [("loop", "loop", 100, 3000, ("Baltic loop", "Balti-tengeri kör"), ("Malbork Castle, Gdańsk, Westerplatte, the Hel Peninsula and Sopot.", "A malborki vár, Gdańsk, Westerplatte, a Hel-félsziget és Sopot."),
      ["EPGD", Pt("Malbork Castle", 54.0390, 19.0290), Pt("Gdańsk Old Town", 54.3520, 18.6560), Pt("Westerplatte", 54.4060, 18.6680), Pt("Hel", 54.6000, 18.8000), Pt("Sopot Pier", 54.4470, 18.5710), "EPGD"])])
add("EU", "belgrade-novi-sad", RS, ("Belgrade and Novi Sad", "Belgrád és Újvidék"), ("Kalemegdan Fortress", "Kalemegdan-erőd", 44.8225, 20.4500), ["city", "culture"],
    ("The confluence of the Sava and the Danube under the Kalemegdan fortress, the Petrovaradin Fortress above Novi Sad and the monasteries of Fruška Gora.", "A Száva és a Duna összefolyása a Kalemegdan-erőd alatt, a péterváradi erőd Újvidék felett és a Fruška Gora kolostorai."),
    [("loop", "loop", 100, 3000, ("Danube loop", "Duna-kör"), ("Petrovaradin, Fruška Gora, Belgrade, Smederevo and Avala.", "Péterváradi erőd, Fruška Gora, Belgrád, Szendrő és Avala."),
      ["LYBE", Pt("Petrovaradin Fortress", 45.2530, 19.8680), Pt("Fruška Gora", 45.1500, 19.7200), Pt("Kalemegdan Fortress", 44.8225, 20.4500), Pt("Smederevo Fortress", 44.6640, 20.9290), Pt("Avala Tower", 44.6900, 20.5150), "LYBE"])])
# ---------------- Azsia
add("AS", "seoul", KR, ("Seoul", "Szöul"), ("Gyeongbokgung Palace", "Kjongbokkung-palota", 37.5796, 126.9770), ["city", "mountain", "culture"],
    ("The royal palace under Bukhansan's granite peaks, the Namsan tower, the Han River with its 30 bridges and the Incheon Bridge across the bay.", "A királyi palota a Bukhan gránitcsúcsai alatt, a Namszan-torony, a harminc hídjával átszelt Han-folyó és az incshoni híd az öböl felett."),
    [("loop", "loop", 100, 3000, ("Capital loop", "Fővárosi kör"), ("Bukhansan, Gyeongbokgung, N Seoul Tower, Lotte World Tower and the Incheon Bridge.", "Bukhansan, Kjongbokkung, az N Seoul Tower, a Lotte World Tower és az incshoni híd."),
      ["RKSS", Pt("Gyeongbokgung Palace", 37.5796, 126.9770), Pt("Bukhansan", 37.6600, 126.9770), Pt("Lotte World Tower", 37.5126, 127.1026), Pt("N Seoul Tower", 37.5512, 126.9882), Pt("Incheon Bridge", 37.3880, 126.5920), "RKSS"])])
add("AS", "manila-taal", PH, ("Manila and Taal Volcano", "Manila és a Taal-vulkán"), ("Taal Volcano", "Taal-vulkán", 14.0100, 120.9930), ["volcano", "city", "island"],
    ("A volcano island inside a lake inside a volcano, the fortress island of Corregidor and the walled city of Intramuros.", "Egy tóban álló vulkánsziget egy vulkánban, Corregidor erődszigete és Intramuros fallal körülvett városa."),
    [("loop", "loop", 100, 3500, ("Manila Bay and Taal", "Manila-öböl és Taal"), ("Intramuros, Corregidor, Taal Volcano and Mount Makiling.", "Intramuros, Corregidor, a Taal-vulkán és a Mount Makiling."),
      ["RPLL", Pt("Intramuros", 14.5900, 120.9750), Pt("Corregidor", 14.3850, 120.5740), Pt("Taal Volcano", 14.0100, 120.9930), Pt("Mount Makiling", 14.1360, 121.1960), "RPLL"])])
add("AS", "kuala-lumpur", MY, ("Kuala Lumpur", "Kuala Lumpur"), ("Petronas Towers", "Petronas-tornyok", 3.1578, 101.7116), ["city", "mountain"],
    ("The twin towers, the Batu Caves with their giant golden statue, the hill resort of Genting and the pink-domed administrative capital Putrajaya.", "Az ikertornyok, a Batu-barlangok óriási aranyszobrukkal, a genting-i hegyi üdülőhely és a rózsaszín kupolás közigazgatási főváros, Putrajaya."),
    [("loop", "loop", 100, 4000, ("Twin Towers loop", "Ikertorony-kör"), ("Putrajaya, the Petronas Towers, the Batu Caves and Genting Highlands.", "Putrajaya, a Petronas-tornyok, a Batu-barlangok és a Genting-fennsík."),
      ["WMKK", Pt("Putrajaya", 2.9264, 101.6964), Pt("Petronas Towers", 3.1578, 101.7116), Pt("Batu Caves", 3.2379, 101.6840), Pt("Genting Highlands", 3.4230, 101.7930), "WMKK"])])
add("AS", "chiang-mai", TH, ("Chiang Mai and Doi Inthanon", "Chiang Mai és a Doi Inthanon"), ("Doi Inthanon", "Doi Inthanon", 18.5880, 98.4870), ["mountain", "culture", "jungle"],
    ("The rose of the north: the highest peak of Thailand, the golden temple on Doi Suthep and the limestone massif of Chiang Dao.", "Az északi rózsa: Thaiföld legmagasabb csúcsa, az aranytemplom a Doi Suthepen és a Chiang Dao mészkőhegysége."),
    [("loop", "loop", 100, 6000, ("Northern Thailand", "Észak-Thaiföld"), ("Doi Inthanon, Doi Suthep and Chiang Dao.", "Doi Inthanon, Doi Suthep és Chiang Dao."),
      ["VTCC", Pt("Doi Inthanon", 18.5880, 98.4870), Pt("Doi Suthep", 18.8050, 98.9220), Pt("Chiang Dao", 19.4000, 98.9200), "VTCC"])])
add("AS", "muscat", OM, ("Muscat and Jebel Akhdar", "Maszkat és a Dzsebel Akhdar"), ("Sultan Qaboos Grand Mosque", "Szultán Kábúsz Nagymecset", 23.5859, 58.3829), ["city", "coast", "mountain", "culture"],
    ("White Omani harbour town on the Gulf of Oman, the Daymaniyat islands, the fort of Nakhal and the 3,000-metre Green Mountain.", "Fehér ománi kikötőváros az Ománi-öbölnél, a Daymaniyat-szigetek, Nakhal erődje és a háromezer méteres Zöld-hegység."),
    [("loop", "loop", 100, 7000, ("Muscat loop", "Maszkat-kör"), ("Muttrah, the Daymaniyat Islands, Nakhal Fort and Jebel Akhdar.", "Muttrah, a Daymaniyat-szigetek, a Nakhal-erőd és a Dzsebel Akhdar."),
      ["OOMS", Pt("Muttrah Corniche", 23.6180, 58.5690), Pt("Daymaniyat Islands", 23.8600, 58.1000), Pt("Nakhal Fort", 23.3910, 57.8310), Pt("Jebel Akhdar", 23.0820, 57.6580), "OOMS"])])
add("AS", "antalya", TR, ("Antalya and the Turquoise Coast", "Antalya és a Türkiz-part"), ("Aspendos", "Aszpendosz", 36.9390, 31.1720), ["coast", "culture", "mountain"],
    ("The Roman theatre of Aspendos, the Old Town harbour of Kaleiçi, Termessos in the Taurus Mountains and the eternal flames of the Chimaera.", "Aszpendosz római színháza, Kaleiçi óvárosi kikötője, Termessos a Taurusz-hegységben és a Khimaira örök lángjai."),
    [("loop", "loop", 100, 5000, ("Turquoise loop", "Türkiz kör"), ("Aspendos, Kaleiçi, Termessos and Olympos.", "Aszpendosz, Kaleiçi, Termessos és Olümposz."),
      ["LTAI", Pt("Aspendos", 36.9390, 31.1720), Pt("Kaleiçi", 36.8850, 30.7040), Pt("Termessos", 37.0000, 30.4660), Pt("Olympos", 36.4000, 30.4720), "LTAI"])])
# ---------------- Eszak-Amerika
add("NA", "boston-cape-cod", US, ("Boston and Cape Cod", "Boston és Cape Cod"), ("Provincetown", "Provincetown", 42.0527, -70.1860), ["coast", "island", "city"],
    ("Colonial Plymouth, the sand hook of Cape Cod, the islands of Nantucket and Martha's Vineyard with the clay cliffs of Gay Head.", "A gyarmati Plymouth, Cape Cod homokkampója, Nantucket és Martha's Vineyard szigetei és Gay Head agyagszirtjei."),
    [("long", "loop", 110, 3000, ("Islands loop", "Szigetek köre"), ("Provincetown, Nantucket, Gay Head and Plymouth.", "Provincetown, Nantucket, Gay Head és Plymouth."),
      ["KBOS", Pt("Provincetown", 42.0527, -70.1860), Pt("Nantucket", 41.2835, -70.0995), Pt("Gay Head Cliffs", 41.3510, -70.8350), Pt("Plymouth Rock", 41.9580, -70.6620), "KBOS"])])
add("NA", "new-orleans", US, ("New Orleans and the Bayous", "New Orleans és a mocsárvidék"), ("French Quarter", "Francia negyed", 29.9584, -90.0644), ["city", "culture"],
    ("A crescent city on the Mississippi, the 38-km Causeway over Lake Pontchartrain and the oak-lined Oak Alley Plantation.", "Félhold alakú város a Mississippin, a 38 km-es híd a Pontchartrain-tó felett és a tölgyfasoros Oak Alley ültetvény."),
    [("loop", "loop", 100, 2500, ("Crescent City loop", "Félhold-város kör"), ("The French Quarter, the Causeway, Mandeville and Oak Alley.", "A Francia negyed, a Causeway-híd, Mandeville és Oak Alley."),
      ["KMSY", Pt("French Quarter", 29.9584, -90.0644), Pt("Lake Pontchartrain Causeway", 30.1900, -90.1200), Pt("Mandeville", 30.3580, -90.0650), Pt("Oak Alley Plantation", 30.0070, -90.7770), "KMSY"])])
add("NA", "san-diego", US, ("San Diego", "San Diego"), ("La Jolla Cove", "La Jolla-öböl", 32.8500, -117.2730), ["city", "coast", "mountain"],
    ("The Coronado Bridge over the harbour, Cabrillo Point, the sea cliffs of La Jolla and Torrey Pines and the pine forests of the Cuyamaca mountains.", "A Coronado-híd a kikötő felett, Cabrillo-fok, La Jolla és Torrey Pines tengeri sziklái és a Cuyamaca-hegység fenyvesei."),
    [("loop", "loop", 100, 3500, ("Harbour and cliffs", "Kikötő és sziklák"), ("Point Loma, La Jolla, Torrey Pines, Cuyamaca Peak and the Coronado Bridge.", "Point Loma, La Jolla, Torrey Pines, a Cuyamaca-csúcs és a Coronado-híd."),
      ["KSAN", Pt("Cabrillo Point", 32.6700, -117.2410), Pt("La Jolla Cove", 32.8500, -117.2730), Pt("Torrey Pines", 32.9190, -117.2540), Pt("Cuyamaca Peak", 32.9420, -116.5800), Pt("Coronado Bridge", 32.6880, -117.1480), "KSAN"])])
add("NA", "denver-rockies", US, ("Denver and the Colorado Rockies", "Denver és a Colorádói-Sziklás-hegység"), ("Pikes Peak", "Pikes Peak", 38.8410, -105.0420), ["mountain", "city"],
    ("Fourteeners along the Front Range: Longs Peak, Mount Evans, Pikes Peak that inspired America the Beautiful and the red rocks of the Garden of the Gods.", "Tizennégyezresek a Front Range mentén: a Longs Peak, a Mount Evans, az America the Beautiful dalt ihlető Pikes Peak és a Garden of the Gods vörös sziklái."),
    [("long", "loop", 110, 15000, ("Front Range", "Front Range"), ("Longs Peak, Mount Evans, Pikes Peak and the Garden of the Gods.", "A Longs Peak, a Mount Evans, a Pikes Peak és a Garden of the Gods."),
      ["KDEN", Pt("Longs Peak", 40.2550, -105.6150), Pt("Mount Evans", 39.5880, -105.6440), Pt("Pikes Peak", 38.8410, -105.0420), Pt("Garden of the Gods", 38.8780, -104.8890), "KDEN"])])
add("NA", "sedona", US, ("Sedona and the Verde Valley", "Sedona és a Verde-völgy"), ("Cathedral Rock", "Cathedral Rock", 34.8200, -111.7900), ["mountain", "culture"],
    ("Red rock buttes and spires, Oak Creek Canyon, the cliff dwellings of Montezuma Castle and the snowy San Francisco Peaks.", "Vörös sziklatornyok, az Oak Creek-kanyon, a Montezuma-kastély sziklalakásai és a havas San Francisco-csúcsok."),
    [("loop", "loop", 100, 9000, ("Red Rock Country", "A vörös sziklák országa"), ("Oak Creek Canyon, Humphreys Peak, Montezuma Castle and Jerome.", "Oak Creek-kanyon, Humphreys Peak, Montezuma-kastély és Jerome."),
      ["KSEZ", Pt("Oak Creek Canyon", 34.9800, -111.7500), Pt("Humphreys Peak", 35.3460, -111.6780), Pt("Montezuma Castle", 34.6120, -111.8400), Pt("Jerome", 34.7490, -112.1140), "KSEZ"])])
add("NA", "quebec", CA, ("Quebec City and the St. Lawrence", "Québec és a Szent Lőrinc-folyó"), ("Château Frontenac", "Château Frontenac", 46.8120, -71.2050), ["city", "culture", "unesco"],
    ("The only walled city north of Mexico, the Montmorency Falls that are taller than Niagara, Île d'Orléans and the basilica of Sainte-Anne-de-Beaupré.", "Mexikótól északra az egyetlen fallal körülvett város, a Niagaránál magasabb Montmorency-vízesés, az Île d'Orléans és a Sainte-Anne-de-Beaupré bazilika."),
    [("loop", "loop", 100, 3000, ("Old Quebec loop", "A régi Québec köre"), ("Montmorency Falls, Château Frontenac, Île d'Orléans and Cap Tourmente.", "A Montmorency-vízesés, a Château Frontenac, az Île d'Orléans és a Cap Tourmente."),
      ["CYQB", Pt("Montmorency Falls", 46.8910, -71.1480), Pt("Château Frontenac", 46.8120, -71.2050), Pt("Île d'Orléans", 46.9000, -70.9000), Pt("Cap Tourmente", 47.0750, -70.7800), "CYQB"])])
# ---------------- Afrika
add("AF", "entebbe-nile", UG, ("Lake Victoria and the Source of the Nile", "A Viktória-tó és a Nílus forrása"), ("Source of the Nile", "A Nílus forrása", 0.4240, 33.2110), ["coast", "island", "city"],
    ("The largest lake of Africa, Kampala's seven hills and Jinja where the Nile starts its 6,650-kilometre journey to the Mediterranean.", "Afrika legnagyobb tava, Kampala hét dombja és Jinja, ahol a Nílus 6650 kilométeres útjára indul a Földközi-tenger felé."),
    [("loop", "loop", 100, 3000, ("Pearl of Africa", "Afrika gyöngye"), ("Kampala, Jinja and the Ngamba Island.", "Kampala, Jinja és a Ngamba-sziget."),
      ["HUEN", Pt("Kampala", 0.3476, 32.5825), Pt("Source of the Nile", 0.4240, 33.2110), Pt("Ngamba Island", 0.1100, 32.6500), "HUEN"])])
add("AF", "swakopmund", NA_, ("Swakopmund and the Namib Coast", "Swakopmund és a Namíb-part"), ("Sandwich Harbour", "Sandwich Harbour", -23.3800, 14.4800), ["coast", "mountain"],
    ("Where the Namib dunes plunge into the Atlantic: Sandwich Harbour, the Moon Landscape of the Swakop valley and the flamingos of Walvis Bay.", "Ahol a Namíb dűnéi az Atlanti-óceánba zuhannak: Sandwich Harbour, a Swakop-völgy holdbéli tája és a Walvis Bay flamingói."),
    [("loop", "loop", 100, 2500, ("Coast and desert", "Part és sivatag"), ("The Moon Landscape, Dune 7, Sandwich Harbour and the Walvis Bay lagoon.", "A Holdbéli táj, a Dune 7, Sandwich Harbour és a Walvis Bay-i lagúna."),
      ["FYSM", Pt("Moon Landscape", -22.6200, 14.9800), Pt("Dune 7", -22.9170, 14.5400), Pt("Sandwich Harbour", -23.3800, 14.4800), Pt("Walvis Bay Lagoon", -22.9500, 14.5000), "FYSM"])])
add("AF", "fes", MA, ("Fes, Meknes and the Middle Atlas", "Fez, Meknes és a Közép-Atlasz"), ("Fes Medina", "Fez medina", 34.0650, -4.9730), ["culture", "unesco", "mountain"],
    ("The largest car-free urban area in the world, the Roman ruins of Volubilis, imperial Meknes and the cedar forests of Ifrane.", "A világ legnagyobb autómentes városi területe, Volubilis római romjai, a császári Meknes és az ifrane-i cédruserdők."),
    [("loop", "loop", 100, 5000, ("Imperial cities", "Császárvárosok"), ("Volubilis, Meknes, Ifrane and Fes Medina.", "Volubilis, Meknes, Ifrane és a fezi medina."),
      ["GMFF", Pt("Volubilis", 34.0720, -5.5540), Pt("Meknes", 33.8950, -5.5550), Pt("Ifrane", 33.5330, -5.1070), Pt("Fes Medina", 34.0650, -4.9730), "GMFF"])])
add("AF", "mombasa-diani", KE, ("Mombasa and Diani Beach", "Mombasa és a Diani-part"), ("Fort Jesus", "Fort Jesus", -4.0620, 39.6790), ["coast", "culture", "jungle"],
    ("A Portuguese fort of the 16th century, the white sand of Diani, the Shimba Hills forest and the coral reefs of Wasini.", "16. századi portugál erőd, Diani fehér homokja, a Shimba-hegyek erdeje és a Wasini korallzátonyai."),
    [("loop", "loop", 100, 2500, ("Swahili coast", "Szuahéli part"), ("Fort Jesus, Diani Beach, Shimba Hills and Wasini.", "Fort Jesus, a Diani-part, a Shimba-hegyek és Wasini."),
      ["HKMO", Pt("Fort Jesus", -4.0620, 39.6790), Pt("Diani Beach", -4.3000, 39.5800), Pt("Wasini Island", -4.6600, 39.3700), Pt("Shimba Hills", -4.2500, 39.4000), "HKMO"])])
# ---------------- Del-Amerika
add("SA", "florianopolis", BR, ("Florianópolis", "Florianópolis"), ("Joaquina Dunes", "Joaquina-dűnék", -27.6300, -48.4500), ["island", "coast", "city"],
    ("The Magic Island of 42 beaches: sand dunes at Joaquina, the lagoon of Conceição and the steel Hercílio Luz Bridge.", "A 42 strandú varázslatos sziget: homokdűnék Joaquinánál, a Conceição-lagúna és a Hercílio Luz acélhíd."),
    [("loop", "loop", 100, 2500, ("Magic Island", "Varázslatos sziget"), ("Campeche Island, the Joaquina Dunes, Lagoa da Conceição, Jurerê and the Hercílio Luz Bridge.", "A Campeche-sziget, a Joaquina-dűnék, Lagoa da Conceição, Jurerê és a Hercílio Luz híd."),
      ["SBFL", Pt("Campeche Island", -27.6870, -48.4700), Pt("Joaquina Dunes", -27.6300, -48.4500), Pt("Lagoa da Conceição", -27.6000, -48.4600), Pt("Jurerê", -27.4380, -48.4930), Pt("Hercílio Luz Bridge", -27.5990, -48.5640), "SBFL"])])
add("SA", "quito-cotopaxi", EC, ("Quito and the Avenue of Volcanoes", "Quito és a Vulkánok sétánya"), ("Cotopaxi", "Cotopaxi", -0.6840, -78.4380), ["volcano", "mountain", "city", "unesco"],
    ("The best-preserved colonial capital at 2,850 m surrounded by glaciated volcanoes: Cayambe on the equator, Antisana, Cotopaxi and Iliniza.", "A legjobban megőrzött gyarmati főváros 2850 méteren, gleccseres vulkánokkal körülvéve: az egyenlítői Cayambe, az Antisana, a Cotopaxi és az Iliniza."),
    [("loop", "loop", 100, 16000, ("Avenue of Volcanoes", "Vulkánok sétánya"), ("Cayambe, Antisana, Cotopaxi, Iliniza and Quito Old Town.", "Cayambe, Antisana, Cotopaxi, Iliniza és Quito óvárosa."),
      ["SEQM", Pt("Cayambe", 0.0300, -77.9860), Pt("Antisana", -0.4800, -78.1400), Pt("Cotopaxi", -0.6840, -78.4380), Pt("Iliniza", -0.6590, -78.7140), Pt("Quito Old Town", -0.2200, -78.5120), "SEQM"])])
add("SA", "salta-humahuaca", AR, ("Salta and the Quebrada de Humahuaca", "Salta és a Humahuaca-szurdok"), ("Purmamarca", "Purmamarca", -23.7440, -65.4930), ["mountain", "culture", "unesco"],
    ("The Hill of Seven Colours, the white salt flats of Salinas Grandes and the rainbow ridge of Hornocal.", "A Hét Szín Dombja, a Salinas Grandes fehér sósivataga és a Hornocal szivárványos gerince."),
    [("loop", "loop", 100, 14000, ("Seven Colours loop", "Hét színű kör"), ("Tilcara, Hornocal, Purmamarca and Salinas Grandes.", "Tilcara, Hornocal, Purmamarca és Salinas Grandes."),
      ["SASA", Pt("Tilcara", -23.5800, -65.4000), Pt("Hornocal", -23.2100, -65.1000), Pt("Purmamarca", -23.7440, -65.4930), Pt("Salinas Grandes", -23.6200, -65.8000), "SASA"])])
# ---------------- Oceania
add("OC", "wellington-marlborough", NZ, ("Wellington and the Marlborough Sounds", "Wellington és a Marlborough Sounds"), ("Marlborough Sounds", "Marlborough Sounds", -41.2900, 174.0050), ["city", "coast", "island"],
    ("The windy capital on its harbour, Kapiti Island and the drowned valleys of the Marlborough Sounds on the far side of Cook Strait.", "A szeles főváros a kikötője partján, a Kapiti-sziget és a Marlborough Sounds elsüllyedt völgyei a Cook-szoros túloldalán."),
    [("loop", "loop", 100, 3500, ("Cook Strait loop", "Cook-szoros kör"), ("Kapiti Island, the Marlborough Sounds at Picton and Mount Victoria.", "A Kapiti-sziget, a Marlborough Sounds Pictonnál és a Mount Victoria."),
      ["NZWN", Pt("Kapiti Island", -40.8500, 174.9200), Pt("Picton", -41.2900, 174.0050), Pt("Mount Victoria", -41.2970, 174.7970), "NZWN"])])
add("OC", "blue-mountains", AU, ("Sydney and the Blue Mountains", "Sydney és a Kék-hegység"), ("Three Sisters", "Három Nővér", -33.7320, 150.3120), ["mountain", "city", "unesco"],
    ("From Sydney Harbour Bridge across the Hawkesbury river to the sandstone cliffs and eucalyptus haze of the Blue Mountains.", "A Sydney Harbour Bridge-től a Hawkesbury folyón át a Kék-hegység homokkő szikláiig és eukaliptuszködéig."),
    [("loop", "loop", 100, 4000, ("Blue Mountains loop", "Kék-hegységi kör"), ("The Harbour Bridge, the Hawkesbury, the Three Sisters, Wentworth Falls and the Royal National Park.", "A Harbour Bridge, a Hawkesbury, a Három Nővér, a Wentworth-vízesés és a Royal National Park."),
      ["YSSY", Pt("Sydney Harbour Bridge", -33.8519, 151.2108), Pt("Hawkesbury River", -33.5500, 151.1930), Pt("Three Sisters", -33.7320, 150.3120), Pt("Wentworth Falls", -33.7140, 150.3720), Pt("Royal National Park", -34.1000, 151.0500), "YSSY"])])
add("OC", "darwin-kakadu", AU, ("Darwin and Kakadu", "Darwin és a Kakadu"), ("Ubirr", "Ubirr", -12.8700, 132.9500), ["jungle", "culture", "unesco"],
    ("Floodplains, wetlands full of crocodiles and birds, the Aboriginal rock art of Ubirr and the 215-metre Jim Jim Falls.", "Elárasztott síkságok, krokodilokkal és madarakkal teli mocsarak, az ubirri őslakos sziklafestészet és a 215 méteres Jim Jim-vízesés."),
    [("long", "loop", 120, 3500, ("Kakadu loop", "Kakadu-kör"), ("Fogg Dam, Ubirr, Jim Jim Falls and Mary River.", "Fogg Dam, Ubirr, a Jim Jim-vízesés és a Mary River."),
      ["YPDN", Pt("Fogg Dam", -12.5700, 131.3000), Pt("Mamukala Wetlands", -12.6900, 132.5400), Pt("Ubirr", -12.8700, 132.9500), Pt("Jim Jim Falls", -13.3000, 132.8300), Pt("Mary River", -12.9500, 131.7000), "YPDN"])])
add("OC", "brisbane-moreton", AU, ("Brisbane and Moreton Bay", "Brisbane és a Moreton-öböl"), ("Moreton Island", "Moreton-sziget", -27.1800, 153.3700), ["city", "island", "coast", "mountain"],
    ("The river city, the great sand island of Moreton with its shipwrecks and the volcanic plugs of the Glass House Mountains.", "A folyóparti város, a Moreton-homoksziget hajóroncsaival és a Glass House-hegység vulkáni dugói."),
    [("loop", "loop", 100, 3000, ("Moreton Bay loop", "Moreton-öböl kör"), ("Tangalooma, the Glass House Mountains, Mount Coot-tha and Point Lookout.", "Tangalooma, a Glass House-hegység, a Mount Coot-tha és Point Lookout."),
      ["YBBN", Pt("Tangalooma", -27.1800, 153.3700), Pt("Glass House Mountains", -26.9050, 152.9540), Pt("Mount Coot-tha", -27.4750, 152.9580), Pt("Point Lookout", -27.4380, 153.5450), "YBBN"])])

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
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "r8_ids.txt"), "w").write(" ".join(NEW))
