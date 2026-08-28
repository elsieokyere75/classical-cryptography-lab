"""Educational RSA implementation."""

from math import gcd

from src.number_theory.modular_inverse import modular_inverse


def generate_keypair(p: int, q: int, e: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Generate an RSA public/private key pair.

    Parameters:
        p: First prime.
        q: Second prime.
        e: Public exponent.

    Returns:
        A tuple containing:
            public_key = (e, n)
            private_key = (d, n)
    """
    if p == q:
        raise ValueError("p and q must be distinct primes")

    if p <= 1 or q <= 1:
        raise ValueError("p and q must be greater than 1")

    n = p * q
    phi_n = (p - 1) * (q - 1)

    if not (1 < e < phi_n):
        raise ValueError("e must satisfy 1 < e < phi(n)")

    if gcd(e, phi_n) != 1:
        raise ValueError("e must be coprime to phi(n)")

    d = modular_inverse(e, phi_n)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key