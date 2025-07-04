"""
Write a program to count the distinct element in a list
"""

# def funcount(mylist):
#     return len(set(mylist))

def funcount(mylist):
    count = 1
    for i in range(1, len(mylist)):
        if mylist[i] not in mylist[0:i]:
            count += 1
    return count

x = input("Enter a list separated by commas: ")
mylist = [int(i.strip()) for i in x.split(',')]
result = funcount(mylist)
print("The number of distinct elements are:",result)
