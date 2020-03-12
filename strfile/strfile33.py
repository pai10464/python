def import_file(data):
    x = open(data, 'r')
    ans = []
    for e in x:
        a = [i for i in e.split()]
        ans.append([a[0][-2:], a[0], a[1]])
    ans.sort()
    return ans


x, y = [e for e in input().split()]
ans = import_file(x) + import_file(y)
ans.sort()
for e in ans:
    print(e[1], e[2])
