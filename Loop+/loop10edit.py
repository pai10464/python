a = float(input())
i = a
L = 0
U = 0
while i != 0:
    i = i // 10
    U += 1
x = (U + L) / 2
ans = 10**x
while abs(ans - a) > (10**(-10)) * max(ans, a):
    if ans > a:
        U = x
    else:
        L = x
    x = (U + L) / 2
    ans = 10**x
print(round(x, 6))