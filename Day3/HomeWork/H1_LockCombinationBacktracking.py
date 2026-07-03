"""
================================================================
                Python Workshop - LJU (Data Structures)
----------------------------------------------------------------
Program Name        : 3-Digit Lock Combination
Topic               : Backtracking
Algorithm           : Backtracking (Permutation)
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

A security researcher is testing a 3-digit digital lock.

The lock uses the digits:

1, 2 and 3

Rules:

• Each digit can be used only once.
• No digit should be repeated.
• Generate all possible lock combinations.

Use the Backtracking algorithm to generate every valid
combination.

Operations:

1. Generate All Lock Combinations
2. Display Every Possible Combination

================================================================
"""


# // Function to Generate Lock Combinations
def generateCombination(combination, used):

    # // Base Condition
    if len(combination) == 3:
        print("".join(map(str, combination)))
        return

    # // Try Every Digit
    for digit in [1, 2, 3]:

        # // Check Digit is Already Used or Not
        if digit not in used:

            # // Choose
            used.add(digit)
            combination.append(digit)

            # // Recursive Call
            generateCombination(combination, used)

            # // Backtrack
            combination.pop()
            used.remove(digit)


# // Main Program
print("Possible Lock Combinations:\n")

generateCombination([], set())
