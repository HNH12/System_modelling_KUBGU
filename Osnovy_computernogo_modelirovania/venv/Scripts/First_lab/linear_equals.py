def summary_mult(end, points):
    current_sum = 0
    for i in range(0, end):
        current_sum += points[0][i] * points[1][i]

    return current_sum


def summary_squad(end, points):
    current_sum = 0
    for i in range(0, end):
        current_sum += pow(points[i], 2)

    return current_sum


def get_value_a_b(n, points):
    a = (n * summary_mult(n, points) - sum(points[0]) * sum(points[1])) \
        / (n * summary_squad(n, points[0]) - pow(sum(points[0]), 2))

    b = (1/n) * sum(points[1]) - (a/n) * sum(points[0])

    return round(a, 2), round(b, 2)


def get_value_s(n, points):
    a, b = get_value_a_b(n, points)

    print('    a = ', a)
    print('    b = ', b)

    current_sum = 0
    for i in range(n):
        current_sum += pow((a * points[0][i] + b) - points[1][i], 2)

    return round(current_sum, 4), a, b


def form_polinom(a, b):
    def polinom(list_x):
        list_y = list()
        for x in list_x:
            list_y.append(round(a*x + b,4))
        return list_y

    return polinom


def linear_equals_method(points):
    print('Линейная функция:')
    S, a, b = get_value_s(len(points[0]), points)
    print('    S = ', S, end='\n\n')

    return S, form_polinom(a, b)


if __name__ == '__main__':
    points = [
        [1, 2, 3, 4, 5, 6],
        [1.0, 1.5, 3.0, 4.5, 7.0, 8.5]
    ]

    linear_equals_method()