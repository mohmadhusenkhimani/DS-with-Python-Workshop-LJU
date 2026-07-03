"""
================================================================
                Python Workshop - LJU (Data Structures)
----------------------------------------------------------------
Program Name        : Fibonacci Series
Topic               : Recursion
Algorithm           : Fibonacci Algorithm
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

Write a Python program to generate the Fibonacci Series.

The Fibonacci sequence starts with 0 and 1. Each subsequent
number is the sum of the previous two numbers.

The program should:

1. Accept the number of terms from the user.
2. Generate the Fibonacci Series.
3. Display the series.

================================================================
"""


# // Function to print Fibonacci Series
def fibonacci(number):
    # // First two numbers
    first = 0
    second = 1

    # // Print Fibonacci Series
    for i in range(number):
        print(first, end=" ")

        # // Find next Fibonacci number
        next_number = first + second
        first = second
        second = next_number


# // Main Program
number = int(input("Enter Number of Terms : "))

print("\nFibonacci Series :")
fibonacci(number)
