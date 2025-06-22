"""
Write a program to print inverted triangle pattern for the number n

example :
input = 3
output =
***
**
*
"""

n = int(input("Please enter a number greater than 0: "))

for i in range(n):
    for j in range(n - i):
        print("*", end = " ")
    print()


