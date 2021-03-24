from quadratic_function import quadratic_function_method
from exponential_function import exponential_function_method
from linear_equals import linear_equals_method
from power_function import power_function_method
import matplotlib.pyplot as plt
import random


def read_file():
        POINTS = [[],[]]
        f = open('Points.txt')
        g = f.read().split('\n')
        g[0] = g[0].split(', ')
        g[1] = g[1].split(', ')
        POINTS[0] = list(map(float, g[0]))
        POINTS[1] = list(map(float, g[1]))
        f.close()
        return POINTS


def test(POINTS, NEEDED_N, count_call):
        if (count_call > 2):
                return

        print('\n\n\n****Новый тест***')
        print(POINTS[0])
        print(POINTS[1])


        N = len(POINTS[0]) + 1

        S_qu, quadratic_func = quadratic_function_method(POINTS)
        S_exp, exponential_func = exponential_function_method(POINTS)
        S_linear, linear_func = linear_equals_method(POINTS)
        S_power, power_func = power_function_method(POINTS)


        array_x = [i for i in range(N)]
        array_y_linear = linear_func([i for i in range(N)])
        array_y_power = power_func([i for i in range(N)])
        array_y_exponential = exponential_func([i for i in range(N)])
        array_y_quadratic = quadratic_func([i for i in range(N)])

        if (count_call == 2):
                print('\nЗначения функций на заданном отрезке:\n')
                print('Отрезок X: ', array_x)
                print('Линейная функция: ', array_y_linear)
                print('Степенная функция: ', array_y_power)
                print('Показательная функция', array_y_exponential)
                print('Квадратичная функция', array_y_quadratic, end='\n\n')


                plt.title('Линейная функция (Погрешность = {0})'.format(S_linear))
                plt.scatter(POINTS[0], POINTS[1], c='black', label='Исходное значение')
                plt.plot(array_x, array_y_linear, label='Значение функции')
                plt.xlabel('Ось X')
                plt.ylabel('Ось Y')
                plt.legend()
                plt.show()

                plt.title('Степенная функция (Погрешность = {0})'.format(S_power))
                plt.scatter(POINTS[0], POINTS[1], c='black', label='Исходное значение')
                plt.plot(array_x, array_y_power, label='Значение функции')
                plt.xlabel('Ось X')
                plt.ylabel('Ось Y')
                plt.show()

                plt.title('Показательная функция (Погрешность = {0})'.format(S_exp))
                plt.scatter(POINTS[0], POINTS[1], c='black', label='Исходное значение')
                plt.plot(array_x, array_y_exponential, label='Значение функции')
                plt.xlabel('Ось X')
                plt.ylabel('Ось Y')
                plt.show()

                plt.title('Квадратичная функция (Погрешность = {0})'.format(S_qu))
                plt.scatter(POINTS[0], POINTS[1], c='black', label='Исходное значение')
                plt.plot(array_x, array_y_quadratic, label='Значение функции')
                plt.xlabel('Ось X')
                plt.ylabel('Ось Y')
                plt.show()


                plt.title('Сравнение функций')
                plt.scatter(POINTS[0], POINTS[1], c='black', label='Исходное значение')
                plt.plot(array_x, array_y_linear, label = 'Линейная функция')
                plt.plot(array_x, array_y_power, label = 'Степенная функция')
                plt.plot(array_x, array_y_exponential, label = 'Показательная функция')
                plt.plot(array_x, array_y_quadratic, label = 'Квадратичная функция')
                plt.xlabel('Ось X')
                plt.ylabel('Ось Y')
                plt.legend()
                plt.show()


                print('Лучшая погрешность: ', min(S_qu,S_linear,S_exp,S_power))
        count_call += 1
        new_x = [i for i in range(1, NEEDED_N)]
        new_y = quadratic_func(new_x)
        for i in range(len(new_y)):
                if i % 10 == 0:
                        new_y[i] += random.randrange(-1,1,1)/10

        test([new_x,new_y], NEEDED_N, count_call)


POINTS = read_file()
test(POINTS, 50, 1)