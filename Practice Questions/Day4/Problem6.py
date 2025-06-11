"""
Check if two sets have any common elements
"""

c = []

a = input("Enter the elements for a: ").split(',')
b = input("enter the elements for b: ").split(',')

for items in a:
    if items in b:
        c.append(items)

print(f"Common elements are: {c}")