name1, month1, day1, year1 = [e for e in input().split()]
name2, month2, day2, year2 = [e for e in input().split()]
no_month1 = 0
no_month2 = 0
no_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for i in range(12):
    if month1 == no_month[i]:
        no_month1 = i + 1
    if month2 == no_month[i]:
        no_month2 = i + 1
if year1 == year2 and no_month1 == no_month2 and day1 == day2:
    print(name1, name2)
if year1 > year2:
    print(name2)
elif year2 > year1:
    print(name1)
elif no_month1 > no_month2:
    print(name2)
elif no_month2 > no_month1:
    print(name1)
elif day1 > day2:
    print(name1)
elif day2 > day1:
    print(name2)