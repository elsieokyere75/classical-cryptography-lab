# Prime Numbers

**Author:** Elsie Okyere

**Project:** Classical Cryptography Laboratory


---

## 1. Introduction

A prime number is a natural number greater than 1 that has exactly two positive divisors:

1. The number 1.

2. The number itself.

Examples of prime numbers include:

2, 3, 5, 7, 11, 13, 17, 19, 23, 29.

Prime numbers are the foundation of many cryptographic algorithms, including RSA.

---

## 2. Mathematical Definition

An integer p is prime if:

p > 1

and the only divisors of p are:

1 and p.

A number that is not prime is called a composite number.

Examples:

Prime:

7

Divisors:

1, 7

Composite:

12

Divisors:

1, 2, 3, 4, 6, 12

---

## 3. Cryptographic Relevance

RSA depends on very large prime numbers.

During RSA key generation:

Two large primes are selected.

They are multiplied together to form:

n = p × q

The difficulty of factoring n into p and q provides RSA's security.

Prime numbers are also important in:

- Diffie-Hellman
- Elliptic Curve Cryptography
- Post-quantum cryptography