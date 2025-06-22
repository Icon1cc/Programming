"""
Write a program to print triangle pattern for a given input n
input = 3
output:
*
**
***
"""

n = int(input("Please enter a number greater than 0: "))

for i in range(n):
    for j in range(i+1):
        print("*", end = " ")
    print()
