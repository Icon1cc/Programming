"""
Write a function that returns the square of a number
"""

def myfunc(num):
    return num ** 2

num = float(input("Please enter the number to return the square: "))
result = myfunc(num)
print(f"The square of the number is: {result}")