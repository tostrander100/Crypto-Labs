What are you talking about same IV? I told you already my cookies are securely AES-CTR encrypted.
Here, I'll even give you a plaintext and ciphertext pair:

P1: "USER: guest; ADMIN: 0;"
C1: 96d95a7974bc3ad497cbb032ad502e7267d7b2752277

I'll believe you if you can figure out this message:

C2: a5e67e4c35d86dcf86e7963af862596060a9c6162131

## Walkthrough
See solution.py for the code example
### AES CTR Same IV vulnerability
For AES CTR, the secure relies in us using a random Nonce/IV.
If there are the same value, then 
P1 XOR P2 = C1 XOR C2.

From here we can rearrange the equation to solve for P2:

P2 = C1 XOR C2 XOR C3

### Encoding

The hardest part of this challenge is getting our given text into byte format.
We see C1 and C2 are in hex, and P1 is in plaintext.
We use bytes.fromhex(HEX) and .encode() to get into byte format.

### Flag
The result after performing the XOR operations is the following:

flag{D0nt_R3us3_N0NC3}
