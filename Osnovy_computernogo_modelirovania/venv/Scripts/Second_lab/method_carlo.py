import random
import numpy as np



def form_first_func(n):
    def func(x):
        return (10*x/n)
    return func


def form_second_func(n):
    def func(x):
        return 10*(x-20)/(n-20)
    return func


def form_random_values(a, b, N):
    list_x = list()
    for i in range(N):
        list_x.append(round(a+(b-a+1)*random.uniform(0, 1), 2))

    return sorted(list_x)


def get_values_func(func, list_x):
    values_func = list()
    for x in list_x:
        values_func.append(func(x))
    return values_func


def get_approximate_area(first_func, second_func, max_y, a, b, n, N):
    M = 0
    current_sum = 0
    first_list_x = form_random_values(a, n, N)
    for i in range(N):
        random_y = round(random.uniform(0, max_y))
        real_y = first_func(first_list_x[i])
        if random_y < real_y:
            M += 1
        current_sum += real_y
    first_area = ((n - a) / N) * current_sum

    second_list_x = form_random_values(n, b, N)
    second_list_y = form_random_values(0, max_y, N)
    current_sum = 0
    for i in range(N):
        random_y = round(random.uniform(0, max_y))
        real_y = second_func(second_list_x[i])
        if random_y < real_y:
            M += 1
        current_sum += real_y
    second_area = ((b - n) / N) * current_sum

    return (first_area + second_area)


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

    # get_accuracy(func, func2, N, first_segment_start, n, second_segment_end)
    values_first_func, first_max_y = solve_intergral(first_segment_start, first_segment_end, N, func)
    values_second_func, second_max_y = solve_intergral(second_segment_start, second_segment_end, N, func2)

    total_max_y = max(first_max_y, second_max_y)
    total_area = values_first_func + values_second_func

    approximate_area =\
        get_approximate_area(func, func2, total_max_y, first_segment_start, second_segment_end, first_segment_end, N)

    print("Площадь фигуры: ", total_area)
    print("Площадь фигуры через точки: ", approximate_area)
    get_accuracy(total_area, approximate_area)


if __name__ == '__main__':
    value_integral()