Sana = input('Anna sana: ')
print('Antamasi sanan kolme ensimmäistä kirjainta ovat', Sana[:3])
print('Sanan neljä viimeistä kirjainta ovat', Sana[-4:])
print('Kirjaimet 3, 4, 5 ja 6 ovat', Sana[2]+Sana[3]+Sana[4]+Sana[5])
print('')
print('Sanan joka kolmas kirjain alkaen ensimmäisestä kirjaimesta:', Sana[::3])
print('')
print('Antamasi sana', "'"+Sana+"'", 'on takaperin', "'"+Sana[::-1]+"'.")
print('')
Ap = int(input('Anna aloituspaikka: '))
Lp = int(input('Anna lopetuspaikka: '))
Si = int(input('Anna siirtymä: '))
print('Antamillasi asetuksilla sana', Sana, 'tulostuu näin:', Sana[Ap:Lp:Si])
print('')
print('Antamasi sanan pituus oli', len(Sana), 'merkkiä.')
print('Kiitos ohjelman käytöstä.')
