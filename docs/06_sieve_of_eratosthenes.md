# Sieve of Eratosthenes

**Author:** Elsie Okyere

**Project:** Classical Cryptography Laboratory

**Date Started:** August 2026

---

## 1. Introduction

The Sieve of Eratosthenes is an algorithm for finding all prime numbers up to a given limit.

Instead of checking each number individually, the algorithm repeatedly eliminates multiples of known prime numbers.

The remaining numbers are prime.

---

## 2. Example

Find all prime numbers up to 30.

Write the numbers:

2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30

Start with 2.

Remove all multiples of 2:

4 6 8 10 12 14 16 18 20 22 24 26 28 30

Move to 3.

Remove all multiples of 3:

6 9 12 15 18 21 24 27 30

Move to 5.

Remove all multiples of 5:

10 15 20 25 30

The remaining numbers are prime.

---

## 3. Cryptographic Relevance

Efficient prime generation is essential for:

- RSA
- Finite fields
- Elliptic curve cryptography
- Post-quantum cryptography
  
  ---

## 4. Python Implementation

The Sieve of Eratosthenes was implemented in:

`src/number_theory/sieve.py`

The implementation:

1. Creates a boolean list representing possible prime numbers.
2. Marks 0 and 1 as non-prime.
3. Iterates through possible prime factors up to √n.
4. Marks multiples of each discovered prime as composite.
5. Returns the remaining prime numbers.

### Example

For:

```python
sieve(10)
The result is [2, 3, 5, 7]