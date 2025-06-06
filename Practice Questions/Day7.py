"""
Write a function that returns whether a number is even or odd
"""

def odd_even_check(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

num = int(input("Provide the number to check if it is odd or even: "))
result = odd_even_check(num)
print(f"The provided number is {result}")