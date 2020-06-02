import numpy as np


def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data


def report_lower_than_mean(weight, data):
    ans = np.ndarray((len(data), 2), int)
    for e in range(len(ans)):
        ans[e] = [data[e][0], data[e][1] * weight[0] + data[e][2] * weight[1] + data[e][3] * weight[2]]
    mean = sum([ans[e][1] for e in range(len(ans))]) / len(ans)
    a = []
    for e in ans:
        if e[1] < mean:
            a.append(str(e[0]))
    if len(a) == 0:
        print('None')
    else:
        print(', '.join(a))

exec(input().strip())