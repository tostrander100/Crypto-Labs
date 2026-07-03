# Walkthrough
See solution.py for code
## Outer loop
To brute force a Caesar Cipher, we need to perform the operation for ever possible rotaiton offset.
We only need to do 0 -> 25, because 26 would be wrap around back to 0, 27 would be 1, and so on again.
Therefore our outer loop, we need it iterate range(0,26)
## Inner loop
We only want to rotate our letters, so we need a check to ignore our special characters "{", "}", and "_"
Alternatively, we could just remove these and insert them back in after running our brute force algorithm
We start with an empty string, and we add to this string character by character, whether rotated or a special character to build the new potential word.
## Code
See solution.py for code walkthrough
