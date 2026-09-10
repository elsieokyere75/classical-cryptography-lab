# Educational ML-KEM Model

## 1. Introduction

ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism) is a
post-quantum key-encapsulation mechanism standardized by NIST.

It is designed to allow two parties to establish shared secret key
material over an insecure communication channel while providing
security against both classical and quantum adversaries under its
underlying security assumptions.

ML-KEM is derived from CRYSTALS-Kyber and is based on structured
lattice cryptography, with security closely connected to the
Module Learning With Errors (Module-LWE) problem.

This repository implements an **educational model** showing how
Module-LWE-style mathematics can lead to the three high-level
operations:

1. Key Generation (KeyGen)
2. Encapsulation (Encaps)
3. Decapsulation (Decaps)

This implementation is intended for learning and research preparation.

**It is not a FIPS 203-compliant implementation and must not be used
for production cryptography.**

---

## 2. From LWE to ML-KEM

The Learning With Errors (LWE) problem can be introduced using:

\[
b = \langle a,s\rangle + e \pmod q
\]

where:

- \(a\) is public,
- \(s\) is secret,
- \(e\) is a small error term,
- \(q\) is the modulus,
- \(b\) is the resulting public value.

The error term prevents the problem from being treated as a simple
system of exact linear equations.

Module-LWE extends this idea to vectors whose components are elements
of a polynomial ring.

A useful conceptual form is:

\[
\mathbf{t}=A\mathbf{s}+\mathbf{e}\pmod q
\]

where:

- \(A\) is a public matrix,
- \(\mathbf{s}\) is a secret vector,
- \(\mathbf{e}\) is a small error vector,
- \(\mathbf{t}\) is public information.

The educational ML-KEM model in this repository builds on this
relationship.

---

## 3. Polynomial Ring Used by ML-KEM

Standardized ML-KEM operates using polynomial arithmetic in the ring:

\[
R_q=\mathbb{Z}_{3329}[x]/(x^{256}+1)
\]

This means that polynomial coefficients are reduced modulo:

\[
q=3329
\]

and polynomial degrees are reduced using:

\[
x^{256}=-1
\]

The educational implementation in this repository does **not**
implement the full polynomial ring used by ML-KEM.

Instead, ordinary integer matrices and vectors are used to make the
underlying Module-LWE relationships easier to inspect and understand.

---

## 4. ML-KEM Parameter Sets

ML-KEM defines three parameter sets:

| Parameter Set | Module Rank \(k\) |
|---|---:|
| ML-KEM-512 | 2 |
| ML-KEM-768 | 3 |
| ML-KEM-1024 | 4 |

All three use:

\[
n=256
\]

and:

\[
q=3329
\]

Increasing the parameter set increases the targeted security strength,
while also increasing key and ciphertext sizes and computational cost.

The educational examples in this repository use small \(2\times2\)
matrices because they provide an intuitive bridge to the module
dimension used by ML-KEM-512.

The toy parameters used here are not ML-KEM-512 parameters.

---

# 5. Key Generation

The first stage is key generation.

At the conceptual Module-LWE level, the central relationship is:

\[
\mathbf{t}=A\mathbf{s}+\mathbf{e}\pmod q
\]

The educational example uses:

\[
A=
\begin{bmatrix}
1 & 2\\
3 & 1
\end{bmatrix}
\]

with secret:

\[
\mathbf{s}=
\begin{bmatrix}
2\\
1
\end{bmatrix}
\]

error:

\[
\mathbf{e}=
\begin{bmatrix}
1\\
-1
\end{bmatrix}
\]

and modulus:

\[
q=7
\]

First calculate:

\[
A\mathbf{s}
=
\begin{bmatrix}
1(2)+2(1)\\
3(2)+1(1)
\end{bmatrix}
=
\begin{bmatrix}
4\\
7
\end{bmatrix}
\]

Then add the error:

\[
A\mathbf{s}+\mathbf{e}
=
\begin{bmatrix}
4\\
7
\end{bmatrix}
+
\begin{bmatrix}
1\\
-1
\end{bmatrix}
=
\begin{bmatrix}
5\\
6
\end{bmatrix}
\]

Therefore:

\[
\boxed{
\mathbf{t}=
\begin{bmatrix}
5\\
6
\end{bmatrix}
}
\]

The educational implementation represents the encapsulation key as:

```text
(A, t)
```

while the secret vector:

```text
s
```

is retained as the educational decapsulation secret.

Implementation:

```text
src/pqc/ml_kem_keygen.py
```

---

# 6. Encapsulation

The encapsulation operation represents the sender using the
recipient's public information to construct a ciphertext and shared
secret material.

In the educational model, the sender chooses a temporary secret:

\[
\mathbf{r}
\]

and error values.

One of the central calculations is:

\[
\mathbf{u}=A^T\mathbf{r}+\mathbf{e}_1\pmod q
\]

For the example:

\[
A=
\begin{bmatrix}
1 & 2\\
3 & 1
\end{bmatrix}
\]

therefore:

\[
A^T=
\begin{bmatrix}
1 & 3\\
2 & 1
\end{bmatrix}
\]

Let:

\[
\mathbf{r}=
\begin{bmatrix}
1\\
1
\end{bmatrix}
\]

Then:

\[
A^T\mathbf{r}
=
\begin{bmatrix}
1(1)+3(1)\\
2(1)+1(1)
\end{bmatrix}
=
\begin{bmatrix}
4\\
3
\end{bmatrix}
\]

Using:

\[
\mathbf{e}_1=
\begin{bmatrix}
0\\
1
\end{bmatrix}
\]

gives:

\[
\mathbf{u}=
\begin{bmatrix}
4\\
4
\end{bmatrix}
\pmod 7
\]

The educational model also computes:

\[
v=\langle\mathbf{t},\mathbf{r}\rangle+e_2+m\pmod q
\]

where \(m\) represents toy message material.

Using:

\[
\mathbf{t}=[5,6]
\]

\[
\mathbf{r}=[1,1]
\]

\[
e_2=0
\]

and:

\[
m=1
\]

we obtain:

\[
\langle\mathbf{t},\mathbf{r}\rangle
=
5(1)+6(1)
=
11
\]

Therefore:

\[
v=11+0+1=12
\]

and:

\[
12\bmod7=5
\]

The resulting educational ciphertext is:

\[
\boxed{c=([4,4],5)}
\]

Implementation:

```text
src/pqc/ml_kem_encaps.py
```

---

# 7. Decapsulation

The receiver uses secret information together with the ciphertext to
recover the encoded message material.

The simplified educational calculation is:

\[
m'=v-\langle\mathbf{s},\mathbf{u}\rangle\pmod q
\]

For a clean educational example, use:

\[
\mathbf{s}=[2,1]
\]

\[
\mathbf{u}=[4,3]
\]

and:

\[
v=5
\]

Then:

\[
\langle\mathbf{s},\mathbf{u}\rangle
=
2(4)+1(3)
=
11
\]

Therefore:

\[
m'=5-11=-6
\]

and:

\[
-6\bmod7=1
\]

so:

\[
\boxed{m'=1}
\]

which matches the original toy message material.

Implementation:

```text
src/pqc/ml_kem_decaps.py
```

---

# 8. KeyGen → Encaps → Decaps

The high-level KEM workflow can be represented as:

```text
                 Alice
                   |
                KeyGen
                   |
             +-----+-----+
             |           |
            ek          dk
          public       secret
             |
             |------------------------>
             |                         Bob
             |                         |
             |                      Encaps
             |                         |
             |                    +----+----+
             |                    |         |
             |                    K         c
             |                  keeps       |
             |                              |
             |<-----------------------------|
             |
          Decaps
             |
             K'

                  K' = K
```

The sender transmits the ciphertext:

\[
\boxed{c}
\]

but does not transmit the shared secret:

\[
\boxed{K}
\]

The recipient uses the decapsulation key and ciphertext to derive the
corresponding shared secret.

---

# 9. Relationship to Classical Key Establishment

Earlier parts of this repository implemented classical key
establishment mechanisms including Diffie-Hellman and Elliptic Curve
Diffie-Hellman.

Their security depends on discrete-logarithm problems.

A sufficiently capable fault-tolerant quantum computer running Shor's
algorithm would threaten these assumptions.

ML-KEM is designed for the post-quantum setting and relies on
module-lattice-based hardness assumptions rather than integer
factorization or discrete logarithms.

This creates the progression:

\[
\text{DH/ECDH}
\rightarrow
\text{Quantum Threat}
\rightarrow
\text{Lattices}
\rightarrow
\text{LWE}
\rightarrow
\text{Module-LWE}
\rightarrow
\text{ML-KEM}
\]

---

# 10. Implementation Structure

The educational PQC implementation currently includes:

```text
src/pqc/
    lwe.py
    ml_kem_keygen.py
    ml_kem_encaps.py
    ml_kem_decaps.py
```

Tests include:

```text
tests/pqc/
    test_lwe.py
    test_ml_kem_keygen.py
    test_ml_kem_encaps.py
    test_ml_kem_decaps.py
```

The repository currently passes:

```text
188 tests
```

This provides regression testing across both the classical
cryptography implementations and the current PQC educational work.

---

# 11. Security Assumptions and Limitations

This implementation is strictly educational.

It is **not a complete or standards-compliant implementation of
ML-KEM**.

Among other differences, the educational implementation does not
implement the full standardized:

- polynomial-ring arithmetic,
- Number Theoretic Transform (NTT),
- pseudorandom matrix generation,
- noise sampling procedures,
- encoding and decoding,
- compression and decompression,
- hashing,
- key derivation,
- ciphertext validation,
- deterministic re-encryption checks,
- implicit rejection,
- standardized parameter handling,
- constant-time implementation requirements.

The small values used in the examples are intentionally chosen for
manual inspection and are cryptographically insecure.

The functions in this repository must therefore **never be used to
protect real data or establish production cryptographic keys**.

Production ML-KEM should use a vetted implementation that conforms to
the relevant standard and has undergone appropriate security review.

---

# 12. Research Relevance

This implementation forms part of a broader progression from
classical cryptography toward post-quantum cryptography.

The project has developed through:

\[
\text{Number Theory}
\rightarrow
\text{RSA}
\rightarrow
\text{ECC}
\rightarrow
\text{DH}
\rightarrow
\text{ECDH}
\rightarrow
\text{ECDSA}
\rightarrow
\text{SHA-256}
\rightarrow
\text{AES}
\]

followed by:

\[
\text{Quantum Threat}
\rightarrow
\text{Lattice Foundations}
\rightarrow
\text{LWE}
\rightarrow
\text{Module-LWE}
\rightarrow
\text{Educational ML-KEM Model}
\]

The purpose is not merely to reproduce cryptographic algorithms, but
to understand the mathematical assumptions, implementation structure,
security properties, limitations, and transition from classical to
post-quantum cryptography.

Future work can extend this foundation through:

- deeper analysis of standardized ML-KEM,
- polynomial-ring implementation,
- ML-KEM parameter analysis,
- benchmarking of classical and post-quantum schemes,
- ML-DSA study,
- PKI migration analysis,
- hybrid classical/post-quantum deployment considerations.

---

# 13. Conclusion

The educational ML-KEM model demonstrates how concepts introduced
through LWE and Module-LWE can develop into a key-encapsulation
workflow.

The implementation separates the process into:

\[
\boxed{\text{KeyGen} \rightarrow \text{Encaps} \rightarrow \text{Decaps}}
\]

while explicitly distinguishing simplified educational mathematics
from standardized production cryptography.

This provides a foundation for further study of ML-KEM and the broader
transition from classical public-key cryptography to post-quantum
cryptography.