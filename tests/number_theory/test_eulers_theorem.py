import pytest

from src.number_theory.eulers_theorem import euler_totient, eulers_theorem


def test_euler_totient_10():
    assert euler_totient(10) == 4


def test_euler_totient_prime():
    assert euler_totient(7) == 6


def test_euler_totient_1():
    assert euler_totient(1) == 1


def test_euler_theorem_3_mod_10():
    assert eulers_theorem(3, 10) is True


def test_euler_theorem_7_mod_15():
    assert eulers_theorem(7, 15) is True


def test_euler_theorem_prime_modulus():
    assert eulers_theorem(2, 13) is True


def test_euler_theorem_requires_coprime_inputs():
    with pytest.raises(ValueError):
        eulers_theorem(2, 4)


def test_euler_theorem_requires_positive_modulus():
    with pytest.raises(ValueError):
        eulers_theorem(3, 0)