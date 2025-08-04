"""
Write a program to count the digits in a given number
"""

x = int(input("Enter a number greater than 0: "))

count = 0

while x > 0:
    x = x // 10
    count += 1

print("Number of digits:", count)
