"""
Write a program to check if a number is palindrome
"""

def pal(n):
    rev = 0
    temp = n

    while temp != 0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10

    return rev == n

n = int(input("Enter a number: "))
result = pal(n)

if result:
    print("It's a palindrome.")
else:
    print("Not a palindrome.")


