from collections import OrderedDict
data = OrderedDict()
while True:
    x = input().split()
    if len(x) == 1:
        where = x[0]
        break
    else:
        if x[0] in data:
            data[x[0]].append(x[1])
        else:
            data[x[0]] = [x[1]]
        if x[1] in data:
            data[x[1]].append(x[0])
        else:
            data[x[1]] = [x[0]]
if where in data:
    x = set(data[where])
    ans = set(data[where])
    for e in x:
        for i in data[e]:
            ans.add(i)
    ans = list(ans)
    ans.sort()
    print('\n'.join(ans))
else:
    print(where)