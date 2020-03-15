x = [e.lower() for e in input()]
y = [e.lower() for e in input()]
for e in x:
    if e == ' ':
        x.remove(e)
for i in y:
    if i == ' ':
        y.remove(i)
if len(x) != len(y):
    print('NO')
    exit()
for e in x:
    if e in y:
        y.remove(e)
if len(y) == 0:
    print('YES')
else:
    print('NO')