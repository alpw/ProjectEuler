"""NUMBER SPİRAL DIAGNOALS"""

"""3'er 3'er 4 kez, 5'er 5'er 4 kez...
   3 + 2*499 kez artış sağla"""

total = 1
i = 1
for coefficident in range(2,1001,2):
    for num in range(1,5):
        i += coefficident
        total += i

print(total)