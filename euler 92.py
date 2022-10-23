chain = []

def findNum(num):
    numStr = str(num)
    retNum = 0
    for i in numStr:
        retNum += (int(i)) ** 2
    return retNum

def addToChain(num):
    chain.append(num)
    while True:
        alp = findNum(chain[-1])
        if alp in chain:
            break
        chain.append(alp)

one,eightynine = 0,0

for i in range(100):
    addToChain(i)
    if findNum(chain[-1]) == 89:
        eightynine += 1
    print(eightynine,i,chain)
    chain = []

print(eightynine)