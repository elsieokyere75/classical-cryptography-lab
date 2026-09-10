import pytest

from src.pqc.ml_kem_decaps import (
    dot_product,
    educational_decaps,
)


def test_dot_product_basic():
    result = dot_product([2, 1], [4, 3])

    assert result == 11


def test_dot_product_dimension_mismatch():
    with pytest.raises(ValueError):
        dot_product([1, 2], [1])


def test_educational_decaps_basic():
    ciphertext = ([4, 3], 5)
    s = [2, 1]
    q = 7

    recovered = educational_decaps(ciphertext, s, q)

    assert recovered == 1


def test_educational_decaps_modular_reduction():
    ciphertext = ([2, 1], 1)
    s = [3, 2]
    q = 7

    recovered = educational_decaps(ciphertext, s, q)

    assert recovered == 0


def test_educational_decaps_invalid_modulus():
    ciphertext = ([4, 3], 5)
    s = [2, 1]

    with pytest.raises(ValueError):
        educational_decaps(ciphertext, s, 1)


def test_educational_decaps_dimension_mismatch():
    ciphertext = ([4], 5)
    s = [2, 1]

    with pytest.raises(ValueError):
        educational_decaps(ciphertext, s, 7)