#2 milyondan küçük aslların toplamı
import math

def asalmı(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x % i == 0):
            return False
    return True

a = 0
b = 2
while b < 2000000:
    if(asalmı(b)):
        a += b
        print("eklendi  :",b)
    b += 1
print(a)