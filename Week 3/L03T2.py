print('Selvitetään sanojen aakkosjärjestys.')
Sana1 = input('Anna sana 1: ')
Sana2 = input('Anna sana 2: ')
if Sana1 < Sana2:
    print("'"+Sana1+"'", 'on aakkosissa aiemmin kuin', "'"+Sana2+"'"'.')
elif Sana1 == Sana2:
    print('Sanat ovat samoja,', "'" + Sana1 + "'")
else:
    print("'"+Sana2+"'", 'on aakkosissa aimmin kuin', "'"+Sana1+"'"'.')
print("")
print('Selvitetään merkin sisältyminen merkkijonoon.')
Sana3 = input('Anna merkkijono: ')
Kirjain = input('Anna etsittävä merkki: ')
if Kirjain in Sana3:
    print('Merkki', "'"+Kirjain+"'", 'sisältyy merkkijonoon', "'"+Sana3+"'.")
else:
    print('Merkki', "'"+Kirjain+"'", 'ei sisälly merkkijonoon', "'"+Sana3+"'.")
print("")
print('Selvitetään, onko sana palindromi')
Sana4 = input('Anna testattava sana: ')
if Sana4 == (Sana4[::-1]):
    print('Sana', "'"+Sana4+"'", 'on palindromi.')
else:
    print('Sana ei ole palindromi.')
    print('Sana on etuperin', "'"+Sana4+"'", 'ja takaperin', "'"+(Sana4[::-1])+"'.")
print('Kiitos ohjelman käytöstä.')
