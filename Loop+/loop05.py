x = input()
word = input()
a = ''
b = 0
for e in word:
    if e == '"' or e == '(' or e == ')' or e == ',' or e == '.' or e == "'":
        a += ' '
    else :
        a += e
word = [i for i in a.split()]
for e in range(len(word)):
    if x == word[e]:
      b += 1
print(b)