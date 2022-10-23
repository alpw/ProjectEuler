num = 123456789

def isOneTime(x):
    numstr = str(x)
    if len(numstr) == 9:
        numstr = "0" + numstr
    for i in numstr:
        if numstr.count(i) > 1:
            return False
    return True

counter = 0
thex = 0
while num < 987654322:
    if isOneTime(num):
        counter += 1
        num += 1
    else:
        num += 1
    if counter == 1000000:
        thex = num
    print("sayı:{}  ".format(counter),"%",counter/10000,"sayı = {}".format(thex))

