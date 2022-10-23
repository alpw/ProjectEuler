import math

def asalmı(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x % i == 0):
            return False
    return True

def carpanbul(x):
    carpanlar = []
    if(not asalmı(x)):
        for xin in range(2,int(math.sqrt(x))+1):
            if(x % xin == 0):
                carpanlar.append(xin)
                carpanlar.append(int(x/xin))
    tekleyici(carpanlar)
    carpanlar.append(1)
    return carpanlar

def bolmu(x):
    carptop = sum(carpanbul(x))
    if carptop > x:
        return True
    return False

def tekleyici(liste):
    for i in liste:
        for l in liste[liste.index(i)+1:]:
            if i == l:
                liste.remove(l)

bollar = []
for i in range(11,28124):
    if bolmu(i):
        print("Bollar'a eklendi :",i)
        bollar.append(i)

toplamlar = []

for i in bollar:
    print("Toplandı : ",i)
    for l in bollar[bollar.index(i):]:
        toplamlar.append(i+l)

sonuclar = []
sonuc = 0

for i in range(1,28123):
    if toplamlar.count(i) == 0:
        sonuclar.append(i)
        print("EKlendi : ",i)
        sonuc += i
        print("sonuç : ",sonuc)