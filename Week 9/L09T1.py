######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Natunen Aleksi
# Opiskelijanumero: -RETRACTED-
# Päivämäärä: 13.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T1.py
# eof


import sys
def listaLue(Nimi):
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Luetut = Tiedosto.readlines()
        Maara = len(Luetut)
        print("Tiedoston", "'" +str(Nimi)+ "'", "lukeminen onnistui,", Maara, "riviä.")
        Tiedosto.close()
        return Luetut
    except FileNotFoundError:
        print("Tiedoston", "'" + Nimi + "'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

def listaKirjoita(Nimi, Lista):
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        for Alkio in Lista:
            Tiedosto.write(str(Alkio))
        print("Tiedoston", "'" + str(Nimi)+ "'" , "kirjoittaminen onnistui.")
        Tiedosto.close()
        return None
    except FileNotFoundError:
        print("Tiedoston", "'" + Nimi + "'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    except PermissionError:
        print("Tiedoston", "'" + Nimi + "'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)


def paaOhjelma():
    Lista = []
    Tiedostoluettava = input("Anna luettavan tiedoston nimi: ")
    Lista = listaLue(Tiedostoluettava)
    Tiedostokirjoittava = input("Anna kirjoitettavan tiedoston nimi: ")
    listaKirjoita(Tiedostokirjoittava, Lista)
    print("Kiitos ohjelman käytöstä.")
    return None
    
paaOhjelma()
