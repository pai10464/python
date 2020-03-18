x = [e for e in input()]
card_d = {'A': 1, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'C': 1, 'D': 2, 'H': 3, 'S': 4}
card = []
ans = []
for e in range(0, len(x), 2):
    if x[e] in card_d:
        card.append([card_d[x[e]], card_d[x[e + 1]]])
    else:
        card.append([int(x[e]), card_d[x[e + 1]]])
for e in range(len(card) - 1):
    if card[e][0] != card[e + 1][0]:
        if card[e][0] > card[e + 1][0]:
            ans.append('+' + str(card[e][0] - card[e + 1][0]))
        elif card[e][0] < card[e + 1][0]:
            ans.append(str(card[e][0] - card[e + 1][0]))
    else:
        if card[e][1] > card[e + 1][1]:
            ans.append('+' + str(card[e][1] - card[e + 1][1]))
        elif card[e][1] < card[e + 1][1]:
            ans.append(str(card[e][1] - card[e + 1][1]))
        else:
            ans.append('0')
print(''.join(ans))