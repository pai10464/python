N=int(input())
name=["Robert","William","James","John","Margaret","Edward","Sarah","Andrew","Anthony","Deborah"]
nickname=["Dick","Bill","Jim","Jack","Peggy","Ed","Sally","Andy","Tony","Debbie"]
t=[]
for i in range(N):
    x=input()
    if x in name:
        j=name.index(x)
        y=nickname[j]
        t.append(y)
    elif x in nickname:
        j=nickname.index(x)
        y=name[j]
        t.append(y)
    if (x not in name) and (x not in nickname)
        y="Not Found"
        t.append(y)
print(t)
