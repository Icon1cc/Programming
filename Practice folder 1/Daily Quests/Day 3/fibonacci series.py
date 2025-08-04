"""
Write a program to print the Fibonacci series.
"""

n = int(input("Enter how many Fibonacci numbers to print: "))

a = 0
b = 1

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci series:", a)
else:
    print("Fibonacci series:", end=" ")
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
    print()
