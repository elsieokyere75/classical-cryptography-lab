# Elliptic Curve Cryptography Mathematics

## 1. Introduction

Elliptic Curve Cryptography (ECC) is a public-key cryptography
approach based on the algebraic structure of elliptic curves over
finite fields.

For learning purposes, this project uses a small prime field. Real
cryptographic systems use much larger parameters and standardized
curves.

---

## 2. Elliptic Curve Equation

Over a prime field F_p, an elliptic curve can be written as:

y^2 ≡ x^3 + ax + b (mod p)

The curve must satisfy:

4a^3 + 27b^2 != 0 (mod p)

This condition ensures that the curve is non-singular.

For the examples in this project, we use:

y^2 ≡ x^3 + 2x + 2 (mod 17)

Therefore:

- a = 2
- b = 2
- p = 17

---

## 3. Points on the Curve

A point P = (x, y) belongs to the curve if:

y^2 mod p = (x^3 + ax + b) mod p

Example:

P = (5, 1)

Left side:

1^2 mod 17 = 1

Right side:

(5^3 + 2(5) + 2) mod 17
= 137 mod 17
= 1

Therefore:

(5, 1)

is on the curve.

However, the point:

(5, 2)

is not on the curve because:

2^2 mod 17 = 4

while the right side is:

1

---

## 4. Point at Infinity

ECC includes a special point called the point at infinity:

O

It acts as the identity element of the elliptic curve group.

Therefore:

P + O = P

and:

O + P = P

In the Python implementation, the point at infinity is represented
using:

None

---

## 5. Point Negation

For a point:

P = (x, y)

its inverse is:

-P = (x, -y mod p)

For example:

P = (5, 1)

Then:

-P = (5, 16)

because:

-1 mod 17 = 16

Therefore:

P + (-P) = O

---

## 6. Point Addition

For two different points:

P = (x1, y1)

Q = (x2, y2)

the slope is:

lambda = (y2 - y1)(x2 - x1)^(-1) mod p

The resulting coordinates are:

x3 = lambda^2 - x1 - x2 mod p

y3 = lambda(x1 - x3) - y1 mod p

Example:

P = (5, 1)

Q = (6, 3)

The slope is:

lambda = (3 - 1)(6 - 5)^(-1) mod 17

lambda = 2

Then:

x3 = 2^2 - 5 - 6 mod 17
   = -7 mod 17
   = 10

and:

y3 = 2(5 - 10) - 1 mod 17
   = -11 mod 17
   = 6

Therefore:

(5, 1) + (6, 3) = (10, 6)

---

## 7. Point Doubling

When P = Q, the point addition formula becomes point doubling.

For:

P = (x1, y1)

the slope is:

lambda = (3x1^2 + a)(2y1)^(-1) mod p

Then:

x3 = lambda^2 - 2x1 mod p

y3 = lambda(x1 - x3) - y1 mod p

Example:

P = (5, 1)

For the curve:

y^2 = x^3 + 2x + 2 mod 17

we obtain:

2P = (6, 3)

---

## 8. Scalar Multiplication

Scalar multiplication means adding a point to itself repeatedly.

For example:

3P = P + P + P

A naive implementation would require repeated point addition.

A more efficient method uses repeated doubling, also called the
double-and-add algorithm.

For:

P = (5, 1)

we calculated:

P  = (5, 1)
2P = (6, 3)
4P = (3, 1)
8P = (13, 7)

Since:

13 = 8 + 4 + 1

we can compute:

13P = 8P + 4P + P

which gives:

13P = (16, 3)

This is conceptually similar to fast modular exponentiation, where
repeated squaring reduces the number of operations.

Double-and-add requires O(log k) point operations to compute kP.

---

## 9. Elliptic Curve Discrete Logarithm Problem

ECC security relies on the difficulty of the Elliptic Curve Discrete
Logarithm Problem (ECDLP).

Given:

P

and:

Q = kP

it should be computationally difficult, for appropriate cryptographic
parameters, to determine the scalar k.

Computing Q from k and P is efficient using scalar multiplication.

Recovering k from P and Q is the difficult problem on which classical
ECC security relies.

---

## 10. Quantum Computing and ECC

Large-scale fault-tolerant quantum computers running Shor's algorithm
would break the discrete-logarithm assumptions used by conventional
elliptic-curve cryptography.

This is one motivation for studying post-quantum cryptography.

Post-quantum cryptographic systems are designed around mathematical
problems for which no efficient quantum attack comparable to Shor's
attack on factoring and discrete logarithms is currently known.

---

## 11. Security Limitations of This Implementation

This implementation is educational only.

It uses:

- very small curve parameters
- simple integer point representations
- non-constant-time Python operations
- no protection against side-channel attacks
- no standardized production curve
- no protocol-level validation

It must not be used to protect real data.

The purpose is to understand the mathematical foundations of ECC
before studying real elliptic-curve protocols and post-quantum
