p = float(input())
k = 1
t = 1
while 1 - t < p:
    k += 1
    t *= (365 - (k - 1)) / 365
print(k)