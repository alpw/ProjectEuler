pounds = [1,2,5,10,20,50,100,200]
pounds.sort(reverse=True)

ways = [0,0,0,0,0,0,0,0]

theWayCounter = 0

def calculator():
    maxValue = 200
    for cent, counter in zip(pounds,ways):
        maxValue -= cent*counter
    if maxValue == 0:
        theWayCounter += 1
    elif maxValue < 0:
        return False
    else:
        return True

while calcuator:
    pass