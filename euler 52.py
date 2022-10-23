def olurmu1(x):
    doublex = x*2
    for i in str(x):
        if not i in str(doublex):
            return False
    return True

def olurmu2(x):
    doublex = x*2
    for i in str(doublex):
        if not i in str(x):
            return False
    return True

def sağladımı(x):
    if olurmu1 and olurmu2:
        return True
    else:
        return False

sayı = 3

while True:
    sayı += 1
    print(sayı)
    if sağladımı(sayı):
        break

print("Bulundu!!!   : ",sayı)