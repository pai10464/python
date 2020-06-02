import numpy as np


def mult_table(nr, nc):
    ans = np.array(range(1, nr * nc + 1))
    ans = ans.reshape(nr, nc)
    for e in range(1, nr + 1):
        ans[e - 1] = ans[0] * e
    return ans


exec(input().strip())
