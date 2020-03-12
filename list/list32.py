n = int(input())
x = []
order = []
time = []
wait = 1
for e in range(n):
    x.append(input())
for e in x:
    command = [i for i in e.split()]
    if command[0] == 'reset':
        order.append([int(command[1]) - 1])
    elif command[0] == 'new':
        new_order = order[len(order) - 1][0] + 1
        order.append([new_order, int(command[1])])
        print('ticket', new_order)
    elif command[0] == 'next':
        print('call', order[wait][0])
        wait += 1
    elif command[0] == 'order':
        qtime = int(command[1]) - order[wait - 1][1]
        time.append(qtime)
        order[wait - 1].append(int(command[1]))
        print('qtime', order[wait - 1][0], qtime)
    elif command[0] == 'avg_qtime':
        avg_qtime = sum(time) / len(time)
        print('avg_qtime', round(avg_qtime, 4))