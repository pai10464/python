x, y = [e for e in input().split()]
book = open(x, "r")
ans = []
for e in book:
    a = [i for i in e.split()]
    if y[2:] == a[0][:2]:
        ans.append(float(a[1]))
if len(ans) == 0:
    print('No data')
else:
    print(min(ans), max(ans), sum(ans) / len(ans))
