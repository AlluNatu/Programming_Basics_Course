def tiedostoKirjoita():
    nimi = input("Anna tallennettavan tiedoston nimi: ")
    tiedosto = open(nimi, "w")
    while (True):
        nimet = input("Anna tiedostoon tallennettava nimi (enter lopettaa): ")
        if nimet != (""):
            tiedosto.write(nimet)
            tiedosto.write("\n")
        else:
            tiedosto.close()
            break;
    return nimi


def tiedostoLue(nimi):
    tiedosto = open(nimi, "r")
    print("Tiedostoon", "'"+nimi+"'", "on tallennettu seuraavat nimet:")
    while (True):
        rivi = tiedosto.readline()
        if len(rivi) == 0:
            break
        print(rivi, end = "")
    tiedosto.close()
    return None

def paaOhjelma():
    nimi = tiedostoKirjoita()
    tiedostoLue(nimi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaOhjelma()
