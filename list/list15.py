x = [int(e) for e in input().split()]
x.sort()
unique_list = [x[0]]
unique = x[0]
for e in x:
    if e != unique:
        unique = e
        unique_list.append(e)
print(len(unique_list))
if len(unique_list) > 10:
    print(unique_list[:10])
else:
    print(unique_list)
