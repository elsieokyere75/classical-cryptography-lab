import pytest

from src.rsa.rsa import decrypt, encrypt, generate_keypair


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


def test_rsa_encryption():
    public_key, _ = generate_keypair(7, 11, 7)

    ciphertext = encrypt(9, public_key)

    assert ciphertext == 37


def test_rsa_encryption_multiple_messages():
    public_key, _ = generate_keypair(7, 11, 7)

    for message in [1, 2, 3, 4, 5, 6, 8, 9, 10]:
        ciphertext = encrypt(message, public_key)

        assert 0 <= ciphertext < 77


def test_rsa_encryption_rejects_negative_message():
    public_key, _ = generate_keypair(7, 11, 7)

    with pytest.raises(ValueError):
        encrypt(-1, public_key)


def test_rsa_encryption_rejects_message_equal_to_n():
    public_key, _ = generate_keypair(7, 11, 7)

    with pytest.raises(ValueError):
        encrypt(77, public_key)


def test_rsa_decryption():
    public_key, private_key = generate_keypair(7, 11, 7)

    ciphertext = encrypt(9, public_key)
    plaintext = decrypt(ciphertext, private_key)

    assert ciphertext == 37
    assert plaintext == 9


def test_rsa_encrypt_decrypt_multiple_messages():
    public_key, private_key = generate_keypair(7, 11, 7)

    for message in [1, 2, 3, 4, 5, 6, 8, 9, 10]:
        ciphertext = encrypt(message, public_key)
        plaintext = decrypt(ciphertext, private_key)

        assert plaintext == message


def test_rsa_decryption_rejects_negative_ciphertext():
    _, private_key = generate_keypair(7, 11, 7)

    with pytest.raises(ValueError):
        decrypt(-1, private_key)


def test_rsa_decryption_rejects_ciphertext_equal_to_n():
    _, private_key = generate_keypair(7, 11, 7)

    with pytest.raises(ValueError):
        decrypt(77, private_key)