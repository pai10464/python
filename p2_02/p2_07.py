order = []
score_d = {'R': 1, 'Y': 2, 'G': 3, 'W': 4, 'B': 5, 'P': 6, 'K': 7}
score_p1 = 0
score_p2 = 0
while True:
    order.append(input())
    if order[-1][1] == 'K':
        break
for e in order:
    if e[0] == '1':
        for i in e[1:]:
            if i not in score_d:
                continue
            score_p1 += score_d[i]
    elif e[0] == '2':
        for i in e[1:]:
            if i not in score_d:
                continue
            score_p2 += score_d[i]
print(score_p1, score_p2)
if score_p1 > score_p2:
    print('Player 1 wins')
elif score_p2 > score_p1:
    print('Player 2 wins')
else:
    print('Tie')