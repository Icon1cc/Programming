"""
Demonstrate local vs global scope in a function
"""

x = 10  # global variable

def my_func():
    x = 5  # local variable, different from global x
    print("Inside function, local x =", x)

my_func()
print("Outside function, global x =", x)
