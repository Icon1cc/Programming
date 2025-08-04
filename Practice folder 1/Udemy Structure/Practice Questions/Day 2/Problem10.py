"""
Count how many words are in a sentence
"""

x = input("Enter a sentence: ")
# count = 0
# result = x.split(" ")
# for words in result:
#     count += 1

count = len(x.split())
print(f"There are {count} words in your sentence")

