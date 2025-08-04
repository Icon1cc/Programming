"""
Write a program to check if a given string is palindrome or not
"""

intstr = input("Enter the string: ").lower()

# if intstr[::-1] == intstr:
#     print("It is palindrome")
# else:
#     print("Not a palindrome")

low = 0
high = len(intstr) - 1

is_Palindrome = True

while low < high:
    if intstr[low] != intstr[high]:
        is_Palindrome = False
        break

    low += 1
    high -= 1

if is_Palindrome:
    print("It is palindrome")
else:
    print("Not a palindrome")
