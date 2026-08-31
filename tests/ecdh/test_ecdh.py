import pytest

from src.ecdh.ecdh import (
    generate_public_key,
    generate_shared_secret,
)


A = 2
B = 2
P = 17
G = (5, 1)


def test_alice_public_key():
    assert generate_public_key(5, G, A, B, P) == (9, 16)


def test_bob_public_key():
    assert generate_public_key(7, G, A, B, P) == (0, 6)


def test_shared_secret_matches():
    alice_private = 5
    bob_private = 7

    alice_public = generate_public_key(
        alice_private,
        G,
        A,
        B,
        P,
    )

    bob_public = generate_public_key(
        bob_private,
        G,
        A,
        B,
        P,
    )

    alice_secret = generate_shared_secret(
        alice_private,
        bob_public,
        A,
        B,
        P,
    )

    bob_secret = generate_shared_secret(
        bob_private,
        alice_public,
        A,
        B,
        P,
    )

    assert alice_secret == bob_secret
    assert alice_secret == (10, 11)


def test_invalid_private_key():
    with pytest.raises(ValueError):
        generate_public_key(0, G, A, B, P)


def test_base_point_cannot_be_infinity():
    with pytest.raises(ValueError):
        generate_public_key(5, None, A, B, P)


def test_base_point_must_be_on_curve():
    with pytest.raises(ValueError):
        generate_public_key(5, (5, 2), A, B, P)


def test_public_key_cannot_be_infinity():
    with pytest.raises(ValueError):
        generate_shared_secret(5, None, A, B, P)


def test_public_key_must_be_on_curve():
    with pytest.raises(ValueError):
        generate_shared_secret(
            5,
            (5, 2),
            A,
            B,
            P,
        )


def test_invalid_private_key_for_shared_secret():
    with pytest.raises(ValueError):
        generate_shared_secret(
            0,
            (0, 6),
            A,
            B,
            P,
        )