sayı = [0,1,2,3,4,5,6,7,8,9]
kombinasyonlar = []

def değiştirici(ilk,son):
    sayı.insert(son,sayı.pop(ilk))
    kombinasyonlar.append(sayı)

def sayıTümleyici():
    for i in range(10):
        sayı = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for l in range(9):
            sayı = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            değiştirici(i,l)
            print(sayı)

sayıTümleyici()