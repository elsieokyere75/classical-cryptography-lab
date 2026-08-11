def LCM(a, b):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b

        return a

    return abs(a * b) // gcd(a, b)


print(LCM(48, 18))
print(LCM(100, 25))
print(LCM(4, 6))
print(LCM(7, 3))
print(LCM(21, 14))