import random
import math


def form_random_values(a, b, N):
    list_x = list()
    for i in range(N):
        list_x.append(round(a+(b-a)*random.uniform(0, 1), 2))

    return sorted(list_x)


def get_approximate_area(n, N):
    M = 0
    list_x = form_random_values(-n, n, N)
    for i in range(N):
        random_y = round(5*n*random.uniform(0, 1))
        if (pow(list_x[i]+n, 2) - pow(random_y-n, 2)) < pow(n,2):
            M += 1
    return (M/N)*4*pow(n,2)


def get_accuracy(first_area, second_area):
    abs_inaccuracy = abs(first_area - second_area)
    rel_inaccuracy = abs_inaccuracy / max(second_area, first_area)
    print('\nАбсолютная погрешность = ', abs_inaccuracy, '\nОтносительная погрешность = ', rel_inaccuracy)


def value_integral():
    N = 100
    n = 6

    real_S = math.pi*pow(n,2)

    approximate_area = get_approximate_area(n,N)

    print("Площадь фигуры: ", real_S)
    print("Приблизительная площадь: ", approximate_area)
    get_accuracy(real_S, approximate_area)


if __name__ == '__main__':
    value_integral()