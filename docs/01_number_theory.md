# Number Theory Foundations for Cryptography

**Author:** Elsie Okyere  
**Project:** Classical Cryptography Laboratory  
**Date Started:** June 2026

---

## 1. Introduction

Number theory is a branch of mathematics concerned primarily with the
properties and relationships of integers.

It provides many of the mathematical foundations used in modern
cryptography.

Cryptographic algorithms such as RSA, Diffie-Hellman, and elliptic-curve
cryptography rely on mathematical problems involving integers and
algebraic structures.

Understanding these foundations is therefore essential before studying
both classical and post-quantum cryptography.

---

## 2. Why Number Theory Matters in Cryptography

Cryptography relies on mathematical operations that can be easy to
perform in one direction but computationally difficult to reverse.

For example, multiplying two large prime numbers is relatively easy:

p × q = n

However, given a sufficiently large n, determining the original prime
factors p and q can be computationally difficult.

This property forms the basis of the security of RSA.

Other cryptographic systems rely on different mathematical problems.

Examples include:

- Integer factorization
- Discrete logarithms
- Elliptic-curve discrete logarithms
- Lattice problems
- Hash-function security

---

## 3. Important Number Theory Concepts

The following concepts will be studied in this project:

1. Integers
2. Divisibility
3. Prime numbers
4. Greatest Common Divisor (GCD)
5. Euclidean Algorithm
6. Extended Euclidean Algorithm
7. Modular arithmetic
8. Modular inverses
9. Euler's Totient Function
10. Euler's Theorem
11. Fermat's Little Theorem
12. Modular exponentiation

These concepts will eventually be used to implement RSA.

---

## 4. Integers

An integer is a whole number that can be positive, negative, or zero.

Examples:

- -5
- -1
- 0
- 1
- 2
- 10
- 100

The set of integers is commonly represented by:

Z

---

## 5. Divisibility

An integer a divides an integer b if there exists an integer k such that:

b = ak

We write this as:

a | b

For example:

3 | 12

because:

12 = 3 × 4

However:

5 ∤ 12

because there is no integer k for which:

12 = 5k

---

## 6. Prime Numbers

A prime number is an integer greater than 1 that has exactly two
positive divisors:

1. itself

Examples:

2, 3, 5, 7, 11, 13, 17, 19

For example:

7

can only be divided evenly by:

1 and 7

Therefore, 7 is prime.

---

## 7. Composite Numbers

A composite number is an integer greater than 1 that has more than two
positive divisors.

For example:

12

has divisors:

1, 2, 3, 4, 6, 12

Therefore, 12 is composite.

---

## 8. Why Prime Numbers Matter

Prime numbers are fundamental to several cryptographic systems.

RSA, for example, generates keys using large prime numbers.

The basic idea is:

p × q = n

where p and q are large prime numbers.

The resulting value n is used as part of the RSA public key.

The security of RSA relies on the difficulty of factoring a sufficiently
large integer n back into p and q.

---

## 9. Cryptographic Connection

The concepts introduced here will be used throughout this repository.

For example:

GCD
→ used to determine whether numbers are relatively prime.

Extended GCD
→ used to calculate modular inverses.

Prime numbers
→ used during RSA key generation.

Modular arithmetic
→ used throughout RSA.

Euler's Totient Function
→ used to derive RSA's private exponent.

Modular exponentiation
→ used for RSA encryption and decryption.

---

## 10. Connection to Post-Quantum Cryptography

Classical public-key cryptographic systems such as RSA and ECC are
vulnerable to sufficiently powerful quantum computers.

Shor's algorithm provides a quantum algorithm capable of efficiently
solving:

- Integer factorization
- Discrete logarithms

This threatens RSA and ECC.

Post-quantum cryptography therefore investigates cryptographic
constructions based on mathematical problems believed to remain secure
against quantum computers.

Major post-quantum approaches include:

- Lattice-based cryptography
- Hash-based cryptography
- Code-based cryptography
- Multivariate cryptography

Understanding the mathematical foundations of classical cryptography
provides useful context for understanding why these newer approaches
are necessary.

---

## 11. Practical Work

The theoretical concepts in this document will be implemented
programmatically throughout this repository.

Planned implementations include:

- GCD
- Extended Euclidean Algorithm
- Modular arithmetic
- Modular inverse
- Prime number generation
- Prime testing
- Euler's Totient Function
- Modular exponentiation
- RSA

---

## 12. References

### Books

Paar, C., & Pelzl, J. (2010).

*Understanding Cryptography: A Textbook for Students and Practitioners.*

Springer.

Hoffstein, J., Pipher, J., & Silverman, J. H. (2008).

*An Introduction to Mathematical Cryptography.*

Springer.

### Standards and Online Resources

NIST.

Post-Quantum Cryptography Project.

https://csrc.nist.gov/projects/post-quantum-cryptography

IACR.

Cryptology ePrint Archive.

https://eprint.iacr.org/

---

## 13. Learning Notes

This section will be updated as I work through the practical
implementations.

### Questions to investigate

- Why are prime numbers important for RSA?
- Why does RSA require relatively prime values?
- How does the Extended Euclidean Algorithm produce a modular inverse?
- Why does modular exponentiation make RSA practical?
- Which mathematical assumptions used by classical cryptography are
  threatened by quantum computing?

### Current understanding

To be completed as the practical exercises progress.