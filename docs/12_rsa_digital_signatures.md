# RSA Digital Signatures

## 1. Introduction

A digital signature provides a way to verify:

- The authenticity of a message
- The integrity of a message

RSA can be used to create digital signatures using the private key and verify them using the public key.

This document describes the mathematical foundation of textbook RSA digital signatures.

> **Important:** This implementation is educational. Real-world RSA signatures should use secure padding schemes such as RSA-PSS and should normally sign a cryptographic hash of the message rather than the raw message.

---

## 2. RSA Keys

Our educational RSA example uses:

p = 7

q = 11

Therefore:

n = pq

n = 7 × 11

n = 77

Euler's totient is:

φ(n) = (p - 1)(q - 1)

φ(77) = 6 × 10

φ(77) = 60

We choose:

e = 7

because:

gcd(7, 60) = 1

The private exponent satisfies:

ed ≡ 1 (mod φ(n))

Therefore:

7d ≡ 1 (mod 60)

and:

d = 43

The keys are therefore:

Public key = (7, 77)

Private key = (43, 77)

---

## 3. Creating a Signature

In textbook RSA, a signature is created using the private exponent.

The signing equation is:

s ≡ m^d (mod n)

where:

- m = message
- d = private exponent
- n = RSA modulus
- s = digital signature

For our example:

m = 9

d = 43

n = 77

Therefore:

s = 9^43 mod 77

Using repeated squaring:

9^2 ≡ 4 (mod 77)

9^4 ≡ 16 (mod 77)

9^8 ≡ 25 (mod 77)

9^16 ≡ 9 (mod 77)

9^32 ≡ 4 (mod 77)

Since:

43 = 32 + 8 + 2 + 1

we obtain:

9^43 mod 77 = 58

Therefore:

Signature = 58

---

## 4. Verifying a Signature

Signature verification uses the public exponent.

The verification equation is:

m' ≡ s^e (mod n)

If:

m' = m

then the signature is valid.

For our example:

s = 58

e = 7

n = 77

Therefore:

m' = 58^7 mod 77

Using repeated squaring:

58^2 ≡ 53 (mod 77)

58^4 ≡ 37 (mod 77)

Therefore:

58^7 ≡ 58^4 × 58^2 × 58 (mod 77)

58^7 ≡ 37 × 53 × 58 (mod 77)

58^7 ≡ 9 (mod 77)

The recovered message is:

m' = 9

Since:

m' = m

the signature is valid.

---

## 5. Complete Signature Flow

The complete process is:

Message:

9

↓

Sign using private key (43, 77)

↓

Signature:

58

↓

Verify using public key (7, 77)

↓

Recovered message:

9

↓

Valid signature

---

## 6. Message Integrity

A major purpose of digital signatures is detecting message modification.

Suppose the original message is:

m = 9

and its signature is:

s = 58

Verification gives:

58^7 mod 77 = 9

Therefore the signature is valid.

If an attacker changes the message from:

9 → 10

while keeping the signature unchanged:

58^7 mod 77 = 9

The recovered message does not equal 10.

Therefore:

Signature verification = False

This demonstrates the integrity property of digital signatures.

---

## 7. Authentication

The signature is generated using the private key.

Only someone possessing the private key should be able to generate a valid signature.

The corresponding public key can be distributed to others so they can verify the signature.

The basic model is:

Signer:

Message + Private Key → Signature

Verifier:

Message + Signature + Public Key → Valid / Invalid

---

## 8. Security Limitations

The implementation in this project uses textbook RSA signatures for educational purposes.

Textbook RSA signatures should **not** be used in production systems.

Important limitations include:

- No cryptographic hash function
- No secure signature padding
- Small demonstration parameters
- Vulnerability to practical attacks when used without appropriate padding

Real RSA signature systems should use secure constructions such as:

RSA-PSS

and should normally hash the message before signing.

For example:

Message

↓

SHA-256

↓

Message digest

↓

RSA-PSS

↓

Signature

---

## 9. Connection to Hash Functions

In practical digital signature systems, the entire message is generally not signed directly.

Instead, a cryptographic hash function such as SHA-256 produces a fixed-size digest.

Conceptually:

digest = SHA-256(message)

The digest is then incorporated into a secure RSA signature scheme.

This provides efficient processing of large messages and helps prevent attacks against naïve signature constructions.

---

## 10. Complexity

Signature creation and verification rely on modular exponentiation.

The implementation uses the fast modular exponentiation algorithm based on repeated squaring.

The number of modular multiplication steps grows approximately logarithmically with the exponent.

RSA signing with the private exponent is generally more computationally expensive than verification with the public exponent when a small public exponent is used.

---

## 11. Summary

Our educational example demonstrates:

p = 7

q = 11

n = 77

φ(n) = 60

e = 7

d = 43

Public key = (7, 77)

Private key = (43, 77)

Message = 9

Signature = 58

Verification:

58^7 mod 77 = 9

Therefore:

Signature = Valid

The implementation demonstrates the mathematical relationship between:

- RSA private-key operations
- RSA public-key operations
- Modular exponentiation
- Digital signatures
- Message integrity
- Authentication

This implementation is intended for educational purposes and is not suitable for production cryptographic systems.