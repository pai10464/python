x = [e for e in input()]
n = int(input())
frame = list(range(10))
num = list(range(10))
i = 0
for e in range(len(frame)):
    if x[i] == 'X':
        if x[i + 1] == 'X' and x[i + 2] == 'X':
            frame[e] = 30
            i += 1
        elif x[i + 1] == 'X' and int(x[i + 2]) in num:
            frame[e] = 20 + int(x[i + 2])
            i += 1
        elif int(x[i + 1]) in num and x[i + 2] == '/':
            frame[e] = 20
            i += 1
        elif int(x[i + 1]) in num and int(x[i + 2]) in num:
            frame[e] = 10 + int(x[i + 1]) + int(x[i + 2])
            i += 1
    elif int(x[i]) in num:
        if x[i + 1] == '/' and x[i + 2] == 'X':
            frame[e] = 20
            i += 2
        elif x[i + 1] == '/' and int(x[i + 2]) in num:
            frame[e] = 10 + int(x[i + 2])
            i += 2
        elif int(x[i + 1]) in num:
            frame[e] = int(x[i]) + int(x[i + 1])
            i += 2
if n - 1 in num:
    print(frame[n - 1])
else:
    print(sum(frame))