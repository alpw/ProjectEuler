import math

bul = []
c = 0
d = 1

for b in range(500,10,-1):
    for a in range(b,10,-1):
        c = math.sqrt(a**2 + b**2)
        print("bakıldı  :",int(a+b+c))
        if(a + b + c == 1000):
            print("Bulundu  :", a , b , c)
            bul.append(a)
            bul.append(b)
            bul.append(c)
            d = a*b*c
print(bul,d)