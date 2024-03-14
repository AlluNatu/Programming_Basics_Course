print('Anna kaksi kokonaislukua.')
luku1 = int(input('Anna luku 1: '))
luku2 = int(input('Anna luku 2: '))
print('Selvitetään, ovatko antamasi luvut parillisia.')
if luku1 %2 == 0:
    print('Luku', str(luku1), 'on parillinen.')
else: print('Luku', str(luku1), 'on pariton.');
if luku2 %2 == 0:
    print('Luku', str(luku2), 'on parillinen.')
else: print('Luku', str(luku2), 'on pariton.');
print('Selvitetään, kumpi antamistasi luvuista on pienempi.')
if luku1<luku2:
    print('Luku', str(luku1), 'on pienempi.')
elif luku1==luku2:
    print('Luvut', str(luku1), 'ja', str(luku2), 'ovat yhtäsuuria.')
else: print('Luku', str(luku2), 'on pienempi.')
print('Kiitos ohjelman käytöstä.')
