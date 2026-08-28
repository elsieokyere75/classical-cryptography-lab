import pytest

from src.rsa.rsa import generate_keypair
from src.rsa.signatures import sign, verify


def test_rsa_signature():
    public_key, private_key = generate_keypair(7, 11, 7)

    signature = sign(9, private_key)

    assert signature == 58


def test_rsa_signature_verification():
    public_key, private_key = generate_keypair(7, 11, 7)

    signature = sign(9, private_key)

    assert verify(9, signature, public_key) is True


def test_modified_message_fails_verification():
    public_key, private_key = generate_keypair(7, 11, 7)

    signature = sign(9, private_key)

    assert verify(10, signature, public_key) is False


def test_modified_signature_fails_verification():
    public_key, private_key = generate_keypair(7, 11, 7)

    signature = sign(9, private_key)

    assert verify(9, signature + 1, public_key) is False


def test_signature_message_out_of_range():
    _, private_key = generate_keypair(7, 11, 7)

    with pytest.raises(ValueError):
        sign(77, private_key)


def test_negative_message_rejected():
    _, private_key = generate_keypair(7, 11, 7)

    with pytest.raises(ValueError):
        sign(-1, private_key)