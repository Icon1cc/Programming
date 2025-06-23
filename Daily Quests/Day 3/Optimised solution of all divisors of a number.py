"""
Write a program to print all the divisors of a number.
"""

num = int(input("Enter a number: "))

x = 1

while x * x <= num:
    if num % x == 0:
        print(x)
        if x != num // x:
            print(num // x)
    x += 1

