"""
Write a program to print all divisors of a number.
"""

num = int(input("Enter a number: "))

list_of_divisors = []

for i in range(1, num + 1):
    if num % i == 0:
        list_of_divisors.append(i)

print(list_of_divisors)