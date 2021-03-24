import math


def sum_degree(n, points, degree=1):
    current_sum = 0
    for i in range(n):
        current_sum += pow(points[i], degree)

    return round(current_sum, 4)


def sum_degree_xy(n, points, degree=1):
    current_sum = 0
    for i in range(n):
        current_sum += pow(points[0][i], degree) * points[1][i]

    return round(current_sum, 4)


def det(n, points):
    return (
        sum_degree(n, points[0], 4) * sum_degree(n, points[0], 2) * n +
        sum_degree(n, points[0], 3) * sum_degree(n, points[0]) * sum_degree(n, points[0], 2) +
        sum_degree(n, points[0], 2) * sum_degree(n, points[0], 3) * sum_degree(n, points[0]) -
        sum_degree(n, points[0], 2) * sum_degree(n, points[0], 2) * sum_degree(n, points[0], 2) -
        sum_degree(n, points[0], 4) * sum_degree(n, points[0]) * sum_degree(n, points[0]) -
        sum_degree(n, points[0], 3) * sum_degree(n, points[0], 3) * n
    )


def det_a(n, points):
    return (
        sum_degree_xy(n, points, 2) * sum_degree(n, points[0], 2) * n +
        sum_degree(n, points[0], 3) * sum_degree(n, points[0]) * sum_degree(n, points[1]) +
        sum_degree(n, points[0], 2) * sum_degree_xy(n, points) * sum_degree(n, points[0]) -
        sum_degree(n, points[0], 2) * sum_degree(n, points[0], 2) * sum_degree(n, points[1]) -
        sum_degree_xy(n, points, 2) * sum_degree(n, points[0]) * sum_degree(n, points[0]) -
        sum_degree(n, points[0], 3) * sum_degree_xy(n, points) * n
    )


def det_b(n, points):
    return (
            sum_degree(n, points[0], 4) * sum_degree_xy(n, points) * n +
            sum_degree_xy(n, points, 2) * sum(points[0]) * sum_degree(n, points[0], 2) +
            sum_degree(n, points[0], 2) * sum_degree(n, points[0], 3) * sum(points[1]) - sum_degree(n, points[0], 2)
            * sum_degree_xy(n, points) * sum_degree(n, points[0], 2) - sum_degree(n, points[0], 4) *
            sum(points[0]) * sum(points[1]) - sum_degree_xy(n, points, 2) * sum_degree(n, points[0], 3) * n
    )


def det_c(n, points):
    return (
            sum_degree(n, points[0], 4) * sum_degree(n, points[0], 2) * sum(points[1]) + sum_degree(n, points[0], 3) *
            sum_degree_xy(n, points) * sum_degree(n, points[0], 2) + sum_degree_xy(n, points, 2) *
            sum(points[0]) * sum_degree(n, points[0], 3) - sum_degree_xy(n, points, 2) *
            sum_degree(n, points[0], 2) * sum_degree(n, points[0], 2) - sum_degree(n, points[0], 4) * sum(points[0]) *
            sum_degree_xy(n, points) - sum_degree(n, points[0], 3) * sum_degree(n, points[0], 3) * sum(points[1])
    )


def get_values_a_b_c(n, points):
    return (
        round(det_a(n, points)/det(n, points), 2),
        round(det_b(n, points)/det(n, points), 2),
        round(det_c(n, points)/det(n, points), 2)
    )


def get_value_s(n, points):
    a, b, c = get_values_a_b_c(n, points)

    print('    a = ', a)
    print('    b = ', b)
    print('    c = ', c)

    current_sum = 0
    for i in range(n):
        current_sum += pow(
            a*pow(points[0][i], 2) + b * points[0][i] + c - points[1][i]
            , 2)

    return round(current_sum, 4), a, b, c


def form_polinom(a, b, c):
    def polinom(list_x):
        list_y = list()
        for x in list_x:
            list_y.append(round(a*pow(x,2) + b*x + c,4))
        return list_y

    return polinom


def quadratic_function_method(points):
    print('Квадратичная функция:')
    S, a, b, c = get_value_s(len(points[0]), points)
    print('    S = ', S, end='\n\n')

    return S, form_polinom(a, b, c)


if __name__ == '__main__':
    points = [
        [1, 2, 3, 4, 5, 6],
        [1.0, 1.5, 3.0, 4.5, 7.0, 8.5]
    ]

    quadratic_function_method()