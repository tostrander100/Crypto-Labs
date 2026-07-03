from pwn import xor
# Original Information
P1 = "USER: guest; ADMIN: 0;"
C1 = "96d95a7974bc3ad497cbb032ad502e7267d7b2752277"
C2 = "a5e67e4c35d86dcf86e7963af862596060a9c6162131"
# P2 = ????

# Original information in bytes format
# For the ciphertext values we use bytes.fromhex(HEX)
# For the plaintext we use .encode() to get into byte format
b_C1 = bytes.fromhex(C1)
b_C2 = bytes.fromhex(C2)
b_P1 = P1.encode()

# We know that for AES-CTR with the same IV, C1 XOR C2 = P1 XOR P2
# Therefore P2 = P1 XOR C1 XOR C2

b_plaintext = xor(xor(xor(b_C1),b_C2),b_P1)

print(b_plaintext.decode())