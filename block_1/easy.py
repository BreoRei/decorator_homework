def multiply_string(string: str, number: int) -> str:
    inner_count = number
    new_string = ''
    while inner_count:
        if inner_count % 2:
            new_string = string + new_string
        else:
            new_string = string.upper() + new_string
        inner_count -= 1
    return new_string


if __name__ == "__main__":
    func_multiply_string = multiply_string
    print(func_multiply_string)
    result = func_multiply_string(
        string=input('Введите строку: -> '),
        number=int(input('Введите число: -> '))
    )
    print(result)
