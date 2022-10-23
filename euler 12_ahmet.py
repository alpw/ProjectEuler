

import math 

def asalmı(x):
    for e in range(2,int(math.sqrt(x))+1):
        if(x % e == 0):
            return False
    return True

sayaç, counter = 0,0
a = 3
print(a)
while counter < 500 or sayaç != a:
    a+=1
    if not asalmı(a):
        sayaç, counter = 0,0
        for b in range(1,int(math.sqrt(a))+1):
            if a % b == 0:
                sayaç += b
                sayaç += a/b
                counter += 2
        if a % 1000 == 0:
            print(a)

print(a)

