"""
Write a program to find the smallest divisor of a number such that the divisor is greater than 1
"""

n = int(input("Enter the number: "))

for i in range(2, n + 1):
    if n % i == 0:
        print(f"The smallest divisor of {n} greater than 1 is: {i}")
        break

