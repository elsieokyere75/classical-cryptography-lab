"""
Educational ML-KEM KeyGen model.

This module demonstrates how the Module-LWE relation

    t = A*s + e mod q

contributes to the mathematical foundation of ML-KEM key generation.

IMPORTANT:
This is NOT a FIPS 203-compliant ML-KEM implementation and must not
be used for real cryptographic security.
"""


def matrix_vector_multiply(A, s):
    """Multiply an integer matrix A by vector s."""
    if not A:
        raise ValueError("A must not be empty")

    result = []

    for row in A:
        if len(row) != len(s):
            raise ValueError("A and s have incompatible dimensions")

        value = sum(a_ij * s_j for a_ij, s_j in zip(row, s))
        result.append(value)

    return result


def educational_keygen(A, s, e, q):
    """
    Demonstrate the Module-LWE core of key generation.

    Computes:

        t = A*s + e mod q

    Returns:
        encapsulation_key: (A, t)
        decapsulation_secret: s
    """
    if q <= 1:
        raise ValueError("q must be greater than 1")

    if len(A) != len(e):
        raise ValueError("A and e have incompatible dimensions")

    product = matrix_vector_multiply(A, s)

    t = [
        (value + error) % q
        for value, error in zip(product, e)
    ]

    encapsulation_key = (A, t)
    decapsulation_secret = s

    return encapsulation_key, decapsulation_secret


if __name__ == "__main__":
    # Small educational example.
    # Real ML-KEM uses polynomial vectors and standardized parameters.

    A = [
        [1, 2],
        [3, 1],
    ]

    s = [2, 1]
    e = [1, -1]
    q = 7

    ek, dk_secret = educational_keygen(A, s, e, q)

    print("Educational ML-KEM KeyGen")
    print("-------------------------")
    print("Public matrix A:", A)
    print("Secret s:", s)
    print("Error e:", e)
    print("Modulus q:", q)
    print()
    print("Encapsulation key (A, t):", ek)
    print("Decapsulation secret s:", dk_secret)