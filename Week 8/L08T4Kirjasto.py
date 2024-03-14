EROTUS = "\n"
class TULOS:
    Pienin = None
    Suurin = None
    Summa = None
    Keskiarvo = None

def tiedostoNimet(i):
    print(i, "tiedoston nimi on "+"''.")
    Tiedosto = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    return Tiedosto

def tiedostoLuku(tiedosto):
    Luetaan = open(tiedosto, "r", encoding="utf-8")
    Luetut = Luetaan.readlines()
    Luetaan.close()
    return Luetut

def Analyysi(Lista):
    Pienin = 9999999999
    Suurin = 0
    k = 0
    for i in Lista:
        if int(Pienin) > int(i):
            Pienin = int(i)
    for j in Lista:
        if int(Suurin) < int(j):
            Suurin = int(j)
    Luku = TULOS()
    Luku.Pienin = Pienin
    Luku.Suurin = Suurin
    Luku.Summa = sum(Lista)
    Luku.Keskiarvo = round(((sum(Lista))/len(Lista)),0)
    return Luku

def tiedostoKirjoitus(Nimi, Luku):
    Tiedosto = open(Nimi, "w", encoding="utf-8")
    Tiedosto.write("Analyysin tulokset ovat seuraavat:" + EROTUS)
    Tiedosto.write("Datan pienin arvo on " + str(Luku.Pienin) +"." + EROTUS)
    Tiedosto.write("Datan suurin arvo on " + str(Luku.Suurin) +"." + EROTUS)
    Tiedosto.write("Datan summa on "+ str(Luku.Summa)+ "." + EROTUS)
    Tiedosto.write("Datan keskiarvo on " + str(Luku.Keskiarvo)+ "." + EROTUS)
    Tiedosto.close()
    return None
