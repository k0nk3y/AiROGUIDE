#!/usr/bin/env python3
"""Europai valtozatok: rovid (20-30 perc), ~1 oras es hosszabb korok a meglevo turakhoz + uj Velence / Garda tura.
Futtatasi sorrend: add_eu1.py -> add_eu2.py -> add_var_eu.py"""
import json
from tourlib import *
import tourlib

IT = ("Italy", "Olaszország")


def v(tid, vid, kt, alt, lab, desc, pts, kind="loop"):
    addvar(tid, vid, kind, kt, alt, lab, desc, pts)


# ---------- uj turak ----------
tour("venice", IT, ("Venice and the lagoon", "Velence és a lagúna"), ("Venice", "Velence", 45.4408, 12.3155),
     ["culture", "unesco", "city", "coast"],
     ("Venice from above: the lagoon islands, St Mark's and the Brenta Riviera.", "Velence fentről: a lagúna szigetei, a Szent Márk-bazilika és a padovai környék."),
     [["Rialto Bridge", 45.4380, 12.3359], ["Murano", 45.4590, 12.3530]],
     [("lagoon", "loop", 100, 1800, ("Lagoon loop", "Lagúna-kör"), ("A short loop over Torcello, Burano, St Mark's and the Lido.", "Rövid kör Torcello, Burano, a Szent Márk tér és a Lido felett."),
       ["LIPZ", ["Torcello", 45.4975, 12.4177], ["Burano", 45.4850, 12.4170], ["St Mark's Basilica", 45.4340, 12.3397], ["Lido di Venezia", 45.4033, 12.3670], ["Chioggia", 45.2190, 12.2780], "LIPZ"]),
      ("padua", "loop", 110, 2000, ("Lagoon, Chioggia and Padua", "Lagúna, Chioggia és Padova"), ("About an hour: the lagoon, Chioggia and the Scrovegni city of Padua.", "Kb. egy óra: lagúna, Chioggia és Padova."),
       ["LIPZ", ["Torcello", 45.4975, 12.4177], ["St Mark's Basilica", 45.4340, 12.3397], ["Chioggia", 45.2190, 12.2780], ["Prato della Valle, Padua", 45.3985, 11.8774], "LIPZ"])])

tour("garda", IT, ("Lake Garda", "Garda-tó"), ("Lake Garda", "Garda-tó", 45.6, 10.7),
     ["culture", "coast", "mountain"],
     ("Italy's biggest lake: Sirmione, Malcesine, Riva and Monte Baldo, from Verona.", "Olaszország legnagyobb tava: Sirmione, Malcesine, Riva és a Monte Baldo, Veronából."),
     [["Scaliger Castle, Sirmione", 45.4918, 10.6086], ["Salò", 45.6064, 10.5226]],
     [("full", "loop", 110, 8500, ("Around the lake", "A tó körül"), ("About an hour: Sirmione, Salò, Riva, Monte Baldo and Verona's Arena.", "Kb. egy óra: Sirmione, Salò, Riva, Monte Baldo és a veronai Aréna."),
       ["LIPX", ["Sirmione", 45.4918, 10.6086], ["Salò", 45.6064, 10.5226], ["Riva del Garda", 45.8854, 10.8425], ["Monte Baldo", 45.7667, 10.8100], ["Verona Arena", 45.4390, 10.9944], "LIPX"])])
save()

# ---------- Rome, Dolomites ----------
v("rome-naples", "rome-a", 100, 2500, ("Rome classic", "Róma klasszikus"), ("Short loop: Aqueduct Park, Colosseum, St Peter's and Castel Gandolfo.", "Rövid kör: Acquedotti-park, Colosseum, Szent Péter és Castel Gandolfo."),
  ["LIRA", ["Parco degli Acquedotti", 41.8408, 12.5667], ["Colosseum", 41.8902, 12.4922], ["St Peter's Basilica", 41.9022, 12.4539], ["Castel Gandolfo", 41.7470, 12.6490], "LIRA"])
v("rome-naples", "rome-b", 100, 2500, ("Rome, Ostia and Tivoli", "Róma, Ostia és Tivoli"), ("Ostia Antica, the Vatican and Villa d'Este in Tivoli.", "Ostia Antica, a Vatikán és a tivoli Villa d'Este."),
  ["LIRA", ["Ostia Antica", 41.7554, 12.2915], ["St Peter's Basilica", 41.9022, 12.4539], ["Villa d'Este, Tivoli", 41.9632, 12.7966], "LIRA"])
v("dolomites", "bz-short", 100, 12500, ("Dolomites short", "Dolomitok rövid"), ("From Bolzano: Rosengarten, Sassolungo and Seceda.", "Bolzanóból: Catinaccio, Sassolungo és Seceda."),
  ["LIPB", ["Catinaccio / Rosengarten", 46.4650, 11.6330], ["Sassolungo", 46.5106, 11.7286], ["Seceda", 46.6046, 11.7202], "LIPB"])
v("dolomites", "bz-loop", 110, 12500, ("Dolomites loop", "Dolomitok kör"), ("About an hour from Bolzano: Rosengarten, Marmolada, Tre Cime, Lago di Braies, Seceda.", "Kb. egy óra Bolzanóból: Catinaccio, Marmolada, Tre Cime, Braies-tó, Seceda."),
  ["LIPB", ["Catinaccio / Rosengarten", 46.4650, 11.6330], "@Marmolada", "@Tre Cime di Lavaredo", ["Lago di Braies", 46.6944, 12.0855], ["Seceda", 46.6046, 11.7202], "LIPB"])

# ---------- rovid / egyoras korok a tobbi turahoz ----------
v("everest", "short", 90, 17000, ("Namche loop", "Namche-kör"), ("Short loop from Lukla: Namche Bazaar, Tengboche, Dingboche.", "Rövid kör Luklából: Namche Bazaar, Tengboche, Dingboche."),
  ["VNLK", "@Namche Bazaar", "@Tengboche", "@Dingboche", "VNLK"])
v("balaton", "west", 100, 2200, ("West Balaton", "Nyugati Balaton"), ("Short loop: Hévíz, Keszthely and Badacsony.", "Rövid kör: Hévíz, Keszthely, Badacsony."),
  ["LHSM", "@Hévíz Lake", "@Festetics Palace, Keszthely", "@Badacsony", "LHSM"])
v("amalfi", "short", 100, 4500, ("Vesuvius and Capri", "Vezúv és Capri"), ("Short loop: Vesuvius, Pompeii and Capri.", "Rövid kör: Vezúv, Pompeji, Capri."),
  ["LIRN", "@Mount Vesuvius", "@Pompeii", "@Capri", "LIRN"])
v("tuscany", "short", 100, 3000, ("Florence and San Gimignano", "Firenze és San Gimignano"), ("Short loop: Florence and the towers of San Gimignano.", "Rövid kör: Firenze és San Gimignano tornyai."),
  ["LIRQ", "@Florence Cathedral", "@San Gimignano", "@Monteriggioni", "LIRQ"])
v("cinque-terre", "loop", 100, 4500, ("Cinque Terre loop", "Cinque Terre kör"), ("Loop from Pisa: Portovenere and Vernazza.", "Kör Pisából: Portovenere és Vernazza."),
  ["LIRP", "@Portovenere", "@Vernazza", "LIRP"])
v("matterhorn", "short", 100, 15000, ("Matterhorn from Sion", "Matterhorn Sionból"), ("Short loop: Matterhorn and Zermatt.", "Rövid kör: Matterhorn és Zermatt."),
  ["LSGS", "@Matterhorn", "@Zermatt", "LSGS"])
v("salzkammergut", "short", 100, 10500, ("Salzburg lakes", "Salzburgi tavak"), ("Short loop: Hohensalzburg, Mondsee, St. Wolfgang.", "Rövid kör: Hohensalzburg, Mondsee, St. Wolfgang."),
  ["LOWS", "@Hohensalzburg Fortress", "@Mondsee", "@St. Wolfgang", "LOWS"])
v("loire", "paris", 100, 2500, ("Paris and Versailles", "Párizs és Versailles"), ("Short loop: Versailles, Eiffel Tower, Sacré-Cœur, Notre-Dame.", "Rövid kör: Versailles, Eiffel-torony, Sacré-Cœur, Notre-Dame."),
  ["LFPO", "@Versailles", "@Eiffel Tower", ["Sacré-Cœur", 48.8867, 2.3431], "@Notre-Dame de Paris", "LFPO"])
v("golden-circle", "short", 100, 3500, ("Reykjanes and Reykjavík", "Reykjanes és Reykjavík"), ("Short loop: Blue Lagoon and Hallgrímskirkja.", "Rövid kör: Kék-lagúna és Hallgrímskirkja."),
  ["BIRK", "@Blue Lagoon", "@Hallgrímskirkja", "BIRK"])
v("italian-lakes", "short", 105, 6500, ("Milan and Lake Como", "Milánó és a Comói-tó"), ("Short loop: Milan Cathedral and Bellagio.", "Rövid kör: milánói dóm és Bellagio."),
  ["LIML", "@Milan Cathedral", "@Bellagio", "LIML"])
v("sicily", "etna", 110, 12000, ("Etna and Taormina", "Etna és Taormina"), ("Loop from Catania: Mount Etna and Taormina.", "Kör Catániából: Etna és Taormina."),
  ["LICC", "@Mount Etna", "@Taormina", "LICC"])
v("vienna-wachau", "short", 100, 3000, ("Vienna", "Bécs"), ("Short loop: Schönbrunn, the Stephansdom, Kahlenberg.", "Rövid kör: Schönbrunn, Stephansdom, Kahlenberg."),
  ["LOWW", "@Schönbrunn Palace", "@St. Stephen's Cathedral", ["Kahlenberg", 48.2754, 16.3319], "LOWW"])
v("bavaria", "loop", 110, 10500, ("Allgäu loop", "Allgäu-kör"), ("About an hour from Memmingen: Neuschwanstein and Linderhof.", "Kb. egy óra Memmingenből: Neuschwanstein és Linderhof."),
  ["EDJA", "@Neuschwanstein Castle", "@Linderhof Palace", "EDJA"])
v("rhine", "short", 100, 2500, ("Cologne and Drachenfels", "Köln és Drachenfels"), ("Short loop: Cologne Cathedral and Drachenfels.", "Rövid kör: kölni dóm és Drachenfels."),
  ["EDDK", "@Cologne Cathedral", ["Drachenfels", 50.6657, 7.2096], "EDDK"])
v("provence-riviera", "marseille", 110, 3500, ("Marseille and the Calanques", "Marseille és a Calanques"), ("Short loop: Notre-Dame de la Garde and Cap Canaille.", "Rövid kör: Notre-Dame de la Garde és Cap Canaille."),
  ["LFML", ["Notre-Dame de la Garde", 43.2840, 5.3711], ["Cap Canaille", 43.2064, 5.5417], "LFML"])
v("provence-riviera", "provence", 120, 3500, ("Provence loop", "Provence-kör"), ("About an hour: Les Baux, Avignon, Pont du Gard, Arles.", "Kb. egy óra: Les Baux, Avignon, Pont du Gard, Arles."),
  ["LFML", ["Les Baux-de-Provence", 43.7435, 4.7953], "@Palais des Papes, Avignon", "@Pont du Gard", ["Arles Amphitheatre", 43.6777, 4.6311], "LFML"])
v("normandy", "short", 110, 2500, ("Honfleur and Pegasus Bridge", "Honfleur és Pegasus-híd"), ("Short loop from Deauville.", "Rövid kör Deauville-ből."),
  ["LFRG", "@Honfleur", ["Pegasus Bridge", 49.2447, -0.2755], "LFRG"])
v("normandy", "beaches", 120, 2500, ("D-Day beaches", "A partraszállás partjai"), ("About an hour: Pegasus Bridge, Arromanches, Omaha, Pointe du Hoc.", "Kb. egy óra: Pegasus-híd, Arromanches, Omaha, Pointe du Hoc."),
  ["LFRG", ["Pegasus Bridge", 49.2447, -0.2755], "@Arromanches", "@Omaha Beach", "@Pointe du Hoc", "LFRG"])
v("andalusia", "cordoba", 120, 5000, ("Seville and Córdoba", "Sevilla és Córdoba"), ("About an hour: Seville and the Mezquita.", "Kb. egy óra: Sevilla és a córdobai Mezquita."),
  ["LEZL", "@Seville Cathedral", "@Mezquita, Córdoba", "LEZL"])
v("andalusia", "costa", 120, 5500, ("Costa del Sol", "Costa del Sol"), ("From Málaga: Ronda and the Rock of Gibraltar.", "Málagából: Ronda és a Gibraltári-szikla."),
  ["LEMG", "@Ronda", "@Rock of Gibraltar", "LEMG"])
v("barcelona", "short", 100, 5000, ("Barcelona and Montserrat", "Barcelona és Montserrat"), ("Short loop: Sagrada Família and Montserrat.", "Rövid kör: Sagrada Família és Montserrat."),
  ["LEBL", "@Sagrada Família", "@Montserrat", "LEBL"])
v("london", "short", 100, 2000, ("London short", "London rövid"), ("Short loop: Tower Bridge, St Paul's, Parliament, Wembley, Greenwich.", "Rövid kör: Tower Bridge, St Paul's, Parlament, Wembley, Greenwich."),
  ["EGLC", "@Tower Bridge", "@St Paul's Cathedral", "@Houses of Parliament", "@Wembley Stadium", ["Royal Observatory Greenwich", 51.4769, -0.0005], "EGLC"])
v("scottish-highlands", "loch-lomond", 110, 4500, ("Loch Lomond and Stirling", "Loch Lomond és Stirling"), ("Loop from Glasgow.", "Kör Glasgow-ból."),
  ["EGPF", ["Loch Lomond (Luss)", 56.1017, -4.6358], ["Stirling Castle", 56.1239, -3.9475], "EGPF"])
v("cornwall", "short", 100, 1800, ("North Cornwall", "Észak-Cornwall"), ("Short loop: Tintagel and the Eden Project.", "Rövid kör: Tintagel és az Eden Project."),
  ["EGHQ", "@Tintagel Castle", "@Eden Project", "EGHQ"])
v("edinburgh", "short", 100, 2500, ("Forth and Falkirk", "Forth és Falkirk"), ("Short loop: Castle, Forth Bridge, Kelpies, Falkirk Wheel.", "Rövid kör: vár, Forth-híd, Kelpies, Falkirk Wheel."),
  ["EGPH", "@Edinburgh Castle", "@Forth Bridge", "@The Kelpies", "@Falkirk Wheel", "EGPH"])
v("norway-fjords", "loop", 110, 7500, ("Ålesund loop", "Ålesund-kör"), ("About an hour: Trollstigen and Geirangerfjord.", "Kb. egy óra: Trollstigen és Geiranger-fjord."),
  ["ENAL", "@Trollstigen", "@Geirangerfjord", "ENAL"])
v("cyclades", "mykonos-naxos", 110, 3000, ("Mykonos, Delos, Naxos", "Mykonos, Délosz, Náxosz"), ("Loop from Mykonos.", "Kör Mykonosról."),
  ["LGMK", "@Delos", "@Portara, Naxos", "@Mykonos Town", "LGMK"])
v("peloponnese", "short", 100, 3000, ("Athens and Sounion", "Athén és Szunion"), ("Short loop: Acropolis and the Temple of Poseidon.", "Rövid kör: Akropolisz és Poszeidón-templom."),
  ["LGAV", "@Acropolis", "@Temple of Poseidon, Sounion", "LGAV"])
v("dalmatia", "dubrovnik", 120, 5000, ("Dubrovnik and Mljet", "Dubrovnik és Mljet"), ("Short loop.", "Rövid kör."),
  ["LDDU", "@Dubrovnik Old Town", ["Mljet National Park", 42.7667, 17.5333], "LDDU"])
v("dalmatia", "split", 120, 3500, ("Split, Hvar and Brač", "Split, Hvar és Brač"), ("Loop from Split.", "Kör Splitből."),
  ["LDSP", "@Diocletian's Palace, Split", "@Hvar Town", ["Zlatni Rat, Brač", 43.2569, 16.6350], "LDSP"])
v("prague", "short", 100, 2500, ("Prague and Karlštejn", "Prága és Karlštejn"), ("Short loop.", "Rövid kör."),
  ["LKPR", "@Karlštejn Castle", "@Prague Castle", "@Charles Bridge", ["Vyšehrad", 50.0642, 14.4197], "LKPR"])
v("zurich-constance", "loop", 110, 9500, ("Zurich and Lake Constance loop", "Zürich és Boden-tó kör"), ("Loop from Zurich.", "Kör Zürichből."),
  ["LSZH", "@Grossmünster, Zurich", "@Rhine Falls", "@Mainau Island", "LSZH"])
save_vars()

# ---------- magassagok javitasa (hegycsucsok fole) ----------
d = json.load(open(tourlib.P, encoding="utf-8"))
ALT = {("dolomites", "ab"): 12500, ("matterhorn", "ab"): 15000, ("bavaria", "ab"): 10500, ("lucerne", "loop"): 11500, ("salzkammergut", "loop"): 10500,
       ("norway-fjords", "ab"): 7500, ("sicily", "ab"): 12000, ("zurich-constance", "ab"): 9500, ("italian-lakes", "loop"): 6500, ("cinque-terre", "ab"): 4500,
       ("amalfi", "loop"): 4500, ("dalmatia", "ab"): 5000, ("barcelona", "ab"): 5000, ("golden-circle", "loop"): 3500}
for t in d["tours"]:
    for w in t["variants"]:
        if (t["id"], w["id"]) in ALT:
            w["alt_ft"] = ALT[(t["id"], w["id"])]
for t in d["tours"]:
    if t["id"] == "amalfi" and "volcano" not in t["tags"]:
        t["tags"].append("volcano")                       # Vezuv
json.dump(d, open(tourlib.P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
