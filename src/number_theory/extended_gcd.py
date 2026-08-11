def extended_gcd(a, b):
    """
    Compute the greatest common divisor of a and b,
    together with Bézout coefficients x and y.

    Returns:
        (gcd, x, y)

    such that:

        a*x + b*y = gcd(a, b)
    """

    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y