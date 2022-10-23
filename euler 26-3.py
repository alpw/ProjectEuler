def findRepeat(text):
    values = [0,]
    for index1 in range(len(text)-2):
        for index2 in range(index1+1,len(text)-1):
            if text[index1] == text[index2]:
                if text[index1:index2] == text[index2:index2+(index2-index1)]:
                    values.append(index2-index1)
                    print(max(values))
    return max(values)


def div(num):
    one = 1
    total = ""
    for _ in range(10000):
        if num > one:
            one *= 10
        total += str(one//num)
        one -= num*(one//num)
        if one == 0:
            return total
    return total

print(findRepeat(div(17)))



whole = []
for i in range(2,1000):
    tp = (findRepeat(div(i)),i)
    whole.append(tp)

print(max(whole))
