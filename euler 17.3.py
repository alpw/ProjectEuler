birlik = ["one","two","three","four","five","six","seven","eight","nine"]

onyirmi = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

onluk = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

yüzlük = ["onehundred","twohundred","threehundred","fourhundred","fivehundred","sixhundred","sevenhundred","eighthundred","ninehundred"]

bin = ["onethousand"]


def birdenyüze():
    liste = []
    for i in birlik:
        liste.append(i)

    liste.append("ten")

    for i in onyirmi:
        liste.append(i)

    for i in onluk:
        liste.append(i)
        for l in birlik:
            liste.append(i+l)

    return liste

liste = birdenyüze()

yeniliste = list()

yeniliste.append(liste)

for i in yüzlük:
    yeniliste.append(i)
    for l in liste:
        yeniliste.append(i+"and"+l)


say = yeniliste.pop(0)

print(yeniliste)

son = 0

for k in yeniliste:
    for s in k:
        son += s.__len__()

son += bin[0].__len__()

for es in say:
    son += es.__len__()

print(son)