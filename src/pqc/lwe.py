def lwe_sample(a, s, e, q):
    """
    Compute a toy LWE sample:

        b = <a, s> + e mod q

    Parameters:
        a (list[int]): public vector
        s (list[int]): secret vector
        e (int): small error term
        q (int): modulus

    Returns:
        int: noisy LWE result b
    """
    if len(a) != len(s):
        raise ValueError("a and s must have the same length")

    if q <= 1:
        raise ValueError("q must be greater than 1")

    dot_product = sum(x * y for x, y in zip(a, s))

    return (dot_product + e) % q


def module_lwe_sample(A, s, e, q):
    """
    Compute a toy Module-LWE-style relation:

        t = A*s + e mod q

    This simplified version uses ordinary integer matrices
    rather than polynomial-ring elements.

    Parameters:
        A (list[list[int]]): public matrix
        s (list[int]): secret vector
        e (list[int]): error vector
        q (int): modulus

    Returns:
        list[int]: public noisy vector t
    """
    if q <= 1:
        raise ValueError("q must be greater than 1")

    if len(A) != len(e):
        raise ValueError("A and e must have compatible dimensions")

    result = []

    for row, error in zip(A, e):
        if len(row) != len(s):
            raise ValueError("A and s must have compatible dimensions")

        value = sum(a_ij * s_j for a_ij, s_j in zip(row, s))
        result.append((value + error) % q)

    return result


if __name__ == "__main__":
    # Simple LWE example
    a = [2, 3]
    s = [1, 2]
    e = 1
    q = 7

    b = lwe_sample(a, s, e, q)

    print("LWE example")
    print("a =", a)
    print("s =", s)
    print("e =", e)
    print("b =", b)

    # Simple Module-LWE-style example
    A = [
        [1, 2],
        [3, 1],
    ]

    s = [2, 1]
    e = [1, -1]

    t = module_lwe_sample(A, s, e, q)

    print("\nModule-LWE-style example")
    print("A =", A)
    print("s =", s)
    print("e =", e)
    print("t =", t)