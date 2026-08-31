"""Educational Diffie-Hellman key exchange implementation."""

from src.number_theory.modular_exponentiation import modular_pow


def generate_public_key(
    private_key: int,
    generator: int,
    prime: int,
) -> int:
    """Generate a Diffie-Hellman public key."""

    if prime <= 2:
        raise ValueError("prime must be greater than 2")

    if not (1 < generator < prime):
        raise ValueError("generator must satisfy 1 < generator < prime")

    if private_key <= 0:
        raise ValueError("private key must be positive")

    return modular_pow(generator, private_key, prime)


def generate_shared_secret(
    other_public_key: int,
    private_key: int,
    prime: int,
) -> int:
    """Generate the shared Diffie-Hellman secret."""

    if prime <= 2:
        raise ValueError("prime must be greater than 2")

    if not (1 <= other_public_key < prime):
        raise ValueError(
            "public key must satisfy 1 <= public key < prime"
        )

    if private_key <= 0:
        raise ValueError("private key must be positive")

    return modular_pow(other_public_key, private_key, prime)