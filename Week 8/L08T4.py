######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Natunen Aleksi
# Opiskelijanumero: 001153516
# Päivämäärä: 4.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T4.py
# eof

import L08T4Kirjasto

def valikko():
    print('Valitse haluamasi toiminto:')
    print('1) Lue tiedosto')
    print('2) Analysoi')
    print('3) Kirjoita tiedosto')
    print('0) Lopeta')
    Valinta = int(input('Anna valintasi: '))
    return Valinta;    

def paaohjelma():
    Lista = []
    Lista2 = []
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    while True:
        Valinta = valikko()
        if Valinta == 1:
            Luettava = L08T4Kirjasto.tiedostoNimet("Luettavan")
            TiedostoLuettava = L08T4Kirjasto.tiedostoLuku(Luettava)
            Lista = L08T4Kirjasto.tiedostoLuku(Luettava)
            for i in Lista:
                Lista2.append(int(i.replace("\n", "").replace("'","")))

            print("Tiedosto", "'"+Luettava+"' luettu.")
        elif Valinta == 2:
            Luku = L08T4Kirjasto.Analyysi(Lista2)
            print("Analyysi suoritettu.")
            
        elif Valinta == 3:
            Kirjoitettava = L08T4Kirjasto.tiedostoNimet("Kirjoitettavan")
            TiedostoKirjoitettava = L08T4Kirjasto.tiedostoKirjoitus(Kirjoitettava, Luku)
            print("Tulokset kirjoitettu tiedostoon.")

        elif Valinta == 0:
            print("Lopetetaan" + "\n")
            print('Kiitos ohjelman käytöstä.')
            break
        
        else:
            print('Tuntematon valinta, yritä uudestaan.')
        print('')

                  
paaohjelma()
