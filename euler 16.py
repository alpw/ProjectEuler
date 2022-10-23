# 2^1000 sayısının rakamları toplamı = ?
a = 1
for i in range(1,1001):
    a *= 2

print(a)
sonuc = 0
for c in str(a):
    sonuc += int(c)

print(sonuc)