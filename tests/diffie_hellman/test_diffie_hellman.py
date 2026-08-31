import pytest

from src.diffie_hellman.diffie_hellman import (
    generate_public_key,
    generate_shared_secret,
)


PRIME = 23
GENERATOR = 5


def test_alice_public_key():
    assert generate_public_key(6, GENERATOR, PRIME) == 8


def test_bob_public_key():
    assert generate_public_key(15, GENERATOR, PRIME) == 19


def test_shared_secret_matches():
    alice_private = 6
    bob_private = 15

    alice_public = generate_public_key(
        alice_private,
        GENERATOR,
        PRIME,
    )

    bob_public = generate_public_key(
        bob_private,
        GENERATOR,
        PRIME,
    )

    alice_secret = generate_shared_secret(
        bob_public,
        alice_private,
        PRIME,
    )

    bob_secret = generate_shared_secret(
        alice_public,
        bob_private,
        PRIME,
    )

    assert alice_secret == bob_secret
    assert alice_secret == 2


def test_invalid_prime():
    with pytest.raises(ValueError):
        generate_public_key(6, GENERATOR, 2)


def test_invalid_generator_too_small():
    with pytest.raises(ValueError):
        generate_public_key(6, 1, PRIME)


def test_invalid_generator_too_large():
    with pytest.raises(ValueError):
        generate_public_key(6, PRIME, PRIME)


def test_invalid_private_key():
    with pytest.raises(ValueError):
        generate_public_key(0, GENERATOR, PRIME)


def test_invalid_public_key():
    with pytest.raises(ValueError):
        generate_shared_secret(0, 6, PRIME)


def test_invalid_private_key_for_shared_secret():
    with pytest.raises(ValueError):
        generate_shared_secret(19, 0, PRIME)