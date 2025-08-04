"""
Write a Python program that takes a string input and returns the frequency of each character (or each word) in the string.
Make sure it handles punctuation and different cases.
"""

import string

input_string = input("Enter a string: ").lower()

# Remove punctuation
cleaned_string = ''.join(char for char in input_string if char not in string.punctuation)

# Character frequency
char_freq = {}

for char in cleaned_string:
    if char == ' ':
        continue
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# Word frequency
words = cleaned_string.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Character Frequencies:")
for k, v in char_freq.items():
    print(f"{k}: {v}")

print("\nWord Frequencies:")
for k, v in word_freq.items():
    print(f"{k}: {v}")
