import math


def distance1(x1, y1, x2, y2):
    d1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return d1


def distance2(p1, p2):
    d2 = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return d2


def distance3(c1, c2):
    d3 = distance2(c1, c2)
    if d3 > c1[2] + c2[2]:
        overlap = False
    else:
        overlap = True
    return d3, overlap


def perimeter(points):
    d4 = 0
    for e in range(len(points)):
        if e == len(points) - 1:
            d4 += distance2(points[e], points[0])
            return d4
        else:
            d4 += distance2(points[e], points[e + 1])


exec(input().strip())
