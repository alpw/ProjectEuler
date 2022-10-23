def isPandigital(num):
    numStr = str(num)
    for digit in numStr:
        if numStr.count(digit) > 1:
            return False
    return True

def isPrime(x):
    if x == 1 or x == 0:
        return False
    elif x == 2:
        return True
    for num in range(2,int(x**(1/2))+1):
        if x % num == 0:
            return False
    return True

total = 0
for number in range(1023456789,9876543210):
    numberStr = str(number)