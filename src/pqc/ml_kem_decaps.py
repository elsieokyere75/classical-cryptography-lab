"""
Educational ML-KEM Decapsulation model.

This module demonstrates the simplified algebra behind recovering
message material from a Module-LWE-style ciphertext.

IMPORTANT:
This is NOT a FIPS 203-compliant ML-KEM implementation and must not
be used for real cryptographic security.
"""


def dot_product(a, b):
    """Compute the dot product of two vectors."""
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")

    return sum(x * y for x, y in zip(a, b))


def educational_decaps(ciphertext, s, q):
    """
    Recover simplified message material.

    ciphertext = (u, v)

    Computes:

        recovered = v - <s, u> mod q

    This is only an educational demonstration of the underlying
    algebraic relationship.
    """

    if q <= 1:
        raise ValueError("q must be greater than 1")

    u, v = ciphertext

    if len(u) != len(s):
        raise ValueError("u and s must have the same length")

    recovered = (v - dot_product(s, u)) % q

    return recovered


if __name__ == "__main__":
    # Simplified example chosen to recover the message cleanly.

    s = [2, 1]

    ciphertext = (
        [4, 3],
        5,
    )

    q = 7

    recovered = educational_decaps(ciphertext, s, q)

    print("Educational ML-KEM Decapsulation")
    print("--------------------------------")
    print("Ciphertext:", ciphertext)
    print("Secret s:", s)
    print("Modulus q:", q)
    print()
    print("Recovered message material:", recovered)