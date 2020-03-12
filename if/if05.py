x = int(input())
n = ['even', 'odd']
c = ['positive', 'negative', 'zero']
if x % 2 == 0:
    i = 0
else:
    i = 1
if x > 0:
    e = 0
elif x < 0:
    e = 1
else:
    e = 2
print(c[e])
print(n[i])