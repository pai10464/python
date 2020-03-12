a = input()
b = input()
ru = ''
rv = ''
i = 0
for e in a:
    if e == '[' or e == ']' or e == " " :
        i += 1
    elif e == ',':
        ru += ' '
    else:
        ru += e
for e in b:
    if e == '[' or e == ']' or e == " " :
        i += 1
    elif e == ',':
        rv += ' '
    else:
        rv += e
u1,u2,u3 = [float(e) for e in ru.split()]
v1,v2,v3 = [float(e) for e in rv.split()]
u = [u1, u2, u3]
v = [v1, v2, v3]
s1 = u1 + v1
s2 = u2 + v2
s3 = u3 + v3
sum = [s1, s2, s3]
print(str(u)+" + "+str(v)+" = "+str(sum))