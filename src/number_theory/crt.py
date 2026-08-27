"""Chinese Remainder Theorem implementation."""

from src.number_theory.modular_inverse import modular_inverse


def crt(a: int, m: int, b: int, n: int) -> int:
    """Solve x ≡ a (mod m), x ≡ b (mod n).

    The moduli m and n must be positive and coprime.

    Returns the unique solution in the range [0, m*n).
    """
    if m <= 0 or n <= 0:
        raise ValueError("moduli must be positive")

    if __import__("math").gcd(m, n) != 1:
        raise ValueError("moduli must be coprime")

    inverse = modular_inverse(m, n)

    k = ((b - a) * inverse) % n

    return (a + m * k) % (m * n)