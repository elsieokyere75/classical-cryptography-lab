def verify_fermat(a, p):
    """
    Verify Fermat's Little Theorem.

    For a prime p and gcd(a, p) = 1:

        a^(p-1) ≡ 1 (mod p)

    Returns True if the theorem holds.
    """

    if p <= 1:
        return False

    if a % p == 0:
        return False

    return pow(a, p - 1, p) == 1

