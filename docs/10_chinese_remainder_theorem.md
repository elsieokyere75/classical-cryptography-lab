# Chinese Remainder Theorem

## 1. Introduction

The Chinese Remainder Theorem (CRT) provides a way to solve systems of simultaneous congruences.

For example:

x ≡ 1 (mod 3)
x ≡ 2 (mod 5)

has the solution:

x ≡ 7 (mod 15)

because:

7 mod 3 = 1
7 mod 5 = 2

---

## 2. The theorem

If m and n are coprime:

gcd(m, n) = 1

then the system:

x ≡ a (mod m)

x ≡ b (mod n)

has a unique solution modulo:

mn

---

## 3. Derivation

From:

x ≡ a (mod m)

we can write:

x = a + mk

Substitute into:

x ≡ b (mod n)

giving:

a + mk ≡ b (mod n)

Therefore:

mk ≡ b - a (mod n)

Since gcd(m,n) = 1, m has a modular inverse modulo n:

m⁻¹ mod n

Thus:

k ≡ (b-a)m⁻¹ (mod n)

Finally:

x = a + mk

---

## 4. Example

Solve:

x ≡ 1 (mod 3)

x ≡ 2 (mod 5)

We have:

a = 1
m = 3
b = 2
n = 5

The inverse of 3 modulo 5 is:

3⁻¹ ≡ 2 (mod 5)

because:

3 × 2 = 6 ≡ 1 (mod 5)

Therefore:

k ≡ (2-1)(2) mod 5

k ≡ 2 mod 5

Then:

x = 1 + 3(2)

x = 7

Therefore:

x ≡ 7 (mod 15)

---

## 5. Connection to RSA

RSA uses:

n = pq

where p and q are distinct primes.

Because:

gcd(p,q) = 1,

CRT allows RSA computations modulo p and q to be performed separately and then recombined.

This is important for:

- proving RSA correctness
- accelerating RSA decryption
- understanding RSA implementations

---

## 6. Complexity

This educational implementation uses a modular inverse and arithmetic operations. The underlying complexity depends on the integer arithmetic and the modular inverse algorithm.

---

## 7. Security considerations

CRT itself is mathematically sound, but cryptographic implementations must protect CRT computations against side-channel and fault attacks.

In particular, RSA-CRT implementations need appropriate countermeasures against attacks that exploit faulty intermediate results.

This implementation is educational and is not intended for production cryptography.