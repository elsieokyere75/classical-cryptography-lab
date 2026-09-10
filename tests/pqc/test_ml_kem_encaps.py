import pytest

from src.pqc.ml_kem_encaps import (
    transpose_matrix,
    matrix_vector_multiply,
    dot_product,
    educational_encaps,
)


def test_transpose_matrix_basic():
    A = [
        [1, 2],
        [3, 4],
    ]

    result = transpose_matrix(A)

    assert result == [
        [1, 3],
        [2, 4],
    ]


def test_transpose_matrix_empty():
    with pytest.raises(ValueError):
        transpose_matrix([])


def test_transpose_matrix_non_rectangular():
    A = [
        [1, 2],
        [3],
    ]

    with pytest.raises(ValueError):
        transpose_matrix(A)


def test_matrix_vector_multiply_basic():
    A = [
        [1, 3],
        [2, 1],
    ]
    vector = [1, 1]

    result = matrix_vector_multiply(A, vector)

    assert result == [4, 3]


def test_matrix_vector_multiply_dimension_mismatch():
    A = [
        [1, 2],
        [3, 4],
    ]
    vector = [1]

    with pytest.raises(ValueError):
        matrix_vector_multiply(A, vector)


def test_dot_product_basic():
    assert dot_product([5, 6], [1, 1]) == 11


def test_dot_product_dimension_mismatch():
    with pytest.raises(ValueError):
        dot_product([1, 2], [1])


def test_educational_encaps_basic():
    A = [
        [1, 2],
        [3, 1],
    ]
    t = [5, 6]
    ek = (A, t)

    r = [1, 1]
    e1 = [0, 1]
    e2 = 0
    message = 1
    q = 7

    ciphertext, shared_material = educational_encaps(
        ek,
        r,
        e1,
        e2,
        message,
        q,
    )

    assert ciphertext == ([4, 4], 5)
    assert shared_material == 1


def test_educational_encaps_modular_reduction():
    A = [
        [2, 4],
        [3, 5],
    ]
    t = [6, 5]
    ek = (A, t)

    r = [2, 1]
    e1 = [1, -1]
    e2 = 1
    message = 2
    q = 7

    ciphertext, shared_material = educational_encaps(
        ek,
        r,
        e1,
        e2,
        message,
        q,
    )

    assert ciphertext == ([1, 5], 6)
    assert shared_material == 2


def test_educational_encaps_invalid_modulus():
    ek = (
        [[1, 2], [3, 1]],
        [5, 6],
    )

    with pytest.raises(ValueError):
        educational_encaps(
            ek,
            [1, 1],
            [0, 1],
            0,
            1,
            1,
        )


def test_educational_encaps_r_dimension_mismatch():
    ek = (
        [[1, 2], [3, 1]],
        [5, 6],
    )

    with pytest.raises(ValueError):
        educational_encaps(
            ek,
            [1],
            [0],
            0,
            1,
            7,
        )


def test_educational_encaps_e1_dimension_mismatch():
    ek = (
        [[1, 2], [3, 1]],
        [5, 6],
    )

    with pytest.raises(ValueError):
        educational_encaps(
            ek,
            [1, 1],
            [0],
            0,
            1,
            7,
        )


def test_educational_encaps_t_dimension_mismatch():
    ek = (
        [[1, 2], [3, 1]],
        [5],
    )

    with pytest.raises(ValueError):
        educational_encaps(
            ek,
            [1, 1],
            [0, 1],
            0,
            1,
            7,
        )