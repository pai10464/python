x = input().lower().strip()
a = 'abcdefghijklmnopqrstuvwxyz'
unique = []
ans = []
for e in x:
    if e not in unique and e in a:
        unique.append(e)
for e in unique:
    ans.append([-x.count(e), e])
ans.sort()
for e in range(len(ans)):
    print(ans[e][1] + ' ->', -ans[e][0])