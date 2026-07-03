"""
================================================================
                Python Workshop - LJU (Data Structures)
----------------------------------------------------------------
Program Name        : Multiplication Using Addition
Topic               : Recursion
Algorithm           : Repeated Addition
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

Imagine you don't have a multiplication (*) operator.

You can only use the addition (+) operator.

For example:

5 × 4 = 5 + 5 + 5 + 5 = 20

Write a Python program using Recursion to perform
multiplication as a series of repeated additions.

Operations:

1. Enter the First Number
2. Enter the Second Number
3. Find Multiplication using Recursion
4. Display the Result

================================================================
"""


# // Function to Multiply Using Recursion
def multiply(firstNumber, secondNumber):

    # // Base Condition
    if secondNumber == 0:
        return 0

    # // Recursive Call
    return firstNumber + multiply(firstNumber, secondNumber - 1)


# // Main Program
firstNumber = int(input("Enter First Number : "))
secondNumber = int(input("Enter Second Number : "))

result = multiply(firstNumber, secondNumber)

# // Display Result
print("\nMultiplication =", result)
