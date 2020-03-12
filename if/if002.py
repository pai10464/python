d, m, y = [int(e) for e in input().split()]
yon = [4, 6, 9, 11]
d += 15
n = 31
if m in yon:
    n = 30
if m == 2:
    n = 28
    x = y - 543
    if x % 400 == 0:
            n = 29
    if x % 4 == 0 and x % 100 > 0:
            n = 29
if d > n:
    m += 1
    d -= n
if m > 12:
    y += 1
    m -= 12
print(str(d)+'/'+str(m)+'/'+str(y))