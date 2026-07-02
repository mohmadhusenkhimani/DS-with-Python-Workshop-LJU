"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Undo Machine
Topic               : Stack
Data Structure Used : Stack (LIFO)
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

You are building a lightweight text editor.

Whenever a user types a character, it is stored in memory.

When the user presses Ctrl + Z (Undo), the most recently typed
character must be removed.

Implement the following operations using a Stack:

1. Type Character
2. Undo Last Character
3. Display Current Text
4. Exit
===============================================================
"""

text = []

while True:
    print("\n1.Type Character")
    print("2.Undo")
    print("3.Get Text")
    print("4.Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        c = input("Enter Character: ")
        text.append(c)

    elif ch == 2:
        if len(text) > 0:
            text.pop()
        else:
            print("Nothing to Undo")

    elif ch == 3:
        print("Current Text:", "".join(text))

    elif ch == 4:
        break

