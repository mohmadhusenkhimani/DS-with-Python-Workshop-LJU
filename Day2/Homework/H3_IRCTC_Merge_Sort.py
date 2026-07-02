"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : IRCTC Waitlist Merger
Topic               : Merge Sort
Algorithm           : Merge Sort
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

IRCTC has two separately sorted waitlists.

One list comes from the Mobile App and another
comes from the Railway Counter.

Instead of sorting everything again, the system
merges both sorted lists into one final sorted
waitlist.

Design a Python program using Merge Sort.

Operations:

1. Enter Waitlist Numbers
2. Sort using Merge Sort
3. Display Final Waitlist

===============================================================
"""

def mergeSort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:

                arr[k] = left[i]
                i += 1

            else:

                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):

            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):

            arr[k] = right[j]
            j += 1
            k += 1


arr = []

n = int(input("Enter Number of Waitlist Numbers: "))

for i in range(n):
    arr.append(int(input("Enter Number: ")))

print("\nOriginal Waitlist :", arr)

mergeSort(arr)

print("\nMerged & Sorted Waitlist :", arr)