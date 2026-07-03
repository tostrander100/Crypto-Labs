# Walkthrough
We start with the given text:
b'\x00\x10\x13\x17*\x13\x08\x00\x1f\x05\x04\x19\x17\t\x06\x03\x04\x1b\x1e\x12\x1a\x0e)'

And the following code:
FLAG = b"???????????"
INTERMEDIATE1 = xor(FLAG, b"SUPER")
INTERMEDIATE2 = xor(INTERMEDIATE1, b"SECRET")
CIPHER = xor(INTERMEDIATE2, b"FLAG")
print(CIPHER)

We simply have to reverse engineer this code to find the original flag.
We started with 3 XOR operations with 3 Keys to get from plaintext to ciphertext
Let's XOR with the 3 Keys again to get back to plaintext:

## Solution
xor(xor(xor(CIPHER,b"FLAG"), b"SUPER"),b"SECRET")

