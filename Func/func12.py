def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True


def next_prime(n):
    e = n + 1
    while True:
        if is_prime(e) is True:
            return e
        e += 1


def next_twin_prime(n):
    e = n + 1
    while True:
        if is_prime(e) is True and is_prime(e + 2) is True:
            return e, e + 2
        e += 1


exec(input().strip())
