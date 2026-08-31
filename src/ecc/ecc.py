"""Educational elliptic curve arithmetic over a prime field."""

from src.number_theory.modular_inverse import modular_inverse


Point = tuple[int, int] | None


def is_on_curve(
    point: Point,
    a: int,
    b: int,
    p: int,
) -> bool:
    """Return True if a point lies on the elliptic curve."""

    if point is None:
        return True

    x, y = point

    return (y * y) % p == (x**3 + a * x + b) % p


def point_neg(point: Point, p: int) -> Point:
    """Return the additive inverse of a point."""

    if point is None:
        return None

    x, y = point

    return x, (-y) % p


def point_add(
    point1: Point,
    point2: Point,
    a: int,
    p: int,
) -> Point:
    """Add two elliptic-curve points."""

    if point1 is None:
        return point2

    if point2 is None:
        return point1

    x1, y1 = point1
    x2, y2 = point2

    # P + (-P) = O
    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    # Point doubling
    if point1 == point2:
        numerator = (3 * x1 * x1 + a) % p
        denominator = (2 * y1) % p
    else:
        # Addition of two different points
        numerator = (y2 - y1) % p
        denominator = (x2 - x1) % p

    denominator_inverse = modular_inverse(denominator, p)

    if denominator_inverse is None:
        raise ValueError("slope denominator has no modular inverse")

    slope = (numerator * denominator_inverse) % p

    x3 = (slope * slope - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p

    return x3, y3


def scalar_multiply(
    scalar: int,
    point: Point,
    a: int,
    p: int,
) -> Point:
    """Compute scalar * point using the double-and-add algorithm."""

    if scalar < 0:
        raise ValueError("scalar must be non-negative")

    result: Point = None
    addend = point

    while scalar > 0:
        if scalar % 2 == 1:
            result = point_add(result, addend, a, p)

        addend = point_add(addend, addend, a, p)
        scalar //= 2

    return result