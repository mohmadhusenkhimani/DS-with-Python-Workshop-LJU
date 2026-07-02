"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : E-Commerce Price Filter
Topic               : Binary Search (Lower Bound)
Algorithm           : Binary Search
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

You are browsing an e-commerce website like Flipkart.

The products are already sorted according to their prices.

You want to find the first product whose price is
greater than or equal to ₹50,000.

Instead of checking every product one by one, use
Binary Search to quickly locate the first matching
product.

Design a Python program using Binary Search (Lower Bound)
to find the first product price greater than or equal
to the target price.

Operations:

1. Enter Product Prices (Sorted)
2. Enter Target Price
3. Display First Matching Product

===============================================================
"""

arr = []

n = int(input("Enter Number of Products: "))

print("\nEnter Product Prices in Sorted Order")

for i in range(n):
    arr.append(int(input("Enter Price: ")))

target = int(input("\nEnter Target Price: "))

low = 0
high = n - 1

answer = -1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] >= target:
        answer = mid
        high = mid - 1

    else:
        low = mid + 1

if answer != -1:

    print("\nFirst Product Found")
    print("Position :", answer + 1)
    print("Price    :", arr[answer])

else:

    print("\nNo Product Found")