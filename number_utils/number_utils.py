def is_prime(n: int) -> bool:
    """Простое ли число"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """n-е число Фибоначи"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def gcd(a: int, b: int) -> int:
    """Наибольший общий делитель"""
    while b:
        a, b = b, a % b
    return abs(a)


def factorial(n: int) -> int:
    """Факториал n"""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    # баг: range(1, n) вместо range(1, n + 1) — не хватает последнего множителя
    for i in range(1, n):
        result *= i
    return result


def sum_of_digits(n: int) -> int:
    """Сумма цифр числа (знак игнорируется)"""
    return sum(int(d) for d in str(abs(n)))