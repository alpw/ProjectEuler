def isPrime(x):
    if x < 2:
        return False
    for i in range(2,int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True

def isTruncatable(x):
    xstr = str(x)
    for i in range(1,len(xstr)):
        num = int(xstr[0:i])
        if not isPrime(num):
            return False
    xstr = xstr[::-1]
    for i in range(1,len(xstr)):
        num = int(xstr[0:i])
        if not isPrime(num):
            return False
    return True

truncatables = []

num = 10
while len(truncatables) < 11:
    num += 1
    if isTruncatable(num) and isPrime(num):
        truncatables.append(num)
    print(len(truncatables),num)

print(sum(truncatables))