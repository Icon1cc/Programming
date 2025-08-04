"""
Write a function that accepts *args and returns the max value
"""

def max_val(*args):
    max_num = args[0]
    for items in args:
        if items > max_num:
            max_num = items
    return max_num

args = input("Enter the numbers: ")
x = [int(i.strip()) for i in args.split(',')]
result = max_val(*x)
print("Max value is", result)
