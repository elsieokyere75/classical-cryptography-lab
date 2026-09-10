import pytest

from src.pqc.lwe import lwe_sample, module_lwe_sample


def test_lwe_sample_basic():
    a = [2, 3]
    s = [1, 2]
    e = 1
    q = 7

    assert lwe_sample(a, s, e, q) == 2


def test_lwe_sample_negative_error():
    a = [4, 1]
    s = [1, 2]
    e = -1
    q = 7

    assert lwe_sample(a, s, e, q) == 5


def test_lwe_sample_modular_reduction():
    a = [3, 2]
    s = [1, 2]
    e = 1
    q = 7

    assert lwe_sample(a, s, e, q) == 1


def test_lwe_vector_length_mismatch():
    with pytest.raises(ValueError):
        lwe_sample([1, 2], [1], 1, 7)


def test_lwe_invalid_modulus():
    with pytest.raises(ValueError):
        lwe_sample([1, 2], [1, 2], 1, 1)


def test_module_lwe_sample_basic():
    A = [
        [1, 2],
        [3, 1],
    ]

    s = [2, 1]
    e = [1, -1]
    q = 7

    assert module_lwe_sample(A, s, e, q) == [5, 6]


def test_module_lwe_modular_reduction():
    A = [
        [4, 2],
        [3, 5],
    ]

    s = [2, 1]
    e = [1, 0]
    q = 7

    # First row: 4*2 + 2*1 + 1 = 11 -> 4 mod 7
    # Second row: 3*2 + 5*1 = 11 -> 4 mod 7
    assert module_lwe_sample(A, s, e, q) == [4, 4]


def test_module_lwe_error_dimension_mismatch():
    A = [
        [1, 2],
        [3, 1],
    ]

    s = [2, 1]
    e = [1]

    with pytest.raises(ValueError):
        module_lwe_sample(A, s, e, 7)


def test_module_lwe_secret_dimension_mismatch():
    A = [
        [1, 2],
        [3, 1],
    ]

    s = [2]
    e = [1, -1]

    with pytest.raises(ValueError):
        module_lwe_sample(A, s, e, 7)


def test_module_lwe_invalid_modulus():
    A = [[1, 2]]
    s = [1, 2]
    e = [1]

    with pytest.raises(ValueError):
        module_lwe_sample(A, s, e, 1)