class roman:
    def __init__(self, r):
        self.r = r

    def __int__(self):
        ronum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(self.r):
            if i + 1 < len(self.r) and self.r[i:i + 2] in ronum:
                num += ronum[self.r[i:i + 2]]
                i += 2
            else:
                num += ronum[self.r[i]]
                i += 1
        return num

    def __lt__(self, other):
        return int(self) < int(other)

    def __str__(self):
        return self.r

    def __add__(self, other):
        ans = int(self) + int(other)
        ronum = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        res = ""
        while ans > 0:
            for i, r in ronum:
                while ans >= i:
                    res += r
                    ans -= i
        return roman(res)


t, r1, r2 = input().split()
a = roman(r1)
b = roman(r2)
if t == "1":
    print(a < b)
elif t == "2":
    print(int(a), int(b))
elif t == "3":
    print(str(a), str(b))
elif t == "4":
    print(int(a + b))
else:
    print(str(a + b))