truncatables = []
num = 9

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2,int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True

def calcTrun(nbr):
    for i in range(1,len(nbr)):
        number = int(nbr[0:i])
        if not isPrime(number):
            return False
    return True

def isTrun(x):
    strx = str(x)
    strxr = strx[::-1]
    if calcTrun(strx) and calcTrun(strxr):
        return True
    return False

while len(truncatables) < 11:
    num += 1
    if isTrun(num) and isPrime(num):
        truncatables.append(num)
    print(len(truncatables),num)

print(sum(truncatables))