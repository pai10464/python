from collections import OrderedDict
data = OrderedDict()
while True:
    x = input().split(', ')
    if 'q' in x:
        break
    if x[1] not in data:
        data[x[1]] = x[0]
    else:
        data[x[1]] += ', ' + x[0]
for e in data:
    print(e + ': ' + data[e])