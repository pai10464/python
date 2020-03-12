x = []
y = []
i = 0
while True:
    a = input()
    if a == 'Zig-Zag' or a == 'Zag-Zig':
        control = a
        break
    b = [int(e) for e in a.split()]
    x.append(b[0])
    y.append(b[1])
red = list(range(len(x)))
blue = list(range(len(x)))
if control == 'Zag-Zig':
    for e in range(len(x)):
        if e % 2 != 0:
            red[e] = x[e]
            blue[e] = y[e]
        else:
            red[e] = y[e]
            blue[e] = x[e]
elif control == 'Zig-Zag':
    for e in range(len(x)):
        if e % 2 != 0:
            red[e] = y[e]
            blue[e] = x[e]
        else:
            red[e] = x[e]
            blue[e] = y[e]
print(str(min(red)) + ' ' + str(max(blue)))