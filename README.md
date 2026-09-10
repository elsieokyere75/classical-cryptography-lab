# Classical to Post-Quantum Cryptography Lab

A research-oriented cryptography learning and implementation project exploring the mathematical foundations, implementation, testing, and security assumptions of classical and post-quantum cryptographic systems.

The project began with number-theoretic foundations and classical public-key cryptography and has progressively moved toward post-quantum cryptography, with particular emphasis on lattice-based constructions, Learning With Errors (LWE), Module-LWE, and the mathematical foundations underlying ML-KEM.

> **Educational purpose:** The implementations in this repository are designed for learning, experimentation, and research preparation. They are not production cryptographic implementations and should not be used to protect real-world data.

---

## Research Motivation

Public-key infrastructure currently relies heavily on cryptographic systems such as RSA and elliptic-curve cryptography.

Large-scale fault-tolerant quantum computers would threaten the mathematical assumptions underlying RSA, Diffie-Hellman, ECDH, and ECDSA through algorithms such as Shor's algorithm.

This project therefore follows the progression:

```text
Mathematical Foundations
        ↓
Classical Public-Key Cryptography
        ↓
Key Exchange and Digital Signatures
        ↓
Symmetric Cryptography and Hashing
        ↓
Quantum Threat Analysis
        ↓
Lattice Foundations
        ↓
Learning With Errors (LWE)
        ↓
Module-LWE
        ↓
Educational ML-KEM Model
```

The broader research interest is understanding how existing cryptographic and Public Key Infrastructure (PKI) systems can transition toward post-quantum security.

---

## Implemented Topics

### Number Theory

The repository includes implementations and tests covering foundational mathematics used throughout cryptography, including:

- prime numbers
- Sieve of Eratosthenes
- greatest common divisor
- extended Euclidean algorithm
- modular inverse
- Fermat's Little Theorem
- Euler's totient function and Euler's theorem
- fast modular exponentiation
- Chinese Remainder Theorem

These foundations are subsequently applied to public-key cryptographic algorithms.

---

### RSA

Implemented educational RSA functionality including:

- key generation
- encryption
- decryption
- digital signatures
- modular arithmetic underlying RSA

The implementation is intended to expose the mathematics behind RSA rather than provide production cryptography.

The project also examines RSA's dependence on the difficulty of integer factorization and the implications of Shor's algorithm for RSA-based PKI.

---

### Elliptic Curve Cryptography

Implemented elliptic-curve arithmetic over a small educational finite field, including:

- point validation
- point addition
- point doubling
- point negation
- scalar multiplication
- point at infinity handling

These operations provide the mathematical foundation for the ECDH and ECDSA implementations in the repository.

---

### Diffie-Hellman and ECDH

Implemented educational versions of:

- finite-field Diffie-Hellman
- Elliptic Curve Diffie-Hellman (ECDH)

These implementations demonstrate how two parties can derive common secret material over an insecure communication channel.

The project also examines why discrete-logarithm-based key establishment is vulnerable to sufficiently capable quantum computers.

---

### ECDSA

Implemented an educational Elliptic Curve Digital Signature Algorithm model covering:

- private/public key relationships
- signature generation
- signature verification
- nonce requirements
- nonce reuse risks

The implementation demonstrates the mathematical relationship between elliptic-curve arithmetic and digital signatures.

---

### SHA-256

Implemented SHA-256 from its internal mathematical and bitwise operations rather than simply wrapping a hashing library.

The implementation explores:

- message padding
- message schedule generation
- compression rounds
- bitwise functions
- digest generation
- known-answer testing
- preimage and collision resistance

---

### AES-128

Implemented an educational AES-128 encryption model including:

- state representation
- SubBytes
- ShiftRows
- MixColumns
- AddRoundKey
- AES-128 key expansion
- finite-field arithmetic in GF(2^8)
- 10-round AES-128 encryption
- standard known-answer testing

The current implementation focuses on educational single-block AES-128 encryption and is not intended to replace authenticated production modes such as AES-GCM.

---

# Post-Quantum Cryptography

## Quantum Threat

The project studies the effect of quantum algorithms on classical cryptography.

### Shor's Algorithm

A sufficiently capable fault-tolerant quantum computer running Shor's algorithm would threaten:

- RSA
- finite-field Diffie-Hellman
- ECDH
- ECDSA

because their security relies on integer factorization or discrete-logarithm problems.

### Grover's Algorithm

Grover's algorithm provides a quadratic speedup for generic search problems.

This affects the security margins of symmetric cryptography and hash functions differently from Shor's impact on public-key cryptography.

---

## Lattice Foundations

The PQC section begins by studying lattice mathematics, including:

- lattice bases
- integer combinations of basis vectors
- Euclidean norms
- shortest-vector intuition
- transition from geometric lattices to LWE-based cryptography

This provides mathematical intuition for lattice-based post-quantum constructions.

---

## Learning With Errors (LWE)

Implemented a small educational LWE model based on:

\[
b = \langle a,s\rangle + e \pmod q
\]

where:

- \(a\) is public,
- \(s\) is secret,
- \(e\) is a small error,
- \(q\) is a modulus.

The implementation demonstrates how deliberately introduced error changes the structure from an exact linear system into the type of noisy relation studied in LWE cryptography.

---

## Module-LWE

The project extends the LWE intuition to a simplified Module-LWE-style relationship:

\[
\mathbf{t}=A\mathbf{s}+\mathbf{e}\pmod q
\]

where:

- \(A\) is public,
- \(\mathbf{s}\) is secret,
- \(\mathbf{e}\) is a small error vector,
- \(\mathbf{t}\) is public.

The current implementation uses small integer matrices for transparency and manual verification.

Standardized lattice cryptography instead operates over structured polynomial rings with carefully selected parameters and sampling procedures.

---

## Educational ML-KEM Model

Building on the LWE and Module-LWE work, the repository contains an educational model of the three high-level ML-KEM operations:

```text
KeyGen → Encaps → Decaps
```

### Key Generation

The model demonstrates the Module-LWE-style relationship:

\[
\mathbf{t}=A\mathbf{s}+\mathbf{e}\pmod q
\]

and separates public encapsulation information from secret decapsulation information.

### Encapsulation

The educational encapsulation model demonstrates relationships including:

\[
\mathbf{u}=A^T\mathbf{r}+\mathbf{e}_1\pmod q
\]

together with a second ciphertext component constructed from public information, a temporary secret, error, and toy message material.

### Decapsulation

The educational decapsulation model demonstrates how secret information can be used with ciphertext components to recover the corresponding toy message material.

### Important Limitation

This is **not a FIPS 203-compliant implementation of ML-KEM**.

It intentionally omits many security-critical components of standardized ML-KEM, including full polynomial-ring arithmetic, standardized sampling, NTT operations, compression, encoding, hashing, key derivation, ciphertext validation, deterministic re-encryption checks, implicit rejection, and constant-time implementation considerations.

The purpose is to understand the mathematical progression from Module-LWE to a KEM architecture before studying a standards-compliant implementation.

---

## Testing

The repository uses `pytest` for automated testing.

Current full test suite:

```text
188 passed
```

Run all tests with:

```bash
python -m pytest
```

Individual cryptographic components also contain targeted tests covering expected outputs, edge cases, invalid inputs, and mathematical properties.

---

## Repository Structure

```text
classical-cryptography-lab/
│
├── docs/
│   ├── number theory documentation
│   ├── RSA documentation
│   ├── ECC documentation
│   ├── Diffie-Hellman / ECDH documentation
│   ├── ECDSA documentation
│   ├── SHA-256 documentation
│   ├── AES documentation
│   ├── LWE / Module-LWE documentation
│   └── educational ML-KEM documentation
│
├── src/
│   ├── number_theory/
│   ├── rsa/
│   ├── ecc/
│   ├── diffie_hellman/
│   ├── ecdh/
│   ├── ecdsa/
│   ├── sha256/
│   ├── aes/
│   └── pqc/
│       ├── lwe.py
│       ├── ml_kem_keygen.py
│       ├── ml_kem_encaps.py
│       └── ml_kem_decaps.py
│
├── tests/
│   ├── number_theory/
│   ├── rsa/
│   ├── ecc/
│   ├── diffie_hellman/
│   ├── ecdh/
│   ├── ecdsa/
│   ├── sha256/
│   ├── aes/
│   └── pqc/
│
└── README.md
```

---

## Research Direction

This repository forms part of an independent research preparation project focused on the transition from classical to post-quantum cryptography.

Future work will focus on:

- deeper analysis of standardized ML-KEM
- polynomial-ring arithmetic used in lattice cryptography
- ML-KEM parameter and performance analysis
- post-quantum digital signatures
- ML-DSA
- classical vs post-quantum performance benchmarking
- hybrid classical/post-quantum cryptographic deployment
- migration of PKI systems from RSA/ECC toward post-quantum cryptography
- implications of PQC for digital identity and certificate infrastructures

A particular area of interest is the operational migration of existing PKI environments to post-quantum and hybrid cryptographic systems while maintaining interoperability, trust, certificate lifecycle management, and security.

---

## Project Status

**Current stage:** Post-quantum cryptography foundations and educational ML-KEM analysis.

Completed progression:

```text
Number Theory
    ↓
RSA
    ↓
ECC
    ↓
Diffie-Hellman
    ↓
ECDH
    ↓
ECDSA
    ↓
SHA-256
    ↓
AES-128
    ↓
Quantum Threat Analysis
    ↓
Lattice Foundations
    ↓
LWE
    ↓
Module-LWE
    ↓
Educational ML-KEM KeyGen / Encaps / Decaps
```

The next phase focuses on deeper ML-KEM analysis, post-quantum signatures, benchmarking, and PKI migration research.

---

## Author

**Elsie Okyere**

PKI & Network Systems Administrator  
Cybersecurity and Cryptography Research Interest

Research interests include:

- Post-Quantum Cryptography
- Applied Cryptography
- Lattice-Based Cryptography
- Public Key Infrastructure
- Cryptographic Key Management
- Digital Identity and Authentication
- Security Protocols