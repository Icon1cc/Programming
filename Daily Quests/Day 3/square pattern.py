"""
Write a program to print a square pattern given a number n should print n*n
"""

x = int(input("Enter the number: "))

i = 0

while i < x:
    j = 0
    while j < x:
        print("*", end = " ")
        j += 1
    print()
    i += 1

