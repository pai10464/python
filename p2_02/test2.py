fn = open('morse_p2_06.txt', 'r')
code = fn.readline()
pattern = fn.readline()
for e in fn:
    ans = []
    e = e.split()
    for i in e:
        print(i)
    print(e)