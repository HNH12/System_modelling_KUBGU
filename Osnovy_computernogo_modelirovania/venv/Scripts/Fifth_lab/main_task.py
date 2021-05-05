import numpy as np


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
    count_time = 0
    count_details = 500
    check_breakdown = True
    all_breakdown_time = 0
    count_breakdown = 0
    current_iter = 0

    while(current_iter != count_details):
        if check_breakdown:
            breakdown_time = np.random.normal(20, 2)
            all_breakdown_time += breakdown_time
            check_breakdown = False

        count_time += np.random.uniform(0.2, 0.5)
        count_time += np.random.normal(0.5, 0.1)

        if count_time >= all_breakdown_time:
            count_breakdown += 1
            current_iter -= 1
            count_time = all_breakdown_time
            check_breakdown = True
            count_time += np.random.uniform(0.1, 0.5)
        current_iter += 1

    print('Время выполнения задания: ' + str(count_time) + ' ч.', 'Количество поломок: ' + str(count_breakdown), sep='\n')


def main():
    modelling()


if __name__ == '__main__':
    main()