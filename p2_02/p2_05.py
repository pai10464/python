x = input()
y = input()
a = [e for e in x.lower()]
b = [e for e in y.lower()]
apl = 'abcdefghijklmnopqrstuvwxyz'
apl_a = {}
for e in a:
    if e in apl and e not in apl_a:
        apl_a[e] = a.count(e)
apl_b = {}
for e in b:
    if e in apl and e not in apl_b:
        apl_b[e] = b.count(e)
fix_a = []
for keys, value in apl_a.items():
    if keys not in apl_b:
        fix_a.append([keys, value])
    elif value > apl_b[keys]:
        fix_a.append([keys, value - apl_b[keys]])
fix_b = []
for keys, value in apl_b.items():
    if keys not in apl_a:
        fix_b.append([keys, value])
    elif value > apl_a[keys]:
        fix_b.append([keys, value - apl_a[keys]])
fix_a.sort()
fix_b.sort()
#Output
print(x)
if len(fix_a) == 0:
    print('- None')
else:
    for e in fix_a:
        if e[1] == 1:
            print('- remove ' + str(e[1]) + ' ' + e[0])
        else:
            print('- remove ' + str(e[1]) + ' ' + e[0] + "'s")

print(y)
if len(fix_b) == 0:
    print('- None')
else:
    for e in fix_b:
        if e[1] == 1:
            print('- remove ' + str(e[1]) + ' ' + e[0])
        else:
            print('- remove ' + str(e[1]) + ' ' + e[0] + "'s")