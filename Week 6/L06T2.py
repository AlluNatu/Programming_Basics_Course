def tiedostoNimi():
    nimi = input("Anna luettavan tiedoston nimi: ")
    return nimi


def tiedostoLueRivit(nimi):
    tiedosto = open(nimi, "r", encoding="utf-8")
    rivi = tiedosto.readlines()
    rivit = len(rivi)
    tiedosto.close()
    return rivit

def tiedostoLueMerkit(nimi):
    tiedosto = open(nimi, "r", encoding="utf-8")
    rivi = tiedosto.read()
    merkit = len(rivi)
    tiedosto.close()
    return merkit

def keskiMaara(rivit,merkit):
    keskimaara = str(round(int((merkit-rivit)/rivit),0))
    return keskimaara

def paaOhjelma():
    nimi = tiedostoNimi()
    rivit = tiedostoLueRivit(nimi)
    merkit = tiedostoLueMerkit(nimi)
    keskimaara = keskiMaara(rivit,merkit)
    print("Tiedostossa oli", rivit, "nimeä ja", merkit, "merkkiä.")
    print("Keskimäärin nimen pituus oli", keskimaara, "merkkiä.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaOhjelma()

