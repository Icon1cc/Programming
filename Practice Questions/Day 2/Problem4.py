"""
Use a loop to count how many times "a" appears in a string
"""

x = input("Please enter the string: ").lower()
count = 0
for letters in x:
    if letters == 'a':
        count += 1

print(f'Number of times a appears in {x} is: {count}')