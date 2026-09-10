import pytest

from src.pqc.ml_kem_keygen import (
    matrix_vector_multiply,
    educational_keygen,
)


def test_matrix_vector_multiply_basic():
    A = [
        [1, 2],
        [3, 1],
    ]
    s = [2, 1]

    result = matrix_vector_multiply(A, s)

    assert result == [4, 7]


def test_matrix_vector_multiply_dimension_mismatch():
    A = [
        [1, 2],
        [3, 1],
    ]
    s = [2]

    with pytest.raises(ValueError):
        matrix_vector_multiply(A, s)


def test_matrix_vector_multiply_empty_matrix():
    with pytest.raises(ValueError):
        matrix_vector_multiply([], [1, 2])


def test_educational_keygen_basic():
    A = [
        [1, 2],
        [3, 1],
    ]
    s = [2, 1]
    e = [1, -1]
    q = 7

    ek, dk_secret = educational_keygen(A, s, e, q)

    assert ek == (A, [5, 6])
    assert dk_secret == s


def test_educational_keygen_modular_reduction():
    A = [
        [4, 2],
        [3, 5],
    ]
    s = [2, 1]
    e = [1, 0]
    q = 7

    ek, dk_secret = educational_keygen(A, s, e, q)

    assert ek == (A, [4, 4])
    assert dk_secret == s


def test_educational_keygen_error_dimension_mismatch():
    A = [
        [1, 2],
        [3, 1],
    ]
    s = [2, 1]
    e = [1]
    q = 7

    with pytest.raises(ValueError):
        educational_keygen(A, s, e, q)


def test_educational_keygen_invalid_modulus():
    A = [
        [1, 2],
        [3, 1],
    ]
    s = [2, 1]
    e = [1, -1]

    with pytest.raises(ValueError):
        educational_keygen(A, s, e, 1)