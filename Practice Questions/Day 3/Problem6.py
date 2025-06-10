"""
Write a function to remove duplicates from a list
"""

# def func(dupl):
#     return set(dupl)

def func(dupl):
    seen_list = set()
    new_list = []
    for items in dupl:
        if items not in seen_list:
            seen_list.add(items)
            new_list.append(items)
    return new_list

dupl = input("Enter the list separated by commas : ")
x = [(i.strip()) for i in dupl.split(',')]
result = func(x)
print(f"New list after removing duplicates is: {result}")