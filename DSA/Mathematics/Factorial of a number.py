"""
Write a program to print the factorial of a given number
"""

def my_fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
result = my_fact(n)
print("Factorial:", result)
