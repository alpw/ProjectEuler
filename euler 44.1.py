pentalar = list()

def pentaekle(x):
    pentalar.append(x*(3*x-1)/2)
    return x*(3*x-1)/2

pentaekle(1)
pentaekle(2)

dur = 0
a = 2
while dur < 5:
    a += 1
    pentaekle(a)
    print(len(pentalar))
    for i in pentalar:
        for l in pentalar:
            if i-l in pentalar and i+l in pentalar:
                print("Bulundu  : ",i," ve ",l)
                print("SONUÇ =  ",abs(i-l))
                dur += 10
                break


