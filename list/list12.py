x = [['Robert', 'Dick'], ['William', 'Bill'], ['James', 'Jim'], ['John', 'Jack'], ['Margaret', 'Peggy'],
    ['Edward', 'Ed'], ['Sarah', 'Sally'], ['Andrew', 'Andy'], ['Anthony', 'Tony'], ['Deborah', 'Debbie']]
a = []
n = int(input())
for e in range(n):
    a.append(input())
for e in range(n):
    g = 0
    for i in range(len(x)):
        if a[e] == x[i][0]:
            print(x[i][1])
            g = 1
        elif a[e] == x[i][1]:
            print(x[i][0])
            g = 1
    if g == 0:
        print('Not found')