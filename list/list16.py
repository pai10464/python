n = int(input())
ans = [n]
i = ''
while n != 1:
    if n % 2 == 0:
        n //= 2
        ans.append(n)
    else:
        n = (3 * n) + 1
        ans.append(n)
if len(ans) < 15:
    for e in ans:
        i += str(e) + '->'
else:
    for e in ans[len(ans) - 15:]:
        i += str(e) + '->'
print(i.strip('->'))
