"""
Write a function to get a list that contains all those items of list that are smaller than x
"""

def getSmallNum(mylist, target):
    return [item for item in mylist if item < target]

target = int(input("Enter the target number: "))
x = input("Please enter a list separated by commas: ")
mylist = [int(i.strip()) for i in x.split(',')]
result = getSmallNum(mylist, target)
print("The new list is", result)

