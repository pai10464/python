x = [int(e) for e in input().split()]
i = 0
for e in range(1, len(x) - 1):
    if x[e] > x[e - 1] and x[e] > x[e + 1 ]:
        i += 1
print(i)