# Fermat's Little Theorem

**Author:** Elsie Okyere

**Project:** Classical Cryptography Laboratory

**Date Started:** August 2026

---

## 1. Introduction

Fermat's Little Theorem is a fundamental result in number theory.

It describes the behavior of powers modulo a prime number.

The theorem is important in cryptography because modular exponentiation and prime numbers are fundamental components of several cryptographic algorithms.

---

## 2. The Theorem

If p is a prime number and a is an integer such that:

gcd(a, p) = 1

then:

a^(p-1) ≡ 1 (mod p)

In words:

If p is prime and a is not divisible by p, then raising a to the power p - 1 produces a remainder of 1 when divided by p.

---

## 3. Example

Let:

a = 2

and:

p = 7

Since 7 is prime and:

gcd(2, 7) = 1

Fermat's Little Theorem states:

2^6 ≡ 1 (mod 7)

Calculate:

2^6 = 64

and:

64 mod 7 = 1

Therefore:

2^6 ≡ 1 (mod 7)

The theorem is verified.

---

## 4. Another Example

Let:

a = 3

and:

p = 5

Since:

gcd(3, 5) = 1

we have:

3^4 ≡ 1 (mod 5)

Calculate:

3^4 = 81

81 mod 5 = 1

Therefore:

3^4 ≡ 1 (mod 5)

---

## 5. Important Condition

The theorem requires:

gcd(a, p) = 1

When p is prime, this means:

p does not divide a.

For example:

a = 7

p = 7

does not satisfy the condition because:

gcd(7, 7) = 7

Therefore, we cannot directly apply the theorem in this case.

---

## 6. Cryptographic Relevance

Fermat's Little Theorem provides an important foundation for modular arithmetic in cryptography.

It is related to:

- Modular exponentiation
- Primality testing
- RSA
- Finite fields
- Group theory

Understanding this theorem provides a mathematical foundation for understanding more advanced cryptographic constructions.

---

## 7. Equivalent Form

Fermat's Little Theorem can also be written as:

a^p ≡ a (mod p)

for a prime number p.

For example:

2^7 ≡ 2 (mod 7)

because:

2^7 = 128

and:

128 mod 7 = 2.

This form is valid even when p divides a.

---

## 8. Practical Verification

The theorem can be verified computationally by calculating:

pow(a, p - 1, p)

and checking whether the result equals 1.

For example:

```python
pow(2, 6, 7)
answer =1 