import numpy as np
import random


def modelling():
    count_evm = 2
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

    while counter <= count_task and queue_on_hold != 0:
        print('В очереди на регистрацию: ')
        if not check_error_first_evm and not check_error_second_evm:
            if (counter + 6 > count_task) and counter < count_task:
                counter += count_task - counter
                queue_on_hold += count_task - counter
            elif counter < count_task:
                counter += 6
                queue_on_hold += 6
            if queue_on_hold != 0:
                queue_on_hold -= 1
                all_time += registration_time

        if workload_first_evm > workload_second_evm:
            workload_second_evm += 1
            all_time += 10
            if random.random() < error_probability and not check_error_second_evm:
                check_error_second_evm = True
                check_error_second_complete = True
                all_time += 3
                workload_second_evm -= 1
            else:
                workload_second_evm -= 1
                check_error_second_complete = False
                check_error_second_evm = False
        else:
            workload_first_evm += 1
            all_time += 10
            if random.random() < error_probability and not check_error_first_evm:
                check_error_first_evm = True
                workload_first_evm -= 1
                all_time += 3
            else:
                workload_first_evm -= 1
                check_error_first_complete = False
                check_error_first_evm = False

    print(all_time/60)


def main():
    modelling()


if __name__ == '__main__':
    main()