x = [e for e in input().split()]
x[0] = int(x[0], 2)
x[1] = int(x[1], 2)
print(bin(sum(x))[2:])