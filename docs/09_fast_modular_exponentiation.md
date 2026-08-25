Fast Modular Exponentiation
**Author:** Elsie Okyere  
**Project:** Classical Cryptography Laboratory  



1. What is modular exponentiation?

Modular exponentiation computes:

$$
a^b \bmod n
$$

Instead of calculating the potentially enormous value $a^b$ first, we repeatedly reduce intermediate results modulo $n$.

Example:

$$
3^4\bmod5=81\bmod5=1
$$

Therefore:

$$
3^4\equiv1\pmod5
$$

2. Why do we need a fast algorithm?

Cryptographic algorithms such as RSA require operations of the form:

$$
m^e\bmod n
$$

and:

$$
c^d\bmod n
$$

The exponents can be very large. Fast modular exponentiation uses repeated squaring.

3. Repeated squaring

Suppose:

$$
5^7\bmod13
$$

Write:

$$
7=4+2+1
$$

Then:

$$
5^7=5^4\cdot5^2\cdot5
$$

Calculate:

$$
5^1\bmod13=5
$$

$$
5^2\bmod13=12
$$

$$
5^4\bmod13=12^2\bmod13=1
$$

Therefore:

$$
5^7\bmod13=(1)(12)(5)\bmod13
=60\bmod13
=\boxed{8}
$$

4. Binary representation

Repeated squaring works because every positive integer has a binary representation.

For example:

$$
13=8+4+1=(1101)_2
$$

So:

$$
a^{13}=a^8a^4a
$$

The algorithm computes:

$$
a^1,\ a^2,\ a^4,\ a^8,\ldots
$$

and multiplies only the powers required by the binary representation.

5. Algorithm

result = 1
base = base mod modulus

while exponent > 0:
    if exponent is odd:
        result = (result * base) mod modulus

    base = (base * base) mod modulus
    exponent = exponent // 2

6. Complexity

The exponent is divided by 2 at every iteration, so the number of iterations is approximately:

$$
O(\log b)
$$

where $b$ is the exponent.

7. Cryptographic importance

RSA encryption:

$$
c=m^e\bmod n
$$

RSA decryption:

$$
m=c^d\bmod n
$$

Diffie-Hellman also uses modular exponentiation:

$$
g^a\bmod p
$$

Understanding this algorithm is therefore an important prerequisite for RSA and Diffie-Hellman.

8. Implementation limitations

This implementation is educational, not production cryptography. Real cryptographic implementations must also consider constant-time behavior, side-channel resistance, secure parameters, and secure key generation.

9. Week 1 progression

$$
\text{GCD}
\rightarrow
\text{Modular Inverse}
\rightarrow
\text{Fermat}
\rightarrow
\text{Euler's Theorem}
\rightarrow
\text{Fast Modular Exponentiation}
\rightarrow
\text{RSA}
$$