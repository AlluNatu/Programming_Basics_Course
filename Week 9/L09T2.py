######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Natunen Aleksi
# Opiskelijanumero: 001153516
# Päivämäärä: 13.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T2.py
# eof

def valikko():
    print('Mitä haluat tehdä:')
    print('1) Testaa ValueError')
    print('2) Testaa IndexError')
    print('3) Testaa ZeroDivisionError')
    print('4) Testaa TypeError')
    print('0) Lopeta')
    Valinta = input('Valintasi: ')
    try :
        Valinta = int(Valinta)
    except ValueError:
        print("Anna Valinta kokonaislukuna.")
        Valinta = input("Valintasi: ")
    return Valinta

def indexTesti():
    try:
        Valinta = int(input("Anna indeksi 0-4: "))
        Lista = [11, 22, 33, 44, 55]
        print("Listan arvo on " + str(Lista[Valinta]) + " indeksillä", str(Valinta)+ ".")
    except IndexError:
        print("Tuli IndexError, indeksi" , str(Valinta) + ".")
    return None

def zerodivisionTesti():
    try:
        Luku = int(input("Anna jakaja: "))
        Lasku = 4/int(Luku)
        print("4" +"/"+ str(Luku), "on", str(format(Lasku,".2f"))+".")
    except ZeroDivisionError:
        print("Tuli ZeroDivisionError, jakaja", str(Luku) +".")
    return None

def typeerrorTesti():
    try:
        Luku = input("Anna numero: ")
        Lasku = (Luku * Luku)
    except TypeError:
        print("Tuli TypeError,", str(Luku) +"*"+ str(Luku), "merkkijonoilla ei onnistunut.")
    return None

def paaohjelma():
    while True:
        Valinta = valikko()
        if Valinta == 1:
            print("Valikko-ohjelma testaa ValueError'n.")

        elif Valinta == 2:
            indexTesti()

        elif Valinta == 3:
            zerodivisionTesti()

        elif Valinta == 4:
            typeerrorTesti()
        elif Valinta == 0:
            print("Lopetetaan" + "\n")
            print('Kiitos ohjelman käytöstä.')
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print('')
    return None
                  
paaohjelma()
