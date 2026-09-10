# Learning With Errors (LWE) and Module-LWE

## 1. Introduction

Learning With Errors (LWE) is a mathematical problem used as a foundation for many post-quantum cryptographic constructions.

The central idea is to hide a secret inside linear equations by deliberately adding small random errors.

A simplified LWE relation is:

\[
b = \langle a, s \rangle + e \pmod q
\]

where:

- \(a\) is public,
- \(s\) is secret,
- \(e\) is a small error term,
- \(q\) is the modulus,
- \(b\) is the public noisy result.

Without the error term, enough linear equations could normally be solved using ordinary linear algebra. The introduction of carefully chosen noise makes recovery of the secret computationally difficult for appropriate cryptographic parameters.

---

## 2. Simple LWE Example

Let:

\[
a = (2,3)
\]

\[
s = (1,2)
\]

\[
e = 1
\]

and:

\[
q = 7
\]

First compute the dot product:

\[
\langle a,s\rangle
=
(2)(1)+(3)(2)
=
8
\]

Add the error:

\[
8+1=9
\]

Reduce modulo 7:

\[
9 \bmod 7 = 2
\]

Therefore:

\[
\boxed{b=2}
\]

---

## 3. From LWE to Module-LWE

Module-LWE extends the LWE idea by working with vectors and matrices whose elements may belong to polynomial rings.

A conceptual relationship is:

\[
\mathbf t=A\mathbf s+\mathbf e \pmod q
\]

where:

- \(A\) is a public matrix,
- \(\mathbf s\) is the secret vector,
- \(\mathbf e\) is a small error vector,
- \(\mathbf t\) is the public noisy result.

In real Module-LWE constructions, the elements are normally polynomials in a structured ring rather than simple integers.

---

## 4. Educational Matrix Example

Consider:

\[
A=
\begin{bmatrix}
1 & 2\\
3 & 1
\end{bmatrix}
\]

and:

\[
\mathbf s=
\begin{bmatrix}
2\\
1
\end{bmatrix}
\]

with:

\[
\mathbf e=
\begin{bmatrix}
1\\
-1
\end{bmatrix}
\]

and:

\[
q=7
\]

First calculate:

\[
A\mathbf s
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

Add the error:

\[
A\mathbf s+\mathbf e
=
\begin{bmatrix}
5\\
6
\end{bmatrix}
\]

Therefore:

\[
\boxed{\mathbf t=[5,6]}
\]

---

## 5. Polynomial Rings

Module-LWE constructions use polynomial rings such as:

\[
R_q=\mathbb Z_q[x]/(x^n+1)
\]

This means:

- coefficients are reduced modulo \(q\),
- polynomial degree is reduced using the relation:

\[
x^n=-1
\]

For example, in the toy ring:

\[
R_7=\mathbb Z_7[x]/(x^2+1)
\]

we have:

\[
x^2=-1 \equiv 6 \pmod 7
\]

---

## 6. Connection to ML-KEM

ML-KEM is a standardized post-quantum key encapsulation mechanism based on structured lattice mathematics related to Module-LWE.

The high-level workflow is:

\[
\text{KeyGen}
\rightarrow
\text{Encaps}
\rightarrow
\text{Decaps}
\]

The public-key structure contains noisy algebraic relationships derived from secret values.

A conceptual relationship studied in this project is:

\[
\mathbf t=A\mathbf s+\mathbf e
\]

where the secret vector \(\mathbf s\) must remain hidden even though \(A\) and \(\mathbf t\) are public.

---

## 7. Implementation

The educational Python implementation is located at:

```text
src/pqc/lwe.py