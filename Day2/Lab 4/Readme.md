Can you XOR brute force this ciphertext?
I heard that XOR is super secure, I am pretty sure if I just have a 1 byte key I'm fine

ciphertext:
e9 e3 ee e8 d4 fc e7 e0 fd fb f0 e4 ea f6 f0 ed ee eb d2

# Walkthrough
The hint suggests that it
1. Go to cyberchef
2. Use a hex decode block
3. Use the XOR Brute Force Block
4. Set the key length to one
5. Look for an intelligible plaintext (You can also put "FLAG{" as the crib to find it faster)
You will find FLAG{SHORT_KEY_BAD}