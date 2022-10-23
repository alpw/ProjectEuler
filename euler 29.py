üsler = []
üsler2 = []
for i in range(2,101):
    for l in range(2,101):
        üsler.append(i**l)


for i in üsler:
    if not i in üsler2:
        üsler2.append(i)

print(len(üsler2))