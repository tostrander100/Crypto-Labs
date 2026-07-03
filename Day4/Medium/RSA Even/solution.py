from Crypto.Util.number import *
n = 17844666266183898290907166228519278095298322
e = 65537
c = 2942645234948531254129638335059069218569795
# Because n is even, we know that one of the primes is 2. And thus the other is n // 2
p = 2
q = n // 2
totient = (p - 1) * (q - 1)
d = pow(e, -1, totient)
m = pow(c, d, n)
print(long_to_bytes(m))
# b'flag{even_modulus}'