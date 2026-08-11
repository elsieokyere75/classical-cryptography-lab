# The Euclidean Algorithm

**Author:** Elsie Okyere  
**Project:** Classical Cryptography Laboratory  


---

## 1. Introduction

The Euclidean Algorithm is an efficient algorithm for computing the
Greatest Common Divisor (GCD) of two integers.

The Greatest Common Divisor of two integers `a` and `b` is the largest
positive integer that divides both numbers without leaving a remainder.

The Euclidean Algorithm is important in cryptography because it forms
the foundation for more advanced number-theoretic operations, including
the Extended Euclidean Algorithm and modular inverses.



------
## 2. The Division Algorithm

The Euclidean Algorithm is based on the division relationship:

a = bq + r

where:

- `a` is the dividend
- `b` is the divisor
- `q` is the quotient
- `r` is the remainder

The remainder satisfies:

0 ≤ r < |b|

For example:

48 = 18 × 2 + 12

Here:

- `a = 48`
- `b = 18`
- `q = 2`
- `r = 12`

------

## 3. The Euclidean Algorithm

The Euclidean Algorithm repeatedly applies the division relationship
until the remainder becomes zero.

The general procedure is:

1. Divide `a` by `b`.
2. Calculate the remainder `r`.
3. Replace `a` with `b`.
4. Replace `b` with `r`.
5. Repeat until `b = 0`.
6. The final non-zero value of `a` is the GCD.

----

### Algorithm

text
while b ≠ 0:

    r = a mod b
    a = b
    b = r

return a







## 4. Worked Example

Consider:

gcd(48, 18)

### Step 1

48 = 18 × 2 + 12

Therefore:

48 mod 18 = 12

The new pair is:

(18, 12)

### Step 2

18 = 12 × 1 + 6

Therefore:

18 mod 12 = 6

The new pair is:

(12, 6)

### Step 3

12 = 6 × 2 + 0

Therefore:

12 mod 6 = 0

The algorithm stops because the remainder is zero.

The last non-zero remainder is `6`.

Therefore:

gcd(48, 18) = 6


-------
## 5. Why the Euclidean Algorithm Works

The key property behind the Euclidean Algorithm is:

gcd(a, b) = gcd(b, a mod b)

Suppose:

a = bq + r

Any number that divides both `a` and `b` must also divide `r`.

Conversely, any number that divides both `b` and `r` must also divide
`a`.

Therefore, the common divisors of `(a, b)` are the same as the common
divisors of `(b, r)`.

Since:

r = a mod b

we obtain:

gcd(a, b) = gcd(b, a mod b)

This allows the algorithm to repeatedly reduce the size of the
problem while preserving the GCD.


----
## 6. Computational Complexity

The Euclidean Algorithm is highly efficient.

Its worst-case time complexity is:

O(log(min(a, b)))

This means that the number of iterations grows logarithmically with
the size of the smaller input.

This efficiency is important because number-theoretic algorithms are
frequently applied to very large integers in cryptographic systems.


-----

## 7. Cryptographic Relevance

The Euclidean Algorithm is a fundamental building block for several
cryptographic operations.

It is used to:

- Compute the GCD of integers.
- Determine whether two integers are relatively prime.
- Support the Extended Euclidean Algorithm.
- Calculate modular inverses through the Extended Euclidean Algorithm.
- Support RSA key generation.

The Euclidean Algorithm therefore provides an important mathematical
foundation for understanding public-key cryptography.

The next stage of this project will extend the algorithm to compute
additional coefficients required for modular inversion.

## 8. Practical Implementation

The Euclidean Algorithm was implemented in Python in:

`src/number_theory/gcd.py`

The implementation was tested using several input pairs.

Example:

```python
gcd(48, 18)
output 6 

Additional test cases included
gcd(100, 25) = 25
gcd(17, 5) = 1
gcd(270, 192) = 6
gcd(1, 1) = 1


