a,b,c,d,e,f,g,h,ill,j,k,l,m,n,o,p,q,r,s,t,u,v,wll,x,y,z = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26


dosya = open("p022_names.txt","r")


alp = dosya.read()

listem = alp.split("\",")
print(listem)
total = 0
ara = 0


for i in listem:
    print("****************************")
    ara += 1
    mintop = 0
    kelime = i[1::]

    for w in kelime:
        sac = mintop
        if w == "A":
            mintop += a
        if w == "B":
            mintop += b
        if w == "C":
            mintop += c
        if w == "D":
            mintop += d
        if w == "E":
            mintop += e
        if w == "F":
            mintop += f
        if w == "G":
            mintop += g
        if w == "H":
            mintop += h
        if w == "I":
            mintop += ill
        if w == "J":
            mintop += j
        if w == "K":
            mintop += k
        if w == "L":
            mintop += l
        if w == "M":
            mintop += m
        if w == "N":
            mintop += n
        if w == "O":
            mintop += o
        if w == "P":
            mintop += p
        if w == "Q":
            mintop += q
        if w == "R":
            mintop += r
        if w == "S":
            mintop += s
        if w == "T":
            mintop += t
        if w == "U":
            mintop += u
        if w == "V":
            mintop += v
        if w == "W":
            mintop += wll
        if w == "X":
            mintop += x
        if w == "Y":
            mintop += y
        if w == "Z":
            mintop += z
        print(w," - ",mintop-sac)


    total += mintop * ara
    print("     ",ara)

print(total)

dosya.close()