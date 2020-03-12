n = input()
c = ['06', '08', '09']
d = n[0] + n[1]
if len(n) == 10:
    if d in c:
        print('Mobile number')
        exit()
print('Not a mobile number')