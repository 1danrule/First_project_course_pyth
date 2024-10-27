def number_check(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == int:
            return result + 10
        else:
            return result
    return wrapper


@number_check
def whole_number(number: int) -> int:
    return int(number)


@number_check
def not_whole_number(number: float) -> float:
    return float(number)


print(whole_number(number=10))
print(not_whole_number(number=10.0))
