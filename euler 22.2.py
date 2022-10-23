alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

dosya = open("p022_names.txt","r")

"""WORKINGGGG""""""WORKINGGGG""""""WORKINGGGG"""

içerik = dosya.read()

listem = içerik.split(",")

for k,l in enumerate(listem):
    listem[k] = l[1:-1]

print(listem)
listem.sort()

puanlar = list()

for index,kelime in enumerate(listem):
    harfPuan = []
    for harf in kelime:
        sayı = alphabet.index(harf)
        harfPuan.append(sayı+1)
    score = sum(harfPuan) * (index+1)
    print(score,harfPuan,kelime)
    puanlar.append(score)

print(sum(puanlar))