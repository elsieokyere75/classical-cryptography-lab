# RSA Mathematics

## 1. Introduction

RSA is a public-key cryptosystem based on modular arithmetic and the difficulty of factoring large composite integers.

The RSA construction uses:

- Prime numbers
- Euler's totient function
- Greatest common divisor
- Modular inverses
- Modular exponentiation
- Chinese Remainder Theorem

This document develops the mathematics behind RSA before implementing it in Python.

---

## 2. Key Generation

RSA begins by selecting two distinct prime numbers:

p and q

For our educational example:

p = 7
q = 11

### Calculate n

The modulus is:

n = pq

Therefore:

n = 7 × 11 = 77

So:

n = 77

---

## 3. Euler's Totient

For two distinct primes:

φ(n) = (p - 1)(q - 1)

Therefore:

φ(77) = (7 - 1)(11 - 1)

φ(77) = 6 × 10

φ(77) = 60

---

## 4. Choosing the Public Exponent

The public exponent e must satisfy:

1 < e < φ(n)

and:

gcd(e, φ(n)) = 1

For this example:

e = 7

We verify:

gcd(7, 60) = 1

Therefore e = 7 is valid.

---

## 5. Calculating the Private Exponent

The private exponent d is the modular inverse of e modulo φ(n):

ed ≡ 1 (mod φ(n))

For our example:

7d ≡ 1 (mod 60)

The solution is:

d = 43

because:

7 × 43 = 301

and:

301 = 1 + 5 × 60

Therefore:

7 × 43 ≡ 1 (mod 60)

---

## 6. RSA Keys

The public key is:

(e, n)

Therefore:

Public key = (7, 77)

The private key is:

(d, n)

Therefore:

Private key = (43, 77)

---

## 7. Encryption

To encrypt a message m:

c ≡ m^e (mod n)

For our example, choose:

m = 9

Therefore:

c ≡ 9^7 (mod 77)

Using modular exponentiation:

9^2 ≡ 4 (mod 77)

9^4 ≡ 16 (mod 77)

Since:

7 = 4 + 2 + 1

we calculate:

9^7 ≡ 9^4 × 9^2 × 9 (mod 77)

9^7 ≡ 16 × 4 × 9 (mod 77)

9^7 ≡ 37 (mod 77)

Therefore:

c = 37

---

## 8. Decryption

To decrypt:

m ≡ c^d (mod n)

For our example:

m ≡ 37^43 (mod 77)

Since:

43 = 32 + 8 + 2 + 1

we use repeated squaring.

The relevant values are:

37^2 ≡ 60 (mod 77)

37^4 ≡ 58 (mod 77)

37^8 ≡ 53 (mod 77)

37^16 ≡ 37 (mod 77)

37^32 ≡ 60 (mod 77)

Therefore:

37^43
= 37^32 × 37^8 × 37^2 × 37

modulo 77:

= 60 × 53 × 60 × 37

≡ 9 (mod 77)

Therefore:

m = 9

The original message is recovered.

---

## 9. Why RSA Works

The private exponent is chosen such that:

ed ≡ 1 (mod φ(n))

Therefore, for appropriate messages:

ed = 1 + kφ(n)

Then:

m^ed = m^(1 + kφ(n))

= m(m^φ(n))^k

Euler's theorem states that if:

gcd(m, n) = 1

then:

m^φ(n) ≡ 1 (mod n)

Therefore:

m^ed ≡ m (mod n)

This explains why decryption recovers the original message.

For a complete proof that handles messages not relatively prime to n, the Chinese Remainder Theorem can be applied separately modulo p and q.

---

## 10. Chinese Remainder Theorem and RSA

RSA uses:

n = pq

where p and q are distinct primes.

Since:

gcd(p, q) = 1

the Chinese Remainder Theorem allows computations modulo p and q to be performed separately and recombined modulo n.

This is useful for:

- proving RSA correctness
- accelerating RSA decryption
- understanding RSA-CRT implementations

---

## 11. Security Assumption

The security of RSA is based on the difficulty of problems related to factoring large composite integers and computing the RSA inverse without the private information.

The educational values used in this project are intentionally tiny and are completely insecure.

Real RSA requires:

- very large parameters
- cryptographically secure random generation
- secure padding
- side-channel protections
- carefully reviewed implementations

This implementation is for educational purposes only.

---

## 12. Complexity

RSA operations involve modular exponentiation.

The fast modular exponentiation algorithm reduces the number of multiplications needed to compute:

a^b mod n

from a linear number of exponent steps to approximately logarithmic depth in the exponent.

RSA key generation also requires prime generation, primality testing, and modular inversion.

CRT can significantly reduce the cost of RSA private-key operations by replacing one large modular exponentiation with smaller computations modulo p and q.

---

## 13. Summary

Our educational RSA example:

p = 7
q = 11

n = 77

φ(n) = 60

e = 7

d = 43

Public key:

(7, 77)

Private key:

(43, 77)

Message:

9

Ciphertext:

37

Decryption:

37^43 mod 77 = 9

Therefore:

9 → 37 → 9

The original message is successfully recovered.