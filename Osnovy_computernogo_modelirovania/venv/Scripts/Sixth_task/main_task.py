import numpy as np
import random


def modelling():
    all_time = 2
    task_receipt_period = 2
    registration_time = 12
    error_probability = 0.7

    workload_first_evm = 0
    workload_second_evm = 0

    check_error_first_evm = False

    count_task = 100
    counter = 1
    queue_on_hold = 1
    current_task = 1

    time_work_first_evm = 0
    time_work_second_evm = 0
    time_registration = 0
    time_error_complete = 0

    while counter <= count_task and queue_on_hold:
        print('Текущее задание', current_task)
        if (counter + 6 > count_task) and counter < count_task:
            differ = count_task - counter
            counter += differ
            queue_on_hold += differ
        elif counter < count_task:
            counter += 6
            queue_on_hold += 6
        if queue_on_hold != 0:
            queue_on_hold -= 1
            all_time += registration_time
            time_registration += registration_time
            print('Регистрация')

        if workload_first_evm <= workload_second_evm and not check_error_first_evm:
            workload_first_evm += 1
            time_work_first_evm += 10
            if queue_on_hold == 0:
                all_time += 10
            print('Выполнение задания на первой ЭВМ')
            if random.random() < error_probability:
                all_time += 3
                time_error_complete += 3
                print('Ошибка!')
                print('Исправление ошибки')
                print('Повтор выполнения', current_task, 'задания')
                time_work_first_evm += 10
                current_task += 1
                workload_first_evm -= 1
                check_error_first_evm = True
            else:
                current_task += 1
                workload_first_evm -= 1
                check_error_first_evm = False
                print()
        else:
            if check_error_first_evm:
                check_error_first_evm = False
            workload_second_evm += 1
            time_work_second_evm += 10
            if queue_on_hold == 0:
                all_time += 10
            print('Выполнение задания на второй ЭВМ')
            if random.random() < error_probability:
                time_error_complete += 3
                print('Ошибка!')
                all_time += 3
                print('Повтор выполнения', current_task, 'задания')
                time_work_second_evm += 10
                current_task += 1
                workload_second_evm -= 1
            else:
                current_task += 1
                workload_second_evm -= 1
        print()

    print('\nВремя выполнения заданий:', all_time/60, 'ч.')
    print('Время работы первой ЭВМ:', round(time_work_first_evm/60, 2), 'ч.')
    print('Время работы второй ЭВМ:', round(time_work_second_evm/60, 2), 'ч.')
    print('Времени затрачено на регистрацию:', round(time_registration/60, 2), 'ч.')
    print('Времени затрачено на починку:', round(time_error_complete/60, 2), 'ч.')


def second_modelling():
    all_time = 2
    task_receipt_period = 2
    registration_time = 12
    number_tasks_received_during_processing = registration_time / task_receipt_period
    error_probability = 0.7
    time_resolve_error = 3
    time_complete = 10

    workload_first_evm = 0
    workload_second_evm = 0

    check_error_first_evm = False

    counter = 1
    queue_on_hold = 1
    current_task = 1

    time_work_first_evm = 0
    time_work_second_evm = 0
    time_registration = 0
    time_error_complete = 0

    while all_time < 24*60:
        print('Текущее задание', current_task)
        counter += 12
        queue_on_hold += 12
        if queue_on_hold != 0:
            queue_on_hold -= 1
            all_time += registration_time
            time_registration += registration_time
            print('Регистрация')

        if workload_first_evm <= workload_second_evm and not check_error_first_evm:
            workload_first_evm += 1
            time_work_first_evm += 10
            if queue_on_hold == 0:
                all_time += 10
            print('Выполнение задания на первой ЭВМ')
            if random.random() < error_probability:
                time_error_complete += 3
                all_time += 3
                print('Ошибка!')
                print('Исправление ошибки')
                print('Повтор выполнения', current_task, 'задания')
                time_work_first_evm += 10
                current_task += 1
                workload_first_evm -= 1
                check_error_first_evm = True
            else:
                current_task += 1
                workload_first_evm -= 1
                check_error_first_evm = False
                print()
        else:
            if check_error_first_evm:
                check_error_first_evm = False
            workload_second_evm += 1
            time_work_second_evm += 10
            if queue_on_hold == 0:
                all_time += 10
            print('Выполнение задания на второй ЭВМ')
            if random.random() < error_probability:
                time_work_second_evm += 10
                print('Ошибка!')
                all_time += 3
                print('Повтор выполнения', current_task, 'задания')
                current_task += 1
                workload_second_evm -= 1
            else:
                current_task += 1
                workload_second_evm -= 1
        print()

    print('\nКоличество обработанных заданий за сутки: ', current_task)
    print('Время работы первой ЭВМ:', round(time_work_first_evm / 60, 2), 'ч.')
    print('Время работы второй ЭВМ:', round(time_work_second_evm / 60, 2), 'ч.')
    print('Времени затрачено на регистрацию:', round(time_registration / 60, 2), 'ч.')
    print('Времени затрачено на починку:', round(time_error_complete / 60, 2), 'ч.')


def main():
    # modelling()
    second_modelling()


if __name__ == '__main__':
    main()