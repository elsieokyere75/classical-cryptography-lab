# Modular Inverse

**Author:** Elsie Okyere
**Project:** Classical Cryptography Laboratory
**Date Started:** August 2026

---

## 1. Introduction

A modular inverse is an integer that reverses multiplication in modular arithmetic.

If an integer a has an inverse modulo m, there exists an integer x such that:

ax ≡ 1 (mod m)

The value x is called the modular inverse of a modulo m.

Not every integer has a modular inverse.

A modular inverse exists only when:

gcd(a, m) = 1

This means that a and m must be relatively prime.

The Extended Euclidean Algorithm can be used to calculate the modular inverse efficiently.

Modular inverses are fundamental to many cryptographic systems, including RSA.


## 2. Mathematical Definition

A modular inverse is defined as an integer x satisfying:

ax ≡ 1 (mod m)

Example:

Find the inverse of:

7⁻¹ mod 40

We need to find an integer x such that:

7x ≡ 1 (mod 40)

Testing several values:

7 × 1 = 7

7 × 2 = 14

7 × 3 = 21

...

7 × 23 = 161

161 mod 40 = 1

Therefore:

7⁻¹ ≡ 23 (mod 40)

## 3. Relationship with the Extended Euclidean Algorithm

The Extended Euclidean Algorithm computes integers x and y satisfying:

ax + my = gcd(a, m)

If:

gcd(a, m) = 1

then:

ax + my = 1

Taking both sides modulo m:

ax ≡ 1 (mod m)

Therefore:

x is the modular inverse of a modulo m.

The Bézout coefficient returned by the Extended Euclidean Algorithm becomes the modular inverse.


## 4. Cryptographic Relevance

Modular inverses are essential in modern cryptography.

One of the most important applications is RSA.

During RSA key generation, a public exponent e is selected.

The private exponent d must satisfy:

ed ≡ 1 (mod φ(n))

Therefore, d is the modular inverse of e modulo φ(n).

Without modular inverses, RSA key generation would not be possible.


## 5. Practical Implementation

The modular inverse implementation will be written in:

src/number_theory/modular_inverse.py

The implementation will:

1. Compute the GCD.

2. Verify that the inverse exists.

3. Return the Bézout coefficient.

4. Verify that:

(a × inverse) mod m = 1

Example:

modular_inverse(7, 40)

Output:

23

