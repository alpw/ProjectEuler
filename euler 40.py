a = 0
sayılarr = ""
while len(sayılarr) < 1000002:
    a += 1
    sayılarr = sayılarr + str(a)

x = int(sayılarr[1-1])
y = int(sayılarr[10-1])
z = int(sayılarr[100-1])
k = int(sayılarr[1000-1])
n = int(sayılarr[10000-1])
m = int(sayılarr[100000-1])
l = int(sayılarr[1000000-1])

print(x*y*z*k*l*m*n)