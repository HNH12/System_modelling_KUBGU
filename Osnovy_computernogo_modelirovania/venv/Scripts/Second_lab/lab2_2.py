import random
import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry import LineString
import math


def func1(x, n):
    return pow(11 - n * pow(math.sin(x), 2), 1/2)


def func2(x, n):
    return pow(29 - n * pow(math.cos(x), 2), 1/2)


def first_task():
    a = 0
    b = 5
    n = int(input('Введите n(<=10): '))
    N = int(input("Введите количество итераций: "))
    points = [[], []]

    inside_points = [[], []]
    outside_points = [[], []]

    step = 0.1
    i = 0
    while i <= b:
        points[0].append(i)
        points[1].append(func1(i, n))
        i += step

    plt.plot(points[0], points[1])
    plt.legend()

    max_y = max(points[1])
    x = np.random.uniform(a, b, N)
    y_rand = np.random.uniform(0, max_y, N)
    M = 0
    s = 0
    for i in range(N):
        y = func1(x[i], n)
        if y_rand[i] < y:
            M += 1
            inside_points[0].append(x[i])
            inside_points[1].append(y_rand[i])
        else:
            outside_points[0].append(x[i])
            outside_points[1].append(y_rand[i])
        s = s + y

    area = (b / N) * s

    S = M / N * max_y * b

    plt.scatter(inside_points[0], inside_points[1], c='red', s=5)
    plt.scatter(outside_points[0], outside_points[1], c='black', s=5)
    plt.show()

    abs_inaccuracy = abs(area - S)
    rel_inaccuracy = abs_inaccuracy / max(S, area)
    print('S =', area, 'Приближенная площадь =', S, '\nАбсолютная погрешность =', abs_inaccuracy,
          '\nОтносительная погрешность =', rel_inaccuracy)


def second_task():
    a = 0
    b = 7
    n = int(input('Введите n(>=11): '))
    N = int(input("Введите количество итераций: "))
    points = [[], []]
    inside_points = [[], []]
    outside_points = [[], []]
    step = 0.1
    i = 0
    while i <= b:
        points[0].append(i)
        points[1].append(func2(i, n))
        i += step

    plt.plot(points[0], points[1])
    plt.legend()

    max_y = max(points[1])
    x = np.random.uniform(a, b, N)
    y_rand = np.random.uniform(0, max_y, N)
    M = 0
    s = 0
    for i in range(N):
        y = func2(x[i], n)
        if y_rand[i] < y:
            M += 1
            inside_points[0].append(x[i])
            inside_points[1].append(y_rand[i])
        else:
            outside_points[0].append(x[i])
            outside_points[1].append(y_rand[i])
        s = s + y

    area = (b / N) * s

    S = M / N * max_y * b
    plt.scatter(inside_points[0], inside_points[1], c='red', s=5)
    plt.scatter(outside_points[0], outside_points[1], c='black', s=5)
    plt.show()
    abs_inaccuracy = abs(area - S)
    rel_inaccuracy = abs_inaccuracy / max(S, area)
    print('S =', area, 'Приближенная площадь =', S, '\nАбсолютная погрешность =', abs_inaccuracy,
          '\nОтносительная погрешность =', rel_inaccuracy)


def main():
    first_task()


if __name__ == '__main__':
    main()
