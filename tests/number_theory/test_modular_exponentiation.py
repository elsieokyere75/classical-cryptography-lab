import pytest

from src.number_theory.modular_exponentiation import modular_pow


def test_3_power_13_mod_7():
    assert modular_pow(3, 13, 7) == 3


def test_5_power_7_mod_13():
    assert modular_pow(5, 7, 13) == 8


def test_3_power_10_mod_11():
    assert modular_pow(3, 10, 11) == 1


def test_exponent_zero():
    assert modular_pow(25, 0, 7) == 1


def test_base_reduction():
    assert modular_pow(15, 2, 7) == 1


def test_modulus_one():
    assert modular_pow(12345, 678, 1) == 0


def test_large_exponent_matches_python_pow():
    base = 123456789
    exponent = 12345
    modulus = 1000000007

    assert modular_pow(base, exponent, modulus) == pow(
        base, exponent, modulus
    )


def test_invalid_modulus():
    with pytest.raises(ValueError):
        modular_pow(2, 10, 0)


def test_negative_exponent():
    with pytest.raises(ValueError):
        modular_pow(2, -1, 5)