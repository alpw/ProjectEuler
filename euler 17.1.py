ilkon = 3+3+5+4+4+3+5+5+4
kümeilkon = [3,3,5,4,4,3,5,5,4]
onyirmi = 3+6+6+8+8+7+7+9+8+8
onluklar = 6+6+6+5+7+6+6
kümeonluklar = [6,6,6,5,7,6,6]
kümeyüzlükler = [10,10,12,11,11,10,12,12,11]

sonuc = 0

biryüz = 0
biryüz += ilkon
biryüz += onyirmi
for i in kümeonluklar:
    biryüz += i
    for l in kümeilkon:
        biryüz += l
        biryüz += i

for a in kümeyüzlükler:
    sonuc += biryüz
    sonuc += a*100
    sonuc += 3*99

sonuc += 11

print(sonuc)