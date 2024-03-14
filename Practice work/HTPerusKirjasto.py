######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Natunen Aleksi
# Opiskelijanumero: 001153516
# Päivämäärä: 11.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerusKirjasto.py
# eof

import datetime
import sys
EROTIN = ";"
PAIVIA = 7

class ANALYYSITIEDOT():
    Pienin = float(0)
    Suurin = float(0)
    Keskihinta = None
    Paivapienin = None
    Paivasuurin = None

class TIEDOT():
    Paiva = None
    Hinta = None
    Alkiomaara = 0

class PAIVATIEDOT():
    Paiva = None
    Keskihinta = None

def tiedostoNimet(Kehote):
    tiedostoNimi = input("Anna " + Kehote + " tiedoston nimi: ")
    return tiedostoNimi

def lueTiedosto(tiedostoNimi, Lista):
    try:
        Tiedosto = open(tiedostoNimi, "r", encoding="UTF-8")
        Tiedosto.readline()
        Rivi = Tiedosto.readline()
        while (len(Rivi) > 0):
            Sarakkeet = Rivi.split(EROTIN)
            Kappale = TIEDOT()
            Kappale.Paiva = datetime.datetime.strptime(Sarakkeet[0], '"%Y-%m-%d %H:%M:%S"')
            Kappale.Hinta = Sarakkeet[1]
            Lista.append(Kappale)
            Rivi = Tiedosto.readline()
            if len(Rivi) == 0:
                break
        Tiedosto.close()
        print("Tiedosto", "'" + tiedostoNimi + "'", "luettu.")
    except Exception:
        print("Tiedoston '"+tiedostoNimi+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return Lista

def Analyysi(Lista):
    Hintayhteen = 0
    Rivimaara = 0
    Analyysitiedot = ANALYYSITIEDOT()
    Analyysitiedot.Pienin = float(Lista[0].Hinta)
    Analyysitiedot.Isoin = float(Lista[0].Hinta)
    for Alkio in Lista:
        Rivimaara = Rivimaara + 1
        Hinta = float(Alkio.Hinta)
        Hintayhteen = Hintayhteen + Hinta
        Analyysitiedot.Keskihinta = format(Hintayhteen / len(Lista), ".1f")
        if Analyysitiedot.Pienin > Hinta:
            Analyysitiedot.Pienin = Hinta
            Analyysitiedot.Paivapienin = Alkio.Paiva
        if Analyysitiedot.Suurin < Hinta:
            Analyysitiedot.Suurin = Hinta
            Analyysitiedot.Paivasuurin = Alkio.Paiva
    Analyysitiedot.Suurin = format(Analyysitiedot.Suurin, ".2f")
    Analyysitiedot.Pienin = format(Analyysitiedot.Pienin, ".2f")
    Analyysitiedot.Rivimaara = len(Lista)
    Analyysitiedot.Paivapienin = Analyysitiedot.Paivapienin.strftime("%d.%m.%Y %H:%M")
    Analyysitiedot.Paivasuurin = Analyysitiedot.Paivasuurin.strftime("%d.%m.%Y %H:%M")
    print("Tilastotietojen analyysi suoritettu", str(Rivimaara), "alkiolle.")
    return Analyysitiedot

def paivaAnalyysi(Lista, palauttavaLista):
    Maara = 0
    Yhteensa = 0
    Jakaja = 0
    Ekapaiva = (Lista[0].Paiva.strftime("%d.%m.%Y"))
    Vikapaiva = (Lista[-1].Paiva.strftime("%d.%m.%Y"))
    for Alkio in Lista:
        Paivatiedot = PAIVATIEDOT()
        Maara = Maara + 1
        PaivaCheck = (Alkio.Paiva.strftime("%d.%m.%Y"))
        if Vikapaiva == Ekapaiva:
            Jakaja = Jakaja + 1
            Yhteensa = Yhteensa + float(Alkio.Hinta)
            if Alkio.Paiva == Lista[-1].Paiva:
                Jakaja = Jakaja + 1
                Yhteensa = Yhteensa + float(Alkio.Hinta)
                Paivatiedot.Paiva = (Ekapaiva)
                Paivatiedot.Keskihinta = (Yhteensa / Jakaja)
                palauttavaLista.append(Paivatiedot)
                break
        if Ekapaiva != PaivaCheck:
            Paivatiedot.Paiva = (Ekapaiva)
            Paivatiedot.Keskihinta = (Yhteensa / Jakaja)
            palauttavaLista.append(Paivatiedot)
            Ekapaiva = PaivaCheck
            Yhteensa = float(Alkio.Hinta)
            Jakaja = 1
        else:
            Yhteensa = Yhteensa + float(Alkio.Hinta)
            Jakaja = Jakaja + 1
    print("Päivittäiset keskiarvot laskettu", len(palauttavaLista), "päivälle.")
    return palauttavaLista

def tiedostoTallenna(tiedostoNimi, PaivaTiedot, analyysiTiedot):
    try:
        Tiedosto = open(tiedostoNimi, "w", encoding="UTF-8")
        Tiedosto.write("Analyysin tulokset " + str(analyysiTiedot.Rivimaara) + " tunnilta ovat seuraavat:" + "\n")
        Tiedosto.write("Sähkön keskihinta oli " + str(analyysiTiedot.Keskihinta) + " snt/kWh." + "\n")
        Tiedosto.write(
            "Halvimmillaan sähkö oli " + str(analyysiTiedot.Pienin) + " snt/kWh," + " " + str(analyysiTiedot.Paivapienin) + "." + "\n")
        Tiedosto.write(
            "Kalleimmillaan sähkö oli " + str(analyysiTiedot.Suurin) + " snt/kWh," + " " + str(analyysiTiedot.Paivasuurin) + "." + "\n")
        Tiedosto.write("\n")
        Tiedosto.write("Päivittäiset keskiarvot (Pvm;snt/kWh):" + "\n")
        for Alkio in PaivaTiedot:
            Tiedosto.write(str(Alkio.Paiva) + EROTIN + str(format(Alkio.Keskihinta, ".1f")) + "\n")
        Tiedosto.close()
        print("Tiedosto", "'" + tiedostoNimi + "'", "kirjoitettu.")
    except Exception:
        print("Tiedoston '"+tiedostoNimi+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def viikonpaivaAnalyysi(paivaTiedot):
    Tulokset = []
    Luku = 0
    paivaHinnat = []
    paivaMaarat = []
    for i in range(PAIVIA):
        paivaHinnat.append(0)

    for i in range(PAIVIA):
        paivaMaarat.append(0)

    for i in range(PAIVIA):
        Tulokset.append(0)
        
    for Alkio in paivaTiedot:
        paivaHinnat[Alkio.Paiva.weekday()] += float(Alkio.Hinta)
        Luku = Alkio.Paiva.weekday()
        paivaMaarat[Luku] = paivaMaarat[Luku] + 1

    for i in range(7):
        Tulokset[i]=paivaHinnat[i]/paivaMaarat[i] if paivaHinnat[i] != 0 else 0
    return Tulokset
        
def viikonpaivatKirjoita(tiedostoNimi, Viikonpaivat):
    try:
        Tiedosto = open(tiedostoNimi, "w", encoding="UTF-8")
        Tiedosto.write("Viikonpäivä;Keskimääräinen hinta snt/kWh"+ "\n")
        Tiedosto.write("Maanantai"+EROTIN+str("%.1f" % Viikonpaivat[0])+ "\n")
        Tiedosto.write("Tiistai"+EROTIN+str("%.1f" % Viikonpaivat[1])+ "\n")
        Tiedosto.write("Keskiviikko"+EROTIN+str("%.1f" % Viikonpaivat[2])+ "\n")
        Tiedosto.write("Torstai"+EROTIN+str("%.1f" % Viikonpaivat[3])+ "\n")
        Tiedosto.write("Perjantai"+EROTIN+str("%.1f" % Viikonpaivat[4])+ "\n")
        Tiedosto.write("Lauantai"+EROTIN+str("%.1f" % Viikonpaivat[5])+ "\n")
        Tiedosto.write("Sunnuntai"+EROTIN+str("%.1f" % Viikonpaivat[6])+ "\n")
        Tiedosto.close()
        print("Tiedosto", "'" + tiedostoNimi + "'", "kirjoitettu.")
        Viikonpaivat.clear()
    except Exception:
        print("Tiedoston '"+tiedostoNimi+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None
