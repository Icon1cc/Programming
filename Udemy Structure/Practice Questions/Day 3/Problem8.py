"""
Return a new list with squares of all numbers in input list
"""
my_list = input("Please enter the numbers separated by commas: ")
x = [int(i.strip()) for i in my_list.split(',')]
new_list = []

for items in x:
    items = items ** 2
    new_list.append(items)

print(new_list)