ciphertext = "JPEK{GEIWEV_FVYXI_JSVGI}"
def caesar_brute_force (ciphertext):
    # The outer loop iterates for every possible rotation offset 0-25
    for i in range(0, 26): 
        output = ""
        # We iterate by each char in the string, for example our first will be J
        for char in ciphertext:
            #We keep these chars the same and don't rotate
            if(char == "{" or char == "}" or char == "_"):
                output += char
            else:
                #Rotation Step, we convert to a number where A=0, 
                #add our offset and wrap around using % operator, then convert back to char
                output += chr(((ord(char) - 65 + i) % 26) + 65)
            
        print(f"{i}: {output}")    
caesar_brute_force(ciphertext)