from random import choice
from typing import Any

CNT = 0


def sum_numbers(num_1: int, num_2: int, num_3: int, num_4: int, *args: Any, **kwargs: Any) -> int:
    global CNT
    num_random = choice(list(kwargs.values())) if len(kwargs) else 0
    inner_sum_num = num_1 + num_2 + num_3 + num_4 + sum(args[:2]) + num_random
    CNT += 1
    return inner_sum_num


if __name__ == "__main__":
    print(sum_numbers(1, 2, 3, 4, *[5, 5, 6, 7, 8]))
    print(sum_numbers(1, 2, 3, 4, *[5, 5, 6, 7, 8]))
    print(sum_numbers(1, 2, 3, 4, *[5, 5, 6, 7, 8]))
    print(sum_numbers(1, 2, 3, 4, *[5, 5, 6, 7, 8]))
    print(CNT)
