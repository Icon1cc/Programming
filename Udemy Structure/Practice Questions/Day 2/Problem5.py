"""
Return the last character of a string
"""

def myfunc(x):
    return x[-1]

x = input("Enter the string please : ")
result = myfunc(x)
print(f'The last character of {x} is {result}')