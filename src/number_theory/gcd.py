def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a
print(gcd(48, 18))
print(gcd(100, 25))
print(gcd(17, 5))
print(gcd(270, 192))
print(gcd(1, 1))
