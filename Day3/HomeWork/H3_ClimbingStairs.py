"""
================================================================
                Python Workshop - LJU (Data Structures)
----------------------------------------------------------------
Program Name        : Climbing Stairs
Topic               : Recursion
Algorithm           : Climbing Stairs Algorithm
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

Imagine you are climbing a staircase.

You can climb either:

• 1 step at a time
• 2 steps at a time

Find the total number of different ways to reach the
Nth stair using Recursion.

Example:

If N = 4

Possible Ways:

1. 1 + 1 + 1 + 1
2. 1 + 1 + 2
3. 1 + 2 + 1
4. 2 + 1 + 1
5. 2 + 2

Output:
Total Ways = 5

Operations:

1. Enter Number of Stairs
2. Calculate Total Ways using Recursion
3. Display Total Number of Ways

================================================================
"""


# // Function to Find Total Ways
def climbStairs(number):

    # // Base Condition
    if number == 0 or number == 1:
        return 1

    # // Recursive Call
    return climbStairs(number - 1) + climbStairs(number - 2)


# // Main Program
number = int(input("Enter Number of Stairs : "))

totalWays = climbStairs(number)

# // Display Result
print("\nTotal Ways =", totalWays)
