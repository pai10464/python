n1, n2, n3, n4 = [float(e) for e in input().split()]
n = [n1, n2, n3, n4]
n.sort()
x = (n[1] + n[2])/2
print(round(x, 2))