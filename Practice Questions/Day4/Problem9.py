"""
Merge two dictionaries
"""

mydict1 = {}
mydict2 = {}
new_dict = {}
while True:
    key_input = input("enter a key for first dictionary or stop to finish: ")
    if key_input.lower() == 'stop':
        break
    value_input = input("Enter the value for the key of first dictionary: ")
    mydict1[key_input] = value_input

while True:
    keys = input("enter a key for second dictionary or stop to finish: ")
    if keys.lower() == 'stop':
        break
    values = input("Enter the value for the key of second dictionary: ")
    mydict2[keys] = values

new_dict = mydict1.copy()
new_dict.update(mydict2)

print("Merged dictionary: ", new_dict)