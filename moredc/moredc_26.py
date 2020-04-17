n = int(input())
id = []
place = []
for e in range(n):
    x = input().split(':')
    id.append(x[0])
    place.append([e.strip(' ') for e in x[1].split(',')])
keyid = id.index(input())
ans = []
for i in place:
    for e in place[keyid]:
        if e in i and id[place.index(i)] not in ans:
            ans.append(id[place.index(i)])
            break
ans.remove(id[keyid])
if len(ans) == 0:
    print('Not Found')
else:
    for e in ans:
        print(e)
