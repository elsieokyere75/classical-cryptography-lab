def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return abs(a)


def euler_totient(n: int) -> int:
    """Return Euler's totient phi(n).

    phi(n) is the number of integers k in {1, ..., n} that are
    relatively prime to n.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    count = 0
    for k in range(1, n + 1):
        if gcd(k, n) == 1:
            count += 1

    return count


def eulers_theorem(a: int, n: int) -> bool:
    """Check Euler's theorem for a and n.

    Euler's theorem states that if gcd(a, n) == 1, then

        a ** phi(n) == 1 (mod n)

    The function raises ValueError when the theorem's coprimality
    condition is not satisfied.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if gcd(a, n) != 1:
        raise ValueError("Euler's theorem requires gcd(a, n) == 1")

    return pow(a, euler_totient(n), n) == 1


if __name__ == "__main__":
    examples = [
        (3, 10),
        (7, 15),
        (2, 9),
    ]

    for a, n in examples:
        print(f"a={a}, n={n}: {eulers_theorem(a, n)}")