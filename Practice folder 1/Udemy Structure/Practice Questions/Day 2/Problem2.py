"""
Write a function that returns True if the sum or difference of two numbers is 5
"""

def func(a, b):
    return a + b == 5 or abs(a - b) == 5

a = int(input("Please enter the first number : "))
b = int(input("Please enter the second number : "))
result = func(a, b)
print(result)