
"""
THATS FUCKN WORKING
"""

def div(num):
    one = 1
    total = ""
    for _ in range(1000):
        if num > one:
            one *= 10
        total += str(one//num)
        one -= num*(one//num)
        if one == 0:
            return total
    return total


def equality(num, index):
    if len(num) > index*2:
        return False
    for i1 in range(0, len(num)-index*2, index):
        i2 = i1+index
        if not num[i1:i2] == num[i2:i2+index]:
            return False
    return True


def findRp(number):
    numStr = str(number)
    for first in range(len(numStr)):
        for second in range(first+1, len(numStr)):
            print(first, second)
            if numStr[first] == numStr[second] and equality(numStr[first::], second-first+1):
                return numStr[first:second]
    return "0"

def findRp2(number):
    numStr = str(div(number))
    for first in range(len(numStr)-1):
        for second in range(first+1, len(numStr)):
            #print(numStr, second , first, equality(numStr[first::], second-first))
            if second - first > 10 and len(numStr[first::])//(second-first)>4 and numStr[first] == numStr[second] and equality(numStr[first::], second-first):
                return second - first
    return 0

def findRp3(number):
    numStr = div(number)
    for index1 in range(len(numStr)//2):
        for index2 in range(index1+1, len(numStr)):
            if numStr[index1] == numStr[index2]:
                if equality(numStr[index1::], index2-index1):
                    return ((index2 - index2, number))
    return ((0,number))

def findRp4(number):
    numStr = str(div(number))
    for index1 in range(len(numStr)//2):
        for index2 in range(index1+1, len(numStr)):
            if numStr[index1] == numStr[index2]:
                repeat = numStr[index1:index2]
                for i in range(0, len(numStr[index1::])//len(repeat)-1):
                    if not numStr[index1+i*len(repeat): index1+(i+1)*len(repeat)] == repeat:
                        return len(repeat)
    return 0


def findRp5(number):
    numStr = div(number)
    for index1 in range(0, len(numStr)-1):
        for index2 in range(index1+1, len(numStr)-(len(numStr)-index1)//2):
            if numStr[index1] == numStr[index2]:
                if isRepeater(numStr[index1::], index2-index1):
                    return (index2-index1, number)
    return (0, number)


def isRepeater(num, count):
    for index in range(0, len(num)-len(num) % count -count, count):
        #print(num[index: index+count] , num[index+count: index+2*count])
        if num[index: index+count] != num[index+count: index+2*count]:
            return False
    return True


print(div(983))

"""
counts = []
for i in range(2,1001):
    counts.append(findRp5(i))

counts.sort(reverse=True)
print(counts[0:5])"""



"""
count kullan ve de ki: coun edilenlerin arası boş ise
"""

"""
counter = []
for i in range(2,12):
    tuplem = (i, findRp4(i))
    print(tuplem)
    counter.append(tuplem)

counter.sort(reverse=True)
print(counter[0:10])"""

"""counts = []
for i in range(2,1001):
    counts.append((findRp2(i), i))

counts.sort(reverse=True)
print(counts[0:10])
"""

#counts = []
#for i in range(2,1001):
#    counts.append((len(findRp(div(i))), i))
#
#counts.sort(reverse=True)
#print(counts[0:5])

