x = int(input())
e = 2
blank = ' '
star = '*'
print((blank*(x-1)) + star + (blank*(x-1)))
while e < x:
    a = (blank*(x - e)) + star + (blank*((2 * (e-1)) - 1)) + star + (blank*(x - e))
    print(a)
    e += 1
print(((2*x)-1) * star)