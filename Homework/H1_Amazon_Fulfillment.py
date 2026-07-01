"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Amazon Fulfillment Centre
Topic               : Fixed Array
Data Structure Used : Array
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

An Amazon fulfillment centre has a conveyor belt with exactly
8 slots numbered from 0 to 7.

Each slot can store only one product.

The warehouse manager wants to perform the following operations:

1. Add a Product
2. Find Product at a Slot
3. Update Product
4. Check Whether the Belt is Full
5. Display All Slots
6. Exit

Implement the system using a Fixed Array.
===============================================================
"""

belt = [None] * 8

while True:
    print("\n1. Add Product")
    print("2. Find Product")
    print("3. Update Product")
    print("4. Check Belt Full")
    print("5. Display")
    print("6. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        index = int(input("Enter Slot (0-7): "))
        if belt[index] == None:
            belt[index] = input("Enter Product: ")
        else:
            print("Slot Already Occupied")

    elif ch == 2:
        index = int(input("Enter Slot: "))
        print("Product =", belt[index])

    elif ch == 3:
        index = int(input("Enter Slot: "))
        belt[index] = input("Enter New Product: ")

    elif ch == 4:
        if None in belt:
            print("Belt is Not Full")
        else:
            print("Belt is Full")

    elif ch == 5:
        for i in range(8):
            print(i, "->", belt[i])

    elif ch == 6:
        break
