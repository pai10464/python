a = float(input())
L = 0; U = a
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
