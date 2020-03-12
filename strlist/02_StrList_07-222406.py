p = input()
a = p[3] + p[10] + p[17] + p[24] + p[31]
b = p[7] + p[12] + p[17] + p[22] + p[27]
c = int(a) + int(b) + 10000
d = str(c)[-4:-1]
e = str(int(d[-3]) + int(d[-2]) + int(d[-1]))
f = (int(e)%10) + 1
g = ['-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(d+g[f])