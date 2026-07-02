"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Scholarship Ranker
Topic               : Selection Sort
Algorithm           : Selection Sort
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

A college must give scholarships to the top scoring students.

The coordinator scans the entire marksheet, finds the highest
scorer and places them in Rank 1.

Then the remaining students are scanned again to find the next
highest scorer.

This process continues until all students are ranked.

Design a Python program using Selection Sort to arrange student
marks in descending order.

Operations:

1. Enter Student Marks
2. Sort using Selection Sort
3. Display Scholarship Ranking

===============================================================
"""

arr = []

n = int(input("Enter Number of Students: "))

for i in range(n):
    arr.append(int(input("Enter Marks: ")))

print("\nOriginal Marks:", arr)

for i in range(n - 1):

    maxIndex = i

    for j in range(i + 1, n):

        if arr[j] > arr[maxIndex]:
            maxIndex = j

    temp = arr[i]
    arr[i] = arr[maxIndex]
    arr[maxIndex] = temp

print("\nScholarship Ranking:")

for i in range(n):
    print("Rank", i + 1, ":", arr[i])