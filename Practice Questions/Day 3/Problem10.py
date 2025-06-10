"""
Slice the last 3 elements from a list
"""

mylist = input("Enter the list : ")
x = [int(i.strip()) for i in mylist.split(',')]
x = x[-3:]
print(f"The last 3 elements are: {x}")