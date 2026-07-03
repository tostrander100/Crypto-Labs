# included the xor function
from pwn import xor
# Replace the mystery flag with our ciphertext
flag = b"{PW\x150\x7fn|G=.\x7fTq<.(w~b\x0f6hqM:\x10"
KEYS = ["This","Is","A","Lot","Of","Random","Text", "Here", "And", "Some", "Random", "Ones", "13291238998472938","238fh2938fh"]
def XOR_LIST(flag):
    cipher = flag
    for key in KEYS:
        cipher = xor(cipher,key.encode())
    print(cipher)
XOR_LIST(flag)

'''
Output:

b'flag{REVERSING_X0R_IS_EASY}'

'''