def first_fit(L, e):
    for i in range(len(L)):
        if sum(L[i]) + e <= 100:
            L[i].append(e)
            break
        elif i == len(L) - 1:
            L.append([e])
    if len(L) == 0:
        L.append([e])


def best_fit(L, e):
    can = []
    for i in range(len(L)):
        if sum(L[i]) + e <= 100:
            can.append([-(sum(L[i]) + e), i])
    if len(can) == 0:
        L.append([e])
    else:
        can.sort()
        L[can[0][1]].append(e)


def partition_FF(D):
    L = []
    L.append([D[0]])
    for e in D[1:]:
        first_fit(L, e)
    return L


def partition_BF(D):
    L = []
    L.append([D[0]])
    for e in D[1:]:
        best_fit(L, e)
    return L


exec(input().strip())