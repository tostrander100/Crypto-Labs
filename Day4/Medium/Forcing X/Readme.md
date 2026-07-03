# Challenge
The Key isn't plaintext this time!
I will tell you though that the key is 3 bytes long and contains the substring "flag"
the flag is not in the traditional "flag{...}" format though, so good luck.
6c91846d9193799886788f847e9ab8669b924093927a879440808f76879a

# Walkthrough
There are two ways to solve this, the easiest to to leverage cyberchef's builtin method:

## Cyberchef
1. From Hex
2. XOR Brute Force (Key Length - 3, Sample Length - 30)
Then choose the one that contains the substring "flag".

## Code
Alternatively this can be solved by brute forcing or using a crib attack. See both examples in code for this.
