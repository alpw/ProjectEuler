import math

def asalmı(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x % i == 0):
            return False
    return True

def carpanbul(x):
    carpanlar = []
    if(not asalmı(x)):
        for xin in range(1,int(math.sqrt(x))+1):
            if(x % xin == 0):
                carpanlar.append(xin)
                carpanlar.append(int(x/xin))
    return carpanlar

def eleme(liste):
    for listedeki in liste:
        if not asalmı(listedeki):
            liste.remove(listedeki)
    return liste

a,b,c,d = 50,0,0,0
while True:
    asallara = []
    asallarb = []
    asallarc = []
    asallard = []
    carpanlara = []
    carpanlarb = []
    carpanlarc = []
    carpanlard = []

    a += 1
    b = a+1
    c = a+2
    d = a+3

    carpanlara = carpanbul(a)
    asallara = eleme(carpanlara)

    if len(asallara) == 3:
        carpanlarb = carpanbul(b)
        asallarb = eleme(carpanlarb)

        if len(asallarb) == 3:
            carpanlarc = carpanbul(c)
            asallarc = eleme(carpanlarc)

            if len(asallarc) == 3:
                carpanlard = carpanbul(d)
                asallard = eleme(carpanlard)
                print("3")

                if len(asallard) == 3:
                    sonuc = a
                    break
                    print("4")

print("Bulundu : ",sonuc)