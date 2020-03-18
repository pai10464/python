def is_odd(n):
    if n % 2 != 0:
        return True
    return False


def has_odds(x):
    for e in x:
        if is_odd(e):
            return True
    return False


def all_odds(x):
    for e in x:
        if not is_odd(e):
            return False
    return True

def no_odds(x):
    for e in x:
        if is_odd(e):
            return False
    return True


def get_odds(x):
    ans = []
    for e in x:
        if is_odd(e):
            ans.append(e)
    return ans


def zip_odds(a, b):
    a = get_odds(a)
    b = get_odds(b)
    ans = []
    i_a = 0
    i_b = 0
    while True:
        if i_a < len(a):
            ans.append(a[i_a])
            i_a += 1
        if i_b < len(b):
            ans.append(b[i_b])
            i_b += 1
        if i_a == len(a) and i_b == len(b):
            return ans


exec(input().strip())