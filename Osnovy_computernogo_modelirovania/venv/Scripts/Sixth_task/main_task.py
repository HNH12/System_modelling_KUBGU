import numpy as np
import random


def modelling():
    all_time = 2
    task_receipt_period = 2
    registration_time = 12
    number_tasks_received_during_processing = registration_time/task_receipt_period
    error_probability = 0.7
    time_resolve_error = 3
    time_complete = 10

    workload_first_evm = 0
    workload_second_evm = 0

    check_registration = False
    check_error_first_evm = False
    check_error_second_evm = False

    check_error_first_complete = True
    check_error_second_complete = True

    count_task = 100
    counter = 1
    queue_on_hold = 1
    current_task = 1

    last_task = 0

    while (counter <= count_task and queue_on_hold):
        # print(counter, queue_on_hold)
        # print('В очереди на регистрацию: ')
        # print('Время', all_time, 'минут')
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
            print('Регистрация')
        if workload_first_evm <= workload_second_evm and not check_error_first_evm:
            workload_first_evm += 1
            if queue_on_hold == 0:
                all_time += 10
            print('Выполнение задания на первой ЭВМ')
            if random.random() < error_probability:
                last_task = current_task
                check_error_first_evm = True
                all_time += 3
                print('Ошибка!')
                print('Исправление ошибки')
                print('Повтор выполнения', current_task, 'задания')
                current_task += 1
                workload_first_evm -= 1
                check_error_first_complete = False
                check_error_first_evm = True
            else:
                current_task += 1
                workload_first_evm -= 1
                check_error_first_complete = False
                check_error_first_evm = False
                print()
        else:
            if check_error_first_evm:
                check_error_first_evm = False
            workload_second_evm += 1
            if queue_on_hold == 0:
                all_time += 10
            print('Выполнение задания на второй ЭВМ')
            if random.random() < error_probability:
                check_error_second_evm = True
                check_error_second_complete = True
                print('Ошибка!')
                all_time += 3
                print('Повтор выполнения', current_task, 'задания')
                current_task += 1
                workload_second_evm -= 1
                check_error_second_complete = False
            else:
                current_task += 1
                workload_second_evm -= 1
                check_error_second_complete = False
                check_error_second_evm = False
        print()
        # if not check_error_first_evm or not check_error_second_evm:
    print()
    print(all_time/60)


def main():
    modelling()


if __name__ == '__main__':
    main()