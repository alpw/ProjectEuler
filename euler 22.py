alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

def silici(x):
    yeni = x[1::]
    return yeni

dosya = open("p042_words.txt","r")


alp = dosya.read()

listem = alp.split("\",")
yeniListem = []
print(listem)
for i in listem:
    yeniListem.append(silici(i))

print(yeniListem)

points = list()
zeler = 0

for kelime in yeniListem:
    for harf in kelime:
        harf = 0
        for harfSayar in alphabet:
            harf += 1
            if harfSayar == harf:
                 points.append(harf)
            if harf == 26:
                zeler += 1
print(zeler)
dosya.close()

