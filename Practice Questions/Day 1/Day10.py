"""
Write a function to greet a user with their name
"""

def greet(name):
    return f"Hello {name}, how are you?"

name = input("Please enter your name: ")
print(greet(name))