"""
Remove duplicates from a list using a set
"""

x = input("Enter the list: ")
z = [i.strip() for i in x.split(',')]
result = set(z)
print(result)