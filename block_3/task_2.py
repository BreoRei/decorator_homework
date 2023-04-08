from typing import Callable, Any


def decorator(repeat_operation=10) -> Callable:
    print('Начапо работы')

    def func_decorator(func: Callable) -> Callable:

        def wrapper(*args, **kwargs) -> Any:
            counter = 0
            while repeat_operation > counter:
                try:
                    result_wrapper = func(*args, **kwargs)
                    print('Конец работы')
                    return result_wrapper
                except Exception:
                    counter += 1
                    print('Итерация №', counter)
            return print('Произошла ошибка исполнения')

        return wrapper

    return func_decorator


@decorator(5)
def upper_messege(txt: str) -> str:
    return txt.upper()


if __name__ == '__main__':
    result = upper_messege('gjf')
    print(result)
    result = upper_messege(5)
    print(result)
