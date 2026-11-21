#!/usr/bin/env python3
"""A turak kozos latnivalo-listaja (data/tour_pois.json): EN-nev -> nyelvenkenti nev (+ keresesi extra szavak). A magyar alias-ok a poi_hu.py-bol jonnek,
a tobbi nyelvet a poi_fill_wikidata.py tolti (internet kell). Futtatas: poi_registry.py  (a mar kitoltott nyelvek megmaradnak)."""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from poi_hu import HU
# Tiszta magyar megjelenitesi nev ott, ahol az alias tobb szot tartalmaz (a tobbi: maga az alias a nev)
HUN = {
"Akbar's Tomb": "Akbar sírja", "Itimad-ud-Daulah": "Itimád-ud-Daula síremléke", "Agra Fort": "Agrai erőd", "Fatehpur Sikri": "Fatehpur Szikri", "City Palace, Jaipur": "Városi palota, Dzsaipur",
"Tengboche": "Tengboche", "Dingboche": "Dingboche", "Kala Patthar": "Kala Patthar", "Mount Everest": "Mount Everest", "Ama Dablam": "Ama Dablam", "Bayon": "Bayon", "Ta Prohm": "Ta Prohm", "Tonle Sap": "Tonlé Sap",
"Banteay Srei": "Banteay Srei", "Phnom Kulen": "Phnom Kulen", "Badacsony": "Badacsony", "Colosseum": "Colosseum", "St Peter's Basilica": "Szent Péter-bazilika", "Capri": "Capri", "Castel Gandolfo": "Castel Gandolfo",
"Villa d'Este, Tivoli": "Villa d'Este, Tivoli", "Villa Rufolo, Ravello": "Villa Rufolo, Ravello", "Marina Piccola, Capri": "Marina Piccola, Capri", "Florence Cathedral": "Firenzei dóm", "Leaning Tower of Pisa": "Pisai ferde torony",
"Sassolungo": "Sassolungo", "Seceda": "Seceda", "Marmolada": "Marmolada", "Tre Cime di Lavaredo": "Tre Cime di Lavaredo", "Lago di Braies": "Braies-tó", "Riomaggiore": "Riomaggiore", "Matterhorn": "Matterhorn", "Pilatus": "Pilatus",
"Dachstein": "Dachstein", "Hohensalzburg Fortress": "Hohensalzburg vára", "Eisriesenwelt": "Eisriesenwelt", "Versailles": "Versailles-i kastély", "Sacré-Cœur": "Sacré-Cœur", "Notre-Dame de Paris": "Notre-Dame",
"Geysir": "Geysir", "Gullfoss": "Gullfoss", "Kerið": "Kerið", "Hallgrímskirkja": "Hallgrímskirkja", "Milan Cathedral": "Milánói dóm", "Isola San Giulio": "San Giulio-sziget", "Isola Bella": "Isola Bella",
"Valley of the Temples, Agrigento": "Templomok völgye, Agrigento", "Greek Theatre, Syracuse": "Görög színház, Siracusa", "Schönbrunn Palace": "Schönbrunni kastély", "St. Stephen's Cathedral": "Szent István-székesegyház, Bécs",
"Dürnstein": "Dürnstein", "Deutsches Eck, Koblenz": "Deutsches Eck, Koblenz", "Marksburg": "Marksburg", "Loreley": "Loreley", "Pont du Gard": "Pont du Gard", "Palais des Papes, Avignon": "Pápai palota, Avignon", "Monaco": "Monaco",
"Notre-Dame de la Garde": "Notre-Dame de la Garde", "Mont Blanc": "Mont Blanc", "Mer de Glace": "Mer de Glace", "Omaha Beach": "Omaha Beach", "Mezquita, Córdoba": "Córdobai mecset", "Alhambra": "Alhambra", "Sagrada Família": "Sagrada Família",
"Montserrat": "Montserrat", "Dalí Theatre-Museum, Figueres": "Dalí Színház-Múzeum, Figueres", "Park Güell": "Park Güell", "Tower Bridge": "Tower Bridge", "Houses of Parliament": "Westminsteri-palota", "St Paul's Cathedral": "Szent Pál-székesegyház",
"London Eye": "London Eye", "Glencoe": "Glencoe", "Glenfinnan Viaduct": "Glenfinnan-viadukt", "Eilean Donan Castle": "Eilean Donan vára", "Urquhart Castle, Loch Ness": "Urquhart vára, Loch Ness", "Tintagel Castle": "Tintagel vára",
"St Michael's Mount": "Szent Mihály-hegy", "Falkirk Wheel": "Falkirk Wheel", "Trollstigen": "Trollstigen", "Acropolis": "Akropolisz", "Epidaurus": "Epidauroszi színház", "Temple of Poseidon, Sounion": "Poszeidón temploma, Szúnion",
"Zlatni Rat, Brač": "Zlatni Rat, Brač", "St Barbara's Church, Kutná Hora": "Szent Borbála-templom, Kutná Hora", "St Mark's Basilica": "Szent Márk-bazilika", "Prato della Valle, Padua": "Prato della Valle, Padova", "Murano": "Murano",
"Verona Arena": "Veronai Aréna", "Zakopane": "Zakopane", "Gamla Stan": "Gamla Stan", "Kronborg Castle": "Kronborg-kastély", "The Little Mermaid": "A kis hableány", "Møns Klint": "Møns Klint", "Suomenlinna": "Suomenlinna",
"Å": "Å", "Reine": "Reine", "Dwejra": "Dwejra", "Ġgantija Temples": "Ġgantija templomai", "Bran Castle": "Törcsvári kastély", "Black Church, Brașov": "Fekete templom, Brassó", "Keukenhof": "Keukenhof", "Kinderdijk": "Kinderdijk",
"Oosterschelde Barrier": "Oosterschelde-gát", "Lion's Mound, Waterloo": "Waterlooi Oroszlán-domb", "Brussels Grand-Place": "Grand-Place, Brüsszel", "Cherni Vrah": "Cserni Vrah", "Alexander Nevsky Cathedral": "Alekszandr Nyevszkij-székesegyház",
"Dún Aonghasa": "Dún Aonghasa", "Poulnabrone Dolmen": "Poulnabrone-dolmen", "Petra tou Romiou": "Aphrodité sziklája", "Blue Lagoon, Akamas": "Kék Lagúna, Akamas", "Vasco da Gama Bridge": "Vasco da Gama-híd", "Praça do Comércio": "Praça do Comércio",
"Cristo Rei": "Cristo Rei", "25 de Abril Bridge": "Április 25. híd", "Cabo da Roca": "Cabo da Roca", "Sintra National Palace": "Sintrai Nemzeti Palota", "Ponta da Piedade": "Ponta da Piedade", "Praia da Marinha": "Praia da Marinha",
"Lagos": "Lagos", "Cape St Vincent Lighthouse": "Szent Vince-fok világítótornya", "Ria Formosa": "Ria Formosa", "Büyükada": "Büyükada", "Hagia Sophia": "Hagia Sophia", "Fatih Sultan Mehmet Bridge": "Fatih Szultán Mehmed-híd",
"Derinkuyu Underground City": "Derinkuyu földalatti város", "Knossos Palace": "Knósszoszi palota", "Chania Old Port": "Hanya régi kikötője", "Berlin Victory Column": "Berlini Győzelmi oszlop", "Berlin TV Tower": "Berlini tévétorony",
"East Side Gallery": "East Side Gallery", "Múlafossur Waterfall": "Múlafossur-vízesés", "Kallur Lighthouse": "Kallur világítótornya", "Perros-Guirec": "Perros-Guirec", "One World Trade Center": "One World Trade Center",
"Empire State Building": "Empire State Building", "Desert View Watchtower": "Desert View őrtornya", "Bright Angel Point": "Bright Angel Point", "Grand Canyon Village": "Grand Canyon Village", "Golden Gate Bridge": "Golden Gate híd",
"Kalalau Valley": "Kalalau-völgy", "Kalaupapa": "Kalaupapa", "Moray": "Moray", "Sacsayhuamán": "Sacsayhuamán", "Pedra da Gávea": "Pedra da Gávea", "Christ the Redeemer": "Megváltó Krisztus-szobor", "Sugarloaf Mountain": "Cukorsüveg-hegy",
"Table Mountain": "Table Mountain", "Boulders Beach": "Boulders Beach", "Cape Point": "Cape Point", "Cairo Citadel": "Kairói fellegvár", "Step Pyramid of Djoser": "Dzsószer lépcsős piramisa", "Red Pyramid": "Vörös piramis",
"Pyramids of Giza": "Gízai piramisok", "Sydney Harbour Bridge": "Sydney Harbour Bridge", "Mitre Peak": "Mitre-csúcs", "Senso-ji Temple": "Szenszódzsi", "Yokohama Landmark Tower": "Yokohama Landmark Tower", "Palm Jebel Ali": "Palm Jebel Ali",
"Palm Jumeirah": "Palm Jumeirah", "Burj Al Arab": "Burdzs al-Arab", "Tsing Ma Bridge": "Tsing Ma híd", "Tian Tan Buddha": "Tian Tan Buddha", "Grand Prismatic Spring": "Grand Prismatic Spring", "Old Faithful": "Old Faithful",
"Las Vegas Strip": "Las Vegas Strip", "Valley of Fire": "Valley of Fire", "Lake Louise": "Lake Louise", "Chichén Itzá": "Chichén Itzá", "Cuernos del Paine": "Cuernos del Paine", "Torres del Paine": "Torres del Paine",
"Daphne Major": "Daphne Major", "Pinnacle Rock": "Pinnacle Rock", "Recoleta Cemetery": "Recoletai temető", "Obelisco": "Obeliszk", "La Boca": "La Boca", "Dendera Temple": "Denderai templom", "Valley of the Kings": "Királyok völgye",
"Ol Doinyo Lengai": "Ol Doinyo Lengai", "Kata Tjuta": "Kata Tjuta", "Mount Olga Lookout": "Mount Olga kilátó", "Uluru": "Uluru", "Bells Beach": "Bells Beach", "Cape Otway Lighthouse": "Cape Otway világítótornya",
"Twelve Apostles": "Tizenkét Apostol", "Aoraki / Mount Cook": "Aoraki / Mount Cook", "Taputapuatea Marae": "Taputapuatea marae", "Nusa Penida": "Nusa Penida", "Marina Bay Sands": "Marina Bay Sands",
}
P = os.path.join(ROOT, "data", "tour_pois.json")
old = json.load(open(P, encoding="utf-8")).get("pois", {}) if os.path.exists(P) else {}
out = {}
for en, alias in HU.items():
    e = dict(old.get(en, {}))                 # a mar kitoltott nyelvek megmaradnak
    e["hu"] = HUN.get(en, alias)
    extra = alias if alias != e["hu"] else ""
    if extra:
        e["k"] = extra
    else:
        e.pop("k", None)
    out[en] = e
json.dump({"v": 1, "pois": out}, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=0, separators=(",", ":"))
print(len(out), "latnivalo")
