def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m


def mult_c(c, A):
    for e in range(len(A)):
        for i in range(len(A[e])):
            A[e][i] *= c
    return A


def mult(A, B):
    ans = []
    for e in range(len(A)):
        c = []
        for i in range(len(B[0])):
            sub_c = 0
            for j in range(len(A[0])):
                sub_c += A[e][j] * B[j][i]
            c.append(sub_c)
        ans.append(c)
    return ans


exec(input().strip())