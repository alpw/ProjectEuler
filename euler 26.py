
"""
def findRepeat(result):
    for index in range(len(result)):
        for index2 in range(index + 1, len(result[index::])):
            
    return 0

print("214567321321321")
print(findRepeat("214567321321321"))


"""




repeats = []   #[[7,6]]

for i in range(2,int(input())):
    result = ""
    num = 1
    for _ in range(100):
        if num < i:
            num *= 10
        result += str(num // i)
        num -= (num // i) * i
    listem = [i,findRepeat(result)]
    repeats.append(listem)

repeats.sort(reverse=True)

for i in repeats:
    print(i)
