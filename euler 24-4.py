nums = "0123456789"
value = ""

def popper(num):
    newStr = ""
    for i in nums:
        if i != num:
            newStr += i
    return num + newStr

def harici(ext):
    the = ""
    for i in nums:
        if i != ext:
            the += i
    return the


for index, num in enumerate(nums):
    value1 = popper(num)[0]
    for l in harici(value1):
        value2 = popper()