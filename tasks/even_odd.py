__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """
    odd_sum = 0
    even_sum = 0
    for i in numbers:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    if odd_sum != 0:
        return even_sum / odd_sum
    else:
        return 0
