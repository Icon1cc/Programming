"""
Write a function that returns the average of numbers in a list
"""

def myfunc(mylist):
    if not mylist:
        return 0
    return sum(mylist) / len(mylist)

mylist = input("Please enter the list comma separated: ")
x = [int(i.strip()) for i in mylist.split(',')]
result = myfunc(x)
print(f"The average is: {result}")