eightynines = 0

def sumSqrt(x):
    txt = str(x)
    total = 0
    for i in txt:
        total += int(i)*int(i)
    return total

def ChainFinder(x):
    global eightynines
    if x == 89:
        eightynines += 1
        return False
    elif x == 1:
        return False
    return True

for num in range(2,int(1e7)):
    while ChainFinder(sumSqrt(num)):
        num = sumSqrt(num)

print(eightynines)
x = input("alperej")

""" ...::: WORKING :::... but slowly""" 