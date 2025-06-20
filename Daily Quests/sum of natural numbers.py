"""
Write a program to print the sum of n natural numbers.
"""

def natural_sum(n):
    return n * (n + 1) / 2

n = int(input("Enter the limit of the numbers: "))
result = natural_sum(n)
print(f"The sum of {n} natural numbers is {result}")