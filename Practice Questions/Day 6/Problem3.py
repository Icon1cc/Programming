"""
Write a function that returns the factorial of a number
"""

def fact(n):
    result = 1
    if n == 0:
        print("The factorial of 0 is 1")
    for i in range(1,n+1):
            result = result*i
    return result

n = int(input("Enter the number to calculate the factorial: "))
factorial = fact(n)
print(f"The factorial of {n} is {factorial}")