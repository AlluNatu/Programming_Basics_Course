######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Natunen Aleksi
# Opiskelijanumero: 001153516
# Päivämäärä: 17.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerus.py
# eof
EROTIN = ";"
import datetime
import sys

class ANALYYSITIEDOT():
    Rivimaara = None
    Pienin = float('inf')
    Suurin = float('-inf')
    Keskihinta = None
    Paivapienin = None
    Paivasuurin = None
    
class TIEDOT():
    Paiva = None
    Hinta = None
    Keskihinta = None
    Keskihintapaiva = 0
    Alkiomaara = 0

class PAIVATIEDOT():
    Paiva = None
    Keskihinta = None
    

def tiedostoNimet(Kehote, Tiedosto):
    print("Anna " + Kehote + " tiedoston nimi, nykyinen on " + Tiedosto + ".")
    Nimi = input("Anna uusi nimi, enter säilyttää nykyisen: ")    
    return Nimi



def lueTiedosto(Nimi, Lista):
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Tiedosto.readline()
        Rivi = Tiedosto.readline()
        while True:
            Sarakkeet = Rivi.split(EROTIN)
            if len(Rivi)>0:
                Kappale = TIEDOT()
                Kappale.Paiva = datetime.datetime.strptime(Sarakkeet[0], '"%Y-%m-%d %H:%M:%S"')
                Kappale.Hinta = Sarakkeet[1]
                Lista.append(Kappale)
                Rivi = Tiedosto.readline()
            if len(Rivi) == 0:
                break
        Tiedosto.close()
    except FileNotFoundError:
        print("Tiedostotyyppi ei yhteensopiva.")
    
    return Lista
#porssisahko2021_15.txt


def Analyysi(Lista):
    Hintayhteen = 0
    Kappale = ANALYYSITIEDOT()
    for Alkio in Lista:
        Hinta = float(Alkio.Hinta)
        Hintayhteen = Hintayhteen + Hinta
        Kappale.Keskihinta = Hintayhteen / len(Lista)
        if Kappale.Pienin > Hinta:
            Kappale.Pienin = Hinta
            Kappale.Paivapienin = Alkio.Paiva
        if Kappale.Suurin < Hinta:
            Kappale.Suurin = Hinta
            Kappale.Paivasuurin = Alkio.Paiva
    Kappale.Keskihinta = format(Kappale.Keskihinta,".1f")
    Kappale.Rivimaara = len(Lista)
    #print(str(Kappale.Rivimaara))
    #print(str(Kappale.Keskihinta))
    #print(str(Kappale.Suurin))
    #print(str(Kappale.Pienin))
    #print(str(Kappale.Paivapienin))
    #print(Kappale.Paivasuurin)
    return Kappale

def paivaAnalyysi(Lista, PalauttavaLista):
    Yhteensa = 0
    Jakaja = 0
    Ekapaiva = (Lista[0].Paiva.strftime("%d.%m.%Y"))
    Vikapaiva = (Lista[-1].Paiva.strftime("%d.%m.%Y"))
    for Alkio in Lista:
        Kappale = PAIVATIEDOT()
        PaivaCheck = (Alkio.Paiva.strftime("%d.%m.%Y"))
        if Vikapaiva == Ekapaiva:
            Jakaja = Jakaja + 1
            Yhteensa = Yhteensa + float(Alkio.Hinta)
            if Alkio.Paiva == Lista[-1].Paiva:
                Jakaja = Jakaja + 1
                Yhteensa = Yhteensa + float(Alkio.Hinta)
                Kappale.Paiva = (Ekapaiva)
                Kappale.Keskihinta = (Yhteensa/Jakaja)
                PalauttavaLista.append(Kappale)
                break
        if Ekapaiva != PaivaCheck:
            Kappale.Paiva = (Ekapaiva)
            Kappale.Keskihinta = (Yhteensa/Jakaja)
            PalauttavaLista.append(Kappale)
            Ekapaiva = PaivaCheck
            Yhteensa = float(Alkio.Hinta) 
            Jakaja = 1
        else:
            Yhteensa = Yhteensa + float(Alkio.Hinta)
            Jakaja = Jakaja + 1
    return PalauttavaLista
    #porssisahko2021_15.txt

def tiedostoTallenna(Nimi, AnalysoituLista):
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        Lista = AnalysoituLista
        for Alkio in Lista:
            PyoristettuAlkio = format(Alkio,".2f")
            Tiedosto.write(str(PyoristettuAlkio)+"\n")
        Tiedosto.write("\n")
        Tiedosto.write("\n")
        Tiedosto.close()
        print("Tulokset tallennettu tiedostoon " + "'"+Nimi+"'"+ ".")
    except FileNotFoundError:
        print("Tiedostonimi ei käy")
    return None

def viikonpaivaAnalyysi():
    print("OK")
    return None
