n = int(input())
data = []
for e in range(n):
    data.append(input().split())
fil = input().split()
data.sort()
ans = []
for e in data:
    check = 0
    for i in fil:
        if i not in e[1:]:
            check = 1
            break
    if check == 0:
        ans.append(e)
        print(' '.join(e))
if len(ans) == 0:
    print('Not Found')