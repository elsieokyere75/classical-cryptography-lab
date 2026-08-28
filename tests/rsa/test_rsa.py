import pytest

from src.rsa.rsa import generate_keypair


def test_rsa_key_generation():
    public_key, private_key = generate_keypair(7, 11, 7)

    assert public_key == (7, 77)
    assert private_key == (43, 77)


def test_rsa_key_relationship():
    public_key, private_key = generate_keypair(7, 11, 7)

    e, n = public_key
    d, private_n = private_key

    assert n == private_n
    assert (e * d) % 60 == 1


def test_e_must_be_coprime_to_phi():
    with pytest.raises(ValueError):
        generate_keypair(7, 11, 6)


def test_e_must_be_greater_than_one():
    with pytest.raises(ValueError):
        generate_keypair(7, 11, 1)


def test_e_must_be_less_than_phi():
    with pytest.raises(ValueError):
        generate_keypair(7, 11, 60)


def test_p_and_q_must_be_distinct():
    with pytest.raises(ValueError):
        generate_keypair(7, 7, 5)