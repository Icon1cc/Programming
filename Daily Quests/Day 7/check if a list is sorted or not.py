"""
Write a program to check if a list is sorted
"""

def sortedlist(l):
    for items in range(len(l) -1):
        if l[items] > l[items + 1]:
            return False
    return True

x = input("Enter the list separated by commas: ")
l = [int(i.strip()) for i in x.split(',')]
result = sortedlist(l)
print("The result of the list if it is sorted is:", result)