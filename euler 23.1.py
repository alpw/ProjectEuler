import math

def bolmu(x):
    if sum(çarpanlar(x)) > x:
        return True
    else:
        return False

def çarpanlar(x):
    carpanlar = list()
    for i in range(1,x):
        if x % i == 0:
            carpanlar.append(i)
    return carpanlar

bollar = list()
tümsay = [x for x in range(0,28124)]

for i in range(5,28124):
    print("bol sayılar bulunuyor... %",i/28123*100)
    if bolmu(i):
        bollar.append(i)

for i in range(0,len(bollar)):
    for l in bollar[i::]:
        if bollar[i] + l < 28124:
            tümsay[bollar[i] + l] = 0

print(sum(tümsay))