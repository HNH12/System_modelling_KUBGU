from matplotlib import pyplot as plt
import random
import numpy as np
import math


def main():
    r = int(input('Введите радиус: '))
    N = int(input('Введите количество интераций: '))
    circle1 = plt.Circle((0, 0), r, color='r', fill=False)

    ax = plt.gca()
    ax.add_patch(circle1)
    plt.axis('scaled')
    plt.plot([-r, r], [r, r], color='b')
    plt.plot([r, r], [r, -r], color='b')
    plt.plot([r, -r], [-r, -r], color='b')
    plt.plot([-r, -r], [-r, r], color='b')


    inside_points = [[], []]
    outside_points = [[], []]
    M = 0
    x = np.random.uniform(-r, r, N)
    y_rand = np.random.uniform(-r, r, N)
    for i in range(N):
        if pow(x[i], 2) + pow(y_rand[i], 2) < pow(r, 2):
            M += 1
            inside_points[0].append(x[i])
            inside_points[1].append(y_rand[i])
        else:
            outside_points[0].append(x[i])
            outside_points[1].append(y_rand[i])

    area = math.pi * r * r
    S = M / N * 4 * r * r

    plt.scatter(inside_points[0], inside_points[1], c='red', s=5)
    plt.scatter(outside_points[0], outside_points[1], c='black', s=5)
    plt.show()
    abs_inaccuracy = abs(area - S)
    rel_inaccuracy = abs_inaccuracy / max(S, area)
    print('S =', area, 'Приближенная площадь =', S, '\nАбсолютная погрешность =', abs_inaccuracy,
          '\nОтносительная погрешность =', rel_inaccuracy)


if __name__ == '__main__':
    main()
