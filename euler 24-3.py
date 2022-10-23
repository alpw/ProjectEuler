nums = []

def counter(x):
    num = str(x)
    listem = []
    for i in num:
        listem.append(num.count(i))
    return listem

for i in range(123456788,9876543211):
    if all(counter(i)):
        nums.append(i)
    
print("birinci aşama tamamlandı")

lasts = []

for i in nums:
    if len(i) == 9:
        lasts.append(i)

print(lasts[999999])