"""
Write a program to print the LCM of two numbers
"""

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Save originals for LCM calculation
a, b = x, y

# Find GCD using Euclidean algorithm
while b != 0:
    a, b = b, a % b

gcd = a
lcm = (x * y) // gcd

print("LCM:", lcm)
