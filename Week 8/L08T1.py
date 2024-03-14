######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Natunen Aleksi
# Opiskelijanumero: 001153516
# Päivämäärä: 04.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T1.py
# eof
import math
import random

def valikko():
    print("Mitä haluat tehdä?")
    print('1) Laske absoluuttinen arvo')
    print('2) Laske kertoma')
    print('3) Laske potenssi')
    print('4) Laske neliöjuuri')
    print('5) Arvo satunnaisluku')
    print('0) Lopeta')
    Valinta = int(input('Anna valintasi: '))
    return Valinta



def paaohjelma():
    random.seed(1)
    while True:
        Valinta = valikko()
        if Valinta == 1:
            Valinta1= input("Minkä luvun absoluuttinen arvo selvitetään: ")
            Absoluuttinen = (math.fabs(float(Valinta1)))
            print("Luvun absoluuttinen arvo on " + str(round(Absoluuttinen,1)))
        elif Valinta == 2:
            Valinta2 = input("Minkä luvun kertoma lasketaan: ")
            Kertoma = math.factorial(int(Valinta2))
            print("Luvun kertoma on " + str(Kertoma))
        elif Valinta == 3:
            Valinta31 = input("Mikä luku korotetaan potenssiin: ")
            Valinta32 = input("Mitä eksponenttia käytetään: ")
            Potenssi = math.pow(int(Valinta31),int(Valinta32))
            print("Luku korotettuna eksponenttiin on " + str(Potenssi))            
        elif Valinta == 4:
            Valinta4 = input("Mikä luvun neliöjuuri lasketaan: ")
            Neliojuuri = math.sqrt(int(Valinta4))
            print("Luvun neliöjuuri on " + str(Neliojuuri))
        elif Valinta == 5:
            print("Arvotaan satunnaisluku, anna rajat kokonaislukuina.")
            Valinta51 = input("Anna minimi (otetaan mukaan): ")
            Valinta52 = input("Anna maksimi (otetaan mukaan): ")
            Satunnaisluku = random.randint(int(Valinta51), int(Valinta52))
            print("Arvottiin satunnaisluku " +str(Satunnaisluku))
        elif Valinta == 0:
            print("Lopetetaan" + "\n")
            print('Kiitos ohjelman käytöstä.')
            break
        
        else:
            print('Tuntematon valinta, yritä uudestaan.')
        print('')
                  
paaohjelma()
