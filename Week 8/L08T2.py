######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Natunen Aleksi
# Opiskelijanumero: -RETRACTED-
# Päivämäärä: 04.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T2.py
# eof

import L08T2Kirjasto


def valikko():
    print("Minkä muunnoksen haluat tehdä?")
    print('1) Anna muunnettava tilavuus')
    print("2) Muunna litra gallon'ksi")
    print("3) Muunna litra pint'ksi")
    print("4) Muunna litra cup'ksi")
    print("5) Muunna litra fluid ounce'ksi")
    print("6) Muunna gallon litroiksi")
    print("7) Muunna pint litroiksi")
    print("8) Muunna cup litroiksi")
    print("9) Muunna fluid ounce litroiksi")
    print('0) Lopeta')
    Valinta = int(input('Anna valintasi: '))
    return Valinta



def paaohjelma():
    Valinnanluku = 0
    print("Käytetään kirjaston versiota " + str(L08T2Kirjasto.versio))
    while True:
        Valinta = valikko()
        if Valinta == 1:
            Valinnanluku = float(input("Anna muunnettava tilavuus desimaalilukuna: "))

        elif Valinta == 2:
            Gallon = L08T2Kirjasto.gallon(Valinnanluku)
            print("Litrat muutettuina gallon'ksi: " + str(round(Gallon,2)))
            
        elif Valinta == 3:
            Pintti = L08T2Kirjasto.pintti(Valinnanluku)
            print("Litrat muutettuina pint'ksi: " + str(round(Pintti,2)))
                  
        elif Valinta == 4:
            Cuppi = L08T2Kirjasto.cuppi(Valinnanluku)
            print("Litrat muutettuina cup'iksi: " + str(round(Cuppi,2)))
                  
        elif Valinta == 5:
            Fluidounce = L08T2Kirjasto.fluidounce(Valinnanluku)
            print("Litrat muutettuina fluid ounce'ksi: " + str(round(Fluidounce,2)))
                  
        elif Valinta == 6:
            Gallonlitra = L08T2Kirjasto.gallonlitra(Valinnanluku)
            print("Gallon't muutettuina litroiksi: " + str(round(Gallonlitra,2)))
                  
        elif Valinta == 7:
            Pinttilitra = L08T2Kirjasto.pinttilitra(Valinnanluku)
            print("Pint't muutettuina litroiksi: " + str(round(Pinttilitra,2)))
                  
        elif Valinta == 8:
            Cuplitra = L08T2Kirjasto.cuplitra(Valinnanluku)
            print("Cup't muutettuina litroiksi: " + str(round(Cuplitra,2)))
                  
        elif Valinta == 9:
            Fluidouncelitra = L08T2Kirjasto.fluidouncelitra(Valinnanluku)
            print("Fluid ounce't muutettuina litroiksi: " + str(round(Fluidouncelitra,2)))
            
        elif Valinta == 0:
            print("Lopetetaan" + "\n")
            print('Kiitos ohjelman käytöstä.')
            break
        
        else:
            print('Tuntematon valinta, yritä uudestaan.')
        print('')
                  
paaohjelma()
