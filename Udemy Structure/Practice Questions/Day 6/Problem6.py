"""
Use a nested function (function inside another)
"""

## Lets assume we want to take input a number, square it and add 10

def mynum(n):
    def square(x):
        return x*x

    result = square(n) + 10
    return result

num = int(input("Enter a number: "))
final_result = mynum(num)
print("Final result:", final_result)