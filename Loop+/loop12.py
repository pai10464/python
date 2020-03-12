a = int(input())
x = list(range(a))
y = list(range(a))
for e in range(a):
    x[e], y[e] = [int(i) for i in input().split()]
control = input()
red = list(range(a))
blue = list(range(a))
if control == 'Zag-Zig':
    for e in range(a):
        if e % 2 != 0:
            red[e] = x[e]
            blue[e] = y[e]
        else:
            red[e] = y[e]
            blue[e] = x[e]
elif control == 'Zig-Zag':
    for e in range(a):
        if e % 2 != 0:
            red[e] = y[e]
            blue[e] = x[e]
        else:
            red[e] = x[e]
            blue[e] = y[e]
print(str(min(red)) + ' ' + str(max(blue)))