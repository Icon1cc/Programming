"""
write a program to print all those numbers in a list that are not multiple of 5
"""

my_list = input("Enter the numbers separated by commas ',': ")
x = [int(i.strip()) for i in my_list.split(',')]

print("Your list is: ", x)

new_list = []

for items in x:
    if items % 5 == 0:
        continue
    print(items)
    new_list.append(items)

print("Filtered list (not multiples of 5): ", new_list)

