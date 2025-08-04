"""
Write a program to take two numbers a and b from the user depending on their values print one of the following:

a) A is greater
b) B is greate
c) A and B are same
"""

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a == b:
    print("A and B are same")
elif a > b:
    print("A is greater")
else:
    print("B is greater")
