"""
Write a program to reverse a string
"""

input_string = input("Enter the string for reversal: ")
out_string = input_string[::-1]

print(f"The reversed string is: {out_string}")


# Alternative approach
#
# input_string = input("Enter the string for reversal: ")
# out_string = " "
#
# for char in input_string:
#     out_string = char + out_string
#
# print(f"The reversed string is: {out_string}")