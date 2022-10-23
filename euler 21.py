amicab = []

def carpanbul(x):
    carpanlar = []
    carpanlar.append(x)
    for i in range(1,int(x/2)+1):
        if(x % i == 0):
            carpanlar.append(i)
    return carpanlar

amicab = []
carpanlar = []

a = 0
while a < 1e4:
    a += 1
    print("bakılıyor : ",a)
    carpanbul(a)
    topa = sum(carpanlar)
    b = topa
    carpanbul(b)
    topb = sum(carpanlar)
    if(topb == a):
        amicab.append(a)
        amicab.append(b)

print("bulundu  : ",sum(amicab))