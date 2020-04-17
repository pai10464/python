n = int(input())
data = []
winner = []
loser = []
for e in range(n):
    data.append(input().split())
sub = []
for e in data:
    winner.append(e[0])
    loser.append(e[1])
    sub += e
all_team = []
for i in sub:
    if i not in all_team:
        all_team.append(i)
no_lose = []
for e in all_team:
    if e not in loser:
        no_lose.append(e)
print(sorted(no_lose))