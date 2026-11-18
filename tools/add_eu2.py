#!/usr/bin/env python3
"""2. csomag (Europa): Olaszorszag, Ausztria, Nemetorszag, Franciaorszag, Spanyolorszag, Egyesult Kiralysag, Norvegia, Gorogorszag, Horvatorszag, Csehorszag, Svajc."""
from tourlib import tour, save
IT = ("Italy", "Olaszország"); DE = ("Germany", "Németország"); FR = ("France", "Franciaország"); ES = ("Spain", "Spanyolország"); GB = ("United Kingdom", "Egyesült Királyság")

tour("italian-lakes", IT, ("Lake Como and Lake Maggiore", "Comói- és Maggiore-tó"), ("Bellagio", "Bellagio", 45.9855, 9.2605), ["coast", "culture", "city"],
     ("Milan's cathedral, then the Italian lakes: the villas of Lake Como, the Borromean islands on Lake Maggiore and little Lake Orta.", "Milánó dómja, majd az olasz tavak: a Comói-tó villái, a Maggiore-tó Borromei-szigetei és a kis Orta-tó."),
     [["Stresa", 45.8856, 8.5333]],
     [("loop", "loop", 110, 3500, ("Lakes loop", "Tókör"), ("From Linate over Milan Cathedral and Lake Como to Lake Maggiore and Lake Orta, then back.", "Linatéból a milánói dóm és a Comói-tó felett a Maggiore- és az Orta-tóhoz, majd vissza."),
       ["LIML", ["Milan Cathedral", 45.4642, 9.1916], ["Bellagio", 45.9855, 9.2605], ["Villa del Balbianello", 45.9644, 9.2166], ["Isola Bella", 45.9033, 8.5278], ["Isola San Giulio", 45.7973, 8.4143], "LIML"])])
tour("sicily", IT, ("Sicily: Etna to Agrigento", "Szicília: az Etnától Agrigentóig"), ("Mount Etna", "Etna", 37.7510, 14.9934), ["volcano", "culture", "unesco", "coast"],
     ("Europe's most active volcano, the Greek theatre of Taormina, Syracuse and the Temples of Agrigento, ending in Palermo.", "Európa legaktívabb vulkánja, a taorminai görög színház, Szirakúza és az agrigentói templomok, Palermóban végződve."),
     [["Greek Theatre, Syracuse", 37.0764, 15.2790]],
     [("ab", "ab", 125, 6500, ("Catania to Palermo", "Catania – Palermo"), ("A long one-way flight across Sicily. Keep clear of Etna's summit plume.", "Hosszú egyirányú repülés Szicílián át. Az Etna csúcsának füstfelhőjét kerüld."),
       ["LICC", ["Mount Etna", 37.7510, 14.9934], ["Taormina", 37.8524, 15.2926], ["Ortygia, Syracuse", 37.0613, 15.2940], ["Valley of the Temples, Agrigento", 37.2905, 13.5911], ["Palermo Cathedral", 38.1140, 13.3562], "LICJ"])])
tour("vienna-wachau", ("Austria", "Ausztria"), ("Vienna and the Wachau valley", "Bécs és a Wachau-völgy"), ("Schönbrunn Palace", "Schönbrunn", 48.1845, 16.3122), ["city", "culture", "unesco"],
     ("Imperial Vienna from the air, then up the Danube through the vineyards of the Wachau to Melk Abbey.", "A császári Bécs a levegőből, majd a Duna mentén a Wachau szőlői között a melki apátsághoz."),
     [["Hofburg", 48.2065, 16.3656]],
     [("ab", "ab", 110, 3000, ("Vienna to Linz", "Bécs – Linz"), ("One-way along the Danube from Vienna's palaces through the Wachau to Linz.", "Egyirányú repülés a Duna mentén Bécs palotáitól a Wachau-n át Linzig."),
       ["LOWW", ["Schönbrunn Palace", 48.1845, 16.3122], ["St. Stephen's Cathedral", 48.2086, 16.3733], ["Dürnstein", 48.3938, 15.5192], ["Melk Abbey", 48.2278, 15.3306], "LOWL"])])
tour("bavaria", DE, ("Bavarian castles and the Alps", "Bajor kastélyok és az Alpok"), ("Neuschwanstein Castle", "Neuschwansteini kastély", 47.5576, 10.7498), ["mountain", "culture"],
     ("King Ludwig's fairytale castles below the Alps, the Wieskirche and Germany's highest peak, the Zugspitze, ending in Munich.", "Lajos király mesebeli kastélyai az Alpok alatt, a Wieskirche és Németország legmagasabb csúcsa, a Zugspitze, Münchenben végződve."),
     [["Hohenschwangau Castle", 47.5543, 10.7355]],
     [("ab", "ab", 110, 7500, ("Memmingen to Munich", "Memmingen – München"), ("From the Allgäu over Neuschwanstein, Linderhof and the Zugspitze to Munich.", "Az Allgäu felől Neuschwanstein, Linderhof és a Zugspitze felett Münchenbe."),
       ["EDJA", ["Neuschwanstein Castle", 47.5576, 10.7498], ["Wieskirche", 47.6808, 10.9006], ["Linderhof Palace", 47.5714, 10.9606], ["Zugspitze", 47.4211, 10.9863], ["Munich Frauenkirche", 48.1386, 11.5736], "EDDM"])])
tour("rhine", DE, ("Rhine Valley castles", "A Rajna-völgy kastélyai"), ("Loreley", "Loreley", 50.1397, 7.7289), ["culture", "unesco", "city"],
     ("Cologne Cathedral and then the romantic Middle Rhine: Koblenz, Marksburg, the Loreley rock and Rüdesheim, ending at Mainz.", "A kölni dóm, majd a romantikus Közép-Rajna: Koblenz, a Marksburg, a Loreley-szikla és Rüdesheim, Mainzban végződve."),
     [["Rüdesheim am Rhein", 49.9809, 7.9215]],
     [("ab", "ab", 110, 2500, ("Cologne to Frankfurt", "Kölntől Frankfurtig"), ("Follow the Rhine upstream from Cologne to the castle-lined gorge and on to Frankfurt.", "Kövesd a Rajnát felfelé Kölntől a várakkal szegélyezett szorosig, majd Frankfurtig."),
       ["EDDK", ["Cologne Cathedral", 50.9413, 6.9583], ["Deutsches Eck, Koblenz", 50.3639, 7.6061], ["Marksburg", 50.2742, 7.6342], ["Loreley", 50.1397, 7.7289], ["Rüdesheim am Rhein", 49.9809, 7.9215], ["Mainz Cathedral", 50.0005, 8.2735], "EDDF"])])
tour("provence-riviera", FR, ("Provence and the Riviera", "Provence és a Riviéra"), ("Pont du Gard", "Pont du Gard", 43.9475, 4.5352), ["culture", "coast", "unesco"],
     ("Roman aqueducts and papal Avignon, the Verdon gorge, then the glamour of Cannes, Monaco and Nice.", "Római vízvezetékek és a pápai Avignon, a Verdon-szoros, majd Cannes, Monaco és Nizza csillogása."),
     [["Cannes", 43.5513, 7.0128], ["Palais des Papes, Avignon", 43.9508, 4.8075]],
     [("ab", "ab", 120, 4000, ("Marseille to Nice", "Marseille – Nizza"), ("One-way from Marseille over Pont du Gard and Avignon, the Verdon gorge and the Riviera to Nice.", "Egyirányú repülés Marseille-ből a Pont du Gard és Avignon, a Verdon-szoros és a Riviéra felett Nizzába."),
       ["LFML", ["Pont du Gard", 43.9475, 4.5352], ["Palais des Papes, Avignon", 43.9508, 4.8075], ["Gorges du Verdon", 43.7500, 6.3300], ["Cannes", 43.5513, 7.0128], ["Monaco", 43.7384, 7.4246], "LFMN"])])
tour("mont-blanc", FR, ("Mont Blanc and Lake Annecy", "Mont Blanc és az Annecy-tó"), ("Mont Blanc", "Mont Blanc", 45.8326, 6.8652), ["mountain", "coast"],
     ("Lake Annecy and the Alps' highest peak: Chamonix, the Aiguille du Midi and the Mer de Glace. Needs a high-altitude capable aircraft.", "Az Annecy-tó és az Alpok legmagasabb csúcsa: Chamonix, az Aiguille du Midi és a Mer de Glace. Magaslati repülésre alkalmas gép kell hozzá."),
     [["Chamonix", 45.9237, 6.8694]],
     [("loop", "loop", 110, 17000, ("Mont Blanc loop", "Mont Blanc-kör"), ("From Annecy over the lake to Chamonix, around Mont Blanc and back.", "Annecyból a tó felett Chamonix-ba, a Mont Blanc körül, majd vissza."),
       ["LFLP", ["Lake Annecy", 45.8992, 6.1294], ["Chamonix", 45.9237, 6.8694], ["Mont Blanc", 45.8326, 6.8652], ["Aiguille du Midi", 45.8786, 6.8873], ["Mer de Glace", 45.9300, 6.9300], "LFLP"])])
tour("normandy", FR, ("Normandy and Mont-Saint-Michel", "Normandia és a Mont-Saint-Michel"), ("Mont-Saint-Michel", "Mont-Saint-Michel", 48.6361, -1.5115), ["culture", "unesco", "coast"],
     ("The D-Day beaches of Normandy and the tidal abbey of Mont-Saint-Michel.", "Normandia partraszállási partjai és az apály-dagály szigetén álló Mont-Saint-Michel apátság."),
     [["Honfleur", 49.4193, 0.2327]],
     [("ab", "ab", 120, 2500, ("Deauville to Dinard", "Deauville – Dinard"), ("Along the invasion coast over Arromanches, Omaha Beach and Pointe du Hoc to Mont-Saint-Michel.", "A partraszállás partvonala mentén Arromanches, Omaha Beach és Pointe du Hoc felett a Mont-Saint-Michelhez."),
       ["LFRG", ["Honfleur", 49.4193, 0.2327], ["Arromanches", 49.3397, -0.6224], ["Omaha Beach", 49.3720, -0.8830], ["Pointe du Hoc", 49.3955, -0.9889], ["Mont-Saint-Michel", 48.6361, -1.5115], "LFRD"])])
tour("andalusia", ES, ("Andalusia: Seville to Gibraltar", "Andalúzia: Sevillától Gibraltárig"), ("Alhambra", "Alhambra", 37.1770, -3.5881), ["culture", "unesco", "city"],
     ("The Moorish heart of Spain: Seville, the Mezquita of Córdoba, the Alhambra, Ronda's gorge and the Rock of Gibraltar.", "Spanyolország mór szíve: Sevilla, a córdobai Mezquita, az Alhambra, Ronda szurdoka és a gibraltári szikla."),
     [["Giralda, Seville", 37.3860, -5.9926]],
     [("ab", "ab", 120, 5000, ("Seville to Gibraltar", "Sevilla – Gibraltár"), ("One-way through Andalusia's white towns and cities to the Rock of Gibraltar.", "Egyirányú repülés Andalúzia fehér városai felett a gibraltári sziklához."),
       ["LEZL", ["Seville Cathedral", 37.3861, -5.9926], ["Mezquita, Córdoba", 37.8789, -4.7794], ["Alhambra", 37.1770, -3.5881], ["Ronda", 36.7413, -5.1673], ["Rock of Gibraltar", 36.1408, -5.3536], "LXGB"])])
tour("barcelona", ES, ("Barcelona and the Costa Brava", "Barcelona és a Costa Brava"), ("Sagrada Família", "Sagrada Família", 41.4036, 2.1744), ["city", "culture", "coast"],
     ("Gaudí's Barcelona, the serrated mountain of Montserrat, Dalí's Figueres and the wild cape of Cap de Creus.", "Gaudí Barcelonája, a fogazott Montserrat-hegy, Dalí Figueres-e és a Cap de Creus vad foka."),
     [["Park Güell", 41.4145, 2.1527]],
     [("ab", "ab", 110, 3000, ("Barcelona to Girona", "Barcelona – Girona"), ("One-way from Barcelona over Montserrat and Figueres to the Cap de Creus and Girona.", "Egyirányú repülés Barcelonából a Montserrat és Figueres felett a Cap de Creushoz és Gironába."),
       ["LEBL", ["Sagrada Família", 41.4036, 2.1744], ["Montserrat", 41.5933, 1.8112], ["Dalí Theatre-Museum, Figueres", 42.2672, 2.9617], ["Cap de Creus", 42.3190, 3.3160], ["Girona Cathedral", 41.9877, 2.8260], "LEGE"])])
tour("london", GB, ("London landmarks", "London nevezetességei"), ("Tower Bridge", "Tower Bridge", 51.5055, -0.0754), ["city", "culture"],
     ("The Thames through the capital: Tower Bridge, St Paul's, the Houses of Parliament and Big Ben, with Wembley and Windsor Castle.", "A Temze a fővároson át: Tower Bridge, a Szent Pál-székesegyház, a Parlament és a London Eye, Wembley és a Windsori-kastély."),
     [["London Eye", 51.5033, -0.1196], ["Buckingham Palace", 51.5014, -0.1419]],
     [("loop", "loop", 100, 2000, ("London loop", "Londoni kör"), ("A loop from London City over the Thames bridges and Westminster to Wembley and Windsor.", "Kör a London City repülőtérről a Temze hídjai és Westminster felett Wembley-be és Windsorba."),
       ["EGLC", ["Tower Bridge", 51.5055, -0.0754], ["St Paul's Cathedral", 51.5138, -0.0984], ["Houses of Parliament", 51.4995, -0.1248], ["Wembley Stadium", 51.5560, -0.2795], ["Windsor Castle", 51.4839, -0.6044], "EGLC"])])
tour("scottish-highlands", GB, ("Scottish Highlands", "Skót felföld"), ("Ben Nevis", "Ben Nevis", 56.7969, -5.0036), ["mountain", "coast", "culture"],
     ("Glencoe, Britain's highest mountain Ben Nevis, the Glenfinnan Viaduct, Eilean Donan Castle and Loch Ness.", "Glencoe, Nagy-Britannia legmagasabb hegye, a Ben Nevis, a glenfinnani viadukt, az Eilean Donan-kastély és a Loch Ness."),
     [["Glencoe", 56.6827, -5.0833]],
     [("ab", "ab", 120, 5500, ("Glasgow to Inverness", "Glasgow – Inverness"), ("A one-way flight north through the Highlands to Inverness.", "Egyirányú repülés északra a Felföldön át Invernessbe."),
       ["EGPF", ["Glencoe", 56.6827, -5.0833], ["Ben Nevis", 56.7969, -5.0036], ["Glenfinnan Viaduct", 56.8763, -5.4322], ["Eilean Donan Castle", 57.2742, -5.5161], ["Urquhart Castle, Loch Ness", 57.3243, -4.4421], "EGPE"])])
tour("cornwall", GB, ("Cornwall coast", "Cornwall partvidéke"), ("Land's End", "Land's End", 50.0657, -5.7132), ["coast", "culture"],
     ("The rugged Cornish coast: the Eden Project, St Michael's Mount, Land's End, St Ives and Tintagel.", "A zord cornwalli tengerpart: az Eden Project, a St Michael's Mount, a Land's End, St Ives és Tintagel."),
     [["Minack Theatre", 50.0425, -5.6501]],
     [("loop", "loop", 105, 1800, ("Cornwall loop", "Cornwalli kör"), ("From Newquay to the Eden Project, round Land's End and back along the north coast via Tintagel.", "Newquay-ből az Eden Projecthez, a Land's End körül, majd Tintagelen át az északi parton vissza."),
       ["EGHQ", ["Eden Project", 50.3602, -4.7447], ["St Michael's Mount", 50.1161, -5.4775], ["Land's End", 50.0657, -5.7132], ["St Ives", 50.2111, -5.4800], ["Tintagel Castle", 50.6680, -4.7510], "EGHQ"])])
tour("edinburgh", GB, ("Edinburgh and the Forth", "Edinburgh és a Forth"), ("Edinburgh Castle", "Edinburgh-i kastély", 55.9486, -3.1999), ["city", "culture", "unesco"],
     ("Edinburgh Castle, the Forth bridges, the Kelpies and the Falkirk Wheel, ending at Stirling Castle.", "Az edinburgh-i kastély, a Forth hídjai, a Kelpies szobrok és a Falkirk-kerék, a stirlingi kastélynál végződve."),
     [["Arthur's Seat", 55.9441, -3.1618]],
     [("loop", "loop", 100, 2500, ("Edinburgh loop", "Edinburgh-i kör"), ("From Edinburgh Airport over the castle and the Forth Bridge to the Kelpies, the Falkirk Wheel and Stirling.", "Az edinburgh-i repülőtérről a kastély és a Forth-híd felett a Kelpieshez, a Falkirk-kerékhez és Stirlingbe."),
       ["EGPH", ["Edinburgh Castle", 55.9486, -3.1999], ["Forth Bridge", 56.0003, -3.3887], ["The Kelpies", 56.0185, -3.7500], ["Falkirk Wheel", 55.9990, -3.8450], ["Stirling Castle", 56.1230, -3.9475], "EGPH"])])
tour("norway-fjords", ("Norway", "Norvégia"), ("Fjords of western Norway", "Nyugat-Norvégia fjordjai"), ("Geirangerfjord", "Geirangerfjord", 62.1049, 7.2060), ["mountain", "coast", "unesco"],
     ("The Trollstigen road, the Geirangerfjord, the Briksdal glacier and the Flåm valley, ending in Bergen.", "A Trollstigen út, a Geirangerfjord, a briksdali gleccser és a Flåm-völgy, Bergenben végződve."),
     [["Flåm", 60.8627, 7.1138]],
     [("ab", "ab", 110, 5500, ("Ålesund to Bergen", "Ålesund – Bergen"), ("A one-way flight through the fjord country from Ålesund to Bergen.", "Egyirányú repülés a fjordvidéken át Ålesundtól Bergenig."),
       ["ENAL", ["Trollstigen", 62.4553, 7.6694], ["Geirangerfjord", 62.1049, 7.2060], ["Briksdalsbreen", 61.6580, 6.8400], ["Flåm", 60.8627, 7.1138], "ENBR"])])
tour("cyclades", ("Greece", "Görögország"), ("Cyclades island hopping", "Ciklád-szigetek"), ("Santorini caldera", "Santorini kaldera", 36.4150, 25.4350), ["island", "coast", "volcano"],
     ("The flooded caldera of Santorini, Naxos with its marble gate, sacred Delos and cosmopolitan Mykonos.", "Santorini elárasztott kalderája, Naxos márványkapuja, a szent Délosz és a világvárosias Mykonos."),
     [["Delos", 37.3959, 25.2693]],
     [("ab", "ab", 110, 3000, ("Santorini to Mykonos", "Santorinitől Mykonosig"), ("Island hopping from Santorini via Naxos and Delos to Mykonos.", "Szigetugrálás Santorinitől Naxoson és Délosz-on át Mykonosig."),
       ["LGSR", ["Santorini caldera", 36.4150, 25.4350], ["Portara, Naxos", 37.1060, 25.3720], ["Delos", 37.3959, 25.2693], ["Mykonos Town", 37.4467, 25.3289], "LGMK"])])
tour("peloponnese", ("Greece", "Görögország"), ("Athens and the Peloponnese", "Athén és a Peloponnészosz"), ("Acropolis", "Akropolisz", 37.9715, 23.7257), ["culture", "unesco", "city"],
     ("The Acropolis, the Corinth Canal, Mycenae and the theatre of Epidaurus, plus Cape Sounion.", "Az Akropolisz, a Korinthoszi-csatorna, Mükéné és az epidauroszi színház, valamint a Szuniono-fok."),
     [["Temple of Poseidon, Sounion", 37.6497, 24.0247]],
     [("loop", "loop", 110, 3000, ("Athens and Peloponnese loop", "Athén és Peloponnészosz kör"), ("From Athens over Cape Sounion and the Acropolis to Corinth, Mycenae and Epidaurus.", "Athénból a Szuniono-fok és az Akropolisz felett Korinthoszba, Mükénébe és Epidauroszba."),
       ["LGAV", ["Temple of Poseidon, Sounion", 37.6497, 24.0247], ["Acropolis", 37.9715, 23.7257], ["Corinth Canal", 37.9328, 22.9810], ["Mycenae", 37.7308, 22.7564], ["Epidaurus", 37.5964, 23.0793], "LGAV"])])
tour("dalmatia", ("Croatia", "Horvátország"), ("Dalmatian coast", "Dalmát tengerpart"), ("Diocletian's Palace, Split", "Diocletianus-palota, Split", 43.5081, 16.4402), ["coast", "island", "unesco"],
     ("The walled city of Dubrovnik, the island of Hvar, Diocletian's Palace in Split and the Krka waterfalls.", "A fallal körülvett Dubrovnik, Hvar szigete, a spliti Diocletianus-palota és a Krka-vízesések."),
     [["Hvar Town", 43.1729, 16.4411]],
     [("ab", "ab", 120, 3500, ("Dubrovnik to Zadar", "Dubrovniktól Zadarig"), ("A one-way coastal flight over islands and old towns from Dubrovnik to Zadar.", "Egyirányú tengerparti repülés szigetek és óvárosok felett Dubrovniktól Zadarig."),
       ["LDDU", ["Dubrovnik Old Town", 42.6410, 18.1100], ["Hvar Town", 43.1729, 16.4411], ["Diocletian's Palace, Split", 43.5081, 16.4402], ["Krka Waterfalls", 43.8030, 15.9710], "LDZD"])])
tour("prague", ("Czechia", "Csehország"), ("Prague and Bohemia", "Prága és Csehország"), ("Prague Castle", "Prágai vár", 50.0909, 14.4004), ["city", "culture", "unesco"],
     ("The Hradčany castle and Charles Bridge in Prague, Karlštejn castle and the bone church of Kutná Hora.", "A Hradzsin és a Károly-híd Prágában, a Karlštejn-vár és a kutnahorai csontkápolna."),
     [["Charles Bridge", 50.0865, 14.4114]],
     [("loop", "loop", 100, 2500, ("Prague loop", "Prágai kör"), ("From Prague over Karlštejn Castle and the city to Kutná Hora and back.", "Prágából a Karlštejn-vár és a város felett Kutná Horába és vissza."),
       ["LKPR", ["Karlštejn Castle", 49.9393, 14.1881], ["Prague Castle", 50.0909, 14.4004], ["Charles Bridge", 50.0865, 14.4114], ["St Barbara's Church, Kutná Hora", 49.9503, 15.2622], "LKPR"])])
tour("zurich-constance", ("Switzerland", "Svájc"), ("Zurich to Lake Constance", "Zürichtől a Boden-tóig"), ("Rhine Falls", "Rajnai-vízesés", 47.6779, 8.6150), ["mountain", "coast", "city"],
     ("Zurich's old town, the Rhine Falls (Europe's largest waterfall), the island of Mainau and the Säntis massif.", "Zürich óvárosa, a Rajnai-vízesés (Európa legnagyobb vízesése), Mainau szigete és a Säntis-hegység."),
     [["Säntis", 47.2494, 9.3430]],
     [("ab", "ab", 110, 6500, ("Zurich to Altenrhein", "Zürich – Altenrhein"), ("One-way from Zurich over the Rhine Falls and Mainau to the Säntis and Altenrhein.", "Egyirányú repülés Zürichből a Rajnai-vízesés és Mainau felett a Säntishez és Altenrheinbe."),
       ["LSZH", ["Grossmünster, Zurich", 47.3700, 8.5440], ["Rhine Falls", 47.6779, 8.6150], ["Mainau Island", 47.7054, 9.1954], ["Säntis", 47.2494, 9.3430], "LSZR"])])
save()
