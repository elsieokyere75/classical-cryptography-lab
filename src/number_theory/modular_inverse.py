from src.number_theory.extended_gcd import extended_gcd


def modular_inverse(a, m):

    gcd, x, y = extended_gcd(a, m)

    if gcd != 1:
        return None

    return x % m


print(modular_inverse(7, 40))

print(modular_inverse(3, 11))

print(modular_inverse(10, 20))