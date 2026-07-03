# Challenge 
0b 05 05 09 12 14 07 19 13 1b 10 0c 02 16 32 1d 0c 0b 36 08 0a 02 1f 00 0c 12 38 04 03 1a 13 0b 1b 38 01 07 29 1d 10 06 0f 11 10

# Walkthrough
## Setup
Navigate to Cyberchef.
1. Use the From Hex block.
2. Use the XOR block, change the key input to UTF-8 
## Key discovery
Use our known plaintext crib "flag{" as the key
This gives us the following result:
midnirkxt`v`cqI{`jQsln~gwtTedaugz_zaE|w}i}q

This means that we can lock in "midni" as part of our key. From here we have two methods to generate more information.
1. If the key appears to be a word, try to complete the key. 
2. Increase the length of the key using a random char such as "?" to uncover the likely key length and cause visible information to leak.

## Completing the Key
This is a good method to generate more information, but it is not enough on its own.
We have the word "midni", my guess is that it is "midnight", let's try that word.
Completing the key gives us the following:

flag{som~rtbkqZiabRfcewta{\jj}{.vQei@zxrbxt

Unfortunately this is not enough, however if we hold "midnight" as our key, then "flag{som?????????" is at least confirmed, and the substring "som" is probably "some", which we could try.

## Finding the Key Length
This is another good method to try to gain more information. We don't know the length of our key, but if we do have the right length then we would except partial words in the flag to be exposed.
Using our guess key of "midnight", continue adding "?" chars after until we start to see interesting results.
After adding six "?"s, we get the following:
key: "midnight??????"
result: flag{som,$/3=)_the_obv ?3-.;nswer_is."/90.}

This message is particularly interesting, we have the words "the" and "is", and partials for "answer", and potentially "obvious" and "some". Thus we believe our key length is 14 chars.
## Guessing Flag Words to completion
Using our potential words, we start to edit our "?" characters to edit characters at a specific position. Using our established key length of 14, we can arrange the problem as thus, where our key lets us know 0-7 for sure.

flag{som,$/3=)_the_obv ?3-.;nswer_is."/90.}
0123456789abcd0123456789abcd0123456789abcd0
flag{som??????_the_obv??????nswer_is??????}

To make "answer", we must edit position d (the 14th position).

This gives us the following:
0123456789abcd0123456789abcd0123456789abcd0
flag{som?????s_the_obv?????answer_is?????t}

If we guess "obvious", we get:
key: midnightvoya?e
flag: flag{sometim=s_the_obvious.answer_is_rig0t}

From there, the key midnightvoyage gives us the flag:
## Flag
flag{sometimes_the_obvious_answer_is_right}

