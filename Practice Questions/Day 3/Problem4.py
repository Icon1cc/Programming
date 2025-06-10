"""
Reverse a list without using reverse()
"""

new_list = []
mylist = input("Provide the details separated by comma: ")
x = [int(i.strip()) for i in mylist.split(',')]

for i in range(len(x) -1, -1, -1):
    new_list.append(x[i])
print(new_list)