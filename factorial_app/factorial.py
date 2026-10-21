def factorial(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(f"очікується ціле число, отримано {type(n).__name__}")
    if n < 0:
        raise ValueError("факторіал визначено лише для невід'ємних чисел")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
