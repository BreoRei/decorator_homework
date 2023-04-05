from random import choice
from typing import Any

CNT = 0


def sum_numbers(num_1: int, num_2: int, num_3: int, num_4: int, *args: Any, **kwargs: Any) -> int:
    global CNT
    num_random = choice(list(kwargs.values())) if len(kwargs) else 0
    inner_sum_num = num_1 + num_2 + num_3 + num_4 + sum(args[:2]) + num_random
    CNT += 1
    return inner_sum_num


def upper_messege(txt: str) -> str:
    global CNT
    CNT += 1
    return txt.upper()


def multiply_by_five(value: str | int) -> str | int:
    global CNT
    CNT += 1
    return value * 5


def function():
    print('Запуск внутренней функции')

    def inner_sum_numbers(num_1: int, num_2: int, num_3: int, num_4: int, *args: Any, **kwargs: Any) -> int:
        global CNT
        num_random = choice(list(kwargs.values())) if len(kwargs) else 0
        inner_sum_num = num_1 + num_2 + num_3 + num_4 + sum(args[:2]) + num_random
        CNT += 1
        return inner_sum_num

    return inner_sum_numbers


if __name__ == "__main__":
    # 1
    # print(sum_numbers(1, 2, 3, 4, *[5, 5, 6, 7, 8]))
    # print(CNT)
    # print(upper_messege('ddsd'))
    # print(upper_messege('dd'))
    # print(CNT)
    # print(multiply_by_five('faf'))
    # print(multiply_by_five(5))
    # print(CNT)

    # 3
    result_function = function()
    print(result_function)

    # 4
    print(result_function(1, 2, 3, 4, *[5, 5, 6, 7, 8]))
