"""
Write a program to print the greatest common divisor of two numbers.
"""

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input("Enter first number: "))
m = int(input("Enter second number: "))

gcd = find_gcd(n, m)
print(f"GCD of {n} and {m} is {gcd}")

