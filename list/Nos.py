data=[float(e) for e in input().split()]
count=0
for i in range(1,len(data)-1):
    if data[i]>data[i+1] and data[i]>data[i-1]:
        count+=1
print(count)
