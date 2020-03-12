def reverse(d):
    new = {}
    for key, value in d.items():
        new[value] = key
    return new


def keys(d, v):
    ans = []
    for key, value in d.items():
        if value == v:
            ans.append(key)
    return ans


exec(input().strip())
