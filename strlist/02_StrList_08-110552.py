import math
a, b, c = [e for e in input().split(',')]
x = int(b + c) - int('0' + b)
y = int(('9' * len(c)) + ('0' * len(b)))
if b == '' and c == 0:
    y = 1
x += int(a)*y
i = math.gcd(x, y)
if i > 1:
    x //= i
    y //= i
print(str(x) + ' / ' + str(y))
