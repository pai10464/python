def make_int_list(x):
    x = [int(e) for e in x.split()]
    return x


def is_odd(e):
    if e % 2 == 0:
        return False
    return True


def odd_list(alist):
    olist = []
    for e in alist:
        if e % 2 != 0:
            olist.append(e)
    return olist


def sum_square(alist):
    ans = 0
    for e in alist:
        ans += e**2
    return ans


exec(input().strip())