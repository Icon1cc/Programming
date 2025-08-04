"""
Write a program to decide if an input number is:
    a) positive even
    b) positive odd
    c) negative even
    d) negative odd
    e) zero
"""

x = int(input("Please enter the number: "))

if x == 0:
    print("Zero")
elif x > 0:
    if x % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if x % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")