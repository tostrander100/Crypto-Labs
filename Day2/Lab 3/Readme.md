# Walkthrough
We start with the following text:
15 19 11 02 29 13 0a 0b 0c 05 1c 04 1b 05 1a 0d 16 0d 04 1a 13 1f 11 18 10 1e 2d
We can use cyberchef, along with some notes and intuition to complete this challenge.
## Using the Plaintext
First, within cyberchef use the from hex and an XOR filter.
Change our key input from Hex to UTF-8 so that we can input plaintext.
We want the first five chars of the plaintext to be "FLAG{" and we have the ciphertext.
This allows us to find the first 5 chars of the key by XORing the plaintext with the ciphertext

1. Apply From Hex
2. Apply XOR filter - change to UTF-8 Key
3. Enter the plaintext FLAG{
4. The resulting first 5 chars will be from our key
Following these steps you should find the following output:
SUPERUFJK~ZHZBaKZLCaUSP_kXa
We know know that our key is "SUPER???" Where the "?" symbol represents the parts we don't know
## Using the Paritial Key to lock in Knowns
Now we will put "SECRET???" As our key and recreate a partial flag from what we know.
You should get the following text: (The "???" text is irrelevant, so long as our key is 8 chars long)
Entering a key of "SUPER???" Gives us the following flag:
FLAG{,54_PLAI:%2EXT_A .'CK}
123456781234567812345678123

The repeating 12345678 below the flag is for us to find out our knowns.
Becuase we know the first 5 chars of the key and XOR repeats, we can lock in all chars with 12345 and represent 678 as a ?
Let's lock in our knowns:

FLAG{???_PLAI???EXT_A???CK}
123456781234567812345678123

## Making logical guesses to complete the key
From here, we need to complete the last 3 characters of our key.
A good way to do this is to pick up what words may be visible.
My guess here is that "A???CK" is actually ATTACK.
I known change the question marks in "SUPER???" Until the word ATTACK appears

A good way to do this is to replace "SUPER???" with "SUPERTTA" becuase "TTA" was our target for the question marks. We can then see the value at that position and use it as a potential answer.

KEY: SECRET???
FLAG{???_PLAI???EXT_A???CK}
123456789abcdefghijklmnopqr
KEY: SUPERTTA
FLAG{G^J_PLAIQNLEXT_AKEYCK}
123456789abcdefghijklmnopqr

In the following example, we xor our guess "TTA" with the ciphertext "A???CK", this should produce the potential key value at the same index.
Looking at the index, ??? is at index mno in our example,
the values at mno in our guess is KEY. 

Completing the key then gives us a potential answer "SUPERKEY"

## Testing the Answer
Now using "SUPERKEY" reveals FLAG{XOR_PLAIN_TEXT_ATTACK}, that is intelligible text, it is our flag.
