"""
Write a program to print the table of the numbers where the range of the numbers and the table numbers both are provided
"""

table_upto = int(input("Enter the number you want to print tables up to: "))
range_upto = int(input("Enter the range for each table: "))

for num in range(1, table_upto + 1):
    print(f"\nTable of {num}:")
    for i in range(1, range_upto + 1):
        print(f"{num} x {i} = {num * i}")

