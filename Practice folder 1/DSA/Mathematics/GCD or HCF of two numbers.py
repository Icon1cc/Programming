"""
Write a program to find the GCD or HC
"""

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

while y != 0:
    x,y = y, x%y
print(x)
