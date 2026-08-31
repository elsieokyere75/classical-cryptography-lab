import pytest

from src.ecc.ecc import (
    is_on_curve,
    point_add,
    point_neg,
    scalar_multiply,
)


A = 2
B = 2
P = 17

BASE_POINT = (5, 1)


def test_point_is_on_curve():
    assert is_on_curve((5, 1), A, B, P) is True


def test_point_is_not_on_curve():
    assert is_on_curve((5, 2), A, B, P) is False


def test_point_at_infinity_is_on_curve():
    assert is_on_curve(None, A, B, P) is True


def test_point_negation():
    assert point_neg((5, 1), P) == (5, 16)


def test_point_at_infinity_negation():
    assert point_neg(None, P) is None


def test_add_point_and_infinity():
    assert point_add(BASE_POINT, None, A, P) == BASE_POINT


def test_add_infinity_and_point():
    assert point_add(None, BASE_POINT, A, P) == BASE_POINT


def test_add_point_and_inverse():
    negative_point = point_neg(BASE_POINT, P)

    assert point_add(BASE_POINT, negative_point, A, P) is None


def test_point_addition():
    result = point_add((5, 1), (6, 3), A, P)

    assert result == (10, 6)


def test_point_doubling():
    result = point_add(BASE_POINT, BASE_POINT, A, P)

    assert result == (6, 3)


def test_scalar_multiply_zero():
    assert scalar_multiply(0, BASE_POINT, A, P) is None


def test_scalar_multiply_one():
    assert scalar_multiply(1, BASE_POINT, A, P) == (5, 1)


def test_scalar_multiply_two():
    assert scalar_multiply(2, BASE_POINT, A, P) == (6, 3)


def test_scalar_multiply_four():
    assert scalar_multiply(4, BASE_POINT, A, P) == (3, 1)


def test_scalar_multiply_eight():
    assert scalar_multiply(8, BASE_POINT, A, P) == (13, 7)


def test_scalar_multiply_thirteen():
    assert scalar_multiply(13, BASE_POINT, A, P) == (16, 4)


def test_negative_scalar_raises_error():
    with pytest.raises(ValueError):
        scalar_multiply(-1, BASE_POINT, A, P)