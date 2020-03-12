def no_lowercase(t):
    a = 'abcdefghijklmnopqrstuvwxyz'
    for e in t:
        if e in a:
            return False
    return True

print(no_lowercase('PASS'))