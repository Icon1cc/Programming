"""
Function that adds a number to a global variable
"""

x = 20

def func(a):
    global x
    x = x + a
    return x

a = int(input("Enter the number: "))
result = func(a)
print(result)