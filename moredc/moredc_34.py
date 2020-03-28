def pattern1(nrows, ncols):
    ans = []
    i = 1
    for e in range(nrows):
        sub = []
        for j in range(ncols):
            sub.append(i)
            i += 1
        ans.append(sub)
    return ans


def pattern2(nrows, ncols):
    ans = []
    i = 1
    for e in range(nrows):
        ans.append([])
    for e in range(ncols):
        for j in range(nrows):
            ans[j].append(i)
            i += 1
    return ans


def pattern3(N):
    ans = []
    i = 1
    for e in range(N):
        sub = []
        for k in range(e):
            sub.append(0)
        for j in range(N - e):
            sub.append(i)
            i += 1
        ans.append(sub)
    return ans


def pattern4(N):
    ans = [[1]]
    i = 2
    if N == 0:
        return []
    for e in range(N - 1):
        ans.append([0])
    for e in range(N - 1):
        for j in range(N - 1, e + 1, -1):
            ans[j].append(0)
        for j in range(e + 1, -1, -1):
            ans[j].append(i)
            i += 1
    return ans


def pattern5(N):
    ans = [[1]]
    i = 2
    if N == 0:
        return []
    for e in range(N - 1):
        ans.append([0])
    for e in range(N - 1):
        for j in range(N - 1, e + 1, -1):
            ans[j].append(0)
        ans[e + 1].append(i)
        i += 1
    for e in range(N - 1):
        for j in range(N - 1 - e):
            ans[j].append(i)
            i += 1
    return ans


def pattern6(N):
    ans = [[1]]
    i = 2
    if N == 0:
        return []
    for e in range(N - 1):
        ans.append([0])
    for e in range(N - 1):
        for j in range(N - 1, e + 1, -1):
            ans[j].append(0)
        ans[e + 1].append(i)
        i += 1
    for e in range(N - 1):
        if e % 2 != 0:
        # down
            for j in range(N - 1 - e):
                ans[j].append(i)
                i += 1
        elif e % 2 == 0:
        # up
            for j in range(N - 2 - e, -1, -1):
                ans[j].append(i)
                i += 1
    return ans


exec(input().strip())