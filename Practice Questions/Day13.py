"""
Write a function that returns the number of characters in a string
"""

def myfunc(your_str):
    count = 0
    for char in your_str:
        if char!= ' ':  # Can remove if not needed...
            count = count + 1
    return count

your_str = input("Please provide the string to count the number of characters: ")
result = myfunc(your_str)
print(f"The total number of characters in {your_str} is {result}")
