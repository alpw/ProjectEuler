starter = 2 ** 19

i = 19


def counter(x):
    count = 0
    while x > 0:
        x /= 10
        count += 1
    return count


def dublicate(x):
    new = x * 2
    if x % 25 == 0:
        new = int(str(new)[-10::])
    return new


while i < 7830457:
    i += 1
    starter = dublicate(starter)

multi = starter * 28433

total = multi + 1
print(total)
print(total[-10::])

