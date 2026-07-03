from math import gcd
from sympy import mod_inverse
ciphertext = "UOZT{ZUURMV_RH_RMHVXFIV}"
def calc_a_values():
    a_values = []
    for i in range(1,26):
        # Is i coprime? if so add to the list
        if(gcd(i,26) == 1):
            a_values.append(i)
    return a_values
        

def affine_brute_force(ciphertext, knowntext, a_values):
    counter = 0
    correct_values = []
    # Loop through every a value
    for a in a_values:
        a_inv = mod_inverse(a, 26)
        # Loop through every b value
        for b in range(0, 26):
            plaintext = ""
            for char in ciphertext:
                # Ignore Special Chars
                if(char == "{" or char == "}" or char == "_"):
                    plaintext += char
                else:
                    # Perform Affine Decrypt for given a and b value
                    x = ord(char) - 65
                    result = (((x-b) % 26) * (a_inv) % 26) % 26
                    plaintext += chr(result + 65)
            #Prints output, appends to correct_list if starts with "FLAG"        
            print(f"{counter}: a={a}, b={b}, {plaintext}")
            if(plaintext[0:len(knowntext)] == knowntext):
                correct_values.append(plaintext)
            counter += 1
    return correct_values
a_values = calc_a_values()
print(f"Valid a values: {a_values}")
correct_values = affine_brute_force(ciphertext, "FLAG", a_values)
print(f"Correct: {correct_values[0]}")