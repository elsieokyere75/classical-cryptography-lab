def modular_pow(base: int, exponent: int, modulus: int) -> int:
    """Compute (base ** exponent) % modulus using repeated squaring."""
    if modulus <= 0:
        raise ValueError("modulus must be a positive integer")

    if exponent < 0:
        raise ValueError("exponent must be non-negative")

    result = 1
    base %= modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus

        base = (base * base) % modulus
        exponent //= 2

    return result


if __name__ == "__main__":
    examples = [
        (3, 13, 7),
        (5, 7, 13),
        (3, 10, 11),
    ]

    for base, exponent, modulus in examples:
        print(f"{base}^{exponent} mod {modulus} = {modular_pow(base, exponent, modulus)}")