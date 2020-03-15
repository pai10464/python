x1 = 'ABCDEFGHIJKLM'
x2 = 'NOPQRSTUVWXYZ'
y1 = 'abcdefghijklm'
y2 = 'nopqrstuvwxyz'
i = ''
ans = []
while True:
    i = input()
    if i == 'end':
        break
    i_ans = ''
    i = [e for e in i]
    for e in i:
        if e in x1:
            i_ans += x2[x1.find(e)]
        elif e in x2:
            i_ans += x1[x2.find(e)]
        elif e in y1:
            i_ans += y2[y1.find(e)]
        elif e in y2:
            i_ans += y1[y2.find(e)]
        else: i_ans += e
    ans.append(i_ans)
for e in ans:
    print(e)
    
