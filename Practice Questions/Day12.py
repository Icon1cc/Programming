"""
Write a function that prints all characters of a string on separate lines
"""

def myfunc(string_format):
    for char in string_format:
        if char != ' ':
            print(char)

string_format = input("Please enter the string: ")
myfunc(string_format)

