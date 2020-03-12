control = input()
no_x = int(input())
x = list(range(no_x))
ans = ''
for e in range(no_x):
    x[e] = [e for e in input()]
for e in range(no_x):
    if e == no_x - 1:
        break
    if len(x[e]) != len(x[e+1]):
        print('Invalid size')
        exit()
if control == 'flip':
    for e in range(no_x):
        for i in reversed(x[e]):
            ans += i
        print(ans)
        ans = ''
elif control == '90':
    for e in (range(len(x[0]))):
        for i in reversed(range(no_x)):
            ans += x[i][e]
        print(ans)
        ans = ''
elif control == '180':
    for e in reversed(range(no_x)):
        for i in reversed(x[e]):
            ans += i
        print(ans)
        ans = ''