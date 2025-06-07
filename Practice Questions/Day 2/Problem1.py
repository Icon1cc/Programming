"""
Write a function to check if a string is a palindrome
"""

def palindrome(string):
    reversed_str = ""
    for letter in string:
        reversed_str = letter + reversed_str
    if reversed_str == string:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

string = input("Please enter a string to check if it is a palindrome or not: ")
palindrome(string)
