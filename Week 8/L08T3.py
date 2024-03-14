
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
# Tehtävä L08T3.py
# eof

import datetime

def valikko():
    print('Mitä haluat tehdä:')
    print('1) Tunnista aika-olion komponentit')
    print('2) Laske ikä päivinä')
    print('3) Tulosta viikonpäivät')
    print('4) Tulosta kuukaudet')
    print('0) Lopeta')
    Valinta = int(input('Anna valintasi: '))
    return Valinta

def aikaKomponentti(Aika):
    Paiva = datetime.datetime.strptime(Aika,"%d.%m.%Y %H:%M")
    print(Paiva.strftime(" Annoit vuoden " + str(Paiva.year)))
    print(Paiva.strftime("Annoit kuukauden " + str(Paiva.month)))
    print(Paiva.strftime("Annoit päivän " + str(Paiva.day)))
    print(Paiva.strftime("Annoit tunnin " + str(Paiva.hour)))
    print(Paiva.strftime("Annoit minuutin " + str(Paiva.minute)))
    return None

def ikaPaivina(Aika):
    Syntymapaiva = datetime.datetime.strptime(Aika,"%d.%m.%Y")
    Eroavaisuus = datetime.datetime(2000, 1, 1, 00, 00)
    Ika = Eroavaisuus - Syntymapaiva
    print("1.1.2000 henkilö oli " +str(Ika.days) + " päivää vanha.")
    return None

def viikonPaivat():
    Paiva = datetime.datetime.strptime("31.10.2022", "%d.%m.%Y")
    i = range(7)
    for n in i:
        Viikonpaiva = Paiva + datetime.timedelta(days=+n)
        print(Viikonpaiva.strftime("%A"))
    return None

def tulostaKuukaudet():
    Paiva = datetime.datetime.strptime("1.1.2022", "%d.%m.%Y")
    i = range(12)
    for n in i:
        Kuukausi = Paiva + datetime.timedelta(days=+31*n)
        print(Kuukausi.strftime("%b"))
    return None
    
def paaohjelma():
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    while True:
        Valinta = valikko()
        if Valinta == 1:
            Valinta1 = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm':")
            aikaKomponentti(Valinta1)
        elif Valinta == 2:
            Valinta2 = input("Anna syntymäpäivä muodossa pp.kk.vvvv: ")
            ikaPaivina(Valinta2)
        elif Valinta == 3:
            viikonPaivat()
        elif Valinta == 4:
            tulostaKuukaudet()
        elif Valinta == 0:
            print("Lopetetaan." + "\n")
            print('Kiitos ohjelman käytöstä.')
            break
        
        else:
            print('Tuntematon valinta, yritä uudestaan.')
        print('')
                  
paaohjelma()
