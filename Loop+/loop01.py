i = []
x = 0
while 'q' not in i:
    i.append(input())
if len(i) == 1:
    print('No Data')
    exit()
for e in i:
    if e == 'q':
        break
    x += float(e)
x /= len(i) - 1
print(round(x, 2))