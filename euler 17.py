"""BİRDEN BİNE KADAR SAYI YAZILIŞI, HARFLERİ SAYSI(1 VE 1000 DAHİL)"""

birtodokuz = [3,3,5,4,4,3,5,5,4]
onluklar =   [6,6,6,5,5,7,6,6]
ontoondokuz = [3,6,6,8,8,7,7,9,8,8]
yuzlukler =  [10,10,12,11,11,10,12,12,11]

top = 0
bir = sum(birtodokuz)
on = sum(onluklar)
yuz = sum(yuzlukler)

#10'A KADAR
top += bir
#100'E KADAR
yirmiyüz = on + len(onluklar)*bir
yüzbin = (yirmiyüz + 3)*9
#KALAN ONLUKLAR
onyirmi = 3+6+6+7+8+7+9+8+8
top += onyirmi*10
#1000
top += 10
#KULLANILAN TÜM ANDLER
top += 99*9*3

print(top)