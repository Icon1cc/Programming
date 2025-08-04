"""
Read numbers from a file and return their sum
"""

with open('textfile.txt', "r") as f:
    contents = f.read().splitlines()
    total = 0
    for item in contents:
        if item.strip().isdigit():
            total += int(item)
    print("The sum is", total)
