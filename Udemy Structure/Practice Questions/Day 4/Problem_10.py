"""
Return only unique values from a dictionary
"""

my_dict = {}
while True:
    key_input = input("Enter a key or stop to finish: ")
    if key_input.lower() == 'stop':
        break
    value_input = input("Enter the value for the key: ")
    my_dict[key_input] = value_input

result = set(my_dict.values())
print(result)