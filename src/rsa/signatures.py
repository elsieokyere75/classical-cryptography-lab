"""Educational RSA digital signature implementation."""

from src.number_theory.modular_exponentiation import modular_pow


def sign(message: int, private_key: tuple[int, int]) -> int:
    """Create a textbook RSA signature.

    Signature:
        s = m^d mod n
    """
    d, n = private_key

    if message < 0 or message >= n:
        raise ValueError("message must satisfy 0 <= message < n")

    return modular_pow(message, d, n)


def verify(
    message: int,
    signature: int,
    public_key: tuple[int, int],
) -> bool:
    """Verify a textbook RSA signature.

    Verification:
        m' = s^e mod n

    The signature is valid when m' equals the original message.
    """
    e, n = public_key

    if message < 0 or message >= n:
        return False

    if signature < 0 or signature >= n:
        return False

    recovered_message = modular_pow(signature, e, n)

    return recovered_message == message