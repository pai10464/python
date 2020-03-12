x = [e for e in input()]
not_du = []
ans = ''
for e in range(len(x)):
    if x[e] not in not_du:
        not_du.append(x[e])
num = list(range(len(not_du)))
no_du = 0
for e in not_du:
    num[no_du] = 0
    for i in x:
        if i == e:
            num[no_du] += 1
    no_du += 1
for e in range(len(not_du)):
    ans += not_du[e] + ' ' + str(num[e]) + ' '
print(ans)