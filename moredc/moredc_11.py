n = int(input())
data = []
for e in range(n):
    data.append(input())
for e in data:
    count = 0
    for i in range(len(e)):
        if e[i] == '.':
            count += 1
            continue
        else:
            print('.' * (count // 2) + e[i:])
            break
