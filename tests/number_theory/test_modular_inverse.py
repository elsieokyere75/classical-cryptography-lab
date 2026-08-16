from src.number_theory.modular_inverse import modular_inverse


def test_modular_inverse():

    assert modular_inverse(7, 40) == 23

    assert modular_inverse(3, 11) == 4

    assert modular_inverse(10, 20) is None