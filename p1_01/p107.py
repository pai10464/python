import math
bd, bm, by, d, m, y = [int(e) for e in input().split()]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (by - 543) % 400 == 0:
    month[1] = 29
elif (by - 543) % 4 == 0 and (by - 543) % 100 != 0:
    month[1] = 29
rad = month[bm - 1] - bd + 1
for e in range(bm, 12):
    rad += month[e]
black = (y - by - 1) * 365
blue = d - 1
month[1] = 28
if (y - 543) % 400 == 0:
    month[1] = 29
elif (y - 543) % 4 == 0 and (y - 543) % 100 != 0:
    month[1] = 29
for e in range(m-1):
    blue += month[e]
sum_day = rad + black + blue
phy = math.sin((2 * math.pi * sum_day) / 23)
emo = math.sin((2 * math.pi * sum_day) / 28)
inte = math.sin((2 * math.pi * sum_day) / 33)
print(sum_day, "{:.2f}".format(phy), "{:.2f}".format(emo), "{:.2f}".format(inte))