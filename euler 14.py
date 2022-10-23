def kachamle(a):
    dongu = 1
    while True:
        if not a == 1:
            if(a % 2 == 0):
                a = a/2
                dongu += 1
            elif(a % 2 == 1):
                a = 3*a+1
                dongu += 1
        elif a == 1:
            break
    return dongu

hamle = 0
bykhmle = 10
sonuc = 1
for i in range(1,int(1e6)):
    hamle = kachamle(i)
    print("Bakılıyor    : ",i," ",hamle)
    if(hamle > bykhmle):
        bykhmle = hamle
        sonuc = i

print("Sonuç    : ",sonuc,"sayısı,",bykhmle,"hamlede biter.")
