from collections import OrderedDict


class piggybank:
    def __init__ (self):
        self.coins = OrderedDict()
        self.ncoin = 0

    def add(self, v, n):
        if self.ncoin + n > 100:
            return False
        else:
            v = float(v)
            if v in self.coins:
                self.coins[v] += n
                self.ncoin += n
            else:
                self.coins[v] = n
                self.ncoin += n
            return True

    def __float__(self):
        ans = 0
        for key, value in self.coins.items():
            ans += key * value
        if ans == 0:
            return float(0)
        else:
            return ans

    def __str__(self):
        ans = '{'
        for k, v in sorted(self.coins.items()):
            ans += str(k) + ':' + str(v) + ', '
        if len(ans) > 1:
            ans = ans[:-2]
        ans += '}'
        return ans


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
