import numpy as np


def p(X):
    logit = lambda e: -3.98 + (0.1 * e[0]) + (0.5 * e[1])
    ans = np.array([1 / (1 + np.exp(-logit(xi))) for xi in X])
    return ans


exec(input().strip())