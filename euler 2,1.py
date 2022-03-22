#Fibonacci sayılarından çift olanların toplamı
x = 0
a = 0
b = 1

while b < 4e6:
    y = a
    a = b
    b += y
    print(y)

    if(a % 2 == 0):
        x += a

print(x)