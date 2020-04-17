n = int(input())
data = []
union = []
for e in range(n):
    data.append([int(e) for e in input().split()])

# union
for e in data:
    union += e
ans_union = []
for e in union:
    if e not in ans_union:
        ans_union.append(e)
print(len(ans_union))

# intersection
ans_inter = []
for e in ans_union:
    b_check = 0
    for i in data:
        if e not in i:
            b_check = 1
            break
    if b_check == 0:
        ans_inter.append(e)
print(len(ans_inter))
