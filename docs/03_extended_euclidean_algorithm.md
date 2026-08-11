# Extended Euclidean Algorithm

**Author:** Elsie Okyere  
**Project:** Classical Cryptography Laboratory  


## 1. Introduction

The Extended Euclidean Algorithm is an extension of the Euclidean
Algorithm.

While the ordinary Euclidean Algorithm computes the Greatest Common
Divisor (GCD) of two integers, the Extended Euclidean Algorithm also
computes two integer coefficients that satisfy Bézout's identity.

For integers `a` and `b`, the algorithm finds integers `x` and `y` such
that:

ax + by = gcd(a, b)

This relationship is known as Bézout's identity.

The Extended Euclidean Algorithm is particularly important in
cryptography because it can be used to compute modular inverses.

Modular inverses are fundamental to several cryptographic algorithms,
including RSA.



## 2. Bézout's Identity

Bézout's identity states that for any two integers `a` and `b`, there
exist integers `x` and `y` such that:

ax + by = gcd(a, b)

The values `x` and `y` are called Bézout coefficients.

For example, consider:

a = 48
b = 18

We know from the Euclidean Algorithm that:

gcd(48, 18) = 6

The Extended Euclidean Algorithm can find:

x = -1
y = 3

Therefore:

48(-1) + 18(3) = 6

which gives:

-48 + 54 = 6

Therefore:

48(-1) + 18(3) = gcd(48, 18)


## 3. Euclidean Algorithm Recap

Before applying the Extended Euclidean Algorithm, consider the
Euclidean Algorithm for:

gcd(48, 18)

The divisions are:

48 = 18 × 2 + 12

18 = 12 × 1 + 6

12 = 6 × 2 + 0

The final non-zero remainder is `6`.

Therefore:

gcd(48, 18) = 6


## 4. Back-Substitution

The Extended Euclidean Algorithm works by expressing the GCD as a
linear combination of the original two integers.

Starting from:

18 = 12 × 1 + 6

we rearrange the equation:

6 = 18 - 12

From the previous step of the Euclidean Algorithm:

48 = 18 × 2 + 12

Rearranging gives:

12 = 48 - 18 × 2

Substituting this expression for `12` into the previous equation:

6 = 18 - (48 - 18 × 2)

Expanding:

6 = 18 - 48 + 36

Therefore:

6 = -48 + 3 × 18

This can be written as:

6 = 48(-1) + 18(3)

Therefore, the Bézout coefficients are:

x = -1
y = 3


## 5. Verification

The calculated coefficients can be verified directly.

Using:

x = -1
y = 3

we calculate:

48(-1) + 18(3)

= -48 + 54

= 6

Since:

gcd(48, 18) = 6

the Bézout identity is satisfied:

48(-1) + 18(3) = gcd(48, 18)


## 6. Cryptographic Relevance

The Extended Euclidean Algorithm is an important mathematical
primitive in cryptography.

One of its most important applications is calculating modular
inverses.

A modular inverse of `a` modulo `m` is an integer `x` satisfying:

ax ≡ 1 (mod m)

The Extended Euclidean Algorithm can be used to find this value when:

gcd(a, m) = 1

For example, consider:

7x ≡ 1 (mod 40)

The Extended Euclidean Algorithm can be used to find:

x = 23

because:

7 × 23 = 161

and:

161 mod 40 = 1

Therefore:

7⁻¹ ≡ 23 (mod 40)

This concept will be implemented later in this project.


## 7. Connection to RSA

The Extended Euclidean Algorithm is directly relevant to RSA key
generation.

RSA requires the calculation of a private exponent that is related
to the modular inverse of the public exponent.

If the RSA public exponent is `e` and the relevant modulus is `φ(n)`,
the private exponent `d` satisfies:

ed ≡ 1 (mod φ(n))

Therefore, `d` is the modular inverse of `e` modulo `φ(n)`.

The Extended Euclidean Algorithm provides an efficient method for
calculating this inverse.

This creates the following relationship:

Euclidean Algorithm--Extended Euclidean Algorithm--Modular Inverse--RSA Key Generation


## 8. Practical Implementation

The Extended Euclidean Algorithm will be implemented in Python in:

`src/number_theory/extended_gcd.py`

The implementation will return:

- The GCD
- The first Bézout coefficient
- The second Bézout coefficient

For example:

```text
extended_gcd(48, 18)

GCD = 6
x = -1
y = 3


