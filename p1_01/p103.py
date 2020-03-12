win_point = int(input())
win = ['Player 1 wins', 'Player 2 wins', 'Tie']
no_win = 0
i = 0
p1s = 0
p2s = 0
while True:
    if i == (3 * win_point):
        no_win = 2
        break
    p1, p2 = [e for e in input().split()]
    if p1 == p2:
        i += 1
        continue
    elif p1 == 'R' and p2 == 'S':
        p1s += 1
    elif p1 == 'R' and p2 == 'P':
        p2s += 1
    elif p1 == 'S' and p2 == 'P':
        p1s += 1
    elif p1 == 'S' and p2 == 'R':
        p2s += 1
    elif p1 == 'P' and p2 == 'R':
        p1s += 1
    elif p1 == 'P' and p2 == 'S':
        p2s += 1
    if p1s == win_point:
        no_win = 0
        break
    if p2s == win_point:
        no_win = 1
        break
    i += 1
print(p1s, p2s)
print(win[no_win])