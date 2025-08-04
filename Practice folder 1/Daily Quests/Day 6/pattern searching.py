"""
Write a program to search a pattern in the given string
"""

input_string = input("Please enter the string: ")
input_pattern = input("Please enter the pattern to search: ")

position = input_string.find(input_pattern)
found = False

while position >= 0:
    print("Pattern is found at the index position", position)
    found = True
    position = input_string.find(input_pattern, position + 1)

if not found:
    print("Pattern not found in string.")
else:
    print("There is no pattern left to find after position", position)