
fractions = []

def denetletyici(x):
    tekrarlar = []
    num = str(x)
    num = num[2::]
    for i in range(len(num)):
        for l in range(len(num)):
            if i+l < len(num):
                if num[i] == num[i+l]:
                    print("bulunduu")
                    tekrarlar.append([num[i],num[i+l]])
                    i += 1
                    continue
                else:
                    fractions.append(toStr(tekrarlar))
                    tekrarlar = []            
            else:
                fractions.append(toStr(tekrarlar))
                tekrarlar = []

def toStr(x):
    total = "0."
    for i in x:
        total += str(i)
    return total


for xx in range(2,11):
    num = 1/xx
    denetletyici(num)
    
for i in fractions:
    for l in i:
        

print(fractions)