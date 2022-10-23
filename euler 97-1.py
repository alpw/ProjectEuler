total = 2**30

def toTen(x):
    num = str(x)[-6::]
    return int(num)

for i in range(31,7830458):
    total = toTen(total)
    total = total ** 2

total = toTen(total)
print(total)

total *= 28433
total += 1

print(total)
print(str(total)[-10::])