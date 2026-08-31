import pytest

from src.ecdsa.ecdsa import (
    generate_public_key,
    sign,
    verify,
)


A = 2
B = 2
P = 17
N = 19
G = (5, 1)


def test_generate_public_key():
    assert generate_public_key(7, G, A, B, P, N) == (0, 6)


def test_sign_known_example():
    signature = sign(
        9,
        7,
        3,
        G,
        A,
        P,
        N,
    )

    assert signature == (10, 1)


def test_verify_valid_signature():
    public_key = generate_public_key(
        7,
        G,
        A,
        B,
        P,
        N,
    )

    signature = sign(
        9,
        7,
        3,
        G,
        A,
        P,
        N,
    )

    assert verify(
        9,
        signature,
        public_key,
        G,
        A,
        B,
        P,
        N,
    )


def test_verify_wrong_message_hash():
    public_key = generate_public_key(
        7,
        G,
        A,
        B,
        P,
        N,
    )

    signature = sign(
        9,
        7,
        3,
        G,
        A,
        P,
        N,
    )

    assert not verify(
        8,
        signature,
        public_key,
        G,
        A,
        B,
        P,
        N,
    )


def test_verify_modified_signature():
    public_key = generate_public_key(
        7,
        G,
        A,
        B,
        P,
        N,
    )

    assert not verify(
        9,
        (10, 2),
        public_key,
        G,
        A,
        B,
        P,
        N,
    )


def test_invalid_private_key_zero():
    with pytest.raises(ValueError):
        generate_public_key(
            0,
            G,
            A,
            B,
            P,
            N,
        )


def test_invalid_private_key_too_large():
    with pytest.raises(ValueError):
        generate_public_key(
            N,
            G,
            A,
            B,
            P,
            N,
        )


def test_invalid_nonce_zero():
    with pytest.raises(ValueError):
        sign(
            9,
            7,
            0,
            G,
            A,
            P,
            N,
        )


def test_invalid_nonce_too_large():
    with pytest.raises(ValueError):
        sign(
            9,
            7,
            N,
            G,
            A,
            P,
            N,
        )


def test_verify_invalid_r():
    public_key = generate_public_key(
        7,
        G,
        A,
        B,
        P,
        N,
    )

    assert not verify(
        9,
        (0, 1),
        public_key,
        G,
        A,
        B,
        P,
        N,
    )


def test_verify_invalid_s():
    public_key = generate_public_key(
        7,
        G,
        A,
        B,
        P,
        N,
    )

    assert not verify(
        9,
        (10, 0),
        public_key,
        G,
        A,
        B,
        P,
        N,
    )


def test_verify_invalid_public_key():
    assert not verify(
        9,
        (10, 1),
        (5, 2),
        G,
        A,
        B,
        P,
        N,
    )