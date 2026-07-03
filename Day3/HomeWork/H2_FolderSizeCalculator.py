"""
================================================================
                Python Workshop - LJU (Data Structures)
----------------------------------------------------------------
Program Name        : Folder Size Calculator
Topic               : Recursion
Algorithm           : Recursive Directory Traversal
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

Imagine Windows File Explorer.

When you right-click a folder and select Properties,
Windows calculates the total size of the folder.

A folder may contain:

• Files
• One or more Subfolders

The program should recursively visit every subfolder,
calculate the size of each file, and display the total
folder size.

Operations:

1. Enter Folder Path
2. Calculate Folder Size using Recursion
3. Display Total Folder Size

================================================================
"""

import os


# // Function to Calculate Folder Size
def calculateFolderSize(folderPath):

    # // Initialize Total Size
    totalSize = 0

    # // Visit Every File and Folder
    for item in os.scandir(folderPath):

        # // If Item is File
        if item.is_file():
            totalSize += item.stat().st_size

        # // If Item is Folder
        elif item.is_dir():
            totalSize += calculateFolderSize(item.path)

    # // Return Total Size
    return totalSize


# // Main Program
folderPath = input("Enter Folder Path : ")

# // Check Folder Exists
if os.path.exists(folderPath):

    totalSize = calculateFolderSize(folderPath)

    print("\nTotal Folder Size :", totalSize, "Bytes")

else:
    print("\nFolder Not Found.")
