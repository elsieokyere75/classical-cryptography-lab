## Euler's Totient Function and Euler's Theorem

**Author:** Elsie Okyere  
**Project:** Classical Cryptography Laboratory  
**Date Started:** June 2026
---------
## 1. Euler's Totient Function

Euler's totient function, written as $\phi(n)$, counts the positive integers from
1 through $n$ that are relatively prime to $n$.

In other words:

$$
\phi(n) = |{k \in {1,\ldots,n} : \gcd(k,n)=1}|
$$

Example

For $n=10$, the numbers relatively prime to 10 are:

$$
1,3,7,9
$$

Therefore:

$$
\phi(10)=4
$$

For a prime number $p$:

$$
\phi(p)=p-1
$$

For two distinct primes $p$ and $q$:

$$
\phi(pq)=(p-1)(q-1)
$$

This last identity is particularly important for RSA.
--------


## 2. Euler's Theorem

Euler's theorem states that if:

$$
\gcd(a,n)=1
$$

then:

$$
a^{\phi(n)} \equiv 1 \pmod n
$$

The condition $\gcd(a,n)=1$ is essential.

Example

Take:

$$
a=3,\quad n=10
$$

We have:

$$
\gcd(3,10)=1
$$

and:

$$
\phi(10)=4
$$

Therefore:

$$
3^4 \equiv 1 \pmod{10}
$$

Indeed:

$$
81 \equiv 1 \pmod{10}
$$

---------

## 3. Why this matters for cryptography

Euler's theorem is one of the mathematical foundations of RSA.

RSA chooses two primes $p$ and $q$ and computes:

$$
n=pq
$$

Then:

$$
\phi(n)=(p-1)(q-1)
$$

The private exponent $d$ is chosen so that:

$$
ed \equiv 1 \pmod{\phi(n)}
$$

This means there is an integer $k$ such that:

$$
ed=1+k\phi(n)
$$

Euler's theorem is then used to show why RSA decryption recovers the original message under the appropriate conditions.

So the progression is:

$$
\text{Fermat's Little Theorem}
\rightarrow
\text{Euler's Totient Function}
\rightarrow
\text{Euler's Theorem}
\rightarrow
\text{RSA}
$$

---------

## 4. Fermat's Little Theorem vs Euler's Theorem

For a prime $p$, Fermat's Little Theorem says:

$$
a^{p-1}\equiv1\pmod p
$$

when $p\nmid a$.

Euler's theorem generalizes this to arbitrary positive integers $n$:

$$
a^{\phi(n)}\equiv1\pmod n
$$

when:

$$
\gcd(a,n)=1
$$

Because for a prime $p$:

$$
\phi(p)=p-1
$$

Fermat's Little Theorem is a special case of Euler's theorem.

-------

## 5. Implementation notes

This implementation is educational.

It uses trial division to calculate $\phi(n)$ and Python's built-in modular exponentiation:

pow(a, exponent, modulus)

The implementation is intended to make the mathematics explicit, not to provide production cryptographic primitives.

----------

## 6. Important limitation

Euler's theorem does not say that:

$$
a^{\phi(n)}\equiv1\pmod n
$$

for every $a$.

The required condition is:

$$
\gcd(a,n)=1
$$

For example, with $a=2$ and $n=4$:

$$
\gcd(2,4)=2
$$

and:

$$
2^{\phi(4)}=2^2=4\equiv0\pmod4
$$

not 1.

This is an important condition to remember when we later analyze RSA.