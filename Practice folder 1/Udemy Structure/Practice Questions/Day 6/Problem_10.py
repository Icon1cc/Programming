"""
Use return with multiple values (return tuple)
"""

def myfunc(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # returns with multiple values (return tuple)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
q, r = myfunc(a, b)
print(f"Quotient is {q}, Remainder is {r}")
