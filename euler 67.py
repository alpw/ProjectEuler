file = open("p067_triangle.txt","r")

triangle = []
dal = []
for i in file:
    dal = i[:-1].split(" ")
    for ct,l in enumerate(dal):
        dal[ct] = int(dal[ct])
    triangle.append(dal)

print(triangle)
print(len(triangle))

file.close()

twoPows = list(map(lambda x: 2**x, range(42)))
twoPows.reverse()

def findPow(x):
    counter = 0
    while True:
        if 2**counter == x:
            return counter
        counter += 1

def decToBin(dec):
    bin = []
    for i in range(100):
        bin.append(0)
    for pow in twoPows:
        if dec >= pow:
            bin[-findPow(pow)-1] = 1
            dec = dec - pow
    return(bin)

def summer(num):
    way = decToBin(num)
    road = 0
    total = 0
    for counter,i in enumerate(triangle):
        road += way[counter]
        total += i[road]
    return total

maxInPath = 0

for i in range(1000000000000):
    araTop = summer(i)
    if maxInPath < araTop:
        maxInPath = araTop
        print(maxInPath)

print(maxInPath)