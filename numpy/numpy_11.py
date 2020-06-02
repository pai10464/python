import numpy as np


# A is a 2-d array
def get_column_from_bottom_to_top(A, c):
    x = A[::-1]
    ans = np.dstack(x)
    return ans[0][c]


def get_odd_rows(A):
    ans = A[1::2]
    return ans


def get_even_column_last_row(A):
    x = A[-1]
    return x[::2]

def get_diagonal1(A): # A is a square matrix
    # from top-left corner down to bottom-right corner
    ans = np.array(range(len(A)))
    for e in range(len(A)):
        ans[e] = A[e][e]
    return ans


def get_diagonal2(A): # A is a square matrix
    # from top-right corner down to bottom-left corner
    ans = np.array(range(len(A)))
    i = 0
    for e in range(len(A) - 1, -1, -1):
        ans[i] = A[i][e]
        i += 1
    return ans


exec(input().strip())