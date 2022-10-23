def kalan(bölünen, bölen):
    ct = bölünen // bölen
    return bölünen - (ct * bölen)

kallan = 0

def bölme(böllünen, böllen):
    global kallan
    sıfırlar = 0
    bölüm = ""
    while böllünen < böllen:
        böllünen *= 10
        bölüm += "0" * sıfırlar
        sıfırlar += 1
    bölüm += str(böllünen//böllen)
    kallan = kalan(böllünen,böllen)
    return bölüm

values = []

for num in range(2,1000):
    kallan = 0
    değer = ""
    değer += bölme(1,num)
    for x in range(300):
        if kallan == 0:
            break
        değer += bölme(kallan,num)
    #print("1/{}: ".format(num), "0,",değer,sep="")
    values.append((num,değer))
"""
def counter2(val,index2):
    for index1 in val:
        if index1 != index2:
            return False
        index2 += 1
    return True

def tekrar(val):
    sayılar = [0]
    x = str(val)
    for index1, digit in enumerate(x):
        for index2,first in enumerate(x[0:index1]):
            if digit == first:
                vall2 = counter2(val[index1:2*index2-index1],index2)

                if index2 == 0:
                    sayılar.append((index1-index2)//2)
                else:
                    sayılar.append(index1-index2)
    return max(sayılar)

print(tekrar("123123123"))"""