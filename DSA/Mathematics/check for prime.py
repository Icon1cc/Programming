"""
Write a program to check if a given number is prime
"""

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

x = int(input("Enter a number: "))
if is_prime(x):
    print("It is a prime number")
else:
    print("Not a prime")
