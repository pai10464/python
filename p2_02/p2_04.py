order = []
t_d = {'E': 1, 'Q': 3, 'N': 7, 'F': 14}
while True:
    order.append(input().split())
    if order[-1][0] == 'END':
        break


def d_month(m, y):
    f = 28
    if (y - 543) % 400 == 0:
        f = 29
    if (y - 543) % 4 == 0 and (y - 543) % 100 != 0:
        f = 29
    month = [31, f, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month[m - 1]


def sent(d, m, y, t):
    d += t_d[t]
    if d > d_month(m, y):
        d -= d_month(m, y)
        m += 1
    if m > 12:
        m -= 12
        y += 1
    return [y, m, d]


ans = []
for e in order[:-1]:
    if int(e[4]) < 2558:
        print('Error: ' + ' '.join(e) + ' --> Invalid year')
    elif int(e[3]) not in range(1, 13):
        print('Error: ' + ' '.join(e) + ' --> Invalid month')
    elif int(e[2]) > d_month(int(e[3]), int(e[4])) or int(e[2]) == 0:
        print('Error: ' + ' '.join(e) + ' --> Invalid date')
    elif e[1] not in t_d:
        print('Error: ' + ' '.join(e) + ' --> Invalid delivery type')
    else:
        x = sent(int(e[2]), int(e[3]), int(e[4]), e[1])
        x.append(e[0])
        ans.append(x)
ans.sort()
for e in ans:
    print(str(e[-1]) + ': delivered on ' + str(e[2]) + '/' + str(e[1]) + '/' + str(e[0]))