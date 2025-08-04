"""
Write a program to print tables of number from 1 to 10
"""

x = int(input("Enter a number: "))
y = int(input("Enter the range: "))
for i in range(1, y+1):
    print(f"{i} x {x} = {x*i}")