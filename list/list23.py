import math
n = int(input())
point = []
for e in range(n):
    point.append([float(i) for i in input().split()])
    point[e].append(e + 1)
    dist = math.sqrt((point[e][0] ** 2) + (point[e][1] ** 2))
    point[e].append(dist)
point = sorted(point, key=lambda e: e[3])
print('#' + str(point[2][2]) + ': (' + str(point[2][0]) + ', ' + str(point[2][1]) + ')')