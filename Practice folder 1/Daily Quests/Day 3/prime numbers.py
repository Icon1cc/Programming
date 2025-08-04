"""
Write a program to check if a number is prime or not
"""

num = int(input("Enter number to check: "))

if num <= 1:
    print("It is not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("It is not Prime")
            break
    else:
        print("It is Prime")
