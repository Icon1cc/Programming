"""
Write a function that checks if a key exists in a dictionary
"""
def myfunc(my_dict, keys):
    return keys in my_dict

my_dict = {}
while True:
    key_input = input("Enter a key or stop to finish: ")
    if key_input.lower() == 'stop':
        break
    value_input = input("Enter the value for the key: ")
    my_dict[key_input] = value_input

search_key = input("Enter the key to be searched: ")

if myfunc(my_dict, search_key):
    print("The key exists")
else:
    print("The key does not exists")
