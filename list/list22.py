ids = []
grade = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
while True:
    x = [e for e in input().split()]
    if 'q' in x:
        break
    ids.append(x)
for e in range(len(ids)):
    for i in range(8):
        if grade[i] == ids[e][1]:
            ids[e].append(i)
uids = [e for e in input().split()]
ids = sorted(ids, key=lambda e: e[0])
for e in range(len(ids)):
    if ids[e][0] in uids and ids[e][2] != 7:
        print(ids[e][0], grade[ids[e][2] + 1])
    else:
        print(ids[e][0], grade[ids[e][2]])
