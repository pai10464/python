sol = [e for e in input()]
ans = [e for e in input()]
score = 0
n = 0
if len(sol) != len(ans):
    print('Incomplete answer')
    exit()
for e in range(len(sol)):
    if sol[e] == ans[e]:
        score += 1
    n += 1
print(score)