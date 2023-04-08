from typing import Any, Callable


# 1.1
# def func_decorator(func: Callable) -> Callable:
#     print('Печатаем сообщение.')
#
#     def wrapper(*args, **kwargs) -> Any:
#         return func(*args, **kwargs)
#     return wrapper
#
# @func_decorator
# def upper_messege(txt: str) -> str:
#     return txt.upper()

# 1.2
def decorator(param_messeg) -> Callable:
    def func_decorator(func: Callable) -> Callable:
        print(param_messeg)

        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return func_decorator


@decorator('Печатаем сообщение.')
def upper_messege(txt: str) -> str:
    return txt.upper()


if __name__ == '__main__':
    result = upper_messege('gfdh')
    print(result)
