def tulostaOhjeet():
    print('Tämä ohjelma kysyy ja tulostaa tietoja.')
    print('Tämä aliohjelma tulostaa ohjeita käyttäjälle.')
    return None;

def kysyNimi():
    print('Anna nimesi kahdessa osassa.')
    print('Tämä aliohjelma kysyy nimen.')
    Nimi1 = input('Anna etunimi: ')
    print('Tämä aliohjelma kysyy nimen.')
    Nimi2 = input('Anna Sukunimi: ')
    return Nimi1 + ' ' + Nimi2;


def tulostaTulokset(i):
    print('Tämä aliohjelma tulostaa nimesi.')
    print('Hei', i);
    return None;

def paaohjelma():
    tulostaOhjeet()
    Nimi = kysyNimi()
    tulostaTulokset(Nimi)
    print('Kiitos ohjelman käytöstä.')
    return None;

paaohjelma()
