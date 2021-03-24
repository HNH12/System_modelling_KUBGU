import matplotlib.pyplot as plt
import numpy as np
import math


def polar2cart(p, phi):
    x = p*math.cos(phi)
    y = p*math.sin(phi)
    return x, y


def cart2polar(x, y):
    p = np.sqrt(x ** 2 + y ** 2)
    phi = np.arctan2(y, x)
    return (p, phi)


def func1(phi, n):
    return np.sqrt((11 + n) * pow(np.cos(phi), 2) + (11 - n) * pow(np.sin(phi), 2))


def func2(phi, n):
    return np.sqrt((10 + n) * pow(np.cos(phi), 2) + (n - 10) * pow(np.sin(phi), 2))


def first_task():
    n = int(input('Введите n(<=10): '))
    N = int(input("Введите количество итераций: "))

    phi = np.arange(0, 2*np.pi, 0.01)
    rho = np.sqrt((11 + n)*pow(np.cos(phi), 2) + (11 - n)*pow(np.sin(phi), 2))

    point_x = []
    point_y = []

    for i in range(len(phi)):
        x, y = polar2cart(rho[i], phi[i])
        point_x.append(x)
        point_y.append(y)

    x_max = max(point_x)
    y_max = max(point_y)

    inside_points = [[], []]
    outside_points = [[], []]
    M = 0
    s = 0
    x = np.random.uniform(-x_max, x_max, N)
    y_rand = np.random.uniform(-y_max, y_max, N)
    for i in range(N):
        p, f = cart2polar(x[i], y_rand[i])
        r = func1(f, n)
        if p < r:
            M += 1
            inside_points[0].append(x[i])
            inside_points[1].append(y_rand[i])
        else:
            outside_points[0].append(x[i])
            outside_points[1].append(y_rand[i])
        s = s + r

    area = (x_max * 2 / N) * s

    S = M / N * y_max * x_max * 4

    abs_inaccuracy = abs(area - S)
    rel_inaccuracy = abs_inaccuracy / max(S, area)
    print('S =', area, 'Приближенная площадь =', S, '\nАбсолютная погрешность =', abs_inaccuracy,
              '\nОтносительная погрешность =', rel_inaccuracy)

    plt.plot([-x_max, x_max], [y_max, y_max], color='b')
    plt.plot([-x_max, x_max], [-y_max, -y_max], color='b')
    plt.plot([-x_max, -x_max], [-y_max, y_max], color='b')
    plt.plot([x_max, x_max], [-y_max, y_max], color='b')
    plt.scatter(inside_points[0], inside_points[1], c='red', s=5)
    plt.scatter(outside_points[0], outside_points[1], c='black', s=5)
    plt.plot(point_x, point_y, color='r')
    plt.show()


def second_task():
    n = int(input('Введите n(>=11): '))
    N = int(input("Введите количество итераций: "))

    phi = np.arange(0, 2*np.pi, 0.01)
    rho = np.sqrt((10 + n)*pow(np.cos(phi), 2) + (n - 10)*pow(np.sin(phi), 2))

    point_x = []
    point_y = []

    for i in range(len(phi)):
        x, y = polar2cart(rho[i], phi[i])
        point_x.append(x)
        point_y.append(y)

    x_max = max(point_x)
    y_max = max(point_y)

    inside_points = [[], []]
    outside_points = [[], []]
    M = 0
    s = 0
    x = np.random.uniform(-x_max, x_max, N)
    y_rand = np.random.uniform(-y_max, y_max, N)
    for i in range(N):
        p, f = cart2polar(x[i], y_rand[i])
        r = func2(f, n)
        if p < r:
            M += 1
            inside_points[0].append(x[i])
            inside_points[1].append(y_rand[i])
        else:
            outside_points[0].append(x[i])
            outside_points[1].append(y_rand[i])
        s = s + r

    area = (x_max * 2 / N) * s

    S = M / N * y_max * x_max * 4

    abs_inaccuracy = abs(area - S)
    rel_inaccuracy = abs_inaccuracy / max(S, area)
    print('S =', area, 'Приближенная площадь =', S, '\nАбсолютная погрешность =', abs_inaccuracy,
              '\nОтносительная погрешность =', rel_inaccuracy)

    plt.plot([-x_max, x_max], [y_max, y_max], color='b')
    plt.plot([-x_max, x_max], [-y_max, -y_max], color='b')
    plt.plot([-x_max, -x_max], [-y_max, y_max], color='b')
    plt.plot([x_max, x_max], [-y_max, y_max], color='b')
    plt.scatter(inside_points[0], inside_points[1], c='red', s=5)
    plt.scatter(outside_points[0], outside_points[1], c='black', s=5)
    plt.plot(point_x, point_y, color='r')
    plt.show()


if __name__ == '__main__':
    first_task()
