import pytest

from src.number_theory.extended_gcd import extended_gcd


@pytest.mark.parametrize(
    "a, b, expected_gcd",
    [
        (48, 18, 6),
        (100, 25, 25),
        (17, 5, 1),
        (270, 192, 6),
        (35, 15, 5),
    ],
)
def test_extended_gcd(a, b, expected_gcd):
    gcd, x, y = extended_gcd(a, b)

    assert gcd == expected_gcd
    assert a * x + b * y == gcd