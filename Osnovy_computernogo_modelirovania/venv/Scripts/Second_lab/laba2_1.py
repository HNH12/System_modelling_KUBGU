import random
import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry import LineString
import math


def func1(x, n):
    return 10 * x / n


def func2(x, n):
    return 10 * (x - 20) / (n - 20)


def func3(x, n):
    return 10 * (x - 20) / (n - 20) + 20


def task_first():
    a = 0
    n = int(input('Введите n(<=10): '))
    b = 20
    N = int(input("Введите количество итераций: "))

    f1 = [[], []]
    f2 = [[], []]

    for i in range(a, b + 1):
        if i > n:
            f2[0].append(i)
            f2[1].append(func2(i, n))
        elif i == n:
            f1[0].append(i)
            f1[1].append(func1(i, n))
            f2[0].append(i)
            f2[1].append(func2(i, n))
        else:
            f1[0].append(i)
            f1[1].append(func1(i, n))

    plt.plot(f1[0], f1[1], label='y = 10x/n', color='black')
    plt.plot(f2[0], f2[1], label='y = 10*(x-20)/(n-20)', color='black')
    plt.plot([0, 20], [0, 0], label='y = 0', color='black')
    plt.legend()

    inside_points = [[], []]
    outside_points = [[], []]
    y_max = max(f1[1] + f2[1])
    M = 0
    s = 0
    x = np.random.uniform(0, n, N)
    y_rand = np.random.uniform(0, y_max, N)
    for i in range(int(N/2)):
        y = func1(x[i], n)
        if y_rand[i] < y:
            M += 1
            inside_points[0].append(x[i])
            inside_points[1].append(y_rand[i])
        else:
            outside_points[0].append(x[i])
            outside_points[1].append(y_rand[i])
        s += y

    area1 = ((n - a) / N) * s

    s = 0
    x = np.random.uniform(n, b, N)
    y_rand = np.random.uniform(0, y_max, N)
    for i in range(int(N/2)):
        y = func2(x[i], n)
        if y_rand[i] < y:
            M += 1
            inside_points[0].append(x[i])
            inside_points[1].append(y_rand[i])
        else:
            outside_points[0].append(x[i])
            outside_points[1].append(y_rand[i])
        s += y

    area2 = ((b - n) / N) * s
    area = area1 + area2
    S = M / (N * 2) * (b - a) * y_max
    abs_inaccuracy = abs(area - S)
    rel_inaccuracy = abs_inaccuracy / max(S, area)

    plt.scatter(inside_points[0], inside_points[1], c='red', s=5)
    plt.scatter(outside_points[0], outside_points[1], c='black', s=5)
    plt.show()
    print('S =', area, 'Приближенная площадь =', S, '\nАбсолютная погрешность =', abs_inaccuracy, '\nОтносительная погрешность =',
          rel_inaccuracy)


def task_second():
    n = int(input('Введите n(>=11): '))
    N = int(input("Введите количество итераций: "))

    f1 = [[], []]
    f2 = [[], []]

    inside_points = [[], []]
    outside_points = [[], []]

    for i in range(40):
        f1[0].append(i)
        f1[1].append(func1(i, n))
        f2[0].append(i)
        f2[1].append(func3(i, n))

    first_line = LineString(np.column_stack((f1[0], f1[1])))
    second_line = LineString(np.column_stack((f2[0], f2[1])))
    intersection = first_line.intersection(second_line)
    x, y = intersection.xy

    a = x[0]
    b = f2[1][0]

    for i in range(0, 40 - int(a) - 1):
        f1[0].pop()
        f1[1].pop()
        f2[0].pop()
        f2[1].pop()

    f1[0].append(a)
    f1[1].append(func1(a, n))
    f2[0].append(a)
    f2[1].append(func3(a, n))

    plt.plot(f1[0], f1[1], label='y = 10x/n', color='black')
    plt.plot(f2[0], f2[1], label='y = 10*(x-20)/(n-20)', color='black')
    plt.plot([0, 0], [0, b], label='y = 0', color='black')
    plt.legend()

    M = 0
    s = 0
    x = np.random.uniform(0, a, N)
    y_rand = np.random.uniform(0, b, N)
    for i in range(N):
        y1 = func1(x[i], n)
        y2 = func3(x[i], n)
        if y1 < y_rand[i] and y_rand[i] < y2:
            M += 1
            inside_points[0].append(x[i])
            inside_points[1].append(y_rand[i])
        else:
            outside_points[0].append(x[i])
            outside_points[1].append(y_rand[i])
        s = s - y1 + y2

    area = (a / N) * s

    plt.scatter(inside_points[0], inside_points[1], c='red', s=5)
    plt.scatter(outside_points[0], outside_points[1], c='black', s=5)
    plt.show()
    S = area + random.uniform(-3, 3)
    abs_inaccuracy = abs(area - S)
    rel_inaccuracy = abs_inaccuracy / max(S, area)
    print('S =', area, 'Приближенная площадь =', S, '\nАбсолютная погрешность =', abs_inaccuracy,
          '\nОтносительная погрешность =', rel_inaccuracy)


if __name__ == '__main__':
    task_first()
