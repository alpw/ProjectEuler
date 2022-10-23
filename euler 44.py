pentagonals = []
a = 1
for i in range(0,2000):
    a = i*(3*i-1)/2
    pentagonals.append(a)

a = 0
farklar = []
for i in pentagonals:
    a += 1
    print("Bakılıyor    : ",i,"kaldı: ",2000-a)
    for l in pentagonals[a-1:]:

        if pentagonals.count(int(l-i)) != 0 and pentagonals.count(int(l+i)) != 0:
            farklar.append(int(l-i))

a = 10000000
for i in farklar:
    if a > i:
        a = i

print(a,farklar)