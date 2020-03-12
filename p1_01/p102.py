switch = input()
if switch == 'str2RLE':
    x = [e for e in input()]
    control = x[0]
    no_control = [x[0]]
    count = [0]
    i = 0
    ans = ''
    for e in range(len(x)):
        if x[e] != control:
            no_control.append(x[e])
            control = x[e]
            count.append(1)
            i += 1
        else:
            count[i] += 1
    for e in range(len(no_control)):
        ans += no_control[e] + ' ' + str(count[e]) + ' '
    print(ans)
elif switch == 'RLE2str':
    x = [e for e in input().split()]
    alpha = [e for e in x[:-1:2]]
    num = [e for e in x[1::2]]
    ans = ''
    for e in range(len(alpha)):
        ans += alpha[e] * int(num[e])
    print(ans)
else:
    print('Error')