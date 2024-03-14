print('Selvitetään tuotteen alennusprosentti ja myyntihinta.') 
LH = int(input('Mikä on tuotteen listahinta: '))
print('Lasketaanko hinta')
print ('1) yhdellä monihaaraisella valintarakenteella')
print ('2) useilla erillisillä valintarakenteilla?')
Valinta = int(input('Anna valintasi: '))
if Valinta < 1 or Valinta > 2:
    print('Tuntematon valinta.')
    print('Tuotteen alennus on 0% ja hinnaksi jää', str(round(LH*1.0,2))+'e.')
if Valinta ==1:
    print('Yhdellä monihaaraisella valintarakenteella tulokset ovat seuraavat:')
    if LH > 300:
        print('Tuotteen alennus on 30% ja hinnaksi jää', str(round((LH*0.70),2)) + 'e.')
    elif 300 >= LH >= 200:
        print('Tuotteen alennus on 20% ja hinnaksi jää', str(round((LH*0.80),2)) + 'e.')
    elif 200 >= LH >= 100:
        print('Tuotteen alennus on 10% ja hinnaksi jää', str(round((LH*0.90),2)) + 'e.')
    elif LH < 100:
        print('Tuotteen alennus on 0% ja hinnaksi jää', str(round(LH,2)) + 'e.')
Alennus = ""
if Valinta == 2:
    print('Monella erillisellä valintarakenteella tulokset ovat seuraavat:')
    if LH >= 300:
        LH = LH*0.7
        Alennus = "30%"
    if LH >= 200:
        LH = LH*0.8
        Alennus = "20%"
    if LH >= 100:
        LH = LH*0.9
        Alennus = "10%"
    print('Tuotteen alennus on ' + Alennus + ' ja hinnaksi jää ' + str(round(LH,2)) + 'e.')
print("Kiitos ohjelman käytöstä.")
