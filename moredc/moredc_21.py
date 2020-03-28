def prime(n):
    for e in range(2, n):
        if n % e == 0:
            return False
    return True


def factor(n):
    ans = []
    for e in range(2, n + 1):
        if prime(n):
            ans.append([n, 1])
            return ans
        if prime(e) and n % e == 0:
            count = 0
            while n % e == 0:
                n //= e
                count += 1
            ans.append([e, count])
        if e > n:
            return ans


exec(input().strip())
