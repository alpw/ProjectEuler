prime = 2**25

for i in range(26,6972593):
    prime = prime ** 2
    prime = int(str(prime)[-10::])

print(prime)
print(str(prime)[-10::])