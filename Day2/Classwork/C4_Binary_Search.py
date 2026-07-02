"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Dictionary Hunt
Topic               : Binary Search
Algorithm           : Binary Search
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

You are in a library with a physical English dictionary.

You need to find the word "Ephemeral".

Instead of checking every page, you open the dictionary in the
middle.

If your required word comes before the current word, you search
the left half.

Otherwise, you search the right half.

This process continues until the word is found.

Design a Python program using Binary Search.

Operations:

1. Enter Dictionary Words
2. Search Word
3. Display Result

===============================================================
"""

words = []

n = int(input("Enter Number of Words: "))

for i in range(n):
    words.append(input("Enter Word: "))

words.sort()

print("\nDictionary:", words)

search = input("\nEnter Word to Search: ")

low = 0
high = n - 1
found = False

while low <= high:

    mid = (low + high) // 2

    if words[mid].lower() == search.lower():

        print("\nWord Found")
        print("Position :", mid + 1)
        found = True
        break

    elif search.lower() < words[mid].lower():

        high = mid - 1

    else:

        low = mid + 1

if found == False:
    print("\nWord Not Found")