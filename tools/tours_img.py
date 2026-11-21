#!/usr/bin/env python3
"""A turak fejlec-kepe: tours.json 'img' = angol Wikipedia-cikk cime; az app a cikk vezerkepet toltI le futaskor (nincs kep a repoban)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = {
"courchevel": "Courchevel Altiport|Courchevel", "barra-st-kilda": "Barra Airport|St Kilda, Scotland", "saba-statia": "Saba|Mount Scenery", "st-barth": "Saint Barthélemy|Gustavia, Saint Barthélemy", "mccarthy": "Kennecott, Alaska|McCarthy, Alaska", "telluride": "Telluride, Colorado|Mount Sneffels",
"jeju": "Hallasan|Jeju Island", "rajasthan": "Amber Fort|Jaipur", "java": "Borobudur", "bhutan": "Paro Taktsang", "sri-lanka": "Sigiriya", "chicago": "Chicago|Willis Tower",
"seattle-rainier": "Mount Rainier", "zion-bryce": "Bryce Canyon", "mexico-city": "Teotihuacan", "nazca": "Nazca Lines", "uyuni": "Salar de Uyuni", "angel-falls": "Angel Falls",
"manaus": "Teatro Amazonas|Manaus", "serengeti-mara": "Serengeti", "mauritius": "Le Morne Brabant", "zanzibar": "Stone Town", "sahara-merzouga": "Erg Chebbi",
"auckland": "Sky Tower, Auckland|Auckland", "queenstown": "Queenstown, New Zealand|The Remarkables",
"agra-taj": "Taj Mahal", "everest": "Mount Everest", "angkor": "Angkor Wat", "bagan": "Bagan", "budapest": "Hungarian Parliament Building", "balaton": "Tihany Abbey",
"rome-naples": "Colosseum", "amalfi": "Amalfi Coast", "tuscany": "Val d'Orcia", "dolomites": "Tre Cime di Lavaredo", "cinque-terre": "Vernazza", "matterhorn": "Matterhorn",
"lucerne": "Chapel Bridge", "salzkammergut": "Hallstatt", "loire": "Château de Chambord", "golden-circle": "Gullfoss", "italian-lakes": "Lake Como", "sicily": "Mount Etna",
"vienna-wachau": "Schönbrunn Palace", "bavaria": "Neuschwanstein Castle", "rhine": "Rhine Gorge", "provence-riviera": "Pont du Gard", "mont-blanc": "Mont Blanc", "normandy": "Mont-Saint-Michel",
"andalusia": "Alhambra", "barcelona": "Sagrada Família", "london": "Tower Bridge", "scottish-highlands": "Glenfinnan Viaduct", "cornwall": "St Michael's Mount", "edinburgh": "Edinburgh Castle",
"norway-fjords": "Geirangerfjord", "cyclades": "Santorini", "peloponnese": "Acropolis of Athens", "dalmatia": "Dubrovnik", "prague": "Charles Bridge", "zurich-constance": "Rhine Falls",
"venice": "Grand Canal (Venice)", "garda": "Sirmione", "krakow-tatras": "Wawel Castle", "stockholm": "Gamla stan", "copenhagen": "Kronborg", "helsinki": "Helsinki Cathedral",
"lofoten": "Reine, Norway", "slovenia": "Lake Bled", "malta": "Valletta", "transylvania": "Bran Castle", "montenegro": "Bay of Kotor", "netherlands": "Keukenhof",
"belgium": "Grand-Place", "tatras-slovakia": "High Tatras", "bulgaria": "Rila Monastery", "istria": "Rovinj", "ireland-west": "Cliffs of Moher", "cyprus": "Petra tou Romiou",
"lisbon-sintra": "Belém Tower", "algarve": "Benagil Cave", "istanbul": "Hagia Sophia", "cappadocia": "Göreme", "mallorca": "Sa Calobra", "crete": "Balos Lagoon",
"berlin": "Brandenburg Gate", "faroe": "Mulafossur", "brittany": "Côte de Granit Rose", "new-york": "Statue of Liberty", "grand-canyon": "Grand Canyon", "sf-bay": "Golden Gate Bridge",
"oahu": "Diamond Head, Hawaii", "machu-picchu": "Machu Picchu", "rio": "Christ the Redeemer (statue)", "iguazu": "Iguazu Falls", "cape-town": "Table Mountain", "giza": "Giza pyramid complex",
"kilimanjaro": "Mount Kilimanjaro", "sydney": "Sydney Opera House", "whitsundays": "Whitehaven Beach", "milford-sound": "Milford Sound", "tokyo-fuji": "Mount Fuji", "dubai": "Burj Khalifa",
"hong-kong": "Victoria Harbour", "yellowstone": "Grand Prismatic Spring", "las-vegas": "Hoover Dam", "yosemite": "Half Dome", "banff": "Moraine Lake", "yucatan": "Chichen Itza",
"torres-del-paine": "Cuernos del Paine|Torres del Paine National Park", "perito-moreno": "Perito Moreno Glacier", "galapagos": "Galápagos Islands", "buenos-aires": "Obelisco de Buenos Aires|Buenos Aires", "marrakech-atlas": "Koutoubia Mosque",
"victoria-falls": "Victoria Falls", "luxor": "Karnak", "ngorongoro": "Ngorongoro Conservation Area", "uluru": "Uluru", "great-ocean-road": "Twelve Apostles (Victoria)", "aoraki": "Aoraki / Mount Cook",
"bora-bora": "Mount Otemanu", "bali": "Tanah Lot", "singapore": "Marina Bay Sands",
"okavango": "Okavango Delta", "sossusvlei": "Sossusvlei", "seychelles": "Anse Source d'Argent", "garden-route": "Knysna", "petra-wadi-rum": "Petra", "maldives": "Ari Atoll",
"halong": "Ha Long Bay", "kyoto-osaka": "Fushimi Inari-taisha", "beijing": "Great Wall of China", "phuket": "Phi Phi Islands", "denali": "Denali", "monument-valley": "Monument Valley",
"toronto-niagara": "Niagara Falls|Toronto", "florida-keys": "Southernmost Point Buoy|Bahia Honda State Park|Seven Mile Bridge", "easter-island": "Ahu Tongariki", "atacama": "Atacama Desert", "tasmania": "Wineglass Bay",
"cairns": "Great Barrier Reef", "fiji": "Mamanuca Islands", "madeira": "Cabo Girão|Madeira", "tenerife": "Teide", "paris": "Eiffel Tower",
}
P = os.path.join(ROOT, "data", "tours.json")
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
