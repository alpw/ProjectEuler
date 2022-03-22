fibo = [1,1,2]

def ömer():
    while True:
        a = fibo[-1] + fibo[-2]
        fibo.append(a)

        if len(fibo) == 500:
            break



