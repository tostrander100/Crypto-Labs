from pwn import xor
print(xor(xor(xor(CIPHER,b"FLAG"), b"SUPER"),b"SECRET"))