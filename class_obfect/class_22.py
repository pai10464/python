class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.score = 0

    def __str__(self):
        return '(' + str(self.value) + ' ' + self.suit + ')'

    def getScore(self):
        if self.value == 'A':
            self.score = 1
        elif self.value == 'J' or self.value == 'Q' or self.value == 'K':
            self.score = 10
        else:
            self.score = int(self.value)
        return self.score

    def sum(self, other):
        ans = (self.score + other.score) % 10
        return ans
    def __lt__(self, rhs):
        values = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
        suits = ["club", "diamond", "heart", "spade"]
        return (values.index(self.value), suits.index(self.suit)) < (values.index(rhs.value), suits.index(rhs.suit))


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])
