######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Natunen Aleksi
# Opiskelijanumero: -RETRACTED-
# Päivämäärä: 28.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T3.py
# eof


def Paaohjelma():
    Annettu = input("Anna tiedoston nimi: ")
    Tiedosto = open(Annettu, "r", encoding="utf-8")
    print("Kalastuskilpailun tulokset ovat seuraavat:")
    Rivi = Tiedosto.readline()
    Rivi = Tiedosto.readline()
    while len(Rivi)>0:
        Rivi = Rivi.replace("\n","")
        Rivi2 = Rivi.split(";")
        Rivi = Tiedosto.readline()
        print("Joukkue", "'"+Rivi2[0]+"'", "sai kalan", Rivi2[1] +","+ " joka oli", Rivi2[2],"cm.")
    print("Kiitos ohjelman käytöstä.")





Paaohjelma()
