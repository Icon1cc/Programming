"""
Reverse a string without slicing
"""

def func(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

s = input("Provide the string to be reversed : ")
result = func(s)
print(f"The reversed string is : {result}")