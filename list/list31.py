card = [e for e in input().split()]
half = len(card) // 2
opr = [e for e in input()]
for e in opr:
    ans = []
    if e == 'C':
        for e in range(len(card)):
            if e < half:
                ans.append(card[e + half])
            else:
                ans.append(card[e - half])
        card = ans
    elif e == 'S':
        for e in range(half):
            ans.append(card[e])
            ans.append(card[half + e])
        card = ans
ans = ''
for e in card:
    ans += str(e) + ' '
print(ans.strip())