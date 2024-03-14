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

import HTPerusKirjasto

def valikko():
    print('Valitse haluamasi toiminto:')
    print('1) Lue tiedosto')
    print('2) Analysoi')
    print('3) Kirjoita tiedosto')
    print('4) Analysoi viikonpäivättäiset keskiarvot')
    print('0) Lopeta')
    Valinta = input('Valintasi: ')
    try :
        Valinta = int(Valinta)
    except ValueError:
        ""
    return Valinta;    

def paaohjelma():
    LuettuNimi = "''"
    KirjoitettuNimi = "''"
    Tiedot = []
    paivaTiedot = []
    while True:
        Valinta = valikko()
        if Valinta == 1:
            Luettava = HTPerusKirjasto.tiedostoNimet("luettavan", LuettuNimi)       
            Tiedot = HTPerusKirjasto.lueTiedosto(Luettava, Tiedot)
            LuettuNimi=Luettava
            
        elif Valinta == 2:
            anTiedot = HTPerusKirjasto.Analyysi(Tiedot)
            paivaTiedot = HTPerusKirjasto.paivaAnalyysi(Tiedot, paivaTiedot)
            for Alkio in paivaTiedot:
                print(Alkio.Paiva, Alkio.Keskihinta)

        elif Valinta == 3:
            Kirjoitettava = HTPerusKirjasto.tiedostoNimet("kirjoitettavan", KirjoitettuNimi)
            Kirjoita = HTPerusKirjasto.tiedostoTallenna(Kirjoitettava, AnalysoidutTiedot)
            KirjoitettuNimi=Kirjoitettava

        elif Valinta == 4:
            print("OK")

        elif Valinta == 0:
            print("Lopetetaan." + "\n")
            print('Kiitos ohjelman käytöstä.')
            break
        
        else:
            print('Tuntematon valinta, yritä uudestaan.')
        print('')
    return None
                  
paaohjelma()
