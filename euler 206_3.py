

for i in range(1010101010,1389026623+1):
    statement = True
    for counter, digit in enumerate(str(i*i)):
        if counter % 2 == 0 and counter != int(digit):
            statement = False
            print(i)

    if statement:
        break
print(i)
