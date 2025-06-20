"""
Write a function to get all even numbers from a list
"""

def func(mylist):
    new_list = []
    for item in mylist:
        if item % 2 == 0:
            new_list.append(item)
    return new_list

mylist = input("Enter the numbers separated by commas: ")
x = [int(i.strip()) for i in mylist.split(',')]
result = func(x)
print(f"Even numbers from the list are {result}")