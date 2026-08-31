"""Educational ECDSA implementation."""

from src.ecc.ecc import Point, is_on_curve, scalar_multiply, point_add
from src.number_theory.modular_inverse import modular_inverse


def generate_public_key(
    private_key: int,
    base_point: Point,
    a: int,
    b: int,
    p: int,
    n: int,
) -> Point:
    """Generate an ECDSA public key."""

    if not (1 <= private_key < n):
        raise ValueError("private key must satisfy 1 <= private_key < n")

    if base_point is None or not is_on_curve(base_point, a, b, p):
        raise ValueError("base point must be a valid curve point")

    public_key = scalar_multiply(private_key, base_point, a, p)

    if public_key is None:
        raise ValueError("public key cannot be the point at infinity")

    return public_key


def sign(
    message_hash: int,
    private_key: int,
    nonce: int,
    base_point: Point,
    a: int,
    p: int,
    n: int,
) -> tuple[int, int]:
    """Create an educational ECDSA signature."""

    if not (1 <= private_key < n):
        raise ValueError("private key must satisfy 1 <= private_key < n")

    if not (1 <= nonce < n):
        raise ValueError("nonce must satisfy 1 <= nonce < n")

    if base_point is None:
        raise ValueError("base point cannot be the point at infinity")

    nonce_point = scalar_multiply(nonce, base_point, a, p)

    if nonce_point is None:
        raise ValueError("nonce produced the point at infinity")

    r = nonce_point[0] % n

    if r == 0:
        raise ValueError("invalid nonce produced r = 0")

    nonce_inverse = modular_inverse(nonce, n)

    if nonce_inverse is None:
        raise ValueError("nonce has no modular inverse")

    s = (nonce_inverse * (message_hash + r * private_key)) % n

    if s == 0:
        raise ValueError("invalid nonce produced s = 0")

    return r, s


def verify(
    message_hash: int,
    signature: tuple[int, int],
    public_key: Point,
    base_point: Point,
    a: int,
    b: int,
    p: int,
    n: int,
) -> bool:
    """Verify an educational ECDSA signature."""

    r, s = signature

    if not (1 <= r < n and 1 <= s < n):
        return False

    if public_key is None or not is_on_curve(public_key, a, b, p):
        return False

    if base_point is None or not is_on_curve(base_point, a, b, p):
        return False

    s_inverse = modular_inverse(s, n)

    if s_inverse is None:
        return False

    u1 = (message_hash * s_inverse) % n
    u2 = (r * s_inverse) % n

    point1 = scalar_multiply(u1, base_point, a, p)
    point2 = scalar_multiply(u2, public_key, a, p)

    verification_point = point_add(point1, point2, a, p)

    if verification_point is None:
        return False

    return verification_point[0] % n == r
