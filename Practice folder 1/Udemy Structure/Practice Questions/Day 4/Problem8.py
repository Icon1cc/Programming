"""
Swap keys and values in a dictionary
"""

mydict = {}
new_dict = {}
while True:
    key_input = input("enter a key or stop to finish: ")
    if key_input.lower() == 'stop':
        break
    value_input = input("Enter the value for the key: ")
    mydict[key_input] = value_input

for key, values in mydict.items():
    new_dict[values] = key
print(new_dict)