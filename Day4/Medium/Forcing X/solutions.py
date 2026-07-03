# BRUTE Force Method
from pwn import xor
import time
cipher_hex = "6c91846d9193799886788f847e9ab8669b924093927a879440808f76879a"
cipher_bytes = bytes.fromhex(cipher_hex)
def xor_brute_force(max_bytes, crib):
    #Iterate up to max_bytes
    start = time.time()
    for i in range(256**max_bytes):
        guess = xor(i.to_bytes(max_bytes),cipher_bytes) 
        if(i % 100000 == 0):
            print(f"Iteration: {i} / {256**max_bytes}")
        if(crib in guess):
            print(guess)
            end = time.time()
            print(f"Time: {end - start}")
xor_brute_force(3,b"flag")
# Leveraging Known Crib Method (Much More efficent)
from pwn import xor
cipher_hex = "d39184d29193c69886c78f84c19ab8d99b92ff9392c58794ff808fc9879a"
cipher = bytes.fromhex(cipher_hex)

crib = b"flag"
key_len = 3

for pos in range(len(cipher) - len(crib) + 1):
    key = [None] * key_len
    valid = True

    # Recover key bytes implied by placing the crib here
    for i, c in enumerate(crib):
        kidx = (pos + i) % key_len
        kbyte = cipher[pos + i] ^ c

        if key[kidx] is None:
            key[kidx] = kbyte
        elif key[kidx] != kbyte:
            valid = False
            break

    if not valid or None in key:
        continue

    key = bytes(key)
    plaintext = xor(cipher, key)

    print(f"Position: {pos}")
    print(f"Key: {key.hex()} ({key})")
    print(plaintext)
    print()