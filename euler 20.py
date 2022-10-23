# 100! sayısının rakamları toplamı

def fakto(x):
    sonuc = 1
    for i in range(2,x+1):
        sonuc *= i
    return sonuc

def rakamtop(x):
    toplam = 0
    for i in str(x):
        toplam += int(i)
    return toplam

sayı = int(input("Sayıyı giriniz    :"))
print("Sonuç        :",rakamtop(fakto(sayı)))