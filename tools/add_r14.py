#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""14. kor (1.2.1): 50 uj STOL-tura rovid kifutokkal. Sorrend: add_r14 -> tours_order <r14_ids> -> dup_check -> poi_registry -> tours_kw -> tours_img -> tours_check"""
from tourlib import *
import json, os
C = lambda e, h: (e, h)
CONT = {}
POI = {}


def add(cont, *a):
    a = list(a)
    a.insert(6, [])
    tour(*a); CONT[a[0]] = cont


def Pt(n, hu, kw, la, lo):
    POI[n] = (hu, kw)
    return [n, la, lo]


def L(ic, pts, name, desc, kind="loop", kt=100, alt=3000, vid="loop"):
    """Egy korut: ic = indulo es erkezo repter."""
    return [(vid, kind, kt, alt, name, desc, [ic] + pts + [ic])]



# ------------------------------------------------------------------ AFRIKA# ------------------------------------------------------------------ ESZAK-AMERIKA
add("NA", "stol-wrangell", C("United States", "Egyesült Államok"), ("Alaska: Chisana and the Wrangell Volcanoes", "Alaszka: Chisana és a Wrangell-vulkánok"), ("Mount Blackburn", "Blackburn-hegy", 61.7310, -143.4030), ["mountain", "glacier", "volcano"],
    ("A STOL flight from the tiny Chisana gravel strip past Mount Bona, Mount Blackburn and the steaming Mount Wrangell, deep inside America's biggest national park.", "STOL repülés a parányi chisanai murvás pályáról a Bona-hegy, a Blackburn-hegy és a gőzölgő Wrangell-vulkán mellett az USA legnagyobb nemzeti parkjában."),
    L("CZN", [Pt("Mount Bona", "Bona-hegy", "Mount Bona Alaszka", 61.3856, -141.7458), Pt("Mount Blackburn", "Blackburn-hegy", "Mount Blackburn Wrangell", 61.7310, -143.4030), Pt("Mount Sanford", "Sanford-hegy", "Mount Sanford Wrangell", 62.2133, -144.1283), Pt("Mount Wrangell", "Wrangell-vulkán", "Mount Wrangell vulkán", 62.0058, -144.0194)],
      ("Wrangell loop", "Wrangell-kör"), ("Mount Bona, Blackburn, Sanford and Wrangell.", "Bona, Blackburn, Sanford és Wrangell."), kt=100, alt=14000))
add("NA", "stol-gates-arctic", C("United States", "Egyesült Államok"), ("Alaska: Gates of the Arctic from Wiseman", "Alaszka: az Északi-sarkvidék kapui Wisemanből"), ("Frigid Crags", "Frigid Crags", 67.7444, -151.5583), ["arctic", "mountain", "wildlife"],
    ("From the gravel strip at Wiseman over the Brooks Range: the granite spires of Frigid Crags, the Dalton Highway at Sukakpak and the Arrigetch Peaks.", "A wisemani murvás pályáról a Brooks-hegység fölött: a Frigid Crags gránittűi, a Dalton-főút Sukakpaknál és az Arrigetch-csúcsok."),
    L("WSM", [Pt("Sukakpak Mountain", "Sukakpak-hegy", "Sukakpak Mountain Dalton", 67.5833, -149.7000), Pt("Frigid Crags", "Frigid Crags", "Frigid Crags Boreal Mountain", 67.7444, -151.5583), Pt("Arrigetch Peaks", "Arrigetch-csúcsok", "Arrigetch Peaks Brooks Range", 67.3500, -154.1000)],
      ("Brooks Range loop", "Brooks-hegységi kör"), ("Sukakpak, Frigid Crags and the Arrigetch Peaks.", "Sukakpak, Frigid Crags és az Arrigetch-csúcsok."), kt=100, alt=7500))
add("NA", "stol-kantishna", C("United States", "Egyesült Államok"), ("Alaska: Denali from Kantishna", "Alaszka: a Denali Kantishnából"), ("Denali", "Denali", 63.0692, -151.0070), ["mountain", "glacier", "wildlife"],
    ("A short hop from the Kantishna strip to Wonder Lake, the Muldrow Glacier and the 6,190 m summit of Denali, North America's highest peak.", "Rövid ugrás a kantishnai pályáról a Wonder-tóhoz, a Muldrow-gleccserhez és a Denali 6190 méteres csúcsához, Észak-Amerika legmagasabb hegyéhez."),
    L("5Z5", [Pt("Wonder Lake", "Wonder-tó", "Wonder Lake Denali", 63.4667, -150.8667), Pt("Muldrow Glacier", "Muldrow-gleccser", "Muldrow Glacier Denali", 63.2800, -150.5000), Pt("Denali", "Denali", "Denali csúcs McKinley", 63.0692, -151.0070)],
      ("Denali loop", "Denali-kör"), ("Wonder Lake, Muldrow Glacier and Denali.", "Wonder-tó, Muldrow-gleccser és a Denali."), kt=100, alt=12000))
add("NA", "stol-lake-clark", C("United States", "Egyesült Államok"), ("Alaska: Lake Clark and Redoubt", "Alaszka: Clark-tó és Redoubt"), ("Lake Clark", "Clark-tó", 60.2000, -154.3000), ["lake", "volcano", "wildlife"],
    ("From Port Alsworth over the turquoise Lake Clark and Tanalian Falls to the smoking cones of Iliamna and Redoubt volcanoes.", "Port Alsworthből a türkiz Clark-tó és a Tanalian-vízesés fölött az Iliamna és a Redoubt füstölgő kúpjaihoz."),
    L("PALJ", [Pt("Tanalian Falls", "Tanalian-vízesés", "Tanalian Falls Lake Clark", 60.1800, -154.3100), Pt("Iliamna Volcano", "Iliamna-vulkán", "Iliamna Volcano Alaszka", 60.0319, -153.0919), Pt("Redoubt Volcano", "Redoubt-vulkán", "Redoubt Volcano Alaszka", 60.4853, -152.7430)],
      ("Lake Clark loop", "Clark-tó kör"), ("Tanalian Falls, Iliamna and Redoubt.", "Tanalian-vízesés, Iliamna és Redoubt."), kt=100, alt=7500))
add("NA", "stol-icy-strait", C("United States", "Egyesült Államok"), ("Alaska: Icy Strait and Glacier Bay", "Alaszka: Icy Strait és a Glacier-öböl"), ("Margerie Glacier", "Margerie-gleccser", 58.9000, -137.1000), ["glacier", "coast", "wildlife"],
    ("From little Hoonah across Icy Strait, past humpback feeding grounds at Point Adolphus to the calving Margerie Glacier and Mount Fairweather.", "A kis Hoonahból az Icy Strait felett, a Point Adolphus tengeri emlősei mellett a borjadzó Margerie-gleccserhez és a Fairweather-hegyhez."),
    L("PAOH", [Pt("Icy Strait Point", "Icy Strait Point", "Icy Strait Point Hoonah", 58.1194, -135.4519), Pt("Point Adolphus", "Point Adolphus", "Point Adolphus bálna", 58.2972, -135.9000), Pt("Margerie Glacier", "Margerie-gleccser", "Margerie Glacier Glacier Bay", 58.9000, -137.1000), Pt("Mount Fairweather", "Fairweather-hegy", "Mount Fairweather", 58.9061, -137.5300)],
      ("Glacier Bay loop", "Glacier Bay kör"), ("Icy Strait, Point Adolphus, Margerie Glacier and Fairweather.", "Icy Strait, Point Adolphus, Margerie-gleccser és Fairweather."), kt=100, alt=8500))
add("NA", "stol-molokai", C("United States", "Egyesült Államok"), ("Hawaii: Molokai and Kalaupapa", "Hawaii: Molokai és Kalaupapa"), ("Kalaupapa Peninsula", "Kalaupapa-félsziget", 21.2111, -156.9740), ["island", "coast", "waterfall"],
    ("The remote Kalaupapa peninsula under the world's tallest sea cliffs, Halawa Valley's waterfalls and the long beaches of western Molokai.", "A távoli Kalaupapa-félsziget a világ legmagasabb tengeri sziklái alatt, a Halawa-völgy vízesései és Molokai nyugati partjának hosszú strandjai."),
    L("PHLU", [Pt("Kaunakakai Wharf", "Kaunakakai-móló", "Kaunakakai móló Molokai", 21.0884, -157.0278), Pt("Papohaku Beach", "Papohaku-strand", "Papohaku Beach Molokai", 21.1594, -157.2825), Pt("Kamakou", "Kamakou", "Kamakou Molokai csúcs", 21.1128, -156.8903), Pt("Halawa Valley", "Halawa-völgy", "Halawa völgy Molokai vízesés", 21.1500, -156.7333)],
      ("Molokai loop", "Molokai-kör"), ("Kaunakakai, Papohaku, Kamakou and Halawa Valley.", "Kaunakakai, Papohaku, Kamakou és a Halawa-völgy."), kt=100, alt=4000))
add("NA", "stol-catalina", C("United States", "Egyesült Államok"), ("California: Catalina and the Channel Islands", "Kalifornia: Catalina és a Csatorna-szigetek"), ("Avalon Casino", "Avalon Kaszinó", 33.3455, -118.3255), ["island", "coast"],
    ("The Airport in the Sky on its mountaintop, the Art Deco casino of Avalon, the bays of Two Harbors and the wild outer islands of Santa Barbara and San Clemente.", "A hegytetői repülőtér, Avalon art deco kaszinója, a Two Harbors öblei és a vad külső szigetek, Santa Barbara és San Clemente."),
    L("KAVX", [Pt("Avalon Casino", "Avalon Kaszinó", "Avalon Casino Catalina", 33.3455, -118.3255), Pt("Two Harbors", "Two Harbors", "Two Harbors Catalina", 33.4430, -118.4975), Pt("Santa Barbara Island", "Santa Barbara-sziget", "Santa Barbara Island Channel Islands", 33.4783, -119.0383), Pt("San Clemente Island", "San Clemente-sziget", "San Clemente Island", 32.9000, -118.5000)],
      ("Catalina loop", "Catalina-kör"), ("Avalon, Two Harbors, Santa Barbara and San Clemente.", "Avalon, Two Harbors, Santa Barbara és San Clemente."), kt=100, alt=3500))
add("NA", "stol-san-juan", C("United States", "Egyesült Államok"), ("Washington: San Juan Islands", "Washington: a San Juan-szigetek"), ("Mount Constitution", "Mount Constitution", 48.6781, -122.6428), ["island", "coast", "wildlife"],
    ("From Friday Harbor over orca waters at Lime Kiln Point, the sculpture park at Roche Harbor, Mount Constitution and Deception Pass bridge.", "Friday Harborból a Lime Kiln Point kardszárnyú-bálnás vizei, a Roche Harbor szoborparkja, a Mount Constitution és a Deception Pass-híd fölött."),
    L("KFHR", [Pt("Lime Kiln Point", "Lime Kiln Point", "Lime Kiln Point világítótorony orka", 48.5158, -123.1519), Pt("Roche Harbor", "Roche Harbor", "Roche Harbor San Juan", 48.6086, -123.1558), Pt("Mount Constitution", "Mount Constitution", "Mount Constitution Orcas Island", 48.6781, -122.6428), Pt("Deception Pass", "Deception Pass", "Deception Pass híd", 48.4062, -122.6469)],
      ("San Juan loop", "San Juan-kör"), ("Lime Kiln, Roche Harbor, Mount Constitution and Deception Pass.", "Lime Kiln, Roche Harbor, Mount Constitution és Deception Pass."), kt=100, alt=3000))
add("NA", "stol-bella-coola", C("Canada", "Kanada"), ("British Columbia: Bella Coola and Hunlen Falls", "Brit Columbia: Bella Coola és a Hunlen-vízesés"), ("Hunlen Falls", "Hunlen-vízesés", 52.0700, -125.3600), ["mountain", "waterfall", "wildlife"],
    ("From the Bella Coola valley up to Hunlen Falls in Tweedsmuir Park, the icefields of Mount Waddington and the spirit bear coast of the Great Bear Rainforest.", "A Bella Coola-völgyből a Tweedsmuir Park Hunlen-vízeséséhez, a Waddington-hegy jégmezeihez és a Nagy Medve-esőerdő szellemmedvés partjához."),
    L("CYBD", [Pt("Hunlen Falls", "Hunlen-vízesés", "Hunlen Falls Tweedsmuir", 52.0700, -125.3600), Pt("Mount Waddington", "Waddington-hegy", "Mount Waddington Coast Mountains", 51.3769, -125.2614), Pt("Princess Royal Island", "Princess Royal-sziget", "Princess Royal Island spirit bear", 53.1000, -128.7000)],
      ("Coast Mountains loop", "Parti-hegységi kör"), ("Hunlen Falls, Mount Waddington and Princess Royal Island.", "Hunlen-vízesés, Waddington-hegy és Princess Royal-sziget."), kt=110, alt=9500))
add("NA", "stol-chilko", C("Canada", "Kanada"), ("British Columbia: Chilko Lake", "Brit Columbia: a Chilko-tó"), ("Chilko Lake", "Chilko-tó", 51.6000, -124.1000), ["lake", "mountain", "wildlife"],
    ("The turquoise glacial Chilko Lake in the Chilcotin, Tatlayoko Lake and the 4,019 m Mount Waddington, the highest peak wholly inside British Columbia.", "A Chilcotin türkizkék gleccsertava, a Chilko-tó, a Tatlayoko-tó és az 4019 méteres Waddington-hegy, Brit Columbia legmagasabb csúcsa."),
    L("CAG3", [Pt("Chilko Lake", "Chilko-tó", "Chilko Lake türkiz", 51.6000, -124.1000), Pt("Tatlayoko Lake", "Tatlayoko-tó", "Tatlayoko Lake", 51.6667, -124.4000), Pt("Mount Waddington", "Waddington-hegy", "Mount Waddington", 51.3769, -125.2614)],
      ("Chilcotin loop", "Chilcotin-kör"), ("Chilko Lake, Tatlayoko Lake and Mount Waddington.", "Chilko-tó, Tatlayoko-tó és a Waddington-hegy."), kt=100, alt=10500))
add("NA", "stol-baja-cortez", C("Mexico", "Mexikó"), ("Baja California: Sea of Cortez", "Baja California: a Cortez-tenger"), ("Bahía de los Ángeles", "Bahía de los Ángeles", 28.9500, -113.5500), ["desert", "coast", "island", "wildlife"],
    ("From the dirt strip at Punta San Francisquito along desert coast and whale-rich waters to Bahía de los Ángeles, Ángel de la Guarda island and Mulegé's palm oasis.", "A Punta San Francisquito földpályájáról a sivatagi parton és bálnákban gazdag vizeken át a Bahía de los Ángeleshez, az Ángel de la Guarda-szigethez és Mulegé pálmaoázisához."),
    L("MX-0006", [Pt("Bahía de los Ángeles", "Bahía de los Ángeles", "Bahía de los Ángeles Baja", 28.9500, -113.5500), Pt("Isla Ángel de la Guarda", "Ángel de la Guarda-sziget", "Isla Ángel de la Guarda", 29.1000, -113.3000), Pt("Santa Rosalía", "Santa Rosalía", "Santa Rosalía Baja Eiffel templom", 27.3350, -112.2650), Pt("Mulegé", "Mulegé", "Mulegé oázis Baja", 26.8833, -111.9833)],
      ("Sea of Cortez loop", "Cortez-tengeri kör"), ("Bahía de los Ángeles, Ángel de la Guarda, Santa Rosalía and Mulegé.", "Bahía de los Ángeles, Ángel de la Guarda, Santa Rosalía és Mulegé."), kt=110, alt=5500))
add("NA", "stol-belize-bluehole", C("Belize", "Belize"), ("Belize: Lighthouse Reef and the Blue Hole", "Belize: Lighthouse-zátony és a Kék lyuk"), ("Great Blue Hole", "Nagy Kék lyuk", 17.3156, -87.5347), ["reef", "island", "coast"],
    ("From a little dive-resort strip in the Belize cays over the 300 m wide Great Blue Hole, the booby colony of Half Moon Caye and the cays of Turneffe and Caye Caulker.", "A Lighthouse-zátony pályájáról a 300 méter széles Nagy Kék lyuk, a Half Moon Caye szulákolóniája, valamint a Turneffe és a Caye Caulker szigetei fölött."),
    L("MZHR", [Pt("Great Blue Hole", "Nagy Kék lyuk", "Great Blue Hole Belize", 17.3156, -87.5347), Pt("Half Moon Caye", "Half Moon Caye", "Half Moon Caye Belize", 17.2000, -87.5333), Pt("Turneffe Atoll", "Turneffe-atoll", "Turneffe Atoll Belize", 17.3500, -87.9500), Pt("Caye Caulker", "Caye Caulker", "Caye Caulker Belize", 17.7500, -88.0333)],
      ("Belize reef loop", "Belize-i zátony-kör"), ("The Blue Hole, Half Moon Caye, Turneffe and Caye Caulker.", "A Kék lyuk, Half Moon Caye, Turneffe és Caye Caulker."), kt=100, alt=3000))
add("NA", "stol-grenadines", C("Saint Vincent and the Grenadines", "Saint Vincent és a Grenadine-szigetek"), ("The Grenadines: Mustique and the Tobago Cays", "A Grenadine-szigetek: Mustique és a Tobago Cays"), ("Tobago Cays", "Tobago Cays", 12.6333, -61.3500), ["island", "reef", "coast"],
    ("From Mustique's grass-edged strip past Bequia's harbour to the five uninhabited Tobago Cays turtle reserve and Union Island's Clifton harbour.", "Mustique füves szélű pályájáról Bequia kikötője mellett az öt lakatlan Tobago Cays teknős-rezervátumhoz és Union Island Clifton kikötőjéhez."),
    L("TVSM", [Pt("Bequia", "Bequia", "Bequia Admiralty Bay", 13.0167, -61.2333), Pt("Tobago Cays", "Tobago Cays", "Tobago Cays teknős", 12.6333, -61.3500), Pt("Union Island", "Union Island", "Union Island Clifton", 12.6000, -61.4167)],
      ("Grenadines loop", "Grenadine-kör"), ("Bequia, the Tobago Cays and Union Island.", "Bequia, a Tobago Cays és Union Island."), kt=100, alt=2500))
add("NA", "stol-little-cayman", C("Cayman Islands", "Kajmán-szigetek"), ("Cayman: Little Cayman and Cayman Brac", "Kajmán-szigetek: Little Cayman és Cayman Brac"), ("Bloody Bay Wall", "Bloody Bay-fal", 19.6850, -80.0780), ["island", "reef", "coast"],
    ("The tiny Little Cayman and its Bloody Bay Wall, Cayman Brac's 43 m limestone Bluff and the stingrays of Grand Cayman's North Sound.", "A parányi Little Cayman és a Bloody Bay-fal, Cayman Brac 43 méteres mészkőbérce és Grand Cayman North Sound-jának ráják."),
    L("MWCL", [Pt("Bloody Bay Wall", "Bloody Bay-fal", "Bloody Bay Wall Little Cayman", 19.6850, -80.0780), Pt("Cayman Brac Bluff", "Cayman Brac-bérc", "Cayman Brac Bluff", 19.7000, -79.8000), Pt("Stingray City", "Stingray City", "Stingray City Grand Cayman", 19.3667, -81.3000)],
      ("Cayman loop", "Kajmán-kör"), ("Bloody Bay Wall, the Bluff and Stingray City.", "Bloody Bay-fal, a Bérc és a Stingray City."), kt=100, alt=3000))
add("NA", "stol-les-saintes", C("France", "Franciaország"), ("Guadeloupe: Les Saintes and the Soufrière", "Guadeloupe: Les Saintes és a Soufrière"), ("La Soufrière", "La Soufrière", 16.0444, -61.6639), ["island", "volcano", "coast"],
    ("From the 600 m strip on Terre-de-Haut to Fort Napoléon over the Les Saintes bay, the steaming Soufrière volcano and the white cliffs of Pointe des Châteaux.", "A Terre-de-Haut 600 méteres pályájáról a Napóleon-erőd és a Les Saintes-öböl fölött a gőzölgő Soufrière-vulkánhoz és a Pointe des Châteaux fehér sziklái felé."),
    L("TFFS", [Pt("Fort Napoléon", "Napóleon-erőd", "Fort Napoléon Les Saintes", 15.8667, -61.5833), Pt("La Soufrière", "La Soufrière", "La Soufrière vulkán Guadeloupe", 16.0444, -61.6639), Pt("Pointe des Châteaux", "Pointe des Châteaux", "Pointe des Châteaux Guadeloupe", 16.2500, -61.1833), Pt("Marie-Galante", "Marie-Galante", "Marie-Galante sziget", 15.9000, -61.2667)],
      ("Guadeloupe loop", "Guadeloupe-kör"), ("Fort Napoléon, La Soufrière, Pointe des Châteaux and Marie-Galante.", "Napóleon-erőd, La Soufrière, Pointe des Châteaux és Marie-Galante."), kt=100, alt=5500))

# ------------------------------------------------------------------ DEL-AMERIKA
add("SA", "stol-los-roques", C("Venezuela", "Venezuela"), ("Venezuela: Los Roques Archipelago", "Venezuela: a Los Roques-szigetcsoport"), ("Gran Roque", "Gran Roque", 11.9494, -66.6692), ["island", "reef", "coast"],
    ("Fifty coral cays and white sandbars in turquoise water, with the lighthouse village of Gran Roque as the only settlement.", "Ötven korallsziget és fehér homokpad türkizkék vízben, egyetlen településsel: a világítótornyos Gran Roque faluval."),
    L("SVRS", [Pt("Gran Roque", "Gran Roque", "Gran Roque Los Roques", 11.9494, -66.6692), Pt("Francisqui", "Francisqui", "Francisqui Los Roques", 11.9569, -66.7239), Pt("Cayo de Agua", "Cayo de Agua", "Cayo de Agua Los Roques", 11.8744, -66.8183), Pt("Dos Mosquises", "Dos Mosquises", "Dos Mosquises Los Roques", 11.8000, -66.9000)],
      ("Los Roques loop", "Los Roques-kör"), ("Gran Roque, Francisqui, Cayo de Agua and Dos Mosquises.", "Gran Roque, Francisqui, Cayo de Agua és Dos Mosquises."), kt=100, alt=2500))
add("SA", "stol-juan-fernandez", C("Chile", "Chile"), ("Chile: Robinson Crusoe Island", "Chile: Robinson Crusoe-sziget"), ("Cumberland Bay", "Cumberland-öböl", -33.6372, -78.8350), ["island", "mountain", "coast"],
    ("The volcanic island where Alexander Selkirk was marooned: the green peak of El Yunque, the village of San Juan Bautista and distant Alexander Selkirk Island.", "A vulkáni sziget, ahol Alexander Selkirk kimaradt: az El Yunque zöld csúcsa, San Juan Bautista falu és a távoli Alexander Selkirk-sziget."),
    L("SCIR", [Pt("San Juan Bautista", "San Juan Bautista", "San Juan Bautista Juan Fernández", -33.6372, -78.8350), Pt("El Yunque", "El Yunque", "El Yunque Juan Fernández", -33.6389, -78.9611), Pt("Alexander Selkirk Island", "Alexander Selkirk-sziget", "Alexander Selkirk Island Más Afuera", -33.7667, -80.7833)],
      ("Robinson Crusoe loop", "Robinson Crusoe-kör"), ("San Juan Bautista, El Yunque and Alexander Selkirk Island.", "San Juan Bautista, El Yunque és az Alexander Selkirk-sziget."), kt=100, alt=3500))
add("SA", "stol-falklands", C("Falkland Islands", "Falkland-szigetek"), ("Falkland Islands: Stanley and Volunteer Point", "Falkland-szigetek: Stanley és Volunteer Point"), ("Stanley", "Stanley", -51.6931, -57.8497), ["coast", "wildlife", "island"],
    ("Stanley's Christ Church Cathedral and the whale-bone arch, Gypsy Cove's penguins, the Cape Pembroke lighthouse and Mount Tumbledown's war memorial.", "Stanley székesegyháza és a bálnacsont-kapu, a Gypsy Cove pingvinjei, a Cape Pembroke világítótorony és a Mount Tumbledown hadiemlékműve."),
    L("SFAL", [Pt("Cape Pembroke Lighthouse", "Cape Pembroke világítótorony", "Cape Pembroke Lighthouse", -51.6844, -57.7050), Pt("Gypsy Cove", "Gypsy Cove", "Gypsy Cove pingvin Stanley", -51.6747, -57.8007), Pt("Stanley Cathedral", "Stanley székesegyház", "Stanley Christ Church Cathedral", -51.6931, -57.8497), Pt("Volunteer Point", "Volunteer Point", "Volunteer Point királypingvin", -51.4747, -57.7747)],
      ("Falklands loop", "Falkland-kör"), ("Cape Pembroke, Gypsy Cove, Stanley and Volunteer Point.", "Cape Pembroke, Gypsy Cove, Stanley és Volunteer Point."), kt=100, alt=3000))
add("SA", "stol-general-carrera", C("Chile", "Chile"), ("Chile: Lago General Carrera and the Marble Caves", "Chile: General Carrera-tó és a Márványbarlangok"), ("Marble Caves", "Márványbarlangok", -46.6500, -72.9833), ["lake", "mountain", "unesco"],
    ("The swirling blue Marble Caves on Lago General Carrera, Chile Chico on the Argentine border, the Cerro Castillo massif and the river village of Cochrane.", "A General Carrera-tó kavargó kék márványbarlangjai, az argentin határ melletti Chile Chico, a Cerro Castillo-hegység és Cochrane folyóparti falu."),
    L("SCCC", [Pt("Marble Caves", "Márványbarlangok", "Marble Caves Capillas de Mármol", -46.6500, -72.9833), Pt("Cerro Castillo", "Cerro Castillo", "Cerro Castillo hegy Patagónia", -46.1167, -72.1500), Pt("Cochrane", "Cochrane", "Cochrane Chile Patagónia", -47.2500, -72.5667)],
      ("Carrera lake loop", "Carrera-tavi kör"), ("The Marble Caves, Cerro Castillo and Cochrane.", "A Márványbarlangok, Cerro Castillo és Cochrane."), kt=110, alt=9500))

add("NA", "stol-staniel", C("Bahamas", "Bahama-szigetek"), ("Bahamas: Exuma Cays from Staniel Cay", "Bahama-szigetek: az Exuma-szigetek Staniel Cay-ből"), ("Thunderball Grotto", "Thunderball-barlang", 24.1694, -76.4467), ["island", "reef", "coast"],
    ("Pastel-blue shallows and sandbars of the Exuma Cays: the Thunderball Grotto from the Bond film, the swimming pigs of Big Major Cay and the Land and Sea Park.", "Az Exuma-szigetek pasztellkék sekélyei és homokpadjai: a Bond-filmből ismert Thunderball-barlang, a Big Major Cay úszó malacai és a Land and Sea Park."),
    L("MYES", [Pt("Thunderball Grotto", "Thunderball-barlang", "Thunderball Grotto Staniel Cay", 24.1694, -76.4467), Pt("Big Major Cay", "Big Major Cay", "Big Major Cay malacok", 24.1844, -76.4617), Pt("Compass Cay", "Compass Cay", "Compass Cay Exuma", 24.2667, -76.5167), Pt("Warderick Wells", "Warderick Wells", "Warderick Wells Exuma Land and Sea Park", 24.3969, -76.6272)],
      ("Exuma loop", "Exuma-kör"), ("Thunderball Grotto, Big Major, Compass Cay and Warderick Wells.", "Thunderball-barlang, Big Major, Compass Cay és Warderick Wells."), kt=100, alt=2000))
add("NA", "stol-nain", C("Canada", "Kanada"), ("Labrador: Torngat Mountains from Nain", "Labrador: a Torngat-hegység Nainból"), ("Mount Caubvick", "Caubvick-hegy", 58.6522, -63.3947), ["mountain", "arctic", "coast"],
    ("From the Inuit village of Nain north along the fjords of Labrador to Saglek, Hebron and the Torngat peaks, home of polar bears and ancient Inuit sites.", "Az inuit Nain faluból északra a labradori fjordok mentén Sagleket, Hebront és a Torngat-csúcsokat érintve, jegesmedvék és ősi inuit helyek földjén."),
    L("CYDP", [Pt("Hebron Fjord", "Hebron-fjord", "Hebron Fjord Labrador", 58.2000, -62.6000), Pt("Saglek Fjord", "Saglek-fjord", "Saglek Fjord Torngat", 58.4500, -62.7000), Pt("Mount Caubvick", "Caubvick-hegy", "Mount Caubvick Torngat", 58.6522, -63.3947)],
      ("Torngat loop", "Torngat-kör"), ("Hebron and Saglek fjords and Mount Caubvick.", "Hebron- és Saglek-fjord és a Caubvick-hegy."), kt=120, alt=6000))
add("NA", "stol-skagway", C("United States", "Egyesült Államok"), ("Alaska: Skagway and the Klondike Gold Rush Trail", "Alaszka: Skagway és a klondike-i aranyláz útja"), ("White Pass", "White Pass", 59.6167, -135.1500), ["mountain", "glacier", "history"],
    ("From Skagway's strip up the Chilkoot and White Pass trails of the 1898 gold rush, then to Davidson Glacier and Haines on the Lynn Canal.", "Skagway pályájáról az 1898-as aranyláz Chilkoot- és White Pass-ösvényein át a Davidson-gleccserhez és Haines városához a Lynn-csatornán."),
    L("PAGY", [Pt("White Pass", "White Pass", "White Pass Skagway", 59.6167, -135.1500), Pt("Chilkoot Pass", "Chilkoot-hágó", "Chilkoot Pass", 59.5681, -135.2347), Pt("Davidson Glacier", "Davidson-gleccser", "Davidson Glacier Haines", 59.1500, -135.5000), Pt("Haines", "Haines", "Haines Alaszka", 59.2358, -135.4453)],
      ("Gold Rush loop", "Aranyláz-kör"), ("White Pass, Chilkoot Pass, Davidson Glacier and Haines.", "White Pass, Chilkoot-hágó, Davidson-gleccser és Haines."), kt=100, alt=5500))

# ------------------------------------------------------------------ EUROPA
add("EU", "stol-scilly", C("United Kingdom", "Egyesült Királyság"), ("Isles of Scilly from St Mary's", "A Scilly-szigetek St Mary's-ből"), ("Tresco Abbey Garden", "Tresco apátsági kert", 49.9533, -6.3317), ["island", "coast", "history"],
    ("The subtropical garden of Tresco, the shipwreck-strewn Bishop Rock lighthouse and the white sands of Bryher and St Martin's, 45 km off Cornwall.", "Tresco szubtrópusi kertje, a hajóroncsok közt álló Bishop Rock világítótorony, Bryher és St Martin's fehér homokja Cornwalltól 45 km-re."),
    L("EGHE", [Pt("Tresco Abbey Garden", "Tresco apátsági kert", "Tresco Abbey Garden", 49.9533, -6.3317), Pt("Bryher", "Bryher", "Bryher Scilly", 49.9553, -6.3500), Pt("Bishop Rock Lighthouse", "Bishop Rock világítótorony", "Bishop Rock Lighthouse", 49.8722, -6.4472), Pt("St Martin's", "St Martin's", "St Martin's Scilly", 49.9650, -6.2740)],
      ("Scilly loop", "Scilly-kör"), ("Tresco, Bryher, Bishop Rock and St Martin's.", "Tresco, Bryher, Bishop Rock és St Martin's."), kt=100, alt=1500))
add("EU", "stol-orkney", C("United Kingdom", "Egyesült Királyság"), ("Orkney: Papa Westray and the Neolithic Heart", "Orkney: Papa Westray és a neolitikus szív"), ("Ring of Brodgar", "Brodgar-kőkör", 58.9976, -3.2297), ["island", "history", "coast"],
    ("The world's shortest scheduled flight lands on Papa Westray, home of the Knap of Howar; fly on to Skara Brae, the Ring of Brodgar and the Old Man of Hoy sea stack.", "A világ legrövidebb menetrend szerinti járata Papa Westrayen száll le, a Knap of Howar otthonán; innen tovább Skara Braehoz, a Brodgar-kőkörhöz és az Old Man of Hoy tengeri toronyhoz."),
    L("EGEP", [Pt("Knap of Howar", "Knap of Howar", "Knap of Howar Papa Westray", 59.3356, -2.8908), Pt("Ring of Brodgar", "Brodgar-kőkör", "Ring of Brodgar", 58.9976, -3.2297), Pt("Skara Brae", "Skara Brae", "Skara Brae Orkney", 59.0489, -3.3417), Pt("Old Man of Hoy", "Old Man of Hoy", "Old Man of Hoy", 58.8964, -3.3189)],
      ("Orkney loop", "Orkney-kör"), ("Knap of Howar, Brodgar, Skara Brae and the Old Man of Hoy.", "Knap of Howar, Brodgar, Skara Brae és az Old Man of Hoy."), kt=100, alt=1500))
add("EU", "stol-barra", C("United Kingdom", "Egyesült Királyság"), ("Outer Hebrides: Barra and the Beach Runway", "Külső-Hebridák: Barra és a strandpálya"), ("Kisimul Castle", "Kisimul-vár", 56.9528, -7.4875), ["island", "coast", "history"],
    ("The only airport in the world with a tidal beach runway: Cockle Strand, then Kisimul Castle, Vatersay, abandoned Mingulay and Eriskay.", "A világ egyetlen dagálytól függő strandpályás repülőtere: Cockle Strand, majd a Kisimul-vár, Vatersay, az elhagyott Mingulay és Eriskay."),
    L("EGPR", [Pt("Kisimul Castle", "Kisimul-vár", "Kisimul Castle Barra", 56.9528, -7.4875), Pt("Vatersay", "Vatersay", "Vatersay sziget", 56.9167, -7.5333), Pt("Mingulay", "Mingulay", "Mingulay sziget", 56.8000, -7.6333), Pt("Eriskay", "Eriskay", "Eriskay sziget", 57.0667, -7.3000)],
      ("Barra loop", "Barra-kör"), ("Kisimul Castle, Vatersay, Mingulay and Eriskay.", "Kisimul-vár, Vatersay, Mingulay és Eriskay."), kt=100, alt=1500))
add("EU", "stol-roest", C("Norway", "Norvégia"), ("Lofoten: Røst and the Maelstrom", "Lofoten: Røst és a Moskstraumen"), ("Moskstraumen", "Moskstraumen", 67.7500, 12.8000), ["island", "coast", "wildlife"],
    ("From the lowest and most remote of the Lofoten islands, Røst, past the Moskstraumen whirlpool and Værøy to the red fishing cabins of Reine and Hamnøy.", "A Lofoten legalacsonyabb és legtávolabbi szigetéről, Røstról a Moskstraumen forgatag és Værøy mellett Reine és Hamnøy vörös halászkunyhóihoz."),
    L("ENRS", [Pt("Værøy", "Værøy", "Værøy sziget", 67.6667, 12.6667), Pt("Moskstraumen", "Moskstraumen", "Moskstraumen maelstrom", 67.7500, 12.8000), Pt("Reine", "Reine", "Reine Lofoten", 67.9333, 13.0833), Pt("Hamnøy", "Hamnøy", "Hamnøy Lofoten", 67.9500, 13.1333)],
      ("Lofoten loop", "Lofoten-kör"), ("Værøy, the Moskstraumen, Reine and Hamnøy.", "Værøy, a Moskstraumen, Reine és Hamnøy."), kt=100, alt=2500))
add("EU", "stol-losinj", C("Croatia", "Horvátország"), ("Croatia: Lošinj, Cres and the Kvarner Islands", "Horvátország: Lošinj, Cres és a Kvarner-szigetek"), ("Veli Lošinj", "Veli Lošinj", 44.5167, 14.4833), ["island", "coast"],
    ("A tiny island strip as the base for the Kvarner Gulf: Veli Lošinj's harbour, the old town of Cres, sandy Susak and the walls of Rab.", "Apró szigeti pálya a Kvarner-öböl bejárásához: Veli Lošinj kikötője, Cres óvárosa, a homokos Susak és Rab falai."),
    L("LDLO", [Pt("Veli Lošinj", "Veli Lošinj", "Veli Lošinj kikötő", 44.5167, 14.4833), Pt("Susak", "Susak", "Susak sziget", 44.5083, 14.3000), Pt("Cres", "Cres", "Cres város", 44.9603, 14.4117), Pt("Rab", "Rab", "Rab óváros", 44.7567, 14.7600)],
      ("Kvarner loop", "Kvarner-kör"), ("Veli Lošinj, Susak, Cres and Rab.", "Veli Lošinj, Susak, Cres és Rab."), kt=100, alt=2000))
add("EU", "stol-grimsey", C("Iceland", "Izland"), ("Iceland: Grímsey and the Arctic Circle", "Izland: Grímsey és a sarkkör"), ("Grímsey", "Grímsey", 66.5458, -18.0173), ["island", "arctic", "coast", "waterfall"],
    ("The only part of Iceland inside the Arctic Circle, puffin cliffs, then Hrísey, Drangey with its seabird cliffs and Goðafoss waterfall.", "Izland egyetlen sarkkörön belüli része, lundás sziklák, majd Hrísey, a madárhegyes Drangey és a Goðafoss-vízesés."),
    L("BIGR", [Pt("Hrísey", "Hrísey", "Hrísey sziget", 66.0167, -18.3833), Pt("Drangey", "Drangey", "Drangey sziget", 65.9667, -19.7167), Pt("Goðafoss", "Goðafoss", "Goðafoss vízesés", 65.6828, -17.5500)],
      ("Arctic Circle loop", "Sarkköri kör"), ("Hrísey, Drangey and Goðafoss.", "Hrísey, Drangey és Goðafoss."), kt=110, alt=3500))
add("EU", "stol-heimaey", C("Iceland", "Izland"), ("Iceland: Heimaey and the Westman Islands", "Izland: Heimaey és a Vestmann-szigetek"), ("Eldfell", "Eldfell", 63.4264, -20.2578), ["island", "volcano", "coast"],
    ("The Heimaey volcano that buried half a town in 1973, the brand-new island of Surtsey, Eyjafjallajökull and the cliffs of Skógafoss.", "A Heimaey vulkán, amely 1973-ban a város felét betemette, az új Surtsey-sziget, az Eyjafjallajökull és a Skógafoss szikláit."),
    L("BIVM", [Pt("Eldfell", "Eldfell", "Eldfell Heimaey", 63.4264, -20.2578), Pt("Surtsey", "Surtsey", "Surtsey sziget", 63.3033, -20.6044), Pt("Eyjafjallajökull", "Eyjafjallajökull", "Eyjafjallajökull", 63.6333, -19.6000), Pt("Skógafoss", "Skógafoss", "Skógafoss vízesés", 63.5320, -19.5114)],
      ("Westman loop", "Vestmann-kör"), ("Eldfell, Surtsey, Eyjafjallajökull and Skógafoss.", "Eldfell, Surtsey, Eyjafjallajökull és Skógafoss."), kt=100, alt=3000))
add("EU", "stol-corvo", C("Portugal", "Portugália"), ("Azores: Corvo and Flores", "Azori-szigetek: Corvo és Flores"), ("Caldeirão do Corvo", "Caldeirão do Corvo", 39.7050, -31.1100), ["island", "volcano", "waterfall"],
    ("Europe's smallest inhabited westernmost island Corvo with its volcanic crater lake, then Flores with its cascading waterfalls at Fajã Grande.", "Európa legkisebb, legnyugatabbra fekvő lakott szigete, Corvo vulkáni kráterével, majd Flores zuhatagai Fajã Grandénál."),
    L("LPCR", [Pt("Caldeirão do Corvo", "Caldeirão do Corvo", "Caldeirão do Corvo kráter", 39.7050, -31.1100), Pt("Fajã Grande", "Fajã Grande", "Fajã Grande Flores vízesés", 39.4550, -31.2650)],
      ("Corvo and Flores loop", "Corvo–Flores kör"), ("The Corvo crater and the Fajã Grande waterfalls on Flores.", "A Corvo-kráter és a Fajã Grande vízesései Floresen."), kt=100, alt=3000))
add("EU", "stol-el-hierro", C("Spain", "Spanyolország"), ("Canary Islands: El Hierro and La Gomera", "Kanári-szigetek: El Hierro és La Gomera"), ("Garajonay", "Garajonay", 28.1186, -17.2371), ["island", "volcano", "forest", "unesco"],
    ("The windswept junipers of El Sabinar, Orchilla lighthouse (once the zero meridian), the black cones of La Restinga and the cloud forest of Garajonay.", "El Sabinar szélfútta boróka-erdője, az Orchilla-világítótorony (egykor a nullmeridián), La Restinga fekete kúpjai és Garajonay felhőerdeje."),
    L("GCHI", [Pt("El Sabinar", "El Sabinar", "El Sabinar El Hierro boróka", 27.7150, -18.0290), Pt("Orchilla Lighthouse", "Orchilla világítótorony", "Faro de Orchilla", 27.7000, -18.1300), Pt("La Restinga", "La Restinga", "La Restinga El Hierro", 27.6300, -17.9800), Pt("Garajonay", "Garajonay", "Garajonay La Gomera", 28.1186, -17.2371)],
      ("Hierro loop", "Hierro-kör"), ("El Sabinar, Orchilla, La Restinga and Garajonay.", "El Sabinar, Orchilla, La Restinga és Garajonay."), kt=100, alt=3500))
add("EU", "stol-la-gomera", C("Spain", "Spanyolország"), ("La Gomera and the Teide", "La Gomera és a Teide"), ("Mount Teide", "Teide", 28.2723, -16.6425), ["island", "volcano", "mountain"],
    ("From La Gomera's clifftop strip over the Los Órganos basalt columns and Valle Gran Rey to the 3,718 m volcano Teide on Tenerife.", "La Gomera sziklaszélén álló pályájáról a Los Órganos bazaltoszlopai és a Valle Gran Rey fölött a tenerifei Teide 3718 méteres vulkánjához."),
    L("GCGM", [Pt("Valle Gran Rey", "Valle Gran Rey", "Valle Gran Rey La Gomera", 28.1000, -17.3333), Pt("Los Órganos", "Los Órganos", "Los Órganos La Gomera bazalt", 28.1850, -17.3270), Pt("Mount Teide", "Teide", "Teide vulkán Tenerife", 28.2723, -16.6425)],
      ("Gomera and Teide loop", "Gomera–Teide kör"), ("Valle Gran Rey, Los Órganos and Teide.", "Valle Gran Rey, Los Órganos és a Teide."), kt=100, alt=6000))
add("EU", "stol-gstaad", C("Switzerland", "Svájc"), ("Switzerland: Gstaad and the Bernese Alps", "Svájc: Gstaad és a Berni-Alpok"), ("Eiger", "Eiger", 46.5775, 8.0053), ["mountain", "glacier", "unesco"],
    ("From Saanen's grass-edged airfield beside Gstaad to the Eiger, Mönch and Jungfrau, the Aletsch Glacier and the Matterhorn.", "Saanen füves szélű repülőteréről Gstaad mellett az Eigerhez, a Mönchhöz és a Jungfrauhoz, az Aletsch-gleccserhez és a Matterhornhoz."),
    L("LSGK", [Pt("Eiger", "Eiger", "Eiger északi fal", 46.5775, 8.0053), Pt("Jungfrau", "Jungfrau", "Jungfrau csúcs", 46.5368, 7.9626), Pt("Aletsch Glacier", "Aletsch-gleccser", "Aletsch-gleccser", 46.4500, 8.0500), Pt("Matterhorn", "Matterhorn", "Matterhorn", 45.9766, 7.6585)],
      ("Bernese Alps loop", "Berni-Alpok kör"), ("Eiger, Jungfrau, Aletsch Glacier and the Matterhorn.", "Eiger, Jungfrau, Aletsch-gleccser és Matterhorn."), kt=100, alt=11000))
add("EU", "stol-pantelleria", C("Italy", "Olaszország"), ("Sicily Channel: Pantelleria, Linosa and Lampedusa", "Szicíliai-csatorna: Pantelleria, Linosa és Lampedusa"), ("Pantelleria", "Pantelleria", 36.8333, 11.9833), ["island", "volcano", "coast"],
    ("The black volcanic island of Pantelleria with its dry-stone dammusi, the Arco dell'Elefante, and the remote Linosa and Lampedusa off the Tunisian coast.", "A fekete vulkáni Pantelleria szárazkő dammusijaival, az Arco dell'Elefante, valamint a tunéziai part előtti távoli Linosa és Lampedusa."),
    L("LICG", [Pt("Arco dell'Elefante", "Arco dell'Elefante", "Arco dell'Elefante Pantelleria", 36.8333, 11.9833), Pt("Montagna Grande", "Montagna Grande", "Montagna Grande Pantelleria", 36.7889, 12.0089), Pt("Linosa", "Linosa", "Linosa sziget", 35.8667, 12.8667), Pt("Lampedusa", "Lampedusa", "Lampedusa sziget", 35.5000, 12.6000)],
      ("Sicily Channel loop", "Szicíliai-csatorna kör"), ("The elephant arch, Montagna Grande, Linosa and Lampedusa.", "Az elefántív, Montagna Grande, Linosa és Lampedusa."), kt=110, alt=3500))

# ------------------------------------------------------------------ AZSIA
add("AS", "stol-lukla", C("Nepal", "Nepál"), ("Nepal: Lukla and the Khumbu", "Nepál: Lukla és a Khumbu"), ("Mount Everest", "Mount Everest", 27.9881, 86.9250), ["mountain", "glacier", "unesco"],
    ("The famous sloped runway of Tenzing-Hillary: only 527 m with a cliff edge at the end. Then Namche Bazaar, Ama Dablam, the Gokyo lakes and Everest itself.", "A Tenzing–Hillary lejtős kifutója: mindössze 527 méter, a végén szakadékkal. Majd Namche Bazaar, az Ama Dablam, a Gokyo-tavak és maga az Everest."),
    L("VNLK", [Pt("Namche Bazaar", "Namche Bazaar", "Namche Bazaar", 27.8069, 86.7140), Pt("Ama Dablam", "Ama Dablam", "Ama Dablam", 27.8617, 86.8614), Pt("Mount Everest", "Mount Everest", "Mount Everest", 27.9881, 86.9250), Pt("Gokyo Lakes", "Gokyo-tavak", "Gokyo-tavak", 27.9550, 86.6950)],
      ("Khumbu loop", "Khumbu-kör"), ("Namche Bazaar, Ama Dablam, Everest and the Gokyo Lakes.", "Namche Bazaar, Ama Dablam, Everest és a Gokyo-tavak."), kt=90, alt=17500))
add("AS", "stol-jumla", C("Nepal", "Nepál"), ("Nepal: Jumla, Rara Lake and Dolpo", "Nepál: Jumla, a Rara-tó és Dolpo"), ("Rara Lake", "Rara-tó", 29.5300, 82.0900), ["lake", "mountain"],
    ("From Jumla's 660 m strip to Nepal's largest lake, Rara, the Kanjiroba range and the turquoise Phoksundo Lake in the Dolpo wilderness.", "Jumla 660 méteres pályájáról Nepál legnagyobb tavához, a Rarához, a Kanjiroba-hegységhez és a türkizkék Phoksundo-tóhoz a Dolpo vadonjában."),
    L("VNJL", [Pt("Rara Lake", "Rara-tó", "Rara-tó Nepál", 29.5300, 82.0900), Pt("Kanjiroba", "Kanjiroba", "Kanjiroba Himal", 29.5333, 82.7667), Pt("Phoksundo Lake", "Phoksundo-tó", "Phoksundo-tó Dolpo", 29.1983, 82.9467)],
      ("Jumla loop", "Jumla-kör"), ("Rara Lake, Kanjiroba and Phoksundo Lake.", "Rara-tó, Kanjiroba és Phoksundo-tó."), kt=100, alt=14500))
add("AS", "stol-bumthang", C("Bhutan", "Bhután"), ("Bhutan: Bumthang and the Spiritual Heartland", "Bhután: Bumthang és a spirituális szívvidék"), ("Jakar Dzong", "Jakar Dzong", 27.5500, 90.7400), ["mountain", "history", "temple"],
    ("The remote Bumthang valley's Jakar Dzong, the Trongsa fortress and high above them the unclimbed peak Gangkar Puensum, the world's highest unclimbed mountain.", "A távoli Bumthang-völgy Jakar Dzongja, a trongsai erődkolostor és fölöttük a világ legmagasabb meghódítatlan hegye, a Gangkar Puensum."),
    L("VQBT", [Pt("Jakar Dzong", "Jakar Dzong", "Jakar Dzong Bumthang", 27.5500, 90.7400), Pt("Trongsa Dzong", "Trongsa Dzong", "Trongsa Dzong", 27.5011, 90.5081), Pt("Gangkar Puensum", "Gangkar Puensum", "Gangkar Puensum", 28.0467, 90.4547)],
      ("Bumthang loop", "Bumthang-kör"), ("Jakar Dzong, Trongsa Dzong and Gangkar Puensum.", "Jakar Dzong, Trongsa Dzong és Gangkar Puensum."), kt=100, alt=13500))

# ------------------------------------------------------------------ AFRIKA
add("AF", "stol-okavango-kiri", C("Botswana", "Botswana"), ("Botswana: Okavango Delta from Kiri", "Botswana: az Okavango-delta Kiriből"), ("Chief's Island", "Chief's Island", -19.4500, 23.1000), ["wildlife", "wetland", "unesco"],
    ("A bush strip deep inside the Delta: papyrus lagoons, elephant trails on Chief's Island, Xakanaxa's hippo channels and the lions of Savuti marsh.", "Bokorpálya a delta mélyén: papirusz-lagúnák, elefántösvények Chief's Islanden, Xakanaxa víziló-csatornái és a Savuti-mocsár oroszlánjai."),
    L("FBKI", [Pt("Chief's Island", "Chief's Island", "Chief's Island Okavango", -19.4500, 23.1000), Pt("Xakanaxa", "Xakanaxa", "Xakanaxa Moremi", -19.2167, 23.4167), Pt("Savuti", "Savuti", "Savuti Chobe", -18.5667, 24.0667)],
      ("Delta loop", "Delta-kör"), ("Chief's Island, Xakanaxa and Savuti.", "Chief's Island, Xakanaxa és Savuti."), kt=100, alt=1500))
add("AF", "stol-desroches", C("Seychelles", "Seychelle-szigetek"), ("Seychelles: Desroches, Poivre and Praslin", "Seychelle-szigetek: Desroches, Poivre és Praslin"), ("Vallée de Mai", "Vallée de Mai", -4.3333, 55.7333), ["island", "reef", "unesco"],
    ("From the outer Amirantes coral island of Desroches over remote Poivre Atoll, to the coco de mer palms of Vallée de Mai and La Digue's granite beaches.", "A Seychelle külső Amirante-szigeteinek korallszigetéről, Desrochesről a távoli Poivre-atoll fölött a Vallée de Mai coco de mer pálmáihoz és La Digue gránit-strandjaihoz."),
    L("FSDR", [Pt("Poivre Atoll", "Poivre-atoll", "Poivre Atoll Amirantes", -5.7500, 53.3167), Pt("Vallée de Mai", "Vallée de Mai", "Vallée de Mai Praslin", -4.3333, 55.7333), Pt("Anse Source d'Argent", "Anse Source d'Argent", "Anse Source d'Argent La Digue", -4.3667, 55.8333)],
      ("Amirantes loop", "Amirante-kör"), ("Poivre Atoll, Vallée de Mai and Anse Source d'Argent.", "Poivre-atoll, Vallée de Mai és Anse Source d'Argent."), kt=110, alt=2500))
add("AF", "stol-lake-malawi", C("Malawi", "Malawi"), ("Malawi: Cape Maclear and Lake Malawi", "Malawi: Cape Maclear és a Malawi-tó"), ("Cape Maclear", "Cape Maclear", -14.0167, 34.8333), ["lake", "island", "wildlife"],
    ("The Lake of Stars: Cape Maclear's granite coves, Mumbo island's cichlid reefs and Likoma island with its cathedral on the Mozambican shore.", "A Csillagok tava: Cape Maclear gránitöblei, Mumbo-sziget sügér-zátonyai és Likoma-sziget katedrálisa a mozambiki part mellett."),
    L("FWCM", [Pt("Cape Maclear", "Cape Maclear", "Cape Maclear Malawi", -14.0167, 34.8333), Pt("Mumbo Island", "Mumbo-sziget", "Mumbo Island Lake Malawi", -13.9833, 34.8167), Pt("Likoma Island", "Likoma-sziget", "Likoma Island", -12.0667, 34.7333)],
      ("Lake Malawi loop", "Malawi-tavi kör"), ("Cape Maclear, Mumbo and Likoma.", "Cape Maclear, Mumbo és Likoma."), kt=110, alt=3000))

# ------------------------------------------------------------------ OCEANIA
add("OC", "stol-great-barrier", C("New Zealand", "Új-Zéland"), ("New Zealand: Great Barrier Island and the Hauraki Gulf", "Új-Zéland: Great Barrier-sziget és a Hauraki-öböl"), ("Hirakimata", "Hirakimata", -36.2000, 175.4833), ["island", "coast", "wildlife"],
    ("Off-grid Great Barrier Island's Hirakimata peak, Port Fitzroy's sheltered harbour, Little Barrier's bird sanctuary and the Cuvier lighthouse.", "A hálózatról lekapcsolt Great Barrier-sziget Hirakimata-csúcsa, Port Fitzroy védett kikötője, Little Barrier madárrezervátuma és a Cuvier világítótorony."),
    L("NZGB", [Pt("Hirakimata", "Hirakimata", "Hirakimata Great Barrier", -36.2000, 175.4833), Pt("Port Fitzroy", "Port Fitzroy", "Port Fitzroy Great Barrier", -36.1667, 175.3667), Pt("Little Barrier Island", "Little Barrier-sziget", "Little Barrier Island Hauraki", -36.2000, 175.0833), Pt("Cuvier Island", "Cuvier-sziget", "Cuvier Island", -36.4333, 175.7667)],
      ("Hauraki loop", "Hauraki-kör"), ("Hirakimata, Port Fitzroy, Little Barrier and Cuvier.", "Hirakimata, Port Fitzroy, Little Barrier és Cuvier."), kt=100, alt=2500))
add("OC", "stol-lord-howe", C("Australia", "Ausztrália"), ("Lord Howe Island and Ball's Pyramid", "Lord Howe-sziget és a Ball's Pyramid"), ("Ball's Pyramid", "Ball's Pyramid", -31.7458, 159.2519), ["island", "reef", "unesco"],
    ("A World Heritage subtropical island: Mount Gower and Mount Lidgbird above the lagoon, then 562 m Ball's Pyramid rising straight out of the Pacific.", "Világörökségi szubtrópusi sziget: a lagúna fölé magasodó Gower- és Lidgbird-hegy, majd a Csendes-óceánból egyenesen kiemelkedő, 562 méter magas Ball's Pyramid."),
    L("YLHI", [Pt("Mount Lidgbird", "Lidgbird-hegy", "Mount Lidgbird Lord Howe", -31.5600, 159.0850), Pt("Mount Gower", "Gower-hegy", "Mount Gower Lord Howe", -31.5833, 159.0750), Pt("Ball's Pyramid", "Ball's Pyramid", "Ball's Pyramid", -31.7458, 159.2519)],
      ("Lord Howe loop", "Lord Howe-kör"), ("Mount Lidgbird, Mount Gower and Ball's Pyramid.", "Lidgbird-hegy, Gower-hegy és Ball's Pyramid."), kt=100, alt=2500))
add("OC", "stol-milford", C("New Zealand", "Új-Zéland"), ("New Zealand: Milford Sound Fiordland", "Új-Zéland: Milford Sound, Fiordland"), ("Mitre Peak", "Mitre Peak", -44.6417, 167.8533), ["fjord", "mountain", "waterfall", "unesco"],
    ("A short strip squeezed between Mitre Peak and the fjord walls: Sutherland Falls, the tallest in New Zealand, and the lonely Doubtful Sound.", "Rövid pálya a Mitre Peak és a fjordfalak közé szorulva: a Sutherland-vízesés, Új-Zéland legmagasabbja, és a magányos Doubtful Sound."),
    L("NZMF", [Pt("Mitre Peak", "Mitre Peak", "Mitre Peak Milford Sound", -44.6417, 167.8533), Pt("Sutherland Falls", "Sutherland-vízesés", "Sutherland Falls Milford Track", -44.7936, 167.7242), Pt("Doubtful Sound", "Doubtful Sound", "Doubtful Sound Fiordland", -45.3500, 166.9833)],
      ("Fiordland loop", "Fiordland-kör"), ("Mitre Peak, Sutherland Falls and Doubtful Sound.", "Mitre Peak, Sutherland-vízesés és Doubtful Sound."), kt=100, alt=6500))
add("OC", "stol-chatham", C("New Zealand", "Új-Zéland"), ("Chatham Islands: Edge of the World", "Chatham-szigetek: a világ pereme"), ("Pitt Island", "Pitt-sziget", -44.2833, -176.2333), ["island", "coast", "wildlife"],
    ("The easternmost inhabited islands of New Zealand, 800 km out in the Pacific: Waitangi, Kaingaroa's sand dunes and rugged Pitt Island.", "Új-Zéland legkeletibb lakott szigetei, 800 km-re a Csendes-óceánon: Waitangi, Kaingaroa dűnéi és a zord Pitt-sziget."),
    L("NZCI", [Pt("Waitangi", "Waitangi", "Waitangi Chatham", -43.9500, -176.5500), Pt("Kaingaroa", "Kaingaroa", "Kaingaroa Chatham", -43.7500, -176.3500), Pt("Pitt Island", "Pitt-sziget", "Pitt Island Chatham", -44.2833, -176.2333)],
      ("Chatham loop", "Chatham-kör"), ("Waitangi, Kaingaroa and Pitt Island.", "Waitangi, Kaingaroa és Pitt-sziget."), kt=100, alt=2500))
add("OC", "stol-flinders", C("Australia", "Ausztrália"), ("Tasmania: Flinders Island and Bass Strait", "Tasmánia: Flinders-sziget és a Bass-szoros"), ("Lady Barron", "Lady Barron", -40.2000, 148.2500), ["island", "coast", "wildlife"],
    ("The Furneaux Group in Bass Strait: Cape Barren Island's rugged ranges, Lady Barron's harbour and the white sands of Flinders Island.", "A Bass-szoros Furneaux-szigetei: Cape Barren-sziget zord hegyei, Lady Barron kikötője és a Flinders-sziget fehér homokja."),
    L("YCBN", [Pt("Lady Barron", "Lady Barron", "Lady Barron Flinders Island", -40.2000, 148.2500), Pt("Strzelecki Peaks", "Strzelecki-csúcsok", "Strzelecki Peaks Flinders Island", -40.2000, 148.0800), Pt("Whitemark", "Whitemark", "Whitemark Flinders Island", -40.1167, 148.0167)],
      ("Furneaux loop", "Furneaux-kör"), ("Lady Barron, the Strzelecki Peaks and Whitemark.", "Lady Barron, Strzelecki-csúcsok és Whitemark."), kt=100, alt=2500))


for t in T:
    t["continent"] = CONT[t["id"]]
NEW = [t["id"] for t in T]
for t in T:
    for v in t["variants"]:
        v["stol"] = True
save()
d = json.load(open(P, encoding="utf-8"))
for t in d["tours"]:
    if t["id"] in NEW:
        t["new"] = True
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
here = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(here, "r14_ids.txt"), "w").write(" ".join(NEW))
with open(os.path.join(here, "poi_r14.py"), "w", encoding="utf-8") as f:
    f.write('# -*- coding: utf-8 -*-\n"""A 14. kor latnivaloi: EN nev -> (magyar nev, extra kereso szavak). Az add_r14.py generalja."""\nNEW = {\n')
    for k, (h, x) in POI.items():
        f.write("%r: (%r, %r),\n" % (k, h, x))
    f.write("}\n")
print(len(NEW), "tura,", len(POI), "latnivalo")
