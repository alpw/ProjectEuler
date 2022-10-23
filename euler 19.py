ocak, subat, mart, nisan, mayıs, haziran, temmuz, ağustos, eylül, ekim, kasım, aralık = 31,28,31,30,31,30,31,31,30,31,30,31

yılgün = ocak+subat+mart+nisan+mayıs+haziran+temmuz+ağustos+eylül+ekim+kasım+aralık


günsay = 0

for yıl in range(1991,2001):
    if yıl % 4 == 0 and yıl % 400 != 0:
        günsay += 1
    günsay += yılgün

print(günsay/7)