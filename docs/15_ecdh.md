# Elliptic Curve Diffie-Hellman (ECDH)

## 1. Introduction

Elliptic Curve Diffie-Hellman (ECDH) is a key-agreement method based
on elliptic-curve scalar multiplication.

It allows two parties to independently derive the same shared point
without transmitting their private scalars.

This implementation is educational and uses a very small elliptic
curve.

---

## 2. Elliptic Curve

This project uses the curve:

y^2 ≡ x^3 + 2x + 2 (mod 17)

Therefore:

a = 2
b = 2
p = 17

The base point is:

G = (5, 1)

---

## 3. Private Keys

Alice chooses:

a_private = 5

Bob chooses:

b_private = 7

These values must remain secret.

---

## 4. Public Keys

Alice calculates:

A = a_private * G

Therefore:

A = 5G = (9, 16)

Bob calculates:

B = b_private * G

Therefore:

B = 7G = (0, 6)

The public points A and B can be exchanged.

---

## 5. Shared Point

Alice receives Bob's public point and computes:

S_A = a_private * B

Therefore:

S_A = 5(0, 6)

S_A = (10, 11)

Bob receives Alice's public point and computes:

S_B = b_private * A

Therefore:

S_B = 7(9, 16)

S_B = (10, 11)

Thus:

S_A = S_B = (10, 11)

Both parties independently derive the same elliptic-curve point.

---

## 6. Why the Shared Points Match

Alice's public key is:

A = aG

Bob's public key is:

B = bG

Alice computes:

aB = a(bG)

which gives:

abG

Bob computes:

bA = b(aG)

which also gives:

abG

Therefore:

aB = bA

This is the elliptic-curve analogue of the mathematical relationship
used in finite-field Diffie-Hellman.

---

## 7. Connection to Diffie-Hellman

Finite-field Diffie-Hellman uses modular exponentiation:

A = g^a mod p

B = g^b mod p

ECDH replaces this operation with elliptic-curve scalar multiplication:

A = aG

B = bG

The key-agreement idea remains the same, but the underlying group and
hardness assumption are different.

---

## 8. Security Assumption

ECDH relies on the difficulty of elliptic-curve discrete logarithm
problems for appropriately selected cryptographic curves and
parameters.

Given:

G

and:

A = aG

recovering the private scalar a from G and A should be computationally
difficult for suitable classical cryptographic parameters.

The tiny curve in this project provides no real security.

---

## 9. Public-Key Validation

An implementation should validate received public points before using
them.

This educational implementation checks that a public point:

- is not the point at infinity
- lies on the expected curve

Production implementations require stronger validation appropriate to
the chosen curve and protocol.

---

## 10. Shared Secret Derivation

This project exposes the complete shared point:

S = (x, y)

A production protocol would not normally use the raw point directly as
an encryption key.

A key-derivation function is typically applied to suitable shared
secret material to derive cryptographic keys.

---

## 11. Authentication

ECDH by itself provides key agreement but does not authenticate the
participants.

Without authentication, an active attacker may be able to perform a
man-in-the-middle attack.

Real protocols therefore combine ECDH with authentication mechanisms
such as digital signatures or authenticated protocol designs.

---

## 12. Quantum Computing

ECDH depends on elliptic-curve discrete-logarithm assumptions.

A sufficiently capable fault-tolerant quantum computer running Shor's
algorithm would break conventional elliptic-curve discrete logarithm
cryptography.

Therefore ECDH is not considered post-quantum secure.

---

## 13. Security Limitations

This implementation is educational only.

It uses:

- a tiny elliptic curve
- tiny private scalars
- simplified point validation
- no authentication
- no key-derivation function
- non-constant-time Python arithmetic
- no side-channel protections

It must not be used to protect real data.