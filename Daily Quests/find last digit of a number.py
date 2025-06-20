"""
Write a program to find the last digit of a number.
"""

x = int(input("Enter the number: "))

result = abs(x) % 10

print("The last digit of the number is:",result)