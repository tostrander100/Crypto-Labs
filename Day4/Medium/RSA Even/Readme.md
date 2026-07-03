# Challenge
n = 17844666266183898290907166228519278095298322
e = 65537
c = 2942645234948531254129638335059069218569795
## Walkthrough
RSA works because of the difficulty in finding the value of p and q that make up n.
However, if n is even then one of the primes is already known to be 2. And thus the other is n // 2, that is the integer divison of the p. Solve normally from here.
See solution.py for the code implementation.
## Result
flag{even_modulus}