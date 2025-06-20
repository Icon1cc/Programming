"""
Create a dictionary from two lists: one of keys, one of values
"""

key_input = input("Enter the list of keys (space-separated): ").split()
value_input = input("Enter the values for the keys (space-separated): ").split()

mydict = dict(zip(key_input, value_input))
print(mydict)
