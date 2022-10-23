sec = 1
oldsec = 1
thr = 1
terim = 2

while True:
    oldsec = sec
    sec = thr
    thr += oldsec
    terim +=1
    if(len(str(thr)) == 1e3):
        break

print(thr)
print(terim)