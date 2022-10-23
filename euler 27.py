"""istenen: a,b ===> 1000 için:
    en çok asal bulan denklemi bul ve a*b değerini ver"""
nums = []

def isPrime(x):
    if x < 2:
        return False
    elif x == 2 or x == 3:
        return True
    for i in range(2,int(x**(1/2))):
        if x % i == 0:
            return False
    return True

def finder(a,b):
    num = 0
    while True:
        result = num*num + a*num + b
        num += 1
        if not isPrime(result):
            nums.append([num-1,a*b])
            break

for a in range(-999,1000):
    print((a+1000)/2000*100)
    for b in range(-1000,1001):
        finder(a,b)

print(max(nums))

"""   ...::: WORKED :::...   """