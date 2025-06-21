"""
Write a program to check whether a number is positive, negative.
"""

x = int(input("Enter the number: "))

if x < 0:
    print("Negative")
elif x > 0:
    print("Positive")
else:
    print("Zero")