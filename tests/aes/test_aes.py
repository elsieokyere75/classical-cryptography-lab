import pytest

from src.aes.aes import (
    S_BOX,
    add_round_key,
    aes_encrypt_block,
    bytes_to_state,
    key_expansion,
    mix_columns,
    multiply_by_3,
    shift_rows,
    state_to_bytes,
    sub_bytes,
    xtime,
)


def test_bytes_to_state():
    block = bytes.fromhex("00112233445566778899aabbccddeeff")

    state = bytes_to_state(block)

    assert state == [
        [0x00, 0x44, 0x88, 0xCC],
        [0x11, 0x55, 0x99, 0xDD],
        [0x22, 0x66, 0xAA, 0xEE],
        [0x33, 0x77, 0xBB, 0xFF],
    ]


def test_state_to_bytes():
    state = [
        [0x00, 0x44, 0x88, 0xCC],
        [0x11, 0x55, 0x99, 0xDD],
        [0x22, 0x66, 0xAA, 0xEE],
        [0x33, 0x77, 0xBB, 0xFF],
    ]

    block = state_to_bytes(state)

    assert block.hex() == "00112233445566778899aabbccddeeff"


def test_invalid_block_length():
    with pytest.raises(ValueError):
        bytes_to_state(b"short")


def test_sub_bytes_known_value():
    state = [[0x53, 0, 0, 0]] + [[0, 0, 0, 0] for _ in range(3)]

    result = sub_bytes(state)

    assert result[0][0] == 0xED


def test_shift_rows():
    state = [
        [0x00, 0x01, 0x02, 0x03],
        [0x10, 0x11, 0x12, 0x13],
        [0x20, 0x21, 0x22, 0x23],
        [0x30, 0x31, 0x32, 0x33],
    ]

    result = shift_rows(state)

    assert result == [
        [0x00, 0x01, 0x02, 0x03],
        [0x11, 0x12, 0x13, 0x10],
        [0x22, 0x23, 0x20, 0x21],
        [0x33, 0x30, 0x31, 0x32],
    ]


def test_xtime():
    assert xtime(0x21) == 0x42
    assert xtime(0xA0) == 0x5B
    assert xtime(0x81) == 0x19


def test_multiply_by_3():
    assert multiply_by_3(0xA0) == 0xFB


def test_mix_columns_known_example():
    state = [
        [0xDB, 0x00, 0x00, 0x00],
        [0x13, 0x00, 0x00, 0x00],
        [0x53, 0x00, 0x00, 0x00],
        [0x45, 0x00, 0x00, 0x00],
    ]

    result = mix_columns(state)

    assert result[0][0] == 0x8E
    assert result[1][0] == 0x4D
    assert result[2][0] == 0xA1
    assert result[3][0] == 0xBC


def test_add_round_key():
    state = [
        [0x53, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    round_key = [
        [0xA0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    result = add_round_key(state, round_key)

    assert result[0][0] == 0xF3


def test_key_expansion_produces_11_round_keys():
    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")

    round_keys = key_expansion(key)

    assert len(round_keys) == 11


def test_invalid_key_length():
    with pytest.raises(ValueError):
        key_expansion(b"short")


def test_aes_128_known_answer_vector():
    plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")
    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")

    ciphertext = aes_encrypt_block(plaintext, key)

    assert ciphertext.hex() == "69c4e0d86a7b0430d8cdb78070b4c55a"