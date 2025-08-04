"""
Write a function that takes *args and returns the total sum
"""

def func(*args):
    return sum(args)

input_str = input("Please enter the numbers to print the sum separated by spaces")
args = [float(num) for num in input_str.split()]
result = func(*args)
print(f"The total sum for {args} is {result}")