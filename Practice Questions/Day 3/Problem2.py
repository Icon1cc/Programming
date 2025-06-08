"""
Write a function that returns the max value in a list (no built-ins)
"""

def myfunc(mylist):
    max_val = mylist[0]
    for num in mylist[1:]:
        if num > max_val:
            max_val = num
    return max_val

user_input = input("Please enter the numbers separated by comma: ")
x = [int(i.strip()) for i in user_input.split(',')]

result = myfunc(x)
print(f"max value in the list is {result}")
