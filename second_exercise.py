from matplotlib import pyplot as plt
from math import sin
import numpy as np
from random import random

x1 = [sin(t) for t in np.arange(0, 4, 0.5)]
x2 = list()
for i in range(len(x1)):
    if i % 2 == 0:
        x2.append(x1[i])
    else:
        x2.append(0.5)
j = 0
y1 = []
y2 = []
while 2 * j < len(x1):
    y1.append(x1[2*j])
    y2.append(x2[2*j])
    j += 1


plt.figure(1)
plt.subplot(211)
plt.scatter(range(len(x1)), x1, label='x1')
plt.scatter(range(len(y1)), y1, label='y1')
plt.legend()

plt.subplot(212)
plt.scatter(range(len(x2)), x2, label='x2')
plt.scatter(range(len(y2)), y2, label='y2')


plt.legend()
plt.show()
print("done")
