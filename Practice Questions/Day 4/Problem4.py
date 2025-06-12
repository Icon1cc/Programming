"""
Count frequency of characters in a string using a dictionary
"""

def myfunc(mydict):
    empty_dict = {}
    for char in mydict:
        if char in empty_dict:
            empty_dict[char] += 1
        else:
            empty_dict[char] = 1
    return empty_dict

user_input = input("Enter a string: ")
result = myfunc(user_input)

print("Character frequency:")
for char, freq in result.items():
    print(f"'{char}': {freq}")
