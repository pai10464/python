par = []
stoke = []
check = []
no_stoke = 0
handicap = 0
score = 0
for e in range(9):
    x = [int(e) for e in input().split()]
    par.append(x[0])
    stoke.append(x[1])
    check.append(x[2])
for e in range(9):
    if check[e] == 1:
        no_stoke += min((par[e] + 2), stoke[e])
handicap = int((0.8 * ((1.5 * no_stoke) - sum(par))) // 1)
score = sum(stoke) - handicap
print(sum(stoke))
print(handicap)
print(score)
