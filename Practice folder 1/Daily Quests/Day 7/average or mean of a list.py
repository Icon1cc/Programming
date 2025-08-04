"""
Write a function to print the average or mean of a list
"""

def averagelist(mylist):
    if not mylist:
        print("The list is empty.")
        return None
    total = 0
    for item in mylist:
        total += item
    average = total / len(mylist)
    return average

x = input("Enter the list separated by commas: ")
mylist = [int(i.strip()) for i in x.split(',')]
result = averagelist(mylist)
if result is not None:
    print("The average is:", result)
