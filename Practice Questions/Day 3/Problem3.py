"""
Write a function that returns the average of numbers in a list
"""

def myfunc(lst):
    total = 0
    for num in lst:
        total =  total + num
    return total / len(lst)

user_input = input("Enter the numbers in a list separated by comma: ")
x = [int(i.strip()) for i in user_input.split(',')]
result = myfunc(x)
print(f"The average of the numbers is {result}")
