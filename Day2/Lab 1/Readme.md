# Walkthrough
See solution.py for the code solution
## Generate valid a values
We need to generate all a values such that 1 <= a <= 25, and gcd(a,26) == 1. 
In solution.py, calc_a_values() returns the list of valid a values.
The answer should be: [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

## Create the decrypt function
We need to loop through every combination of a and b values, we can do that with a nested loop. In solution.py, note that a_inv was also calculated within the a loop using the inv_mod function from sympy. Alteratively pow(a, -1, 26) accomplishes the same result.

Within our nested loop of every possible combination of valid a and b values, we transform our text using the decrypt formula for transforming letters while ignoring special chars. We save any output that begins with "FLAG" to our output list, to save for easier printing.

