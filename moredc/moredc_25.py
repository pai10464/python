def row_number(t, e):
    for i in range(len(t)):
        if e in t[i]:
            return i


def flatten(t):
    ans = []
    for e in t:
        for i in e:
            if i != 0:
                ans.append(i)
    return ans


def inversions(x):
    count = 0
    for e in range(len(x)):
        for i in x[e:]:
            if x[e] > i:
                count += 1
    return count


def solvable(t):
    if len(t) % 2 != 0 and inversions(flatten(t)) % 2 == 0:
        return True
    elif len(t) % 2 == 0:
        if inversions(flatten(t)) % 2 != 0 and row_number(t, 0) % 2 == 0:
            return True
        elif inversions(flatten(t)) % 2 == 0 and row_number(t, 0) % 2 != 0:
            return True
    return False


exec(input().strip())
