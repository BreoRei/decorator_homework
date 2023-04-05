from typing import Any


def sum_numbers(num_1: int, num_2: int, num_3: int, num_4: int, *args: Any, **kwargs: Any) -> int:
    inner_sum_num = num_1 + num_2 + num_3 + num_4 + sum(args) + sum(kwargs.values())

    return inner_sum_num


if __name__ == "__main__":
    # argument = (3, 5, 6, 7, 2)
    # argument_2 = {'5': 2, 'nu2': 1, 'num_3': 5, 'num_4': 4, '22': 33, '33': 7}
    # result = sum_numbers(*argument)
    # print(result)
    # result = sum_numbers(num_1=1, num_2=4, **arg)
    # print(result)
    # 1 нехватает 3 аргументов
    # print(sum_numbers(1)) # TypeError: sum_numbers() missing 3 required positional arguments
    # 2 функция получает несколько значений для аргумента
    # print(sum_numbers(1, 2, 3, 4, num_2=2)) #TypeError: sum_numbers() got multiple values for argument 'num_2'
    # 3
    # argument = (3, 5, 6, 7, 2)
    # print(sum_numbers(*argument))
    # 4_1
    # argument_2 = {'5': 2, '2': 1, '3': 5, '4': 4, '22': 33, '33': 7}
    # print(sum_numbers(*argument_2)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    # 4_2
    # argument_2 = {'5': 2, '2': 1, '3': 5, '4': 4, '22': 33, '33': 7}
    # print(sum_numbers(**argument_2)) #TypeError: sum_numbers() missing 4 required positional arguments
    # как сделать правильно
    argument_3 = {'num_3': 5, 'num_4': 4, 'num_1': 2, 'num_2': 1, '3': 5, '4': 4}
    print(sum_numbers(**argument_3))
