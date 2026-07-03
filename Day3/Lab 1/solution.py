from Crypto.Util.number import *
p = 957555418188361627912969
q = 944005931637794413303261
e = 65537
c = 284504807705999661395524777908732950004370262627
n = p * q #Calculate n
totient = (p-1) * (q-1)#Calculate totient
d = pow(e, -1, totient)#Calculate Private Key d, the multiplicative inverse of e
m = pow(c, d, n)#Calculate the message, c^d mod n 
print(long_to_bytes(m)) #Convert from int to byte string
#b'FLAG{RSA_IS_EASY}'