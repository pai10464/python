ids = []
score = []
grade_num = []
grade = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
while True:
    x = [e for e in input().split()]
    if 'q' in x:
        break
    ids.append(x[0])
    score.append(x[1])
for e in score:
    for i in range(8):
        if grade[i] == e:
            grade_num.append(i)
uids = [e for e in input().split()]
for e in range(len(ids)):
    if ids[e] in uids and grade_num[e] != 7:
        print(ids[e], grade[grade_num[e] + 1])
    else:
        print(ids[e], grade[grade_num[e]])