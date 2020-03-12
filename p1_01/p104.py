x = input()
n = int(input())
frame = []
score = []
ans = []
check = 2
count = 0
i = 0
for e in x:
    if e == 'X':
        if count == 9:
            i -= 1
            check = 3
        score.append(10)
        i += 2
    elif e == '/':
        if count == 9:
            i -= 1
        score.append(10 - score[0])
        i += 1
    else:
        score.append(int(e))
        i += 1
    if i == check:
        frame.append(score)
        count += 1
        i = 0
        score = []
for e in range(len(frame)):
    if frame[e][len(frame[e]) - 1] == 10 and e != 9:
        if frame[e + 1][0] == 10 and e + 1 != 9:
            ans.append(sum(frame[e]) + frame[e + 1][0] + frame[e + 2][0])
        elif frame[e + 1][0] == 10 and e + 1 == 9:
            ans.append(sum(frame[e]) + frame[e + 1][0] + frame[e + 1][1])
        else:
            ans.append(sum(frame[e]) + sum(frame[e + 1]))
    elif sum(frame[e]) == 10 and e != 9:
        ans.append(sum(frame[e]) + frame[e + 1][0])
    else:
        ans.append(sum(frame[e]))
if n - 1 in range(10):
    print(ans[n-1])
else:
    print(sum(ans))
