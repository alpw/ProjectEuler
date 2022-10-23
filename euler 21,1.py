import  math

def carptop(x):
    sum = 1
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            sum += i
            sum += x/i
    return int(sum)

amicab = []
for x in range(0,int(1e4)):
    if(x % 100 == 0):
        print("Bakılıyor    : ",x)
    for y in range(x,int(1e4)):
        if carptop(x) == y and carptop(y) == x and x != y:
            amicab.append(x)
            amicab.append(y)
            print("Amicab bulunudu eklendi. Amicab sayısı : ",len(amicab))
print(sum(amicab))
print(amicab)