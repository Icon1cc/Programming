"""
Write a function that returns the longest word in a sentence
"""

def myfunc(x):
    return max(x.split(), key= len)

x = input("Enter the string: ")
result = myfunc(x)
print(result)
