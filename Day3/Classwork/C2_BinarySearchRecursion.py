"""
================================================================
                Python Workshop - LJU (Data Structures)
----------------------------------------------------------------
Program Name        : Binary Search Using Recursion
Topic               : Recursion
Algorithm           : Binary Search
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

Imagine a dictionary where all words are arranged in
alphabetical order. Instead of searching each word one by one,
you open the dictionary from the middle.

- If the required word is found, the search stops.
- If the required word comes before the middle word,
  search the left half.
- Otherwise, search the right half.

This process continues until the element is found or
no elements remain.

Write a Python program using Recursion to perform
Binary Search on a sorted list.

Operations:

1. Enter a Sorted List
2. Enter the Element to Search
3. Display the Position of the Element
4. Display "Element Not Found" if it does not exist.

================================================================
"""


# // Function for Binary Search using Recursion
def binary_search(numbers, low, high, key):

    # // Base Condition
    if low > high:
        return -1

    # // Find Middle Index
    middle = (low + high) // 2

    # // Element Found
    if numbers[middle] == key:
        return middle

    # // Search Left Side
    elif key < numbers[middle]:
        return binary_search(numbers, low, middle - 1, key)

    # // Search Right Side
    else:
        return binary_search(numbers, middle + 1, high, key)


# // Main Program
numbers = list(map(int, input("Enter Sorted Numbers : ").split()))

key = int(input("Enter Element to Search : "))

result = binary_search(numbers, 0, len(numbers) - 1, key)

# // Display Result
if result != -1:
    print("Element Found at Index :", result)
else:
    print("Element Not Found")
