x1 = [e for e in input()]
n = ['"', "'", '(', ')', '.', '>', '<', ';', '-']
for e in range(len(x1)):
	if x1[e] in n:
		x1[e] = ' '
x2 = [e for e in ''.join(x1).split()]
x2[0] = x2[0].lower()
for e in range(1, len(x2)):
	x2[e] = x2[e][0].upper() + x2[e][1:].lower()
print(''.join(x2))