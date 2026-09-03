"""Educational SHA-256 implementation."""


MASK_32 = 0xFFFFFFFF


INITIAL_HASH_VALUES = [
    0x6A09E667,
    0xBB67AE85,
    0x3C6EF372,
    0xA54FF53A,
    0x510E527F,
    0x9B05688C,
    0x1F83D9AB,
    0x5BE0CD19,
]


ROUND_CONSTANTS = [
    0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5,
    0x3956C25B, 0x59F111F1, 0x923F82A4, 0xAB1C5ED5,
    0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3,
    0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174,
    0xE49B69C1, 0xEFBE4786, 0x0FC19DC6, 0x240CA1CC,
    0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA,
    0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7,
    0xC6E00BF3, 0xD5A79147, 0x06CA6351, 0x14292967,
    0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13,
    0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85,
    0xA2BFE8A1, 0xA81A664B, 0xC24B8B70, 0xC76C51A3,
    0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070,
    0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5,
    0x391C0CB3, 0x4ED8AA4A, 0x5B9CCA4F, 0x682E6FF3,
    0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208,
    0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2,
]


def rotr(value: int, shift: int) -> int:
    """Rotate a 32-bit integer right."""
    shift %= 32
    return (
        (value >> shift)
        | (value << (32 - shift))
    ) & MASK_32


def shr(value: int, shift: int) -> int:
    """Shift a 32-bit integer right."""
    return (value & MASK_32) >> shift


def choice(x: int, y: int, z: int) -> int:
    """SHA-256 Choice function."""
    return (x & y) ^ ((~x) & z)


def majority(x: int, y: int, z: int) -> int:
    """SHA-256 Majority function."""
    return (
        (x & y)
        ^ (x & z)
        ^ (y & z)
    )


def small_sigma_0(x: int) -> int:
    """SHA-256 small sigma-0 function."""
    return (
        rotr(x, 7)
        ^ rotr(x, 18)
        ^ shr(x, 3)
    )


def small_sigma_1(x: int) -> int:
    """SHA-256 small sigma-1 function."""
    return (
        rotr(x, 17)
        ^ rotr(x, 19)
        ^ shr(x, 10)
    )


def big_sigma_0(x: int) -> int:
    """SHA-256 big Sigma-0 function."""
    return (
        rotr(x, 2)
        ^ rotr(x, 13)
        ^ rotr(x, 22)
    )


def big_sigma_1(x: int) -> int:
    """SHA-256 big Sigma-1 function."""
    return (
        rotr(x, 6)
        ^ rotr(x, 11)
        ^ rotr(x, 25)
    )


def pad_message(message: bytes) -> bytes:
    """Pad a message according to the SHA-256 specification."""

    original_length_bits = len(message) * 8

    padded = bytearray(message)

    # Append the mandatory 1 bit.
    # 0x80 = 10000000 in binary.
    padded.append(0x80)

    # Add zeros until the length is 56 mod 64 bytes.
    while len(padded) % 64 != 56:
        padded.append(0x00)

    # Append original length as 64-bit big-endian integer.
    padded.extend(
        original_length_bits.to_bytes(
            8,
            byteorder="big",
        )
    )

    return bytes(padded)


def create_message_schedule(block: bytes) -> list[int]:
    """Create the 64-word SHA-256 message schedule."""

    if len(block) != 64:
        raise ValueError(
            "SHA-256 block must be exactly 64 bytes"
        )

    schedule = []

    # First 16 words come directly from the block.
    for i in range(0, 64, 4):
        word = int.from_bytes(
            block[i:i + 4],
            byteorder="big",
        )

        schedule.append(word)

    # Expand from 16 words to 64 words.
    for t in range(16, 64):
        word = (
            schedule[t - 16]
            + small_sigma_0(schedule[t - 15])
            + schedule[t - 7]
            + small_sigma_1(schedule[t - 2])
        ) & MASK_32

        schedule.append(word)

    return schedule


def compress_block(
    block: bytes,
    hash_values: list[int],
) -> list[int]:
    """Compress one 512-bit SHA-256 block."""

    schedule = create_message_schedule(block)

    a, b, c, d, e, f, g, h = hash_values

    for t in range(64):

        temp1 = (
            h
            + big_sigma_1(e)
            + choice(e, f, g)
            + ROUND_CONSTANTS[t]
            + schedule[t]
        ) & MASK_32

        temp2 = (
            big_sigma_0(a)
            + majority(a, b, c)
        ) & MASK_32

        h = g
        g = f
        f = e
        e = (d + temp1) & MASK_32
        d = c
        c = b
        b = a
        a = (temp1 + temp2) & MASK_32

    return [
        (hash_values[0] + a) & MASK_32,
        (hash_values[1] + b) & MASK_32,
        (hash_values[2] + c) & MASK_32,
        (hash_values[3] + d) & MASK_32,
        (hash_values[4] + e) & MASK_32,
        (hash_values[5] + f) & MASK_32,
        (hash_values[6] + g) & MASK_32,
        (hash_values[7] + h) & MASK_32,
    ]


def sha256(message: bytes) -> str:
    """Return the SHA-256 hexadecimal digest of a message."""

    padded_message = pad_message(message)

    hash_values = INITIAL_HASH_VALUES.copy()

    for i in range(0, len(padded_message), 64):

        block = padded_message[i:i + 64]

        hash_values = compress_block(
            block,
            hash_values,
        )

    return "".join(
        f"{value:08x}"
        for value in hash_values
    )