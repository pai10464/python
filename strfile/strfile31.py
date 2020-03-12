x = 'ATGC'
y = 'TACG'
a = input().strip().upper()
b = input().strip().upper()
for e in a:
    if e not in x:
        print('Invalid DNA')
        exit()
if b == 'R':
    ans = ''
    for e in a:
        ans += y[x.find(e)]
    print(ans[-1::-1])
elif b == 'F':
    ans = []
    for e in range(4):
        ans.append(a.count(x[e]))
    print('A=' + str(ans[0]) + ', T=' + str(ans[1]) + ', G=' + str(ans[2]) + ', C=' + str(ans[3]))
elif b == 'D':
    c = input()
    count = 0
    for e in range(len(a) - 1):
        if a[e] == c[0] and a[e + 1] == c[1]:
            count += 1
    print(count)
