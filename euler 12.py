import math

def asalmı(x):
    for e in range(2,int(math.sqrt(x))+1):
        if(x % e == 0):
            return False
    return True

def carpanbul(x):
    carpanlar = []
    if(asalmı(x)):
        carpanlar.append(x)
        carpanlar.append(1)
    else:
        for xin in range(1,int(math.sqrt(x))+1):
            if(x % xin == 0):
                carpanlar.append(xin)
                carpanlar.append(int(x/xin))
    return carpanlar

asd = []
a,tri = 0,0
carpanlar = []
while len(asd) <= 500:
    a += 1
    tri += a
    asd = carpanbul(tri)
    print("Bakılıyor    : ",tri," : ",len(asd))

print(tri, len(asd))