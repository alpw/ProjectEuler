max = 10000000

def facto(x):
    if x == 1:
        return 1
    total = 1
    for i in range(2,x+1):
        total *= i
    return total

def sumFacts(x):
    strx = str(x)
    lal = 0
    for i in strx:
        num = int(i)
        lal += facto(num)
    return lal

num = 2
total = 0

while num < max:
    num += 1
    if num == sumFacts(num):
        total += num
    print(total,num)

    """WORKİİİİNG İ İLE WORKİİİİNG"""