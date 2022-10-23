import random

pounds = [1,2,5,10,20,50,100,200]
ways = []
way = ""
coin = 200
totalWays = []

global choice, creatingWay #,way,ways,coin

def chooser(remain,choosable):
    try:
        index = random.randint(0,len(choosable)-1)
    except:
        index = 0
    chose = choosable[index]
    if chose > remain:
        return chooser(remain,choosable[0:choosable.index(chose)])
    return  chose

def listSort(liste):
    liste = []
    for i in liste:
        if liste.count(i) > 2:
            liste.pop(liste.index(i))
    liste.sort()
    return liste

def createWay(listWays):
    global way
    lastList = listSort(listWays)
    for i in lastList:
        way += "+"
        way += str(i)

def stopper():
    createWay(ways)
    if not way in totalWays:
        totalWays.append(way)

while True:
    ways = []
    choice = chooser(coin,pounds)
    ways.append(choice)
    coin -= choice
    if coin == 0:
        stopper()
    else:
        continue
    print(ways)
    print(len(totalWays))