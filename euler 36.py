pows = list(map(lambda x: 2**x , range(1,20)))
pows.sort(reverse=True)
pows.append(1)
print(pows)

def toBinary(x):
    bin = 0
    for i in pows:
        if i <= x:
            x -= i
            bin += 10**(len(pows) - pows.index(i) - 1)
    return bin

def yielding(x):
    txt = str(x)
    for i in range(len(txt)//2 + 1):
        yield txt[i] == txt[-1-i]

def isPalin(x):
    if all(yielding(x)):
        return True
    else:
        return False

nums = []

for num in range(int(1e6)):
    if isPalin(num) and isPalin(toBinary(num)):
        nums.append(num)

print(nums)
print(sum(nums))


"""WORKIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIING"""