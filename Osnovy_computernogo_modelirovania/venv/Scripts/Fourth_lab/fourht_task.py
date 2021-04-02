import numpy as np
import matplotlib.pyplot as plt

def read_from_file():
    file = open('system_equa')
    x = list(map(int, file.readline().split()))
    y = list(map(int, file.readline().split()))
    return x, y


def value_func(coeff, x, y, z):
    return x * coeff[0] + y * coeff[1] * z + coeff[2]


if __name__ == '__main__':
    coeff_x, coeff_y = read_from_file()
    h = 0.1
    N = int(1 / 0.1)
    # cauchy_x = tuple(list(map(int, input().split())))
    # cauchy_y = tuple(list(map(int, input().split())))
    cauchy_x = (0, 2)
    cauchy_y = (0, 2)
    a = [0]
    x = [cauchy_x[1]]
    y = [cauchy_y[1]]

    list_values = np.arange(0.0, 1.0, h)
    for _ in range(50):
        k1 = h * value_func(coeff_x, a[-1], x[-1], y[-1])
        l1 = h * value_func(coeff_y, a[-1], x[-1], y[-1])
        k2 = h * value_func(coeff_x, a[-1] + h / 2, x[-1] + k1 / 2, y[-1] + l1 / 2)
        l2 = h * value_func(coeff_y, a[-1] + h/2, x[-1] + k1/2, y[-1] + l1/2)
        k3 = h * value_func(coeff_x, a[-1] + h / 2, x[-1] + k2 / 2, y[-1] + l2 / 2)
        l3 = h * value_func(coeff_y, a[-1] + h / 2, x[-1] + k2 / 2, y[-1] + l2 / 2)
        k4 = h * value_func(coeff_x, a[-1] + h, x[-1] + k3, y[-1] + l3)
        l4 = h * value_func(coeff_y, a[-1] + h, x[-1] + k3, y[-1] + l3)
        a.append(a[-1] + h)
        x.append(x[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
        y.append(y[-1] + (l1 + 2 * l2 + 2 * l3 + l4) / 6)

    plt.plot(a, x)
    plt.plot(a, y)
    plt.show()

    for i in range(50):
        print(str(a[i]) + ' ' + str(x[i]))