"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Lost Student (Attendance Register)
Topic               : Linear Search
Algorithm           : Linear Search
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

Professor Sharma enters the classroom and receives a call from
the HOD asking:

"Is Riya Desai present today?"

The attendance register is not sorted because the names are
written in the order in which students entered the classroom.

Since the names are not arranged alphabetically, the professor
must check every student's name one by one until the required
student is found.

Design a Python program using Linear Search to search for a
student's name in the attendance register.

Operations:

1. Enter Student Names
2. Search Student
3. Display Result

===============================================================
"""

students = []

n = int(input("Enter Number of Students: "))

for i in range(n):
    students.append(input("Enter Student Name: "))

search = input("\nEnter Student Name to Search: ")

found = False

for i in range(n):

    if students[i].lower() == search.lower():
        print("\nStudent Found")
        print("Position :", i + 1)
        found = True
        break

if found == False:
    print("\nStudent Not Found")