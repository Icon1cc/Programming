"""
Function that returns both quotient and remainder of two numbers
"""

def myfunc(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
q, r = myfunc(a, b)
print(f"Quotient is {q}, Remainder is {r}")