def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(a, b, c):
    check = [a, b, c]
    for e in range(2, max(check) + 1):
        if a % e == 0 and b % e == 0 and c % e == 0:
            return False
    return True


def primitive_Pythagorean_triples(max_len):
    triple = []
    for c in range(max_len, 2, -1):
        for b in range(c, 2, -1):
            a = ((c**2) - (b**2))**(1 / 2)

            if a % 1 == 0:
                sub = [int(a), int(b), int(c)]
                sub.sort()
                if sub not in triple and is_coprime(sub[0], sub[1], sub[2]):
                    triple.append(sub)
    triple.sort(key=lambda x: x[2])
    return triple


exec(input().strip())
