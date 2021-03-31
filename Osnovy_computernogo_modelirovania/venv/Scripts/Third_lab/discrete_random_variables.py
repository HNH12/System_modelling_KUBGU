import matplotlib.pyplot as plt
import random
import numpy as np


def congruent_method(N, a0=1, q=5 ** 17, M=2 ** 42):
    values = [a0]
    for i in range(N):
        values.append((q * values[-1] % M))
    return list(map(lambda x: round(x / 10 ** len(str(x)),4), values))


def method_square(gamma0, N, k = None):
    if k == None:
        k = len(str(gamma0))
    values = [gamma0]
    for i in range(N):
        values.append(int(pow(values[-1], 2) / pow(10, k / 2)) % pow(10, k))
    return list(map(lambda x: x/(10**k), values))


def create_hist(data, title):
    n, bin, patches = plt.hist(data, bins=len(data))
    plt.xlabel('Значение')
    plt.ylabel('Частота встречи')
    x1, x2, y1, y2 = plt.axis()
    plt.axis((x1, x2, 0, 10))
    plt.title(title)
    plt.show()


def composition_method(y0, q, N):
    n = len(str(y0))
    values = [y0]
    values_res = []
    for _ in range(N):
        mult = values[-1] * q
        values_res.append(int(mult / 10 ** (n / 2)) % 10 ** n)
        values.append(mult % 10 ** n)
    return list(map(lambda x: x / 10 ** len(str(x)), values_res))


if __name__ == '__main__':
    square_result = method_square(2134, 1000)
    square_result_second = method_square(3167, 1000)
    square_result_third = method_square(3485, 1000)
    congruent_result = congruent_method(1000)
    composition_result = composition_method(3729, 5167, 1000)

    create_hist(square_result, 'Метод квадратов (x0 = 2134)')
    create_hist(square_result_second, 'Метод квадратов (x0 = 3167)')
    create_hist(square_result_third, 'Метод произведений (x0 = 3485)')

    create_hist(congruent_result, 'Конгруэнтный метод')
    create_hist(composition_result, 'Метод произведений')