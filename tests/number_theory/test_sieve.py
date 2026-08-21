from src.number_theory.sieve import sieve


def test_sieve_10():
    assert sieve(10) == [2, 3, 5, 7]


def test_sieve_20():
    assert sieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_sieve_2():
    assert sieve(2) == [2]


def test_sieve_1():
    assert sieve(1) == []


def test_sieve_0():
    assert sieve(0) == []