sum = 0
num1 = 0
num2 = 1

while num2 < 4e6:
    temp = num1
    num1 = num2
    num2 = num1 + temp

    if (num1 % 2 == 0):
        sum += num1

print('The sum is: ' + str(sum))