b = 0
for i in range(1, 1001):
    a = i ** i
    b += a
    print(a)

print("işte")
print(b)
print(str(b)[-10::])
