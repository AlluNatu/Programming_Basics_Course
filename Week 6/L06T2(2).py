def tiedostoNimi():
    nimi = input("Anna tallennettavan tiedoston nimi: ")
    return nimi


def tiedostoLue(nimi):
    tiedosto = open(nimi, "r", encoding="utf-8")
    Merkit = len(tiedosto)
    return Merkit

def paaOhjelma():
    nimi = tiedostoNimi()
    tiedostoLue(nimi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaOhjelma()

