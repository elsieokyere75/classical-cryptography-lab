# Diffie-Hellman Key Exchange

## 1. Introduction

Diffie-Hellman is a key-exchange method that allows two parties to
establish a shared secret over a public communication channel.

The shared secret is derived independently by both parties and is
never transmitted directly.

This implementation is educational and uses very small parameters.

---

## 2. Public Parameters

Alice and Bob publicly agree on:

- a prime modulus p
- a suitable generator g

For our example:

p = 23

g = 5

These values do not need to be secret.

---

## 3. Private Keys

Alice chooses a private value:

a = 6

Bob chooses a private value:

b = 15

The private values must remain secret.

---

## 4. Public Keys

Alice computes:

A = g^a mod p

Using our example:

A = 5^6 mod 23

A = 8

Bob computes:

B = g^b mod p

Therefore:

B = 5^15 mod 23

B = 19

Alice and Bob can exchange A and B publicly.

---

## 5. Shared Secret

After receiving Bob's public value, Alice calculates:

S = B^a mod p

Therefore:

S = 19^6 mod 23

S = 2

Bob calculates:

S = A^b mod p

Therefore:

S = 8^15 mod 23

S = 2

Both parties therefore obtain the same shared secret:

S = 2

---

## 6. Why the Shared Secrets Match

Alice computes:

B^a mod p

Since:

B = g^b mod p

Alice effectively computes:

(g^b)^a = g^(ab) mod p

Bob computes:

A^b mod p

Since:

A = g^a mod p

Bob effectively computes:

(g^a)^b = g^(ab) mod p

Therefore both obtain:

g^(ab) mod p

---

## 7. Discrete Logarithm Problem

An observer can know:

p

g

A = g^a mod p

B = g^b mod p

but does not directly know a or b.

Recovering a from:

g^a = A mod p

is an instance of the discrete logarithm problem.

With the tiny parameters used in this project, an attacker can recover
the private values easily by brute force.

Real cryptographic systems require carefully selected large parameters.

---

## 8. Fast Modular Exponentiation

Diffie-Hellman requires calculations such as:

g^a mod p

For large exponents, directly calculating g^a is inefficient.

This project therefore reuses the fast modular exponentiation
implementation from the number-theory module.

The repeated-squaring algorithm requires approximately O(log a)
modular multiplication steps rather than performing a multiplications.

---

## 9. Man-in-the-Middle Attack

Basic Diffie-Hellman provides key agreement but does not authenticate
the participants.

An active attacker can potentially intercept the communication,
establish one shared secret with Alice and another with Bob, and relay
messages between them.

Therefore, practical key-exchange protocols combine key agreement with
authentication mechanisms.

---

## 10. Connection to Elliptic Curves

Traditional finite-field Diffie-Hellman uses:

A = g^a mod p

Elliptic Curve Diffie-Hellman uses scalar multiplication instead:

A = aG

where G is a public elliptic-curve base point.

The underlying idea remains similar:

1. Alice chooses a private scalar.
2. Bob chooses a private scalar.
3. Each computes a public value.
4. They exchange public values.
5. Each derives the same shared secret.

This connection will be explored in the ECDH implementation.

---

## 11. Quantum Computing

The security of conventional finite-field Diffie-Hellman relies on
discrete-logarithm assumptions.

A sufficiently capable fault-tolerant quantum computer running Shor's
algorithm could solve the relevant discrete logarithm problems
efficiently.

Therefore conventional Diffie-Hellman is not considered
post-quantum secure.

This provides another motivation for studying post-quantum
cryptographic key-establishment mechanisms.

---

## 12. Security Limitations

This implementation is for education only.

It uses:

- tiny parameters
- user-supplied private values
- simplified parameter validation
- no authentication
- no key-derivation function
- no constant-time guarantees
- no side-channel protections

The raw shared integer produced by this implementation should not be
treated directly as a production encryption key.

The implementation must not be used to protect real data.