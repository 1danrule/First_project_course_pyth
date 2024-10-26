def number_check(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == int or type(result) == float:
            return result

    return wrapper


@number_check
def whole_number(number: int) -> int:
    whole = number + 10
    return int(whole)


@number_check
def not_whole_number(number: float) -> float:
    not_whole = number
    return float(not_whole)


print(whole_number(number=10))
print(not_whole_number(number=10.0))
