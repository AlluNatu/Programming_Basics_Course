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
# Tehtävä HTPerus.py
# eof

import HTPerusKirjasto


def Valikko():
    print('Valitse haluamasi toiminto:')
    print('1) Lue tiedosto')
    print('2) Analysoi')
    print('3) Kirjoita tiedosto')
    print('4) Analysoi viikonpäivittäiset keskiarvot')
    print('0) Lopeta')
    Valinta = input('Anna valintasi: ')
    try:
        Valinta = int(Valinta)
    except Exception:
        ""
    return Valinta;


def paaohjelma():
    tarkistusAnalyysi = False
    tarkistusTallenna = False
    while True:
        Valinta = Valikko()
        if Valinta == 1:
            alkuperaisetTiedot = []
            luettavaTiedosto = HTPerusKirjasto.tiedostoNimet("luettavan")
            alkuperaisetTiedot = HTPerusKirjasto.lueTiedosto(luettavaTiedosto, alkuperaisetTiedot)
            tarkistusAnalyysi = True

        elif Valinta == 2:
            if tarkistusAnalyysi == True:
                paivaTiedot = []
                analyysiTiedot = HTPerusKirjasto.Analyysi(alkuperaisetTiedot)
                paivaTiedot = HTPerusKirjasto.paivaAnalyysi(alkuperaisetTiedot, paivaTiedot)
                tarkistusTallenna = True
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
        elif Valinta == 3:
            if tarkistusTallenna == True:
                Kirjoitettava = HTPerusKirjasto.tiedostoNimet("kirjoitettavan")
                Kirjoita = HTPerusKirjasto.tiedostoTallenna(Kirjoitettava, paivaTiedot, analyysiTiedot)
            else:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")

        elif Valinta == 4:
            if tarkistusAnalyysi == True:
                PaivaKirjoitettava = HTPerusKirjasto.tiedostoNimet("kirjoitettavan")
                Viikonpaivat = HTPerusKirjasto.viikonpaivaAnalyysi(alkuperaisetTiedot)
                HTPerusKirjasto.viikonpaivatKirjoita(PaivaKirjoitettava, Viikonpaivat)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")

        elif Valinta == 0:
            alkuperaisetTiedot.clear()
            paivaTiedot.clear()
            print("Lopetetaan." + "\n")
            print('Kiitos ohjelman käytöstä.')
            break

        else:
            print('Tuntematon valinta, yritä uudestaan.')
        print('')
    return None


paaohjelma()
