
def div(num):
    one = 1
    total = ""
    for _ in range(1000):
        if num > one:
            one *= 10
        total += str(one//num)
        one -= num*(one//num)
        if one == 0:
            return total
    return total



def findRp(number):
    numStr = str(number)
    for first in range(len(numStr)):
        for second in range(first+1, len(numStr)):
            if numStr[first] == numStr[second]:
                if numStr[first:second] == numStr[second:2*second-first]:
                    return numStr[first:second]
    
    

while True:
    a = int(input("gir: "))
    x = 1 / a
    print(div(a))
    print(findRp(str(x)[2::]))

"""
totals = []
for x in range(3,1000):
    try:
        totals.append(len(findRp(x)))
    except:
        continue

totals.sort

print(totals)"""