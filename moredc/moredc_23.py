n = int(input())
data = {}
for e in range(n):
    x = input().split(',')
    if x[2].strip(' ') not in data:
        time = [int(e) for e in x[3].split(':')]
        data[x[2].strip(' ')] = (time[0] * 60) + time[1]
    else:
        time = [int(e) for e in x[3].split(':')]
        data[x[2].strip(' ')] += (time[0] * 60) + time[1]
ans = []
for key, value in data.items():
    ans.append([value, key])
ans.sort(reverse=True)
if len(ans) >= 3:
    for e in range(3):
        print(ans[e][1] + ' --> ' + str(ans[e][0] // 60) + ':', end='')
        if ans[e][0] % 60 < 10:
            print('0' + str(ans[e][0] % 60))
        else:
            print(str(ans[e][0] % 60))
else:
    for e in range(len(ans)):
        print(ans[e][1] + ' --> ' + str(ans[e][0] // 60) + ':', end='')
        if ans[e][0] % 60 < 10:
            print('0' + str(ans[e][0] % 60))
        else:
            print(str(ans[e][0] % 60))
