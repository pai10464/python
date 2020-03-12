d = int(input())
m = int(input())
y = int(input())
f = 28
p = y - 543
if p % 400 == 0:
    f = 29
if p % 4 == 0 and p % 100 > 0:
    f = 29
i = 0
x = 0
month = [31, f, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while i <= (m-2):
    x += month[i]
    i += 1
x += d
print(int(x))
