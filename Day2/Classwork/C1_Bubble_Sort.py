"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Packing Books
Topic               : Bubble Sort
Algorithm           : Bubble Sort
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

Your younger sibling is packing books into a bag. They don't
plan—they simply compare two adjacent books.

If the heavier book is before the lighter one, they swap them.

This process continues until no more swaps are needed.

The heaviest books slowly "bubble up" to the last position.

Design a Python program using Bubble Sort to sort the book
weights in ascending order.

Operations:

1. Enter Book Weights
2. Sort using Bubble Sort
3. Display Sorted Book Weights

===============================================================
"""

arr = []

n = int(input("Enter Number of Books: "))

for i in range(n):
    arr.append(int(input("Enter Book Weight: ")))

print("\nOriginal List:", arr)

for i in range(n - 1):
    for j in range(n - i - 1):

        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("\nSorted List:", arr)