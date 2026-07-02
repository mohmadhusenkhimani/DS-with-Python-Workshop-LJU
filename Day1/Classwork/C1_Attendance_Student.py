"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Attendance Student
Topic               : Array (Direct Access)
Data Structure Used : Array
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

Imagine a class with 30 students. The teacher maintains an
attendance register where each student's roll number has a
fixed position in an array.

Example:
    Roll No. 1  -> Index 0
    Roll No. 2  -> Index 1
    ...
    Roll No. 30 -> Index 29

Since every student has a fixed slot (index), the teacher can
directly access or update any student's attendance without
searching through previous records.

Design a menu-driven program using an Array that performs the
following operations:

1. Mark Attendance (Present / Absent)
2. View Attendance Register
3. Exit
===============================================================
"""

attendance = ["Absent"] * 30

while True:
    print("\n===== Attendance System =====")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        roll = int(input("Enter Roll Number (1-30): "))

        if 1 <= roll <= 30:
            status = input("Present(P) / Absent(A): ")

            if status.upper() == "P":
                attendance[roll - 1] = "Present"
            else:
                attendance[roll - 1] = "Absent"

            print("Attendance Updated Successfully.")
        else:
            print("Invalid Roll Number")

    elif ch == 2:
        print("\nAttendance Register")
        for i in range(30):
            print(f"Roll No {i+1} : {attendance[i]}")

    elif ch == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
