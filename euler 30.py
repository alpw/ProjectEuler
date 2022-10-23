max = (9 ** 5) * 5

def sumPowFive(x):
    strx = str(x)
    sum = 0
    for i in strx:
        digit = int(i)
        sum += digit**5
    return sum

total = 0
for num in range(2,max+1):
    if num == sumPowFive(num):
        total += num
    print("%{}".format(num/max*100))

print(total)