from src.number_theory.fermat import verify_fermat


def test_fermat_2_mod_7():
    assert verify_fermat(2, 7) is True


def test_fermat_3_mod_5():
    assert verify_fermat(3, 5) is True


def test_fermat_4_mod_7():
    assert verify_fermat(4, 7) is True


def test_fermat_multiple_values():
    assert verify_fermat(2, 11) is True
    assert verify_fermat(3, 11) is True
    assert verify_fermat(5, 11) is True


def test_fermat_when_a_equals_p():
    assert verify_fermat(7, 7) is False


def test_fermat_invalid_prime():
    assert verify_fermat(2, 1) is False