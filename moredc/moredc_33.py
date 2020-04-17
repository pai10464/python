from collections import OrderedDict


def add_poly(p1, p2):
    ans = OrderedDict()
    for e in p1:
        ans[e[1]] = e[0]
    for e in p2:
        if e[1] in ans:
            ans[e[1]] += e[0]
        else:
            ans[e[1]] = e[0]
    x = []
    for key, value in ans.items():
        if value != 0:
            x.append((value, key))
    x.sort(reverse=True, key=lambda g: g[1])
    return x


def mult_poly(p1, p2):
    ans = OrderedDict()
    for e in p1:
        for i in p2:
            k = e[1] + i[1]
            v = e[0] * i[0]
            if k in ans:
                ans[k] += v
            else:
                ans[k] = v
    x = []
    for key, value in ans.items():
        if value != 0:
            x.append((value, key))
    x.sort(reverse=True, key=lambda g: g[1])
    return x


for i in range(3):
    exec(input().strip())