from random import choice
from typing import Any


def function():
    CNT = 0
    print('Запуск внутренней функции')

    def inner_sum_numbers(num_1: int, num_2: int, num_3: int, num_4: int, *args: Any, **kwargs: Any) -> int:
        nonlocal CNT
        num_random = choice(list(kwargs.values())) if len(kwargs) else 0
        inner_sum_num = num_1 + num_2 + num_3 + num_4 + sum(args[:2]) + num_random
        CNT += 1
        return inner_sum_num

    return inner_sum_numbers


if __name__ == "__main__":
    result_func = function()
    print(result_func(1, 2, 3, 4))
    result_func = function()
    print(result_func(1, 2, 1, 4))
