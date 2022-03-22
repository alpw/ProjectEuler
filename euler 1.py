# 1000'den küçük, 3'ün ve 5'in katlarını topla
x = sum([x for x in range(1000) if ((x % 5 == 0) or (x % 3 == 0))])
print(x)
