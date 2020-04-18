n = int(input())
limit = {}
amount = {}
for e in range(n):
    x = input().split()
    limit[x[0]] = int(x[1])
    amount[x[0]] = 0
data = []
m = int(input())
for e in range(m):
    x = input().split()
    data.append([float(x[1]), x[0], x[2:]])
data.sort(reverse=True)
ans = []
for e in data:
    for i in e[2]:
        if amount[i] < limit[i]:
            ans.append([e[1], i])
            amount[i] += 1
            break
ans.sort()
for e in ans:
    print(' '.join(e))