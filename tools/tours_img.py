#!/usr/bin/env python3
"""A turak fejlec-kepe: tours.json 'img' = angol Wikipedia-cikk cime; az app a cikk vezerkepet toltI le futaskor (nincs kep a repoban)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = {
"lamu": "Lamu|Shela", "langkawi": "Langkawi|Langkawi Sky Bridge", "kota-kinabalu": "Mount Kinabalu|Kota Kinabalu", "baku": "Flame Towers|Gobustan National Park", "lake-baikal": "Lake Baikal|Olkhon Island", "kamchatka": "Avachinsky|Koryaksky", "galicia": "Santiago de Compostela Cathedral|Cíes Islands", "fernando-de-noronha": "Fernando de Noronha|Morro do Pico", 
"valencia-costa-blanca": "City of Arts and Sciences|Albufera", "gran-canaria": "Roque Nublo|Maspalomas", "ibiza-formentera": "Es Vedrà|Ibiza (town)", "northern-ireland": "Giant's Causeway|Dunluce Castle", "gotland": "Visby|Fårö", "iceland-north": "Dettifoss|Lake Mývatn", "ephesus-pamukkale": "Pamukkale|Library of Celsus", "almaty": "Big Almaty Lake|Almaty", "ulaanbaatar": "Genghis Khan Equestrian Statue|Gorkhi-Terelj National Park", "japan-alps": "Matsumoto Castle|Kamikōchi", "zhangjiajie": "Wulingyuan|Zhangjiajie National Forest Park", "xian": "Terracotta Army|Xi'an", "lebanon": "Baalbek|Byblos", "andaman": "Radhanagar Beach|Cellular Jail", "lombok": "Mount Rinjani|Lombok", "anchorage-glaciers": "Portage Glacier|Anchorage, Alaska", "big-sur": "Bixby Creek Bridge|Big Sur", "portland-gorge": "Mount Hood|Multnomah Falls", "washington-dc": "National Mall|Washington Monument", "virgin-islands": "Trunk Bay|Magens Bay", "oaxaca": "Monte Albán|Hierve el Agua", "tikal": "Tikal|Flores, Petén", "arequipa-colca": "Colca Canyon|Arequipa", "punta-del-este": "Casapueblo|Punta del Este", "peninsula-valdes": "Valdés Peninsula|Puerto Pirámides", "tangier-chefchaouen": "Chefchaouen|Tangier", "dunedin-otago": "Baldwin Street|Otago Peninsula", "nelson-abel-tasman": "Abel Tasman National Park|Split Apple Rock", "lord-howe": "Ball's Pyramid|Lord Howe Island", "rarotonga": "Rarotonga|Muri Lagoon", "king-george-island": "King George Island (South Shetland Islands)|Great Wall Station", "antarctic-sound": "Paulet Island|Brown Bluff", "mcmurdo": "Mount Erebus|McMurdo Station", "vinson-union-glacier": "Vinson Massif|Ellsworth Mountains", 
"sarajevo-mostar": "Stari Most|Mostar", "vilnius-trakai": "Trakai Island Castle|Vilnius", "kiruna-abisko": "Abisko National Park|Kebnekaise", "svalbard": "Longyearbyen|Pyramiden",
"azores-sao-miguel": "Sete Cidades|Lagoa do Fogo", "orkney": "Ring of Brodgar|Skara Brae", "albanian-alps": "Valbona Valley National Park|Theth", "yerevan-ararat": "Khor Virap|Mount Ararat", "samarkand": "Registan|Samarkand",
"kerala": "Kerala backwaters|Fort Kochi", "komodo": "Padar|Komodo National Park", "guilin": "Li River|Guilin", "kyushu-aso": "Mount Aso|Beppu", "busan": "Haeundae Beach|Gamcheon Culture Village", "bangkok-ayutthaya": "Wat Arun|Ayutthaya (city)",
"glacier-np": "Going-to-the-Sun Road|Lake McDonald (Montana)", "black-hills": "Mount Rushmore|Badlands National Park", "moab-arches": "Delicate Arch|Arches National Park",
"panama-canal": "Panama Canal|Panama City|Bridge of the Americas|Casco Viejo, Panama City", "antigua-atitlan": "Volcán de Fuego|Lake Atitlán", "havana-vinales": "Viñales Valley|Havana", "ilulissat": "Ilulissat Icefjord|Ilulissat",
"puerto-varas": "Osorno (volcano)|Puerto Varas", "ushuaia-beagle": "Ushuaia|Les Eclaireurs Lighthouse", "bogota-zipaquira": "Monserrate|Salt Cathedral of Zipaquirá", "red-sea-sinai": "Mount Sinai|Ras Mohammed National Park", "reunion": "Piton de la Fournaise|Cirque de Mafate",
"adelaide-kangaroo": "Remarkable Rocks|Kangaroo Island", "alice-springs": "Ormiston Gorge|Alice Springs", "christchurch-banks": "Akaroa|Banks Peninsula",
"hamburg-lubeck": "Elbphilharmonie|Holstentor", "black-forest": "Triberg Waterfalls|Black Forest", "bordeaux": "Dune of Pilat|Saint-Émilion", "corsica": "Scandola Nature Reserve|Calvi, Haute-Corse", "basque-coast": "San Sebastián|Gaztelugatxe",
"costa-brava": "Cadaqués|Tossa de Mar", "douro": "Dom Luís I Bridge|Porto|Douro Valley", "gdansk": "Gdańsk|Long Market", "belgrade-novi-sad": "Belgrade Fortress|Petrovaradin Fortress", "seoul": "Gyeongbokgung|N Seoul Tower",
"manila-taal": "Taal Volcano|Intramuros", "kuala-lumpur": "Petronas Towers|Batu Caves", "chiang-mai": "Doi Suthep|Doi Inthanon", "muscat": "Sultan Qaboos Grand Mosque|Muscat", "antalya": "Aspendos|Antalya",
"boston-cape-cod": "Cape Cod|Provincetown, Massachusetts", "new-orleans": "French Quarter|New Orleans", "san-diego": "La Jolla|Coronado Bridge", "denver-rockies": "Pikes Peak|Garden of the Gods", "sedona": "Sedona, Arizona|Cathedral Rock (Arizona)",
"quebec": "Château Frontenac|Quebec City", "entebbe-nile": "Source of the Nile|Jinja, Uganda", "swakopmund": "Sandwich Harbour|Swakopmund", "fes": "Fes el Bali|Fes, Morocco", "mombasa-diani": "Fort Jesus|Diani Beach",
"florianopolis": "Hercílio Luz Bridge|Florianópolis", "quito-cotopaxi": "Cotopaxi|Quito", "salta-humahuaca": "Quebrada de Humahuaca|Purmamarca", "wellington-marlborough": "Marlborough Sounds|Wellington", "blue-mountains": "Three Sisters (New South Wales)|Blue Mountains (New South Wales)",
"darwin-kakadu": "Jim Jim Falls|Kakadu National Park", "brisbane-moreton": "Moreton Island|Brisbane",
"nairobi-rift": "Lake Naivasha|Hell's Gate National Park", "kigali-volcanoes": "Volcanoes National Park|Mount Karisimbi", "tunis-carthage": "Sidi Bou Said|Carthage", "morondava-tsingy": "Avenue of the Baobabs|Tsingy de Bemaraha Strict Nature Reserve",
"kruger-blyde": "Blyde River Canyon|Kruger National Park", "aswan-abu-simbel": "Abu Simbel temples|Philae", "perth-rottnest": "Rottnest Island|Perth", "gold-coast": "Surfers Paradise, Queensland|Gold Coast, Queensland",
"melbourne-phillip": "Phillip Island|Melbourne", "bay-of-islands": "Hole in the Rock (Piercy Island)|Bay of Islands", "rotorua-tongariro": "Wai-O-Tapu|Tongariro National Park", "palau": "Jellyfish Lake|Koror|Peleliu|Rock Islands Southern Lagoon",
"cartagena-rosario": "Cartagena, Colombia|Rosario Islands", "medellin-guatape": "Piedra del Peñol|Guatapé", "lima": "Miraflores District|Lima", "la-paz-titicaca": "Lake Titicaca|La Paz",
"pucon-volcanoes": "Villarrica (volcano)|Pucón", "ladakh": "Thiksey Monastery|Leh", "pokhara-annapurna": "Machapuchare|Annapurna", "hiroshima-miyajima": "Itsukushima Shrine|Hiroshima",
"okinawa": "Okinawa Churaumi Aquarium|Okinawa Island", "danang-hoian": "Dragon Bridge|Marble Mountains (Vietnam)|Hải Vân Pass|Hội An", "georgia-caucasus": "Gergeti Trinity Church|Mount Kazbek", "puerto-rico": "El Yunque National Forest|Old San Juan",
"cabo": "El Arco de Cabo San Lucas|Cabo San Lucas", "belize-blue-hole": "Great Blue Hole|Caye Caulker", "costa-rica": "Arenal Volcano|Poás Volcano", "jomsom-mustang": "Jomsom|Muktinath",
"idaho-backcountry": "Frank Church-River of No Return Wilderness|Salmon River (Idaho)", "kokoda": "Kokoda Airfield|Kokoda Track campaign|Kokoda Track", "tiree-hebrides": "Fingal's Cave|Iona", "samedan-bernina": "Piz Bernina|St. Moritz", "pyrenees": "Aneto|Pica d'Estats",
"jungfrau": "Jungfrau|Eiger", "iceland-south": "Skógafoss|Seljalandsfoss", "tromso": "Tromsø|Tromsdalen", "meteora": "Meteora", "corfu": "Corfu (city)|Corfu", "rhodes": "Lindos|Rhodes (city)",
"sardinia": "Costa Smeralda|La Maddalena", "puglia": "Alberobello", "lanzarote": "Timanfaya National Park|Lanzarote", "tyrol": "Innsbruck|Zugspitze", "lake-geneva": "Château de Chillon|Lavaux",
"kerry": "Skellig Michael|Dingle Peninsula", "snowdonia": "Snowdon|Conwy Castle", "lake-district": "Windermere|Lake District", "danube-bend": "Danube Bend|Visegrád", "tokaj-eger": "Eger Castle|Tokaj",
"hokkaido": "Lake Tōya|Mount Yōtei", "taiwan": "Taroko National Park|Taipei 101", "los-angeles": "Hollywood Sign|Griffith Observatory", "vancouver": "Stanley Park|Grouse Mountain",
"santiago-andes": "Santiago|Aconcagua", "bariloche": "Nahuel Huapi National Park|Cerro Tronador", "tahiti-moorea": "Moorea|Teahupo'o",
"courchevel": "Courchevel Altiport|Courchevel", "barra-st-kilda": "Barra Airport|St Kilda, Scotland", "saba-statia": "Saba|Mount Scenery", "st-barth": "Maho Beach|Princess Juliana International Airport|Gustavia, Saint Barthélemy", "mccarthy": "Kennecott, Alaska|McCarthy, Alaska", "telluride": "Telluride, Colorado|Mount Sneffels",
"jeju": "Hallasan|Jeju Island", "rajasthan": "Amber Fort|Jaipur", "java": "Borobudur", "bhutan": "Paro Taktsang", "sri-lanka": "Sigiriya", "chicago": "Chicago|Willis Tower",
"seattle-rainier": "Mount Rainier", "zion-bryce": "Bryce Canyon", "mexico-city": "Teotihuacan", "nazca": "Nazca Lines", "uyuni": "Salar de Uyuni", "angel-falls": "Angel Falls",
"manaus": "Teatro Amazonas|Manaus", "serengeti-mara": "Maasai Mara|Serengeti National Park|Great Migration|Serengeti", "mauritius": "Le Morne Brabant", "zanzibar": "Stone Town", "sahara-merzouga": "Erg Chebbi",
"auckland": "Sky Tower, Auckland|Auckland", "queenstown": "Queenstown, New Zealand|The Remarkables",
"agra-taj": "Taj Mahal", "everest": "Mount Everest", "angkor": "Angkor Wat", "bagan": "Bagan", "budapest": "Hungarian Parliament Building", "balaton": "Tihany Abbey",
"rome-naples": "Colosseum", "amalfi": "Amalfi Coast", "tuscany": "Val d'Orcia", "dolomites": "Tre Cime di Lavaredo", "cinque-terre": "Vernazza", "matterhorn": "Matterhorn",
"lucerne": "Chapel Bridge", "salzkammergut": "Hallstatt", "loire": "Château de Chambord", "golden-circle": "Gullfoss", "italian-lakes": "Lake Como", "sicily": "Mount Etna",
"vienna-wachau": "Schönbrunn Palace", "bavaria": "Neuschwanstein Castle", "rhine": "Rhine Gorge", "provence-riviera": "Pont du Gard", "mont-blanc": "Mont Blanc", "normandy": "Mont-Saint-Michel",
"andalusia": "Alhambra", "barcelona": "Sagrada Família", "london": "Tower Bridge", "scottish-highlands": "Glenfinnan Viaduct", "cornwall": "St Michael's Mount", "edinburgh": "Edinburgh Castle",
"norway-fjords": "Geirangerfjord", "cyclades": "Oia, Greece|Mykonos|Santorini", "peloponnese": "Acropolis of Athens", "dalmatia": "Dubrovnik", "prague": "Charles Bridge", "zurich-constance": "Rhine Falls",
"venice": "Grand Canal (Venice)", "garda": "Sirmione", "krakow-tatras": "Wawel Castle", "stockholm": "Gamla stan", "copenhagen": "Kronborg", "helsinki": "Helsinki Cathedral",
"lofoten": "Reine, Norway", "slovenia": "Lake Bled", "malta": "Valletta", "transylvania": "Bran Castle", "montenegro": "Bay of Kotor", "netherlands": "Keukenhof",
"belgium": "Grand-Place", "tatras-slovakia": "High Tatras", "bulgaria": "Rila Monastery", "istria": "Rovinj", "ireland-west": "Cliffs of Moher", "cyprus": "Petra tou Romiou",
"lisbon-sintra": "Belém Tower", "algarve": "Benagil Cave|Algarve", "istanbul": "Hagia Sophia", "cappadocia": "Göreme", "mallorca": "Sa Calobra", "crete": "Balos Lagoon",
"berlin": "Brandenburg Gate", "faroe": "Mulafossur|Gásadalur|Saksun|Vágar|Tórshavn|Faroe Islands", "brittany": "Côte de Granit Rose", "new-york": "Statue of Liberty", "grand-canyon": "Grand Canyon", "sf-bay": "Golden Gate Bridge",
"oahu": "Diamond Head, Hawaii", "machu-picchu": "Machu Picchu", "rio": "Christ the Redeemer (statue)", "iguazu": "Iguazu Falls", "cape-town": "Table Mountain", "giza": "Giza pyramid complex",
"kilimanjaro": "Mount Kilimanjaro", "sydney": "Sydney Opera House", "whitsundays": "Whitehaven Beach", "milford-sound": "Milford Sound", "tokyo-fuji": "Mount Fuji", "dubai": "Burj Khalifa",
"hong-kong": "Victoria Harbour|Victoria Peak|Tsim Sha Tsui|Hong Kong Island|Central, Hong Kong", "yellowstone": "Grand Prismatic Spring", "las-vegas": "Hoover Dam", "yosemite": "Half Dome", "banff": "Moraine Lake", "yucatan": "Chichen Itza",
"torres-del-paine": "Cuernos del Paine|Torres del Paine National Park", "perito-moreno": "Perito Moreno Glacier", "galapagos": "Galápagos Islands", "buenos-aires": "Obelisco de Buenos Aires|Buenos Aires", "marrakech-atlas": "Koutoubia Mosque",
"victoria-falls": "Victoria Falls", "luxor": "Karnak", "ngorongoro": "Ngorongoro Conservation Area", "uluru": "Uluru", "great-ocean-road": "Twelve Apostles (Victoria)", "aoraki": "Aoraki / Mount Cook",
"bora-bora": "Mount Otemanu", "bali": "Tanah Lot", "singapore": "Marina Bay Sands",
"okavango": "Okavango Delta", "sossusvlei": "Sossusvlei", "seychelles": "Anse Source d'Argent", "garden-route": "Knysna", "petra-wadi-rum": "Petra", "maldives": "Ari Atoll",
"halong": "Ha Long Bay", "kyoto-osaka": "Fushimi Inari-taisha", "beijing": "Great Wall of China", "phuket": "Phi Phi Islands", "denali": "Denali", "monument-valley": "Monument Valley",
"toronto-niagara": "Niagara Falls|Toronto", "florida-keys": "Biscayne Bay|Art Deco Historic District|Key West, Florida", "easter-island": "Ahu Tongariki", "atacama": "Atacama Desert", "tasmania": "Wineglass Bay",
"cairns": "Great Barrier Reef", "fiji": "Mamanuca Islands", "madeira": "Cabo Girão|Madeira", "tenerife": "Teide", "paris": "Eiffel Tower",
}
P = os.path.join(ROOT, "data", "tours.json")
IMG.update({
"lalibela": "Lalibela|Church of Saint George, Lalibela", "cabo-verde": "Pico do Fogo|Cidade Velha", "bazaruto": "Bazaruto Archipelago|Bazaruto Island", "lake-malawi": "Lake Malawi|Lake Malawi National Park",
"kolmanskop": "Kolmanskop|Lüderitz", "mount-kenya": "Mount Kenya|Ol Pejeta Conservancy", "dakar-saloum": "Gorée|Lake Retba", "hoggar": "Hoggar Mountains|Assekrem",
"socotra": "Socotra|Dracaena cinnabari", "persepolis": "Persepolis|Naqsh-e Rustam", "musandam": "Musandam Governorate|Khasab", "k2-karakoram": "K2|Baltoro Glacier",
"issyk-kul": "Issyk-Kul|Jeti-Ögüz", "fann-mountains": "Iskanderkul|Fann Mountains", "darvaza": "Darvaza gas crater|Ashgabat", "bukhara": "Po-i-Kalyan|Bukhara",
"altai": "Belukha Mountain|Lake Teletskoye", "tibet-lhasa": "Potala Palace|Yamdrok Lake", "luang-prabang": "Kuang Si Falls|Luang Prabang", "inle-lake": "Inle Lake|Pindaya",
"lake-toba": "Lake Toba|Samosir", "boracay-panay": "Boracay|White Beach (Boracay)", "bohol": "Chocolate Hills|Philippine tarsier", "lijiang": "Jade Dragon Snow Mountain|Lijiang",
"darjeeling-sikkim": "Kangchenjunga|Darjeeling", "estonia": "Tallinn Old Town|Kuressaare Castle", "ohrid": "Lake Ohrid|Church of St. John at Kaneo", "asturias": "Naranjo de Bulnes|Lakes of Covadonga",
"kefalonia": "Myrtos Beach|Navagio Beach", "halkidiki-athos": "Mount Athos|Halkidiki", "trabzon-kackar": "Sumela Monastery|Uzungöl", "auvergne": "Puy de Dôme|Chaîne des Puys",
"danube-delta": "Danube Delta|Sulina", "azores-central": "Mount Pico|Capelinhos", "juneau-passage": "Mendenhall Glacier|Tracy Arm", "exumas": "Pig Beach|Staniel Cay|Great Exuma",
"jamaica": "Blue Mountain Peak (Jamaica)|Dunn's River Falls", "bay-islands": "Roatán|Utila", "nicaragua": "Masaya Volcano|Ometepe", "copper-canyon": "Copper Canyon|Basaseachi Falls",
"gros-morne": "Gros Morne National Park|The Tablelands", "yukon": "Kluane National Park and Reserve|Miles Canyon", "cape-breton": "Cabot Trail|Fortress of Louisbourg",
"guyana": "Kaieteur Falls|Georgetown, Guyana", "lencois-maranhenses": "Lençóis Maranhenses National Park|São Luís, Maranhão", "pantanal": "Pantanal|Bonito, Mato Grosso do Sul",
"vavau": "Neiafu (Vavaʻu)|Neiafu Market", "kimberley": "Purnululu National Park|Lake Argyle", "ningaloo": "Ningaloo Coast|Turquoise Bay", "new-caledonia": "Isle of Pines (New Caledonia)|Nouméa"})
IMG.update({
"ghana-cape-coast": "Cape Coast Castle|Kakum National Park", "angola-lubango": "Tundavala Gap|Lubango", "mali-djenne": "Great Mosque of Djenné|Bandiagara Escarpment", "mauritania-adrar": "Richat Structure|Chinguetti",
"agadez-air": "Agadez|Aïr Mountains", "libya-leptis": "Leptis Magna|Sabratha", "sudan-meroe": "Meroë|Naqa", "asmara-massawa": "Asmara|Massawa",
"djibouti-assal": "Lake Assal (Djibouti)|Tadjoura", "lesotho-maseru": "Maletsunyane Falls|Thaba Bosiu", "sao-tome": "Pico Cão Grande|São Tomé (city)", "south-luangwa": "South Luangwa National Park|Luangwa River",
"bamiyan": "Buddhas of Bamiyan|Band-e Amir National Park", "alula": "Hegra Archaeological Site|AlUla", "mesopotamia": "Babylon|Ctesiphon", "syria-palmyra": "Palmyra|Krak des Chevaliers",
"qatar": "Museum of Islamic Art, Doha|Lusail Stadium", "brunei": "Omar Ali Saifuddien Mosque|Kampong Ayer", "timor-leste": "Cristo Rei of Dili|Atauro Island", "coxs-bazar": "Cox's Bazar|Saint Martin's Island",
"ajanta-ellora": "Ellora Caves|Ajanta Caves", "dunhuang": "Mogao Caves|Dunhuang", "kashgar-karakul": "Kashgar|Muztagh Ata", "karelia-kizhi": "Kizhi Pogost|Kivach Waterfall",
"belarus-mir": "Mir Castle|Nesvizh Castle", "moldova-orhei": "Orheiul Vechi|Cricova", "kola-khibiny": "Khibiny|Teriberka", "kazan-volga": "Kazan Kremlin|Sviyazhsk",
"lviv-carpathians": "Lviv|Hoverla", "kaliningrad-curonian": "Curonian Spit|Kaliningrad", "iqaluit-auyuittuq": "Auyuittuq National Park|Iqaluit", "katmai-alaska": "Katmai National Park and Preserve|Valley of Ten Thousand Smokes",
"copan-honduras": "Copán|Lake Yojoa", "suriname-brownsberg": "Paramaribo|Brownsberg Nature Park", "haiti-citadelle": "Citadelle Laferrière|Sans-Souci Palace", "paraguay-jesuit": "Jesuit Missions of La Santísima Trinidad de Paraná and Jesús de Tavarangué|Itaipu Dam",
"sucre-potosi": "Sucre|Cerro Rico", "vanuatu-tanna": "Mount Yasur|Port Vila", "solomon-islands": "Marovo Lagoon|Guadalcanal", "samoa-upolu": "To Sua Ocean Trench|Lalomanu|Piula Cave Pool|Savai'i|Upolu|Apia|Samoa",
"nan-madol": "Nan Madol|Pohnpei", "gabon-loango": "Loango National Park|Libreville", "benin-ganvie": "Ganvié|Ouidah", "cameroon-mount": "Mount Cameroon|Limbe, Cameroon",
"ivory-coast": "Basilica of Our Lady of Peace, Yamoussoukro|Grand-Bassam", "latvia-gauja": "Riga|Gauja National Park", "kosovo-prizren": "Prizren|Visoki Dečani", "saint-lucia-pitons": "Pitons (Saint Lucia)|Soufrière, Saint Lucia",
"el-salvador-volcanoes": "Lake Coatepeque|Santa Ana Volcano", "dominican-republic": "Zona Colonial|Pico Duarte"})
d = json.load(open(P, encoding="utf-8"))
miss = [t["id"] for t in d["tours"] if t["id"] not in IMG]
for t in d["tours"]:
    if t["id"] in IMG:
        t["img"] = IMG[t["id"]]
import base64
for t in d["tours"]:
    f = os.path.join(ROOT, "tools", "img", t["id"] + ".svg")      # sajat (SVG) fejlec-kep: a tours.json-ba agyazva (az updater csak .json/.py/.gz stb. fajlokat tolt le)
    if os.path.isfile(f):
        t["imgx"] = "data:image/svg+xml;base64," + base64.b64encode(open(f, "rb").read()).decode("ascii")
print("hianyzik:", miss)
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
