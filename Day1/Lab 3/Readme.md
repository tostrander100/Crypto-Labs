# Walkthrough
## Build Partial key from known plaintext
We start knowing that the first four letters of our plaintext is "FLAG"

Be extension, we know that the first four letters of our key is "secr" becuase that produces FLAG when vigenere decoded. This gives us the flag: FLAG{HXORTSTP_OLRBZ_UJGKPM}

## Guess first word of key
The flag still looks like a mess , however "secr" seems oddly similar to "secret". We are told that our key is composed of two words, so this is a good guess.
Upon trying "secret", we reveal more information: FLAG{VIYEJFRN_OLRBN_FTTACK}

## Gain information by completing flag words
This is still incomplete, however our last word "FTTACK" seems very similar to "ATTACK". 
Let's force this to be attack and see if that reveals any more information. 
Use a key value such as "secretaaa" and change the a value that moves the "FTTACK" to "ATTACK". You will land on something like "secretaay" -> FLAG{VIQINERE_PLASR_ATTACK}

Now the word "VIQINERE" seems even more clearly to be "VIGENERE", and we know that "??y" is the second word of our key. Playing Around to complete the word "VIGENERE", we get the key "
