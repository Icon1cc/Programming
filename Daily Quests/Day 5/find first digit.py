"""
Write a program to find first digit of the number

input x = 7549
output = 7

"""

# def myfunc(num):
#     while num >= 10:
#         num = num // 10
#     return num
#
# x = int(input("Enter a number: "))
# result = myfunc(x)
# print("The first digit of the given number is", result)

import math

def myfunc(num):
    d = int(math.log10(num))
    res = num // (10**d)
    return res

x = int(input("Enter a number: "))
result = myfunc(x)
print("The first digit of the given number is", result)