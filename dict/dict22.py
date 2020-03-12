n = int(input())
menu = {}
for e in range(n):
    x, y = input().split()
    menu[x] = int(y)
m = int(input())
sell = {}
for e in range(m):
    x = input().split()
    if x[0] in menu and x[0] not in sell:
        sell[x[0]] = menu[x[0]] * int(x[1])
    elif x[0] in sell:
        sell[x[0]] += menu[x[0]] * int(x[1])
if len(sell) == 0:
    print('No ice cream sales')
    exit()
ans = []
tot = 0
for e, i in sell.items():
    ans.append([-i, e])
    tot += i
ans.sort()
top_seller = []
for e in ans:
    if e[0] == ans[0][0]:
        top_seller.append(e[1])
print('Total ice cream sales:', float(tot))
print('Top sales:', ', '.join(top_seller))