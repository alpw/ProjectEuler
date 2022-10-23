import random

pounds = [1,2,5,10,20,50,100,200]
coins = 200
way = []
index = 0
ways = []

def choose(remain):
    global coins
    global index
    index = random.randint(0,7)
    if pounds[index] > coins:
        choose(remain)
    else:
        coins -= pounds[index]

def toString(counter):
    token = ""
    for i in counter:
        for l in i:
            token += str(l)
            token += "x"
        token += "_"
    return token

def addWay():
    way.sort()
    counter = []
    for i in way:
        eklenecek = [i,way.count(i)]
        if not eklenecek in counter:
            counter.append(eklenecek)
    ourStr = toString(counter)
    if not ourStr in ways:
        ways.append(ourStr)

while True:
    choose(coins)
    if coins > 0:
        way.append(pounds[index])
        continue
    elif coins == 0:
        way.append(pounds[index])
        addWay()
        coins = 200
        way = []
    print(len(ways))