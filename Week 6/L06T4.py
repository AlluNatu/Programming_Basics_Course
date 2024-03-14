def valikko():
    print('Valitse haluamasi toiminto:')
    print('1) Anna tiedostonimet')
    print('2) Analysoi')
    print('3) Kirjoita tiedosto')
    print('0) Lopeta')
    Valinta = int(input('Anna valintasi: '))
    return Valinta;

def tiedostoNimet(kumpi):
    print(kumpi, "tiedoston nimi on ''.")
    tiedosto = input("Anna uusi nimi, enter säilyttää nykyisen: ")    
    return tiedosto

def analyysiIsoin(tiedLukeminen):
    Isoin = 0
    tiedosto = open(tiedLukeminen, "r")
    for rivi in tiedosto:
        if int(Isoin) < int(rivi.strip()):
            Isoin = int(rivi.strip())
    tiedosto.close()
    return Isoin

def analyysiPienin(tiedLukeminen):
    Pienin = 99999999999999
    tiedosto = open(tiedLukeminen, "r")
    for rivi in tiedosto:
        if  int(rivi.strip()) < int(Pienin):
            Pienin = int(rivi.strip())
    tiedosto.close()
    return Pienin

def kirjoitaTiedosto(tiedKirjoitus, Pienin, Isoin):
    tiedosto = open(tiedKirjoitus, "w")
    tiedosto.write("Analyysin tulokset ovat seuraavat:" + '\n')
    tiedosto.write("Datan pienin arvo on "+ str(Pienin) + "." + '\n')
    tiedosto.write("Datan suurin arvo on " + str(Isoin) +"."+ '\n')
    tiedosto.close()

def paaohjelma():
    print('Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.')
    while True:
        Valinta = valikko()
        if Valinta == 1:
            print('Anna tiedostonimet')
            tiedLukeminen = tiedostoNimet("Luettavan")
            tiedKirjoitus = tiedostoNimet("Kirjoitettavan")
            
        elif Valinta == 2:
            print('Suoritetaan analyysi')
            Isoin = analyysiIsoin(tiedLukeminen)
            Pienin = analyysiPienin(tiedLukeminen)
            
        elif Valinta == 3:
            print("Kirjoitetaan tulokset tiedostoon")
            kirjoitaTiedosto(tiedKirjoitus, Pienin, Isoin)

        elif Valinta == 0:
            print('Lopetetaan')
            print('')
            print('Kiitos ohjelman käytöstä.')
            break
        else:
            print('Tuntematon valinta, yritä uudestaan.')
        print('')

                  
paaohjelma()
