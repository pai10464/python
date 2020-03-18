def convex_polygon_area(p):
    area = 0
    for e in range(len(p)):
        if e == len(p) - 1:
            area += (p[e][0] * p[0][1]) - (p[e][1] * p[0][0])
            return abs(1/2 * area)
        area += (p[e][0] * p[e + 1][1]) - (p[e][1] * p[e + 1][0])


def is_heterogram(s):
    s = s.lower()
    alp = 'abcdefghijklmnopqrstuvwxyz'
    have = []
    for e in s:
        if e in alp and e in have:
            return False
        have.append(e)
    return True


def replace_ignorecase(s, a, b):
    x = s.split()
    ans = []
    for e in range(len(x)):
        y = 0
        while x[e].lower().find(a.lower(), y) != -1:
            fix = x[e].lower().find(a.lower(), y)
            x[e] = x[e][:x[e].lower().find(a.lower(), y)] + b + x[e][x[e].lower().find(a.lower(), y) + len(a):]
            y = fix + len(b)
        ans.append(x[e])
    return ' '.join(ans)


def top3(votes):
    ans = []
    for keys, value in votes.items():
        ans.append([-value, keys])
    ans.sort()
    x = []
    for e in range(len((ans))):
        if e == 3:
            break
        x.append(ans[e][1])
    return x


for k in range(2):
    exec(input().strip())
