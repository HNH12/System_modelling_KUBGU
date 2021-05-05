import numpy as np
import matplotlib.pyplot as plt


def read_from_file():
    file = open('system_equa')
    list_func = []
    for line in file:
        list_func.append(list(map(int, line.split())))
    file.close()
    return list_func


def input_conditions(n):
    conditions = []
    for i in range(n):
        conditions.append(tuple(list(map(int, input('Введите условие для функции y{0}: '.format(i)).split()))))
    return conditions


def value_func(coeff, variables):
    p = 0
    for i in range(len(variables)):
        p += coeff[i] * variables[i]
    return p


def calc_value(y, list_func_coeff, h, n):
    next_values = []
    for i in range(n):
        next_values.append(h * value_func(list_func_coeff[i], y))
    return next_values


if __name__ == '__main__':
    list_func_coeff = read_from_file()
    n = len(list_func_coeff)
    conditions = input_conditions(n)

    y_list_func = [[el[1]] for el in conditions]
    x_list_func = [[el[0]] for el in conditions]
    h = 0.1
    N = int(1 / 0.1)


    for _ in range(20):

        value = []
        for i in range(n):
            value.append(y_list_func[i][-1])

        first_values = calc_value(value, list_func_coeff, h, n)

        new = []
        for i in range(n):
            new.append(y_list_func[i][-1] + first_values[i] / 2)

        second_values = calc_value(new, list_func_coeff, h, n)

        new2 = []
        for i in range(n):
            new2.append(y_list_func[i][-1] + second_values[i] / 2)

        third_values = calc_value(new2, list_func_coeff, h, n)

        new3 = []
        for i in range(n):
            new3.append(y_list_func[i][-1] + third_values[i])

        fourth_values = calc_value(new3, list_func_coeff, h, n)
        # print(first_values, second_values, third_values, fourth_values)

        for i in range(n):
            # print(y_list_func[i][-1] + (first_values[i] + 2 * second_values[i] + third_values[i] * 2 + fourth_values[i]))
            y_list_func[i].append(y_list_func[i][-1] + (first_values[i] + 2 * second_values[i] + third_values[i] * 2 + fourth_values[i]) / 6)
            x_list_func[i].append(x_list_func[i][-1] + h)


    # print(y_list_func)
    plt.figure(figsize=(5, 8))
    for i in range(n):
        plt.plot(x_list_func[i], y_list_func[i])
    # plt.plot(x_y, y)
    # plt.plot(x_z, z)
    plt.show()