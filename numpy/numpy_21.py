import numpy as np


def sum_2_rows(M):
    s = np.vsplit(M, len(M) / 2)
    j = np.array([np.add(e[0], e[1]) for e in s])
    return j


def sum_left_right(x):
    s = np.hsplit(x, 2)
    j = np.array([np.add(s[0][e], s[1][e]) for e in range(len(s[0]))])
    return j


def sum_upper_lower(x):
    s = np.vsplit(x, 2)
    j = np.array([np.add(s[0][e], s[1][e]) for e in range(len(s[0]))])
    return j


def sum_4_quadrants(x):
    s = np.vsplit(x, 2)
    g = np.array([np.hsplit(s[0], 2), np.hsplit(s[1], 2)])
    j = np.array(np.add(np.add(g[0][0], g[0][1]), np.add(g[1][0], g[1][1])))
    return j


def sum_4_cells(x):
    s = np.vsplit(x, len(x) / 2)
    g = np.array([np.hsplit(e, len(x) / 2) for e in s])
    ans = np.arange((len(x) // 2) ** 2).reshape(len(x) // 2, len(x) // 2)
    for e in range(len(g)):
        for i in range(len(g[e])):
            t = 0
            for k in np.nditer(g[e][i]):
                t += k
            ans[e][i] = t
    return ans


def count_leap_years(x):
    ans = []
    for e in x:
        if ((e - 543) % 4 == 0 and (e - 543) % 100 != 0) or (e - 543) % 400 == 0:
            ans.append(e)
    return len(ans)


exec(input().strip())
