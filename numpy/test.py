import numpy as np
y = [1, 4, 5.1, 5.2, 5.3, 6, 9, 6.1, 6.2, 7.1, 7.2, 7.3, 8.4, 8.5, 9.2, 9.3, 20, 6, 8, 11.2, 11.5]
x = np.array(y)
x1 = np.diff(x)
x2 = np.diff(x[::-1])
print(x1)
print(x2[::-1])