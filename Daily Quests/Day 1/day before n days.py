"""
Write a program that takes a number n and print the day before that number.
Example:

    0 - Sunday
    1 - Monday
    2 - Tuesday
    3 - Wednesday
    4 - Thursday
    5 - Friday
    6 - Saturday
"""

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

d = int(input("Enter today's day number (0 for Sunday, 1 for Monday, ..., 6 for Saturday): "))
n = int(input("Enter how many days back you want to go: "))

result = (d - n) % 7
print("The day is:", days[result])

