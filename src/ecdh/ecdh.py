"""Educational Elliptic Curve Diffie-Hellman implementation."""

from src.ecc.ecc import Point, is_on_curve, scalar_multiply


def generate_public_key(
    private_key: int,
    base_point: Point,
    a: int,
    b: int,
    p: int,
) -> Point:
    """Generate an ECDH public key."""

    if private_key <= 0:
        raise ValueError("private key must be positive")

    if base_point is None:
        raise ValueError("base point cannot be the point at infinity")

    if not is_on_curve(base_point, a, b, p):
        raise ValueError("base point must lie on the curve")

    public_key = scalar_multiply(
        private_key,
        base_point,
        a,
        p,
    )

    if public_key is None:
        raise ValueError("private key produced the point at infinity")

    return public_key


def generate_shared_secret(
    private_key: int,
    other_public_key: Point,
    a: int,
    b: int,
    p: int,
) -> Point:
    """Generate the ECDH shared point."""

    if private_key <= 0:
        raise ValueError("private key must be positive")

    if other_public_key is None:
        raise ValueError("public key cannot be the point at infinity")

    if not is_on_curve(other_public_key, a, b, p):
        raise ValueError("public key must lie on the curve")

    shared_point = scalar_multiply(
        private_key,
        other_public_key,
        a,
        p,
    )

    if shared_point is None:
        raise ValueError("shared point cannot be the point at infinity")

    return shared_point