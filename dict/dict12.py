n = int(input())
d_name = {}
for e in range(n):
    a, b = input().split()
    d_name[a] = b


def reverse(d):
    new = {}
    for key, value in d.items():
        new[value] = key
    return new


d_nickname = reverse(d_name)
n = int(input())
for e in range(n):
    a = input()
    if a in d_name:
        print(d_name[a])
    elif a in d_nickname:
        print(d_nickname[a])
    else:
        print('Not found')