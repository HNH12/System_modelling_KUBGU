import numpy as np
import random


def read_params(file_path):
    minimum_machine_setup_time = 0
    maximum_machine_setup_time = 0

    mathematical_expectation_task_completion = 0
    standard_deviation_task_completion = 0

    mathematical_expectation_breakdowns = 0
    standard_deviation_breakdowns = 0

    minimum_machine_fixing_breakdown = 0
    maximum_machine_fixing_breakdown = 0

    count_details = 0

    with open(file_path, encoding='utf-8') as file:
        for line in file.readlines():
            if not(line == '\n'):
                if 'Минимальное время наладки станка' in line:
                    pass


# print(np.random.normal(0.5, 0.1, details))
# print(np.random.normal(20, 2, details))
# print(np.random.uniform(0.2, 0.5, details))
# print(np.random.uniform(0.1, 0.5, details))

def modelling():
    current_count_details = 0
    count_time = 0
    count_details = 500
    check_breakdown = True
    all_breakdown_time = 0
    all_next_detail_time = 0
    count_breakdown = 0
    stack_detail = list()
    complete = False

    while((len(stack_detail) != 0) or (not(current_count_details == count_details))):
        time_complete = np.random.normal(0.5, 0.1)

        if not(current_count_details == count_details):
            current_count_details += 1
            stack_detail.append(current_count_details)
            time_next_detail = random.expovariate(1)
            all_next_detail_time += time_next_detail


        if check_breakdown:
            breakdown_time = np.random.normal(20, 2)
            all_breakdown_time += breakdown_time
            check_breakdown = False

        if len(stack_detail) > 0:
            count_time += np.random.uniform(0.2, 0.5)
            count_time += time_complete
            complete = True

        if count_time >= all_breakdown_time:
            count_breakdown += 1
            if count_time - time_complete < all_breakdown_time:
                complete = False

            count_time = all_breakdown_time
            check_breakdown = True
            count_time += np.random.uniform(0.1, 0.5)

        if complete:
            complete = False
            del(stack_detail[0])

        while((count_time > all_next_detail_time) and (not(current_count_details == count_details))):
            current_count_details += 1
            stack_detail.append(current_count_details)
            time_next_detail = random.expovariate(1)
            all_next_detail_time += time_next_detail

        print(current_count_details, stack_detail)


    print('Время выполнения задания: ' + str(count_time) + ' ч.', 'Количество поломок: ' + str(count_breakdown), sep='\n')


def main():
    modelling()
    # list = [random.expovariate(1) for i in range(0,500)]
    # print(sum(list)/500)


if __name__ == '__main__':
    main()