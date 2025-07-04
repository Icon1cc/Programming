"""
Write a program to take an input list and separate the numbers to two different list odd and even
"""

mylist = input("Enter the numbers separated by commas: ")
x = [int(i.strip()) for i in mylist.split(',')]

odd = []
even = []

for items in x:
    if items % 2 == 0:
        even.append(items)
    else:
        odd.append(items)

print("The list of odd numbers are :",odd)
print("The list of even numbers are:",even)


# Alternate list comprehension method

# def getOddEven(mylist):
#     even = [i for i in mylist if i % 2 == 0]
#     odd = [i for i in mylist if i % 2 != 0]
#     return odd,even