n = int(input())
data = []
for e in range(n):
    sub = []
    x = input().split()
    sub.append(x[0])
    for i in x[1:]:
        sub.append(float(i))
    data.append(sub)
command = input().split()


def do_str_list(lv):
    str_list = []
    for j in lv:
        sub_list = []
        for k in j:
            sub_list.append(str(k))
        str_list.append(sub_list)
    return str_list


if command[0] == 'show':
    data = do_str_list(data)
    for e in data:
        print(' '.join(e))

elif command[0] == 'get':
    data = do_str_list(data)
    for e in data:
        if command[1] in e:
            print(' '.join(e))
            exit()
    print(command[1], 'not found')

elif command[0] == 'avg':
    ans = []
    for e in data:
        ans.append(e[int(command[1])])
    ans = sum(ans) / len(ans)
    print(round(ans, 4))

elif command[0] == 'max':
    ans = []
    for e in data:
        ans.append([-e[int(command[1])], e[0]])
    ans.sort()
    do_str_list(ans)
    print(ans[0][1], -ans[0][0])

elif command[0] == 'sort':
    ans = []
    for e in data:
        ans.append([e[int(command[1])], e[0]])
    ans.sort()
    for e in range(len(ans)):
        print(ans[e][1], end=' ')