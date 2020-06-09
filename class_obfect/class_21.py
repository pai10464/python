class Complex:
    def __init__(self, r, i):
        self.Re = r
        self.Im = i

    def __str__(self):
        if self.Im == 0:
            return str(self.Re)
        elif self.Re == 0 and self.Im == 1:
            return 'i'
        elif self.Re == 0 and self.Im == -1:
            return '-i'
        elif self.Re == 0:
            return str(self.Im) + 'i'
        elif self.Im == 1:
            return str(self.Re) + '+i'
        elif self.Im == -1:
            return str(self.Re) + '-i'
        elif self.Im < 0:
            return str(self.Re) + str(self.Im) + 'i'
        else:
            return str(self.Re) + '+' + str(self.Im) + 'i'

    def __add__(self, other):
        x = Complex(0, 0)
        x.Re = self.Re + other.Re
        x.Im = self.Im + other.Im
        return str(x)

    def __mul__(self, other):
        x = Complex(0, 0)
        x.Re = (self.Re * other.Re) - (self.Im * other.Im)
        x.Im = (self.Re * other.Im) + (self.Im * other.Re)
        return str(x)

    def __truediv__(self, other):
        x = Complex(0, 0)
        x.Re = ((self.Re * other.Re) + (self.Im * other.Im)) / (other.Re**2 + other.Im**2)
        x.Im = ((self.Im * other.Re) - (self.Re * other.Im)) / (other.Re**2 + other.Im**2)
        return str(x)


t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if t == 1: print(c1)
elif t == 2: print(c2)
elif t == 3: print(c1+c2)
elif t == 4: print(c1*c2)
else: print(c1/c2)
