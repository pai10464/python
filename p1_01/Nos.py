import math
bd,bm,by,d,m,y = [int(e) for e in input().split()]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (by - 543) % 400 == 0 :
    month[1] = 29
elif (by - 543)%4 == 0 and (by - 543) % 100 != 0:
    month[1] = 29
day1 = month[bm-1] - bd + 1
for e in range(bm,12) :
    day1 += month[e]
day2 = 365*(y-by-1)
month[1] = 28
if (y - 543) % 400 == 0 :
    month[1] = 29
elif (y - 543) % 4 == 0 and (y - 543) % 100 != 0:
    month[1] = 29
day3 = d - 1
for e in range(m-1):
    day3 += month[e]
day = day1+day2+day3
physical = math.sin((2*math.pi*day)/23)
emotional = math.sin((2*math.pi*day)/28)
intellectual = math.sin((2*math.pi*day)/33)
print(day,"{:.2f}".format(physical),"{:.2f}".format(emotional),"{:.2f}".format(intellectual))