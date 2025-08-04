"""
Write a program to check if a number is prime
"""

n = int(input("Enter a number to check if it is prime: "))

if n <= 1:
    print("Not a prime number")
else:
    x = 2
    while x*x <= n:
        if n % x == 0:
            print("It is not a prime number")
            break
        x = x + 1
    else:
        print("It is a prime number")
