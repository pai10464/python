p1 = int(input())
ans = []
i = -1
for e in range(p1):
    if i == 0:
        ans.insert(0, int(input()))
        i = -1
    elif i == -1:
        ans.append(int(input()))
        i = 0
p2 = [int(e) for e in input().split()]
for e in range(len(p2)):
    if i == 0:
        ans.insert(0, p2[e])
        i = -1
    elif i == -1:
        ans.append(p2[e])
        i = 0
while True:
    a = int(input())
    if a == -1:
        print(ans)
        exit()
    if i == 0:
        ans.insert(0, a)
        i = -1
    elif i == -1:
        ans.append(a)
        i = 0
