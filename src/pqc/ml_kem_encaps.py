"""
Educational ML-KEM Encapsulation model.

This module demonstrates some of the Module-LWE mathematical
relationships that motivate ML-KEM encapsulation.

IMPORTANT:
This is NOT a FIPS 203-compliant ML-KEM implementation and must not
be used for real cryptographic security.
"""


def transpose_matrix(A):
    """Return the transpose of matrix A."""
    if not A:
        raise ValueError("A must not be empty")

    row_length = len(A[0])

    if row_length == 0:
        raise ValueError("A must not contain empty rows")

    if any(len(row) != row_length for row in A):
        raise ValueError("A must be rectangular")

    return [list(column) for column in zip(*A)]


def matrix_vector_multiply(A, vector):
    """Multiply matrix A by a vector."""
    result = []

    for row in A:
        if len(row) != len(vector):
            raise ValueError("Matrix and vector have incompatible dimensions")

        value = sum(a * b for a, b in zip(row, vector))
        result.append(value)

    return result


def dot_product(a, b):
    """Compute the dot product of two vectors."""
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")

    return sum(x * y for x, y in zip(a, b))


def educational_encaps(ek, r, e1, e2, message, q):
    """
    Demonstrate a simplified Module-LWE-style encapsulation.

    ek = (A, t)

    Computes:

        u = A^T * r + e1 mod q

        v = <t, r> + e2 + message mod q

    Returns:
        ciphertext = (u, v)
        shared_material = message

    This is an educational model only.
    """

    if q <= 1:
        raise ValueError("q must be greater than 1")

    A, t = ek

    if len(A) != len(r):
        raise ValueError("A and r have incompatible dimensions")

    if len(e1) != len(r):
        raise ValueError("e1 and r must have the same length")

    if len(t) != len(r):
        raise ValueError("t and r must have the same length")

    A_transpose = transpose_matrix(A)

    product = matrix_vector_multiply(A_transpose, r)

    u = [
        (value + error) % q
        for value, error in zip(product, e1)
    ]

    v = (dot_product(t, r) + e2 + message) % q

    ciphertext = (u, v)
    shared_material = message

    return ciphertext, shared_material


if __name__ == "__main__":
    # Public information from our educational KeyGen example.
    A = [
        [1, 2],
        [3, 1],
    ]

    t = [5, 6]

    ek = (A, t)

    # Bob's temporary secret and errors.
    r = [1, 1]
    e1 = [0, 1]
    e2 = 0

    # Toy message representing shared-secret material.
    message = 1

    q = 7

    ciphertext, shared_material = educational_encaps(
        ek,
        r,
        e1,
        e2,
        message,
        q,
    )

    print("Educational ML-KEM Encapsulation")
    print("--------------------------------")
    print("Public key (A, t):", ek)
    print("Temporary secret r:", r)
    print("Error e1:", e1)
    print("Error e2:", e2)
    print("Message:", message)
    print()
    print("Ciphertext (u, v):", ciphertext)
    print("Shared material:", shared_material)