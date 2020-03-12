x = input()
if len(x) < 4:
    print(x)
elif len(x) == 4:
    x = int(x) / 1000
    print(str(round(x, 1))+'K')
elif len(x) < 7:
    i = int(x) % 1000
    if i >= 500:
        x = int(x) + 1000
    x = int(x) // 1000
    print(str(x)+'K')
elif len(x) == 7:
    x = int(x) / 1e6
    print(str(round(x, 1)) + 'M')
elif len(x) < 10:
    i = int(x) % 1e6
    if i >= 5e5:
        x = int(x) + 1e6
    x = int(x) // 1e6
    print(str(int(x)) + 'M')
elif len(x) == 10:
    x = int(x) / 1e9
    print(str(round(x, 1)) + 'B')
else:
    i = int(x) % 1e9
    if i >= 5e8:
        x = int(x) + 1e9
    x = int(x) // 1e9
    print(str(int(x))+'B')