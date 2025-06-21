"""
Write a program to print the table of the numbers where the range of the numbers and the table numbers both are provided
"""

x = int(input("Enter the numbers you want to generate table till: "))
y = int(input("Enter the range for the tables: "))

for num in range(1, x + 1):
    print(f"Table of {num} is: ")
    for items in range(1, y + 1):
        print(items * num)

