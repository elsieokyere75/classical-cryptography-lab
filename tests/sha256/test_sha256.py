from src.sha256.sha256 import (
    MASK_32,
    INITIAL_HASH_VALUES,
    ROUND_CONSTANTS,
    rotr,
    shr,
    choice,
    majority,
    small_sigma_0,
    small_sigma_1,
    big_sigma_0,
    big_sigma_1,
    pad_message,
    create_message_schedule,
    sha256,
)


def test_rotr():
    value = 0b11001001

    result = rotr(value, 1)

    assert result == 0x80000064


def test_shr():
    value = 0b11010110

    result = shr(value, 1)

    assert result == 0b01101011


def test_choice_single_bits():
    assert choice(1, 0, 1) == 0
    assert choice(0, 0, 1) == 1


def test_majority_single_bits():
    assert majority(1, 0, 1) == 1
    assert majority(0, 1, 0) == 0


def test_small_sigma_0():
    x = 0x12345678

    expected = (
        rotr(x, 7)
        ^ rotr(x, 18)
        ^ shr(x, 3)
    )

    assert small_sigma_0(x) == expected


def test_small_sigma_1():
    x = 0x12345678

    expected = (
        rotr(x, 17)
        ^ rotr(x, 19)
        ^ shr(x, 10)
    )

    assert small_sigma_1(x) == expected


def test_big_sigma_0():
    x = 0x12345678

    expected = (
        rotr(x, 2)
        ^ rotr(x, 13)
        ^ rotr(x, 22)
    )

    assert big_sigma_0(x) == expected


def test_big_sigma_1():
    x = 0x12345678

    expected = (
        rotr(x, 6)
        ^ rotr(x, 11)
        ^ rotr(x, 25)
    )

    assert big_sigma_1(x) == expected


def test_pad_message_abc():
    padded = pad_message(b"abc")

    assert len(padded) == 64
    assert padded[:3] == b"abc"
    assert padded[3] == 0x80

    original_length = int.from_bytes(
        padded[-8:],
        byteorder="big",
    )

    assert original_length == 24


def test_pad_message_five_bytes():
    padded = pad_message(b"hello")

    assert len(padded) == 64

    original_length = int.from_bytes(
        padded[-8:],
        byteorder="big",
    )

    assert original_length == 40


def test_pad_message_ten_bytes():
    padded = pad_message(b"0123456789")

    assert len(padded) == 64

    original_length = int.from_bytes(
        padded[-8:],
        byteorder="big",
    )

    assert original_length == 80


def test_padding_creates_second_block_when_needed():
    message = b"a" * 56

    padded = pad_message(message)

    assert len(padded) == 128

    original_length = int.from_bytes(
        padded[-8:],
        byteorder="big",
    )

    assert original_length == 448


def test_message_schedule_abc_first_word():
    padded = pad_message(b"abc")
    block = padded[:64]

    schedule = create_message_schedule(block)

    assert schedule[0] == 0x61626380


def test_message_schedule_abc_middle_words():
    padded = pad_message(b"abc")
    block = padded[:64]

    schedule = create_message_schedule(block)

    assert schedule[1] == 0
    assert schedule[14] == 0


def test_message_schedule_abc_length_word():
    padded = pad_message(b"abc")
    block = padded[:64]

    schedule = create_message_schedule(block)

    assert schedule[15] == 24


def test_message_schedule_words_are_32_bit():
    padded = pad_message(b"abc")
    block = padded[:64]

    schedule = create_message_schedule(block)

    for word in schedule:
        assert 0 <= word <= MASK_32


def test_message_schedule_has_64_words():
    padded = pad_message(b"abc")
    block = padded[:64]

    schedule = create_message_schedule(block)

    assert len(schedule) == 64


def test_initial_hash_values_count():
    assert len(INITIAL_HASH_VALUES) == 8


def test_round_constants_count():
    assert len(ROUND_CONSTANTS) == 64


def test_sha256_empty_message():
    result = sha256(b"")

    assert result == (
        "e3b0c44298fc1c149afbf4c8996fb924"
        "27ae41e4649b934ca495991b7852b855"
    )


def test_sha256_abc():
    result = sha256(b"abc")

    assert result == (
        "ba7816bf8f01cfea414140de5dae2223"
        "b00361a396177a9cb410ff61f20015ad"
    )


def test_sha256_hello():
    result = sha256(b"hello")

    assert result == (
        "2cf24dba5fb0a30e26e83b2ac5b9e29e"
        "1b161e5c1fa7425e73043362938b9824"
    )


def test_sha256_multi_block_message():
    message = b"a" * 100

    result = sha256(message)

    assert result == (
        "2816597888e4a0d3a36b82b83316ab32"
        "680eb8f00f8cd3b904d681246d285a0e"
    )