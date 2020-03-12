n = int(input())
phone_book = {}
for e in range(n):
    x = input().split()
    phone_book[x[0] + ' ' + x[1]] = x[2]


def reverse(d):
    new = {}
    for key, value in d.items():
        new[value] = key
    return new


name_book = reverse(phone_book)
m = int(input())
for e in range(m):
    x = input()
    if x in phone_book:
        print(x + ' --> ' + phone_book[x])
    elif x in name_book:
        print(x + ' --> ' + name_book[x])
    else:
        print(x + ' --> Not found')
