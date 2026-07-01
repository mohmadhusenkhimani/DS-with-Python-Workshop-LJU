"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : GPS Navigation System
Topic               : Backtracking
Data Structure Used : Two Stacks
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

You are building a GPS Navigation System similar to Google Maps.

The user moves through different locations (checkpoints).

If the user takes a wrong turn, they can go back to the
previous location.

After going back, the user can also move forward again,
just like the Back and Forward buttons in a web browser.

Implement the system using two Stacks.

Operations:

1. Visit a New Place
2. Go Back
3. Go Forward
4. Display Current Place
5. Exit
===============================================================
"""

back = []
forward = []

while True:
    print("\n1.Visit Place")
    print("2.Back")
    print("3.Forward")
    print("4.Current Place")
    print("5.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        place = input("Enter Place: ")
        back.append(place)
        forward.clear()

    elif ch == 2:
        if len(back) > 1:
            forward.append(back.pop())
            print("Current:", back[-1])
        else:
            print("No Previous Place")

    elif ch == 3:
        if len(forward) > 0:
            back.append(forward.pop())
            print("Current:", back[-1])
        else:
            print("No Forward Place")

    elif ch == 4:
        if len(back) > 0:
            print("Current Place:", back[-1])
        else:
            print("No Place Visited")

    elif ch == 5:
        break

