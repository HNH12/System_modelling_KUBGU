import random
import numpy as np
from shapely.geometry import LineString


def form_first_func(n):
    def func(x):
        return (10*x/n)
    return func


def form_second_func(n):
    def func(x):
        return (10*(x-20)/(n-20)) + 20
    return func


def form_random_values(a, b, N):
    list_x = list()
    for i in range(N):
        list_x.append(round(a+(b-a)*random.uniform(0, 1), 2))

    return sorted(list_x)


def get_point_intersection(first_func, second_func, a, b, N):
    list_x = form_random_values(a, b, N)

    for i in range(N):
        sd
    return


def get_values_func(func, list_x):
    values_func = list()
    for x in list_x:
        values_func.append(func(x))
    return values_func


def get_approximate_area(first_func, second_func, max_y, a, b, n, N):
    M = 0
    first_sum = 0
    second_sum = 0
    first_list_x = form_random_values(a, n, N)
    second_list_x = form_random_values(n, b, N)
    for i in range(N):
        random_y = round(random.uniform(0, max_y))
        first_real_y = first_func(first_list_x[i])
        second_real_y = second_func(second_list_x[i])
        if first_real_y < random_y and random_y < second_real_y:
            M += 1
        first_sum += first_real_y
        second_sum += second_real_y

    first_area = ((n - a) / N) * first_sum
    second_area = ((b - n) / N) * second_sum

    return abs(first_area - second_area)


def solve_intergral(a, b, N, func):
    list_random_x = form_random_values(a, b, N)
    list_y = list()
    current_sum = 0
    for i in range(N):
        list_y.append(func(list_random_x[i]))

    return (b-a)/N*sum(list_y), max(list_y)


def get_accuracy(first_area, second_area):
    abs_inaccuracy = abs(first_area - second_area)
    rel_inaccuracy = abs_inaccuracy / max(second_area, first_area)
    print('\nАбсолютная погрешность = ', abs_inaccuracy, '\nОтносительная погрешность = ', rel_inaccuracy)


def value_integral():
    N = 100
    n = 6

    first_segment_start = 0
    first_segment_end = n

    second_segment_start = n
    second_segment_end = 20

    func = form_first_func(n)
    func2 = form_second_func(n)




if __name__ == '__main__':
    value_integral()