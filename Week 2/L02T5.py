print('Tämä ohjelma tekee painolle ja pituudelle yksikkömuunnoksia.')
Paino = float(input('Anna paino kiloina: '))
Naula = 2.205*Paino
Naula2 = round(Naula, 2)
print('Paino on', Paino, 'kg eli', Naula, 'naulaa.')
print('')
Sentti = float(input('Anna pituus sentteinä: '))
Metri = Sentti/100
Jalka = Metri/0.3048
Tuuma = float((Jalka-int(Jalka))*12)
#Yksi jalka on 12 tuuma!!!!!!!!!!!!!!!!!! :D :D :D :D :D :D :D
print('Pituus on', Metri, 'metriä', end='')
print(' eli amerikkalaisittain', int(Jalka), end='.0 jalkaa')
print(' ja', round(Tuuma,1), 'tuumaa.')
print('Kiitos ohjelman käytöstä.')
