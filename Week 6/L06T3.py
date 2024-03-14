def tiedostoTarkista(lNimi, kNimi):
    tiedosto_lukeminen = open(lNimi, "r", encoding="utf-8")
    while (True):
        tiedosto_lukeminen.read()
    return None

def tiedostoKirjoita():
    return None

def paaOhjelma():
    lNimi = input("Anna luettavan tiedoston nimi: ")
    kNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    tiedosto_kirjoitus = open(kNimi, "w", encoding="utf-8")
    tiedosto_kirjoitus.close()
    tiedostoTarkista(lNimi, kNimi)
    return None

paaOhjelma()
