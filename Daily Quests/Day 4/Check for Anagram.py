"""
Given two strings, check if they are anagrams of each other.
Ignore cases and whitespace.
"""

import string

input_string_1 = input("Enter string 1: ").lower()
input_string_2 = input("Enter string 2: ").lower()

cleaned_string_1 = ''.join(char for char in input_string_1 if char not in string.punctuation and char != " ")
cleaned_string_2 = ''.join(char for char in input_string_2 if char not in string.punctuation and char != " ")

seen_1 = {}
seen_2 = {}

for char in cleaned_string_1:
    if char in seen_1:
        seen_1[char] += 1
    else:
        seen_1[char] = 1

for char in cleaned_string_2:
    if char in seen_2:
        seen_2[char] += 1
    else:
        seen_2[char] = 1

if seen_1 == seen_2:
    print("They are anagrams of each other.")
else:
    print("They are not anagrams of each other.")