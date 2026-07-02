"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Spam Detector
Topic               : Linear Search
Algorithm           : Linear Search
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

A cybersecurity intern at a startup is building a simple spam
filter.

Incoming email sender IDs are checked against a blacklist of
known spam senders.

Since the blacklist is not sorted, each sender ID must be
checked one by one until a match is found.

Design a Python program using Linear Search to detect whether
an incoming email is spam or safe.

Operations:

1. Enter Blacklisted Sender IDs
2. Search Sender ID
3. Display Result

===============================================================
"""

blacklist = []

n = int(input("Enter Number of Blacklisted IDs: "))

for i in range(n):
    blacklist.append(input("Enter Sender ID: "))

search = input("\nEnter Incoming Sender ID: ")

found = False

for i in range(n):

    if blacklist[i].lower() == search.lower():

        print("\nSpam Detected")
        found = True
        break

if found == False:

    print("\nSafe Email")