"""
Print all vowels in a string
"""
vowel_string = input("Please enter the string: ")
empty_string = ""

for letter in vowel_string:
    if letter.lower() in "aeiou":
        empty_string += letter

print("Vowels in the string:", empty_string)

