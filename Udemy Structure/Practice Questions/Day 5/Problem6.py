"""
Ask user to input lines, save them in a file
"""

x = input("Enter the data: ")

with open('textfile.txt', "w") as f:
    f.write(x)
    print("Data written in textfile.txt")

