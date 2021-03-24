import matplotlib.pyplot as plt
from two_task_carlo import *
import math


x = [i for i in range(0,5)]
y = [round((pow(11 - 7*pow(math.sin(i),2), 1/2)), 3) for i in x]

# value_integral()
print(x)
print(y)


plt.title('Первое задание')
plt.plot(x, y, label = '1-ая функция')
# plt.ylim(0)
plt.xlim(0)
plt.legend()
plt.show()