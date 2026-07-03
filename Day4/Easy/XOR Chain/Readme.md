# Challenge
flag = b"?????????????????"
KEYS = ["This","Is","A","Lot","Of","Random","Text", "Here", "And", "Some", "Random", "Ones", "13291238998472938","238fh2938fh"]
def XOR_LIST(flag):
    cipher = flag
    for key in KEYS:
        cipher = xor(cipher,key.encode())
    print(cipher)
XOR_LIST(flag)

'''
Output:

b'{PW\x150\x7fn|G=.\x7fTq<.(w~b\x0f6hqM:\x10'

'''
# Walkthrough
## Information
This is a crypto XOR reversing challenge.
The interesting part of the XOR function is that it is reversible.
If,
A XOR B = C
Then
C XOR B = A

## Solving
We have an array of all the keys that we XOR'd our plaintext with, to undo this we can XOR our ciphertext with the same keys to get the ciphertext. 
Essentially run the script again but with our ciphertext in place of the original flag varaible. Don't forget to include the XOR function too using the pwn.xor library.

See the Walkthrough for more information

## Result 
flag{REVERSING_X0R_IS_EASY}
