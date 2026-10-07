import pytest
from number_utils.number_utils import (
    is_prime,
    fibonacci,
    gcd,
    factorial,
    sum_of_digits,
)


class TestIsPrime:
    @pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 13, 17, 97, 101])
    def test_primes(self, n):
        assert is_prime(n) is True

    @pytest.mark.parametrize("n", [0, 1, 4, 6, 8, 9, 100, 121])
    def test_composites(self, n):
        assert is_prime(n) is False

    def test_negative(self):
        assert is_prime(-5) is False

    def test_square_of_prime(self):
        assert is_prime(49) is False
        assert is_prime(121) is False


class TestFibonacci:
    def test_base(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_sequence(self):
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(10) == 55
        assert fibonacci(20) == 6765

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            fibonacci(-1)


class TestGcd:
    def test_basic(self):
        assert gcd(12, 8) == 4
        assert gcd(17, 5) == 1
        assert gcd(100, 75) == 25

    def test_zero(self):
        assert gcd(0, 5) == 5
        assert gcd(5, 0) == 5
        assert gcd(0, 0) == 0

    def test_negative(self):
        assert gcd(-12, 8) == 4
        assert gcd(12, -8) == 4


class TestFactorial:
    def test_base(self):
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_small(self):
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120

    def test_large(self):
        assert factorial(10) == 3628800

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            factorial(-1)


class TestSumOfDigits:
    def test_basic(self):
        assert sum_of_digits(123) == 6
        assert sum_of_digits(9999) == 36
        assert sum_of_digits(0) == 0

    def test_negative(self):
        assert sum_of_digits(-456) == 15
