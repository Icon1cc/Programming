"""
Write a program to print a word n times
"""

x = input("Enter the word: ")
y = int(input("Enter the range: "))

i = 1
while i <= y:
    print(f"Iteration number {i} is {x}")
    i += 1