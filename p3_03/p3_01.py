n = int(input())
k = int(input())
if (n <= 0 or n > 15) and (k <= 0 or k > 100):
    print('Invalid n and k')
    exit()
elif n <= 0 or n > 15:
    print('Invalid n')
    exit()
elif k <= 0 or k > 100:
    print('Invalid k')
    exit()
for e in range(1, k + 1):
    if e == k:
        print(str(e) + '-'*(n-len(str(e))))
        break
    print(str(e) + '-' * (n + 1 - len(str(e))), end='')
start = [0, 1]
for e in range(n - 1):
    start = start + start[-1::-1]
    for i in range(len(start) // 2):
        start[i] = '0' + str(start[i])
    for i in range(len(start) // 2, len(start)):
        start[i] = '1' + str(start[i])
for e in range(len(start)):
    if e % k == k - 1 or e == len(start) - 1:
        print(start[e])
    else:
        print(start[e], end=',')
