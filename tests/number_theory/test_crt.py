import pytest

from src.number_theory.crt import crt


def test_basic_crt():
    assert crt(1, 3, 2, 5) == 7


def test_crt_rsa_example():
    assert crt(2, 5, 3, 11) == 47


def test_larger_example():
    result = crt(3, 7, 4, 11)

    assert result % 7 == 3
    assert result % 11 == 4
    assert result == 59


def test_result_is_within_modulus_product():
    result = crt(1, 4, 2, 3)

    assert 0 <= result < 12


def test_non_coprime_moduli():
    with pytest.raises(ValueError):
        crt(1, 4, 2, 6)


def test_invalid_first_modulus():
    with pytest.raises(ValueError):
        crt(1, 0, 2, 5)


def test_invalid_second_modulus():
    with pytest.raises(ValueError):
        crt(1, 3, 2, -5)