class piggybank:
    def __init__(self):
        self.r1 = 0
        self.r2 = 0
        self.r5 = 0
        self.r10 = 0

    def add1(self, n):
        self.r1 += n

    def add2(self, n):
        self.r2 += n

    def add5(self, n):
        self.r5 += n

    def add10(self, n):
        self.r10 += n

    def __int__(self):
        return self.r1 + (self.r2 * 2) + (self.r5 * 5) + (self.r10 * 10)

    def __lt__(self, other):
        return self.__int__() < other.__int__()

    def __str__(self):
        return '{1:' + str(self.r1) + ', 2:' + str(self.r2) + ', 5:' + str(self.r5) + ', 10:' + str(self.r10) + '}'


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)