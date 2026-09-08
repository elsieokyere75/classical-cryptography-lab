# AES-128: Mathematics and Educational Implementation

## 1. Overview

The Advanced Encryption Standard (AES) is a symmetric-key block cipher used to protect data confidentiality.

AES operates on fixed 128-bit blocks.

For AES-128:

- Block size: 128 bits = 16 bytes
- Key size: 128 bits = 16 bytes
- Number of rounds: 10

The same secret key is used for encryption and decryption.

This project implements AES-128 from its underlying transformations for educational and research purposes.

---

## 2. AES State Representation

AES represents each 16-byte block as a 4 x 4 state matrix.

Bytes are placed column by column.

For the input:

```text
00 11 22 33 44 55 66 77
88 99 AA BB CC DD EE FF