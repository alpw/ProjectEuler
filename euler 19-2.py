import datetime 

sundays = 0
day = datetime.datetime(1901,1,1)

for i in range(int(1e12)):
    if day.strftime("%A") + day.strftime("%d") == "Sunday01":
        sundays += 1
    day = day + datetime.timedelta(1)
    if day.strftime("%Y") == "2001":
        break

print(sundays)

" ...::: WORKING EZ :::..."