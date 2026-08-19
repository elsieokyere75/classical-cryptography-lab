import pytest

from src.number_theory.prime_numbers import is_prime


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (3, True),
        (5, True),
        (17, True),
        (97, True),
        (1, False),
        (4, False),
        (18, False),
        (100, False),
    ],
)
def test_is_prime(number, expected):

    assert is_prime(number) == expected