import matplotlib.pyplot as plt
import random
import numpy as np


def composition_method(y0, q, N):
    n = len(str(y0))
    values = [y0]
    values_res = []
    for _ in range(N):
        mult = values[-1] * q
        values_res.append(int(mult / 10 ** (n / 2)) % 10 ** n)
        values.append(mult % 10 ** n)
    return list(map(lambda x: x / 10 ** len(str(x)), values_res))


def square_method(first_digit, N):
    n = len(str(first_digit))
    values = [first_digit]
    for _ in range(N):
        values.append(int(values[-1] ** 2 / 10 ** (n/2)) % 10 ** n)
    return list(map(lambda x: x / 10 ** len(str(x)), values))


def comparison_method(N, a0=1, q=5 ** 17, M=2 ** 42):
    values = [a0]
    for _ in range(N):
        values.append(q * values[-1] % M)
    return list(map(lambda x: x / 10 ** len(str(x)), values))


def create_hist(data):
    n, bin, patches = plt.hist(data, bins=len(data))
    return n, patches


def period(sequence):
    y = sequence[-1]
    periods = []
    count = 0
    for el in sequence:
        if el == y:
            periods.append(count)
            count = 0
        else:
            count += 1
    return max(periods)


def frequency_test(sequence):
    count = 0
    for el in sequence:
        if el > 0.2113 and el < 0.7887:
            count += 1
    return count / len(sequence) * 100


def uniformity_test(sequence):
    x_squad = 0
    N = sum(sequence)
    for el in sequence:
        p = 1/len(sequence)
        x_squad += pow((el - p * N),2)/(p*N)
    return x_squad


if __name__ == '__main__':
    sequence1 = np.random.uniform(0, 1, 500)
    period1 = period(sequence1)
    print()
    print('Uniform (встроенная библиотека):')
    print('Частотный тест ', frequency_test(sequence1))
    print('Период последовательности: ', period1)
    print('Равномерный тест: ', uniformity_test(sequence1))

    sequence2 = composition_method(3729, 5167, 500)
    period2 = period(sequence2)
    print()
    print('Метод произведений:')
    print('Частотный тест ', frequency_test(sequence2))
    print('Период последовательности: ', period2)
    print('Равномерный тест: ', uniformity_test(sequence2))

    sequence3 = square_method(7153, 500)
    period3 = period(sequence3)
    print()
    print('Метод квадратов:')
    print('Частотный тест ', frequency_test(sequence3))
    print('Период последовательности: ', period3)
    print('Равномерный тест: ', uniformity_test(sequence3))

    sequence4 = comparison_method(500, 1357, 1357, 9689)
    period4 = period(sequence4)
    print()
    print('Конгруэнтный метод')
    print('Частотный тест ', frequency_test(sequence4))
    print('Период последовательности: ', period4)
    print('Равномерный тест: ', uniformity_test(sequence4))

    create_hist(sequence1)
    plt.title('Uniform')
    plt.show()
    create_hist(sequence2)
    plt.title('Произведений')
    plt.show()
    create_hist(sequence3)
    plt.title('Квадратов')
    plt.show()
    create_hist(sequence4)
    plt.title('Конгруэнтный')
    plt.show()