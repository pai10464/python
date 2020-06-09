class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.nvalue = 0
        self.nsuit = 0

    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'

    def next1(self):
        values = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
        suits = ["club", "diamond", "heart", "spade"]
        if self.value == '2' and self.suit == 'spade':
            self.nvalue = '3'
            self.nsuit = 'club'
        elif self.suit == 'spade':
            self.nvalue = values[values.index(self.value) + 1]
            self.nsuit = 'club'
        else:
            self.nvalue = self.value
            self.nsuit = suits[suits.index(self.suit) + 1]
        return '(' + self.nvalue + ' ' + self.nsuit + ')'

    def next2(self):
        values = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
        suits = ["club", "diamond", "heart", "spade"]
        if self.value == '2' and self.suit == 'spade':
            self.nvalue = '3'
            self.nsuit = 'club'
        elif self.suit == 'spade':
            self.nvalue = values[values.index(self.value) + 1]
            self.nsuit = 'club'
        else:
            self.nvalue = self.value
            self.nsuit = suits[suits.index(self.suit) + 1]
        x = Card(self.nvalue, self.nsuit)
        self.value = x.value
        self.suit = x.suit


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
