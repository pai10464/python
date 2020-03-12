x = [e for e in input()]
ans = ''
for e in range(len(x)):
    if x[e] == '(':
        x[e] = '['
    elif x[e] == '[':
        x[e] = '('
    elif x[e] == ')':
        x[e] = ']'
    elif x[e] == ']':
        x[e] = ')'
for e in range(len(x)):
    ans += x[e]
print(ans)